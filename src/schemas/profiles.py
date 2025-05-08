from datetime import date

from fastapi import UploadFile, Form, File, HTTPException
from pydantic import BaseModel, field_validator, HttpUrl, ConfigDict

from database.models.accounts import GenderEnum
from validation import (
    validate_name,
    validate_image,
    validate_gender,
    validate_birth_date
)

class ProfileResponseSchema(BaseModel):
    id: int
    user_id: int
    first_name: str
    last_name: str
    gender: GenderEnum
    date_of_birth: date
    info: str
    avatar: HttpUrl


class ProfileCreateSchema(BaseModel):
    first_name: str
    last_name: str
    gender: str
    date_of_birth: date
    info: str
    avatar: UploadFile

    @classmethod
    def from_form(
            cls,
            first_name: str = Form(...),
            last_name: str = Form(...),
            gender: str = Form(...),
            date_of_birth: date = Form(...),
            info: str = Form(...),
            avatar: UploadFile = File(...)
    ) -> "ProfileCreateSchema":

        return cls(
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            date_of_birth=date_of_birth,
            info=info,
            avatar=avatar
        )

    @field_validator("first_name", "last_name")
    def names_validator(cls, value):
        try:
            validate_name(value)
            return value.lower()
        except ValueError as e:
            raise HTTPException(
                status_code=422,
                detail=str(e)
            )

    @field_validator("avatar")
    def avatar_validator(cls, value):
        try:
            validate_image(value)
            return value
        except ValueError as e:
            raise HTTPException(
                status_code=422,
                detail=str(e)
            )

    @field_validator("gender")
    def gender_validator(cls, value):
        try:
            validate_gender(value)
            return value
        except ValueError as e:
            raise HTTPException(
                status_code=422,
                detail=str(e)
            )

    @field_validator("date_of_birth")
    def date_of_birth_validator(cls, value):
        try:
            validate_birth_date(value)
            return value
        except ValueError as e:
            raise HTTPException(
                status_code=422,
                detail=str(e)
            )

    @field_validator("info")
    def info_validator(cls, value):
        if value.strip():
            return value
        raise HTTPException(
            status_code=422,
            detail="Info field cannot be empty or contain only spaces."
        )