from typing import cast

from fastapi import (
    APIRouter,
    Depends,
    status,
    HTTPException,
)

from pydantic import HttpUrl
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from config import get_jwt_auth_manager, get_s3_storage_client
from database import get_db

from database.models.accounts import (
    UserProfileModel,
    UserModel,
    UserGroupModel,
    UserGroupEnum,
    GenderEnum
)

from exceptions import BaseSecurityError, S3FileUploadError
from schemas.profiles import ProfileResponseSchema, ProfileCreateSchema
from security.http import get_token
from security.interfaces import JWTAuthManagerInterface
from storages import S3StorageInterface

router = APIRouter()


@router.post(
    "/users/{user_id}/profile/",
    response_model=ProfileResponseSchema,
    status_code=201
)
async def create_profile(
        user_id: int,
        access_token: str = Depends(get_token),
        profile_data: ProfileCreateSchema = Depends(
            ProfileCreateSchema.from_form
        ),
        jwt_manager: JWTAuthManagerInterface = Depends(get_jwt_auth_manager),
        db: AsyncSession = Depends(get_db),
        s3_client: S3StorageInterface = Depends(get_s3_storage_client)
) -> ProfileResponseSchema:
    try:
        check_token = jwt_manager.decode_access_token(access_token)
        got_user_id = check_token.get("user_id")
    except BaseSecurityError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e)
        )
    if got_user_id != user_id:
        user_group_res = await db.execute(
            select(UserGroupModel).join(UserModel).where(
                UserModel.id == got_user_id
            )
        )
        user_group = user_group_res.scalars().first()
        if not user_group or user_group.name == UserGroupEnum.USER:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You don't have permission to edit this profile."
            )

    find_user_res = await db.execute(select(UserModel).where(
        UserModel.id == user_id
    ))
    find_user = find_user_res.scalars().first()
    if not find_user or not find_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found or not active."
        )

    profile_res = await db.execute(select(UserProfileModel).where(
        UserProfileModel.user_id == user_id))
    find_user_profile = profile_res.scalars().first()

    if find_user_profile:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="User already has a profile.")

    avatar_data = await profile_data.avatar.read()
    avatar_name = f"avatars/{user_id}_{profile_data.avatar.filename}"

    try:
        await s3_client.upload_file(
            file_name=avatar_name,
            file_data=avatar_data
        )
    except S3FileUploadError as e:
        print(f"Error uploading avatar to S3: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to upload avatar. Please try again later."
        )

    new_profile = UserProfileModel(
        user_id=cast(int, user_id),
        first_name=profile_data.first_name,
        last_name=profile_data.last_name,
        gender=cast(GenderEnum, profile_data.gender),
        date_of_birth=profile_data.date_of_birth,
        info=profile_data.info,
        avatar=avatar_name
    )
    db.add(new_profile)
    await db.commit()
    await db.refresh(new_profile)

    avatar_url = await s3_client.get_file_url(new_profile.avatar)

    return ProfileResponseSchema(
        id=new_profile.id,
        user_id=new_profile.user_id,
        first_name=new_profile.first_name,
        last_name=new_profile.last_name,
        gender=new_profile.gender,
        date_of_birth=new_profile.date_of_birth,
        info=new_profile.info,
        avatar=cast(HttpUrl, avatar_url)
    )
