# Movie Theater API Project

Welcome to the **Movie Theater API** project! This educational assignment is designed to help you develop and refine your skills in creating robust web applications using FastAPI, SQLAlchemy, and Docker. Here's what the project offers:

## Table of Contents

- [Movie Theater API Project](#movie-theater-api-project)
  - [Features](#features)
    - [Database setup](#database-setup)
    - [Data population](#data-population)
    - [Docker integration](#docker-integration)
    - [Project structure](#project-structure)
    - [Updated Project Structure Overview](#updated-project-structure-overview)
  - [Root Directory](#root-directory)
  - [Commands](#commands)
  - [Docker Configuration](#docker-configuration)
  - [Source Directory (src)](#source-directory-src)
  - [Additional Features](#additional-features)
  - [Tip: Using Dependency Injection in FastAPI](#tip-using-dependency-injection-in-fastapi)
  - [Using `get_db` for Database Dependency Injection](#using-get_db-for-database-dependency-injection)
  - [Extended Dependency Injection in FastAPI](#extended-dependency-injection-in-fastapi)
  - [Handling Authentication via Authorization Headers](#handling-authentication-via-authorization-headers)
  - [Summary](#summary)
  - [Primary Services (docker-compose.yml)](#primary-services-docker-composeyml)
    - [1. Database Service (`db`)](#1-database-service-db)
    - [2. pgAdmin Service (`pgadmin`)](#2-pgadmin-service-pgadmin)
    - [3. Backend Service (`web`)](#3-backend-service-web)
    - [4. Database Migrator (`migrator`)](#4-database-migrator-migrator)
    - [5. MailHog Service (`mailhog`)](#5-mailhog-service-mailhog)
    - [6. MinIO Object Storage (`minio`)](#6-minio-object-storage-minio)
    - [7. MinIO Client (`minio_mc`)](#7-minio-client-minio_mc)
  - [Testing Services (docker-compose-tests.yml)](#testing-services-docker-compose-testsyml)
    - [1. Test Backend Service (`web`)](#1-test-backend-service-web)
    - [2. Test MailHog Service (`mailhog`)](#2-test-mailhog-service-mailhog)
    - [3. Test MinIO Storage (`minio`)](#3-test-minio-storage-minio)
    - [4. Test MinIO Client (`minio_mc`)](#4-test-minio-client-minio_mc)
  - [Volumes](#volumes)
  - [Networks](#networks)
  - [Summary (again)](#summary-1)
  - [How to Run the Project](#how-to-run-the-project)
    - [1. Clone the Repository](#1-clone-the-repository)
    - [2. Create and Activate a Virtual Environment](#2-create-and-activate-a-virtual-environment)
    - [3. Install Dependencies with Poetry](#3-install-dependencies-with-poetry)
    - [4. Create a `.env` File](#4-create-a-env-file)
    - [5. Run the Project with Docker Compose](#5-run-the-project-with-docker-compose)
    - [6. Access the Services](#6-access-the-services)
    - [7. Verify Setup](#7-verify-setup)
    - [8. Running the Development Server without Docker](#8-running-the-development-server-without-docker)
    - [9. Running End-to-End (E2E) Tests](#9-running-end-to-end-e2e-tests)
    - [10. Running Tests Locally](#10-running-tests-locally)
      - [Project Setup Summary](#project-setup-summary)
    - [Run project with PyCharm](#run-project-with-pycharm)
  - [Models and Entities Overview](#models-and-entities-overview)
    - [Accounts Models](#accounts-models)
      - [1. UserGroupModel](#1-usergroupmodel)
      - [2. UserModel](#2-usermodel)
      - [3. UserProfileModel](#3-userprofilemodel)
      - [4. TokenBaseModel](#4-tokenbasemodel)
      - [5. ActivationTokenModel](#5-activationtokenmodel)
      - [6. PasswordResetTokenModel](#6-passwordresettokenmodel)
      - [7. RefreshTokenModel](#7-refreshtokenmodel)
    - [Movie Models](#movie-models)
      - [1. MovieModel](#1-moviemodel)
      - [2. GenreModel](#2-genremodel)
      - [3. ActorModel](#3-actormodel)
      - [4. CountryModel](#4-countrymodel)
      - [5. LanguageModel](#5-languagemodel)
      - [6. Association Tables](#6-association-tables)
  - [Task Description: Extending the Cinema Application](#task-description-extending-the-cinema-application)
  - [Tasks: Implementing Email Notifications for User Registration and Password Reset](#tasks-implementing-email-notifications-for-user-registration-and-password-reset)
  - [Task: Implement User Profile Creation and Validation Schema](#task-implement-user-profile-creation-and-validation-schema)
    - [1. Profile Schema (`schemas/profiles.py`)](#1-profile-schema-schemasprofilespy)
    - [2. Profile Creation Endpoint (`routes/profiles.py`)](#2-profile-creation-endpoint-routesprofilespy)
    - [3. Endpoint Behavior and Error Handling](#3-endpoint-behavior-and-error-handling)
      - [1️⃣ Token Validation](#1-token-validation)
      - [2️⃣ Authorization Rules](#2-authorization-rules)
      - [3️⃣ User Existence and Status](#3-user-existence-and-status)
      - [4️⃣ Check for Existing Profile](#4-check-for-existing-profile)
      - [5️⃣ Avatar Upload to S3 Storage](#5-avatar-upload-to-s3-storage)
      - [6️⃣ Profile Creation and Storage](#6-profile-creation-and-storage)
    - [4. Full List of Possible Errors](#4-full-list-of-possible-errors)
    - [5. Next Steps](#5-next-steps)
      - [Tips and Guidance](#tips-and-guidance)
      - [Running Tests](#running-tests)
        - [1️⃣ Running Unit and Integration Tests (Without Docker)](#1-running-unit-and-integration-tests-without-docker)
        - [2️⃣ Running End-to-End (E2E) Tests](#2-running-end-to-end-e2e-tests)
      - [Test Results](#test-results)


## Features

### **Database setup**
- **PostgreSQL for development**: The application uses PostgreSQL as the main database for the development environment, configured via Docker Compose.
- **SQLite for testing**: A lightweight SQLite database is utilized for testing, ensuring fast and isolated test execution.

### **Data population**
- The database can be automatically populated with movie data from a provided dataset. This includes associated entities such as genres, actors, languages, and countries, ensuring a rich and interconnected data structure.

### **Docker integration**
- The project is fully Dockerized, allowing seamless setup and execution of the application and its dependencies.
- Docker Compose simplifies the orchestration of services like the FastAPI application, PostgreSQL database, and other required components.
- **MailHog for email testing**: The project includes **MailHog**, which captures outgoing emails and provides a web interface for viewing test emails. This is useful for testing user registration, password reset, and account activation flows.
- **MinIO for object storage**: The project integrates **MinIO**, an S3-compatible storage solution used for handling file uploads, such as user avatars.
- **Separate Docker Compose files**:
  - `docker-compose.yml`: The main configuration for development, including FastAPI, PostgreSQL, MailHog, and MinIO.
  - `docker-compose-test.yml`: A separate configuration optimized for **end-to-end (E2E) testing**, using SQLite as the test database.

### **Project structure**
A well-organized and modular project structure is provided, including:
- **Database models** and schemas for movies and related entities.
- **Routing logic** for managing API endpoints.
- **Utility scripts** for tasks like data seeding and database migrations.
- **Testing framework** integrated with `pytest`, including unit and E2E tests for API functionality.

This setup ensures a scalable, maintainable, and testable API that adheres to best practices in web development.

### Updated Project Structure Overview

The **Movie Theater API** project maintains a structured and modular organization, making development, testing, and deployment more efficient. Below is a detailed breakdown of the project's structure:

```
.
├── Dockerfile
├── README.md
├── README_NEW.md
├── alembic.ini
├── commands
│   ├── run_migration.sh
│   ├── run_web_server_dev.sh
│   ├── setup_mailhog_auth.sh
│   └── setup_minio.sh
├── docker
│   ├── mailhog
│   │   └── Dockerfile
│   ├── minio_mc
│   │   └── Dockerfile
│   └── tests
│       └── Dockerfile
├── docker-compose.yml
├── docker-compose-tests.yml
├── init.sql
├── poetry.lock
├── pyproject.toml
├── pytest.ini
└── src
    ├── __pycache__
    ├── config
    │   ├── __init__.py
    │   ├── dependencies.py
    │   └── settings.py
    ├── database
    │   ├── __init__.py
    │   ├── migrations
    │   │   ├── README
    │   │   ├── env.py
    │   │   ├── script.py.mako
    │   │   └── versions
    │   │       ├── 2da0dc469be8_temp_migration.py
    │   │       ├── 32b1054a69e3_initial_migration.py
    │   │       └── 41cdafa531cf_temp_migration.py
    │   ├── models
    │   │   ├── __init__.py
    │   │   ├── accounts.py
    │   │   ├── base.py
    │   │   └── movies.py
    │   ├── populate.py
    │   ├── seed_data
    │   │   ├── imdb_movies.csv
    │   │   └── test_data.csv
    │   ├── session_postgresql.py
    │   ├── session_sqlite.py
    │   ├── source
    │   │   └── theater.db
    │   └── validators
    │       ├── __init__.py
    │       └── accounts.py
    ├── exceptions
    │   ├── __init__.py
    │   ├── email.py
    │   ├── security.py
    │   └── storage.py
    ├── main.py
    ├── notifications
    │   ├── __init__.py
    │   ├── emails.py
    │   ├── interfaces.py
    │   └── templates
    │       ├── activation_complete.html
    │       ├── activation_request.html
    │       ├── password_reset_complete.html
    │       └── password_reset_request.html
    ├── routes
    │   ├── __init__.py
    │   ├── accounts.py
    │   ├── movies.py
    │   └── profiles.py
    ├── schemas
    │   ├── __init__.py
    │   ├── accounts.py
    │   ├── examples
    │   │   ├── __init__.py
    │   │   └── movies.py
    │   ├── movies.py
    │   └── profiles.py
    ├── security
    │   ├── __init__.py
    │   ├── http.py
    │   ├── interfaces.py
    │   ├── passwords.py
    │   ├── token_manager.py
    │   └── utils.py
    ├── storages
    │   ├── __init__.py
    │   ├── interfaces.py
    │   └── s3.py
    ├── tests
    │   ├── __init__.py
    │   ├── conftest.py
    │   ├── doubles
    │   │   ├── __init__.py
    │   │   ├── fakes
    │   │   │   ├── __init__.py
    │   │   │   └── storage.py
    │   │   └── stubs
    │   │       ├── __init__.py
    │   │       └── emails.py
    │   ├── test_e2e
    │   │   ├── __init__.py
    │   │   ├── test_email_notification.py
    │   │   └── test_storage.py
    │   ├── test_integration
    │   │   ├── __init__.py
    │   │   ├── test_accounts.py
    │   │   ├── test_movies.py
    │   │   └── test_profiles.py
    └── validation
        ├── __init__.py
        └── profile.py

```

---

### **Root Directory**
- **`README.MD`**: Main project documentation.
- **`README_NEW.MD`**: Updated version of the project documentation.
- **`docker-compose.yml`**: Configures the main application services using PostgreSQL, FastAPI, and MinIO.
- **`docker-compose-tests.yml`**: Configures services specifically for **end-to-end (e2e) testing**, including SQLite, MailHog, and MinIO.
- **`poetry.lock`** & **`pyproject.toml`**: Poetry-based dependency management.
- **`pytest.ini`**: Configuration for running tests.

---

### **Commands**
- **`run_migration.sh`**: Script to execute database migrations using Alembic.
- **`run_web_server_dev.sh`**: Script to start the FastAPI development server.
- **`setup_mailhog_auth.sh`**: Initializes authentication for the MailHog testing environment.
- **`setup_minio.sh`**: Configures MinIO client (`mc`) to work with the application.

---

### **Docker Configuration**
The `docker` directory contains **Dockerfiles** for different services:
- **`docker/mailhog/Dockerfile`**: Builds a custom MailHog container for email testing.
- **`docker/minio_mc/Dockerfile`**: Builds a MinIO client (`mc`) container for interacting with MinIO storage.
- **`docker/tests/Dockerfile`**: Builds a container for executing **end-to-end (e2e) tests**.

---

### **Source Directory (`src`)**

#### **Configuration (`config`)**
- **`dependencies.py`**: Defines FastAPI dependencies for dependency injection.
- **`settings.py`**: Manages project settings, including database configurations and external service settings.

#### **Database (`database`)**
- **`models/`**: Defines SQLAlchemy ORM models for **Users, Movies, and related entities**.
- **`migrations/`**: Contains Alembic migration scripts.
- **`populate.py`**: Seeds the database with initial movie data.
- **`session_postgresql.py`**: PostgreSQL session for development.
- **`session_sqlite.py`**: SQLite session for testing.

#### **Exceptions (`exceptions`)**
- **`email.py`**: Custom exceptions related to email notifications.
- **`security.py`**: Handles security-related exceptions.
- **`storage.py`**: Manages MinIO/S3-related exceptions.

#### **Notifications (`notifications`)**
- **`emails.py`**: Implements the **EmailSender** interface for sending email notifications.
- **`interfaces.py`**: Defines an interface for email-related operations.
- **`templates/`**: Stores HTML email templates:
  - `activation_request.html`
  - `activation_complete.html`
  - `password_reset_request.html`
  - `password_reset_complete.html`

#### **Routes (`routes`)**
- **`accounts.py`**: API endpoints for **user authentication and account management**.
- **`movies.py`**: API endpoints for **movies and related information**.
- **`profiles.py`**: API endpoints for **user profile management**.

#### **Schemas (`schemas`)**
- **`accounts.py`**: Defines schemas for user-related requests and responses.
- **`movies.py`**: Defines schemas for movie-related API responses.
- **`profiles.py`**: Defines schemas for user profile-related API operations.

#### **Security (`security`)**
- **`http.py`**: Handles HTTP security-related logic.
- **`interfaces.py`**: Defines interfaces for authentication and authorization services.
- **`passwords.py`**: Implements password hashing and verification.
- **`token_manager.py`**: Manages JWT authentication tokens.
- **`utils.py`**: Security utility functions.

#### **Storage (`storages`)**
- **`s3.py`**: Implements **MinIO/S3 storage client** for handling file uploads.
- **`interfaces.py`**: Defines an interface for interacting with **S3-compatible storage**.

#### **Testing (`tests`)**
- **`conftest.py`**: Defines shared test fixtures.
- **`doubles/`**: Contains test doubles (fakes, stubs, and mocks).
  - **`fakes/storage.py`**: Fake MinIO storage implementation for **unit testing**.
  - **`stubs/emails.py`**: Stub implementation for email notifications.
- **`test_e2e/`**: **End-to-End (E2E) tests** for API endpoints.
  - **`test_email_notification.py`**: Tests email notifications using MailHog.
  - **`test_storage.py`**: Tests S3 file upload functionality with MinIO.
- **`test_integration/`**: **Integration tests** for individual components.
  - **`test_accounts.py`**: Tests user authentication and account creation.
  - **`test_movies.py`**: Tests movie API operations.
  - **`test_profiles.py`**: Tests user profile creation and management.

#### **Validation (`validation`)**
- **`profile.py`**: Implements input validation for user profile creation.

---

### **Additional Features**
- **MinIO Integration**:
  - MinIO is used as an S3-compatible object storage for storing **profile avatars**.
  - Configured via Docker and managed using the MinIO client (`mc`).

- **MailHog Integration**:
  - MailHog is used as a mock SMTP server for testing **email notifications**.
  - A separate **Docker container** ensures email delivery in the testing environment.

- **E2E Testing Setup**:
  - The `docker-compose-tests.yml` file orchestrates services for **end-to-end tests**.
  - Uses **SQLite** for an isolated testing database.

### **Tip: Using Dependency Injection in FastAPI**

FastAPI provides an efficient way to manage dependencies through the `Depends` function, enabling structured and reusable dependency injection for database sessions, authentication, email notifications, and storage clients.

---

## **Using `get_db` for Database Dependency Injection**

The `get_db` function is a generator that provides a SQLAlchemy session for interacting with the database. This ensures proper session management where the session is created before route execution and automatically closed afterward.

### **Example Usage**
```python
from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db  # Import the get_db generator

router = APIRouter()

@router.get("/example")
async def example_route(db: AsyncSession = Depends(get_db)):
    """Use the db session here to interact with the database"""
    pass
```
  
### **Key Benefits**
- Simplifies injecting dependencies into route handlers.
- Ensures session lifecycle management (creation and cleanup).
- Promotes better testability by separating database logic from the route handler.
- Can be used across multiple routes for consistency.

---

## **Extended Dependency Injection in FastAPI**
Apart from database injection, the project also includes dependencies for **settings management, JWT authentication, email notifications, and S3 storage**.

### **`get_settings`: Load Project Settings Based on Environment**
```python
import os
from fastapi import Depends
from config.settings import TestingSettings, Settings, BaseAppSettings

def get_settings() -> BaseAppSettings:
    environment = os.getenv("ENVIRONMENT", "developing")
    if environment == "testing":
        return TestingSettings()
    return Settings()
```
- Determines whether the app is running in **development** or **testing** mode.
- Provides access to relevant configuration settings.

### **`get_jwt_auth_manager`: Manage JWT Authentication**
```python
from security.interfaces import JWTAuthManagerInterface
from security.token_manager import JWTAuthManager

def get_jwt_auth_manager(settings: BaseAppSettings = Depends(get_settings)) -> JWTAuthManagerInterface:
    return JWTAuthManager(
        secret_key_access=settings.SECRET_KEY_ACCESS,
        secret_key_refresh=settings.SECRET_KEY_REFRESH,
        algorithm=settings.JWT_SIGNING_ALGORITHM
    )
```
- Provides JWT authentication management.
- Uses `Depends(get_settings)` to dynamically configure JWT parameters.

### **`get_accounts_email_notificator`: Email Notification Service**
```python
from notifications import EmailSenderInterface, EmailSender

def get_accounts_email_notificator(settings: BaseAppSettings = Depends(get_settings)) -> EmailSenderInterface:
    return EmailSender(
        hostname=settings.EMAIL_HOST,
        port=settings.EMAIL_PORT,
        email=settings.EMAIL_HOST_USER,
        password=settings.EMAIL_HOST_PASSWORD,
        use_tls=settings.EMAIL_USE_TLS,
        template_dir=settings.PATH_TO_EMAIL_TEMPLATES_DIR,
        activation_email_template_name=settings.ACTIVATION_EMAIL_TEMPLATE_NAME,
        activation_complete_email_template_name=settings.ACTIVATION_COMPLETE_EMAIL_TEMPLATE_NAME,
        password_email_template_name=settings.PASSWORD_RESET_TEMPLATE_NAME,
        password_complete_email_template_name=settings.PASSWORD_RESET_COMPLETE_TEMPLATE_NAME
    )
```
- Sends **account activation**, **password reset**, and other notifications.
- Loads email configurations from environment variables.

### **`get_s3_storage_client`: MinIO S3 Storage Client**
```python
from storages import S3StorageInterface, S3StorageClient

def get_s3_storage_client(settings: BaseAppSettings = Depends(get_settings)) -> S3StorageInterface:
    return S3StorageClient(
        endpoint_url=settings.S3_STORAGE_ENDPOINT,
        access_key=settings.S3_STORAGE_ACCESS_KEY,
        secret_key=settings.S3_STORAGE_SECRET_KEY,
        bucket_name=settings.S3_BUCKET_NAME
    )
```
- Provides access to **MinIO S3 storage** for file management.
- Uses settings injected via **`Depends(get_settings)`**.

---

## **Handling Authentication via Authorization Headers**
When implementing authentication, it is critical to properly validate the `Authorization` header to ensure security.

### **`get_token`: Extract and Validate the Bearer Token**
```python
from fastapi import Request, HTTPException, status

def get_token(request: Request) -> str:
    """
    Extracts the Bearer token from the Authorization header.

    :param request: FastAPI Request object.
    :return: Extracted token string.
    :raises HTTPException: If Authorization header is missing or invalid.
    """
    authorization: str = request.headers.get("Authorization")

    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization header is missing"
        )

    scheme, _, token = authorization.partition(" ")

    if scheme.lower() != "bearer" or not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Authorization header format. Expected 'Bearer <token>'"
        )

    return token
```
### **Security Considerations**
- **Ensures a valid `Authorization` header is present.**
- **Validates the `Bearer` scheme** and ensures a token is provided.
- **Raises a `401 Unauthorized` error** if the format is incorrect.

---

## **Summary**
- **Database Connection (`get_db`)**: Injects a session into routes.
- **Settings (`get_settings`)**: Dynamically loads configurations.
- **JWT Authentication (`get_jwt_auth_manager`)**: Manages authentication.
- **Email Notifications (`get_accounts_email_notificator`)**: Sends account-related emails.
- **S3 Storage (`get_s3_storage_client`)**: Handles file storage via MinIO.
- **Authentication (`get_token`)**: Extracts and validates JWT tokens from headers.

Using FastAPI’s **dependency injection system**, these components ensure **cleaner**, **testable**, and **modular** application architecture.

### **Services Overview**

The project is configured with multiple services in both `docker-compose.yml` and `docker-compose-tests.yml`, allowing seamless development, testing, and deployment of the **Movie Theater API**. Below is a breakdown of the services and their roles.

---

## **Primary Services (docker-compose.yml)**

### **1. Database Service (`db`)**
- **Image**: `postgres:latest`
- **Purpose**: Acts as the primary PostgreSQL database for the application.
- **Configuration**:
  - Loads an initial schema from `init.sql`.
  - Uses a persistent Docker volume `postgres_theater_data` to store data.
  - Exposes PostgreSQL on port **5432**.
- **Health Check**: Uses `pg_isready` to ensure the database is ready before dependent services start.
- **Network**: Attached to `theater_network`.

---

### **2. pgAdmin Service (`pgadmin`)**
- **Image**: `dpage/pgadmin4`
- **Purpose**: Provides a web interface for managing and monitoring the PostgreSQL database.
- **Configuration**:
  - Exposes **pgAdmin** on port **3333**.
  - Uses a persistent volume `pgadmin_theater_data` to store settings.
- **Dependency**: Waits until `db` is healthy before starting.
- **Network**: Attached to `theater_network`.

---

### **3. Backend Service (`web`)**
- **Build Context**: Uses the local directory (`.`) as the build source.
- **Purpose**: Runs the **FastAPI application**, serving API endpoints.
- **Configuration**:
  - Runs the development server via `/commands/run_web_server_dev.sh`.
  - Uses `PYTHONPATH` to reference the `src` directory.
  - Enables live file watching (`WATCHFILES_FORCE_POLLING=true`).
  - Exposes the API on port **8000**.
- **Dependencies**:
  - Waits for `db` and `minio` services to be healthy before starting.
- **Network**: Attached to `theater_network`.

---

### **4. Database Migrator (`migrator`)**
- **Build Context**: Shares the same build context as `web`.
- **Purpose**: Runs **Alembic migrations** to keep the database schema up-to-date.
- **Configuration**:
  - Uses the `run_migration.sh` script to apply migrations.
  - Mounts the `src` directory to access migration scripts.
- **Dependency**: Starts only after `db` is healthy.
- **Network**: Attached to `theater_network`.

---

### **5. MailHog Service (`mailhog`)**
- **Build Context**: Uses a **custom MailHog image** (Dockerfile located in `docker/mailhog`).
- **Purpose**: Provides a local SMTP server for **email testing**.
- **Configuration**:
  - Runs `setup_mailhog_auth.sh` to configure authentication.
  - Exposes **MailHog UI on port 8025** and SMTP on **port 1025**.
- **Network**: Attached to `theater_network`.

---

### **6. MinIO Object Storage (`minio`)**
- **Image**: `minio/minio:latest`
- **Purpose**: Provides an **S3-compatible storage** for managing file uploads.
- **Configuration**:
  - Runs the MinIO server with **console access on port 9001**.
  - Uses a persistent volume `minio_data` to store objects.
- **Health Check**: Checks MinIO’s `/minio/health/live` endpoint to ensure it's ready.
- **Network**: Attached to `theater_network`.

---

### **7. MinIO Client (`minio_mc`)**
- **Build Context**: Uses a **custom MinIO Client image** (Dockerfile in `docker/minio_mc`).
- **Purpose**: Configures MinIO storage, creates required buckets, and sets permissions.
- **Configuration**:
  - Runs `setup_minio.sh` to initialize storage.
- **Dependency**: Waits until `minio` is healthy before executing commands.
- **Network**: Attached to `theater_network`.

---

## **Testing Services (docker-compose-tests.yml)**

To support **end-to-end (E2E) testing**, the project includes a **separate testing configuration** in `docker-compose-tests.yml`.

### **1. Test Backend Service (`web`)**
- **Build Context**: Uses a **dedicated test Dockerfile** (`docker/tests/Dockerfile`).
- **Purpose**: Runs **Pytest E2E tests**.
- **Configuration**:
  - Executes `pytest` with specific flags:
    ```sh
    pytest -m e2e --maxfail=5 --disable-warnings -v --tb=short
    ```
  - Uses a dedicated **testing environment** (`ENVIRONMENT=testing`).
- **Dependencies**: Waits for `mailhog` and `minio` before running tests.
- **Network**: Uses a separate network (`theater_network_test`).

---

### **2. Test MailHog Service (`mailhog`)**
- **Image**: `mailhog/mailhog`
- **Purpose**: Provides an SMTP server for email testing.
- **Configuration**:
  - Exposes **MailHog UI on port 8025** and **SMTP on port 1025**.
- **Network**: Attached to `theater_network_test`.

---

### **3. Test MinIO Storage (`minio`)**
- **Image**: `minio/minio:latest`
- **Purpose**: Provides **S3-compatible storage** for E2E tests.
- **Configuration**:
  - Uses **`minio-theater-test`** as the test container name.
  - Stores test files in a separate volume (`minio_data_test`).
  - Health checks ensure MinIO is ready before tests start.
- **Network**: Attached to `theater_network_test`.

---

### **4. Test MinIO Client (`minio_mc`)**
- **Build Context**: Uses the **same MinIO Client image** as production.
- **Purpose**: Configures **MinIO storage for testing**.
- **Configuration**:
  - Runs `setup_minio.sh` to initialize test storage.
- **Dependency**: Waits for `minio` before executing.
- **Network**: Attached to `theater_network_test`.

---

## **Volumes**
| Volume Name           | Purpose |
|-----------------------|---------|
| `postgres_theater_data` | Stores **PostgreSQL database** data. |
| `pgadmin_theater_data` | Stores **pgAdmin configuration**. |
| `minio_data` | Stores **MinIO objects** (production). |
| `minio_data_test` | Stores **MinIO objects** (testing). |

---

## **Networks**
| Network Name | Description |
|-------------|-------------|
| `theater_network` | Connects **production** services. |
| `theater_network_test` | Connects **test** services. |

---

## **Summary**
- The **production services** in `docker-compose.yml` include:
  - PostgreSQL (**`db`**), pgAdmin (**`pgadmin`**), FastAPI backend (**`web`**), Alembic migrations (**`migrator`**), MailHog (**`mailhog`**), MinIO storage (**`minio`**), and MinIO client (**`minio_mc`**).
- The **E2E testing services** in `docker-compose-tests.yml` include:
  - A dedicated **test backend** running **pytest**, a separate **MailHog instance**, and **MinIO storage for test uploads**.
- **Separate networks (`theater_network` and `theater_network_test`)** ensure production and test environments remain isolated.

This modular structure ensures a robust and **scalable** development workflow, supporting **local development, integration testing, and production deployment**.

### **How to Run the Project**

Follow these steps to set up and run the **Movie Theater API** project on your local machine.

---

## **1. Clone the Repository**

Start by cloning the project repository from GitHub:

```bash
git clone <repository-url>
cd <repository-folder>
```

---

## **2. Create and Activate a Virtual Environment**

It is recommended to use a virtual environment to isolate project dependencies:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

---

## **3. Install Dependencies with Poetry**

This project uses **Poetry** for dependency management. Install dependencies as follows:

```bash
# Install Poetry if not already installed
pip install poetry

# Install project dependencies
poetry install
```

---

## **4. Create a `.env` File**

Create a `.env` file in the project root directory with the following variables. Customize the values as needed:

```env
# PostgreSQL
POSTGRES_DB=movies_db
POSTGRES_DB_PORT=5432
POSTGRES_USER=admin
POSTGRES_PASSWORD=some_password
POSTGRES_HOST=postgres_theater

# pgAdmin
PGADMIN_DEFAULT_EMAIL=admin@gmail.com
PGADMIN_DEFAULT_PASSWORD=admin

# JWT keys
SECRET_KEY_ACCESS=838qKq7dGp34hWij3c8txA5ZD2qm9ybt
SECRET_KEY_REFRESH=cFzRk8kllHMW71wQKLXBqDzl24fkhisw
JWT_SIGNING_ALGORITHM=HS256

# MailHog
MAILHOG_USER=admin
MAILHOG_PASSWORD=some_password

# Email settings for MailHog
EMAIL_HOST=mailhog_theater
EMAIL_PORT=1025
EMAIL_HOST_USER=testuser@mate.com
EMAIL_HOST_PASSWORD=test_password
EMAIL_USE_TLS=False

# MinIO (S3-Compatible Storage)
MINIO_ROOT_USER=minioadmin
MINIO_ROOT_PASSWORD=some_password
MINIO_HOST=minio-theater
MINIO_PORT=9000
MINIO_STORAGE=theater-storage
```

---

## **5. Run the Project with Docker Compose**

The project is **Dockerized** for easy setup. To start all the required services (**PostgreSQL, pgAdmin, FastAPI app, MailHog, MinIO, and Alembic migrator**), run:

```bash
docker-compose up --build
```

**Notes**:
- The first run **may take some time** as the database will be populated with initial data.
- Logs for services can be viewed using:

  ```bash
  docker-compose logs -f
  ```

---

## **6. Access the Services**

| Service        | URL |
|---------------|--------------------------|
| **API**       | `http://localhost:8000` |
| **pgAdmin**   | `http://localhost:3333` (Use `.env` credentials) |
| **MailHog UI** | `http://localhost:8025` (SMTP testing) |
| **MinIO Console** | `http://localhost:9001` (S3-compatible storage) |

---

## **7. Verify Setup**

After all services are running, you can test the API by accessing the **OpenAPI documentation**:

```plaintext
http://localhost:8000/docs
```

---

## **8. Running the Development Server without Docker**

If you prefer running the application **without Docker**, follow these steps:

1. **Ensure PostgreSQL is running** on your system with credentials matching `.env`.
2. **Apply migrations manually**:

   ```bash
   poetry run alembic upgrade head
   ```

3. **Start the development server**:

   ```bash
   poetry run uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
   ```

---

## **9. Running End-to-End (E2E) Tests**

The project includes **E2E tests** that validate the system using a **separate testing environment**. These tests run inside **dedicated containers** using `docker-compose-tests.yml`.

### **Steps to Run E2E Tests**
1. **Start the test environment**:
   ```bash
   docker-compose -f docker-compose-tests.yml up --build
   ```

2. **Run E2E tests manually (inside a container)**:
   ```bash
   docker exec -it backend_theater_test pytest -m e2e --maxfail=5 --disable-warnings -v --tb=short
   ```

3. **Stop the test environment**:
   ```bash
   docker-compose -f docker-compose-tests.yml down -v
   ```

---

## **10. Running Tests Locally**

For **unit and integration tests**, use:

```bash
pytest -m "unit or integration" --disable-warnings -v
```

---

### **Project Setup Summary**
| Task | Command |
|------|---------|
| **Run all services (Dockerized)** | `docker-compose up --build` |
| **Run development server manually** | `poetry run uvicorn src.main:app --reload` |
| **Apply database migrations** | `poetry run alembic upgrade head` |
| **Run E2E tests** | `docker-compose -f docker-compose-tests.yml up --build` |
| **Run unit/integration tests** | `pytest -m "unit or integration" -v` |

---

### Run project with PyCharm

1. Mark the `src` directory as root
    ![mark src directory as root](./assets/images/1_mark_directory_as_source_root.png)
2. Close all open code tabs
3. Restart `PyCharm`
4. Create a new Run Configuration for the `FastAPI` project
    ![create new fastapi run configuration](./assets/images/2_create_new_run_config.png)
5. Add the required environment variables to the Run Configuration.
6. Start the local Docker Compose services:
    ```bash
    docker-compose -f docker-compose-local.yml up --build -d
    ```
7. Wait for the initial database seeding to finish (this may take a moment the first time).
    ![seed db](./assets/images/4_seed_db.png)  
8. Run the project via `PyCharm` and use breakpoints for debugging
9. If you need to apply database migrations manually, run:
    ```bash
    docker-compose -f docker-compose-local.yml up --build migrator
    ```

---

This structured setup allows **easy development, testing, and deployment**.

### Models and Entities Overview

The project defines the following entities and relationships using SQLAlchemy. Each entity represents a table in the database and maps to a specific domain concept in the Movie Theater API.

---

#### **Accounts Models**

These models handle user authentication, authorization, and related functionality.


#### **1. UserGroupModel**

Represents user groups in the application (e.g., USER, MODERATOR, ADMIN).

- **Table Name**: `user_groups`
- **Fields**:
    - `id` (Primary Key): Unique identifier for each user group.
    - `name`: Enum value representing the group (`UserGroupEnum`).

- **Relationships**:
    - `users`: One-to-many relationship with `UserModel`.

- **Constraints**:
    - Unique constraint on `name`.


#### **2. UserModel**

Represents application users.

- **Table Name**: `users`
- **Fields**:
    - `id` (Primary Key): Unique identifier for each user.
    - `email`: Email address of the user (unique).
    - `hashed_password`: Securely stored password hash.
    - `is_active`: Boolean indicating whether the user account is active.
    - `created_at`: Timestamp when the user was created.
    - `updated_at`: Timestamp when the user was last updated.
    - `group_id`: Foreign key linking to the `user_groups` table.

- **Relationships**:
    - `group`: Links to `UserGroupModel`.
    - `activation_token`: One-to-one relationship with `ActivationTokenModel`.
    - `password_reset_token`: One-to-one relationship with `PasswordResetTokenModel`.
    - `refresh_tokens`: One-to-many relationship with `RefreshTokenModel`.
    - `profile`: One-to-one relationship with `UserProfileModel`.


#### **3. UserProfileModel**

Represents additional information about a user (optional).

- **Table Name**: `user_profiles`
- **Fields**:
    - `id` (Primary Key): Unique identifier for each profile.
    - `first_name`: User's first name.
    - `last_name`: User's last name.
    - `avatar`: Path to the user's avatar image.
    - `gender`: Enum value representing the user's gender (`GenderEnum`).
    - `date_of_birth`: User's date of birth.
    - `info`: Additional information about the user.
    - `user_id`: Foreign key linking to the `users` table.

- **Relationships**:
    - `user`: Links to `UserModel`.

- **Constraints**:
    - Unique constraint on `user_id`.


#### **4. TokenBaseModel**

Abstract base class for all token-based models.

- **Fields**:
    - `id` (Primary Key): Unique identifier for each token.
    - `token`: Securely generated token value.
    - `expires_at`: Expiration timestamp for the token.
    - `user_id`: Foreign key linking to the `users` table.


#### **5. ActivationTokenModel**

Represents tokens used for user account activation.

- **Table Name**: `activation_tokens`
- **Fields**:
    - Inherits all fields from `TokenBaseModel`.

- **Relationships**:
    - `user`: Links to `UserModel`.

- **Constraints**:
    - Unique constraint on `user_id`.


#### **6. PasswordResetTokenModel**

Represents tokens used for password reset.

- **Table Name**: `password_reset_tokens`
- **Fields**:
    - Inherits all fields from `TokenBaseModel`.

- **Relationships**:
    - `user`: Links to `UserModel`.

- **Constraints**:
    - Unique constraint on `user_id`.


#### **7. RefreshTokenModel**

Represents refresh tokens for user authentication.

- **Table Name**: `refresh_tokens`
- **Fields**:
    - Inherits all fields from `TokenBaseModel`.
    - `token`: Securely generated token value with an extended length.

- **Relationships**:
    - `user`: Links to `UserModel`.

- **Methods**:
    - `create`: Factory method to simplify the creation of new refresh tokens.


---

#### **Movie Models**

These models handle movies theater functionality.


#### **1. MovieModel**

Represents a movie in the database.

- **Table Name**: `movies`
- **Fields**:
    - `id` (Primary Key): Unique identifier for each movie.
    - `name`: Name of the movie.
    - `date`: Release date of the movie.
    - `score`: Movie rating score (e.g., IMDb score).
    - `overview`: A short description or synopsis of the movie.
    - `status`: Production status of the movie (e.g., Released, In Production).
    - `budget`: The budget of the movie (stored as a decimal value).
    - `revenue`: The revenue generated by the movie.
    - `country_id`: Foreign key linking to the `countries` table.

- **Relationships**:
    - `country`: Links to the `CountryModel`.
    - `genres`: Many-to-many relationship with `GenreModel`.
    - `actors`: Many-to-many relationship with `ActorModel`.
    - `languages`: Many-to-many relationship with `LanguageModel`.

- **Constraints**:
    - Unique constraint on `name` and `date` to prevent duplicate entries.

#### **2. GenreModel**

Represents a genre (e.g., Action, Comedy).

- **Table Name**: `genres`
- **Fields**:
    - `id` (Primary Key): Unique identifier for each genre.
    - `name`: Name of the genre (e.g., Action, Drama).

- **Relationships**:
    - `movies`: Many-to-many relationship with `MovieModel`.

#### **3. ActorModel**

Represents an actor in the database.

- **Table Name**: `actors`
- **Fields**:
    - `id` (Primary Key): Unique identifier for each actor.
    - `name`: Name of the actor.

- **Relationships**:
    - `movies`: Many-to-many relationship with `MovieModel`.

#### **4. CountryModel**

Represents a country associated with a movie (e.g., production country).

- **Table Name**: `countries`
- **Fields**:
    - `id` (Primary Key): Unique identifier for each country.
    - `code`: ISO 3166-1 alpha-3 country code (e.g., USA, FRA).
    - `name`: Full name of the country.

- **Relationships**:
    - `movies`: One-to-many relationship with `MovieModel`.

#### **5. LanguageModel**

Represents a language spoken in a movie.

- **Table Name**: `languages`
- **Fields**:
    - `id` (Primary Key): Unique identifier for each language.
    - `name`: Name of the language (e.g., English, French).

- **Relationships**:
    - `movies`: Many-to-many relationship with `MovieModel`.

#### **6. Association Tables**

Used to establish many-to-many relationships between entities.

- **`MoviesGenresModel`**:
    - Links `movies` and `genres`.
    - Fields: `movie_id`, `genre_id`.

- **`ActorsMoviesModel`**:
    - Links `movies` and `actors`.
    - Fields: `movie_id`, `actor_id`.

- **`MoviesLanguagesModel`**:
    - Links `movies` and `languages`.
    - Fields: `movie_id`, `language_id`.

### Task Description: Extending the Cinema Application

In this assignment, you are tasked with continuing the development of the cinema application.  
The `schemas/movies.py` and `routes/movies.py` files have already been provided as examples of implementation and do not require any changes.  

Your objective is as follows:

1. **Enhancing User Account Functionality**  
   - The `routes/accounts.py` and `schemas/accounts.py` files already contain the necessary logic for user registration, authentication, and account management.  
   - However, some controllers need to be extended to include **email notifications**.  
   - Specifically, email notifications should be sent for:
     - Account activation.
     - Password reset requests.
     - Password reset completions.

2. **Implementing User Profile Management**  
   - The `routes/profiles.py` and `schemas/profiles.py` files require full implementation.  
   - You need to develop the logic for **creating a user profile**, including:
     - Handling user input (first name, last name, gender, date of birth, bio, and avatar image).
     - Validating the profile data.
     - Uploading the avatar image to **MinIO** storage.
     - Storing the profile details in the database.

Your implementation should follow the structure and design patterns demonstrated in the existing movie-related files while ensuring proper validation, security, and database consistency.

### **Tasks: Implementing Email Notifications for User Registration and Password Reset**

To enhance the **user account management** functionality, you need to **integrate email notifications** for key user actions. This will involve modifying the following controllers:

1. **User Registration (`register_user`)**
2. **Account Activation (`activate_account`)**
3. **Password Reset Request (`request_password_reset_token`)**
4. **Password Reset Completion (`reset_password`)**

#### **Using the `EmailSender` Class for Notifications**
- The project already includes an email sending utility: **`EmailSender`**.
- You will use the existing dependency injection function:

  ```python
  def get_accounts_email_notificator(settings: BaseAppSettings = Depends(get_settings)) -> EmailSenderInterface:
      return EmailSender(...)
  ```
  
  This function provides an instance of `EmailSenderInterface`, which is responsible for sending different types of account-related emails.

#### **Modifications Required**
- In each of the four mentioned controllers, you will **add email notifications** using the `EmailSender` instance.
- **Background Tasks** (`BackgroundTasks`) should be used to send emails asynchronously without blocking the main request.

#### **How to Use Background Tasks for Email Sending**
- You need to generate a valid **URL** for the email action (e.g., login page, password reset confirmation).
- Example of sending a password reset completion email:
  
  ```python
  login_link = "http://127.0.0.1/accounts/login/"

  background_tasks.add_task(
      email_sender.send_password_reset_complete_email,
      str(data.email),
      login_link
  )
  ```

  - The `background_tasks.add_task(...)` method schedules the email to be sent in the background.
  - The function `send_password_reset_complete_email` is executed asynchronously.
  - The recipient’s email and the required link are passed as arguments.

#### **Next Steps**
- Modify the controllers (`register_user`, `activate_account`, `request_password_reset_token`, `reset_password`) to include the **email notification logic**.
- Ensure that **valid URLs** are generated for actions like activation and password reset.
- Use **background tasks** to handle email dispatching efficiently.

This implementation will enhance the user experience by providing automated email notifications for critical account-related operations.


### **Task: Implement User Profile Creation and Validation Schema**

The next step in extending the **cinema application** is implementing the functionality for **creating user profiles**. 
This includes defining the necessary validation schema (`schemas/profiles.py`) and implementing the route (`routes/profiles.py`) that handles profile creation.

---

## **1. Profile Schema (`schemas/profiles.py`)**
The **profile schema** defines the structure of the user profile request and response. It must include validation rules to ensure the correctness of user input.

#### **Schema Requirements**
- **Validation must be performed** using functions from the `validation` package:
  ```python
  from validation import (
      validate_name,
      validate_image,
      validate_gender,
      validate_birth_date
  )
  ```
- The schema must allow users to submit their:
  - **First Name** (`first_name`) and **Last Name** (`last_name`) → Must contain only English letters.
  - **Gender** (`gender`) → Must be a valid gender option.
  - **Date of Birth** (`date_of_birth`) → Must be a valid date and the user must be at least **18 years old**.
  - **Info** (`info`) → Cannot be empty or consist only of spaces.
  - **Avatar** (`avatar`) → Must be a valid image file (`JPG, JPEG, PNG`) and not exceed **1MB**.

#### **Example Valid Request**
```json
{
  "first_name": "John",
  "last_name": "Doe",
  "gender": "man",
  "date_of_birth": "1990-01-01",
  "info": "This is a test profile.",
  "avatar": "<binary-image-data>"
}
```

---

## **2. Profile Creation Endpoint (`routes/profiles.py`)**
The `POST /users/{user_id}/profile/` endpoint is responsible for handling **user profile creation**.

### **Endpoint Details**
- **HTTP Method**: `POST`
- **Path**: `/users/{user_id}/profile/`
- **Response**: `ProfileResponseSchema`
- **Authorization**: Requires a valid `Bearer` token in the `Authorization` header.

---

### **3. Endpoint Behavior and Error Handling**

### **1️⃣ Token Validation**
The request must include a **valid authentication token** (`Bearer <token>`).

- **If the token is missing**, return:
  ```json
  {
    "detail": "Authorization header is missing"
  }
  ```
  - **Error Code**: `401 Unauthorized`

- **If the token has an invalid format**, return:
  ```json
  {
    "detail": "Invalid Authorization header format. Expected 'Bearer <token>'"
  }
  ```
  - **Error Code**: `401 Unauthorized`

- **If the token is expired**, return:
  ```json
  {
    "detail": "Token has expired."
  }
  ```
  - **Error Code**: `401 Unauthorized`

---

### **2️⃣ Authorization Rules**
- A **user can only create their own profile** unless they have elevated permissions (e.g., **admin**).
- If a **regular user** tries to create a profile for another user, return:
  ```json
  {
    "detail": "You don't have permission to edit this profile."
  }
  ```
  - **Error Code**: `403 Forbidden`

---

### **3️⃣ User Existence and Status**
- The system checks whether the specified `user_id` **exists** and whether the user is **active**.
- If the user does **not exist** or is **not active**, return:
  ```json
  {
    "detail": "User not found or not active."
  }
  ```
  - **Error Code**: `401 Unauthorized`

---

### **4️⃣ Check for Existing Profile**
- If the user **already has a profile**, return:
  ```json
  {
    "detail": "User already has a profile."
  }
  ```
  - **Error Code**: `400 Bad Request`

---

### **5️⃣ Avatar Upload to S3 Storage**
- The avatar image is **uploaded** using:
  ```python
  s3_client: S3StorageInterface = Depends(get_s3_storage_client)
  ```
- If the upload **fails**, return:
  ```json
  {
    "detail": "Failed to upload avatar. Please try again later."
  }
  ```
  - **Error Code**: `500 Internal Server Error`

---

### **6️⃣ Profile Creation and Storage**
- The profile is stored in the database after passing all validations.
- The final **avatar URL** is generated and included in the response.

#### **Example Successful Response**
```json
{
  "id": 1,
  "user_id": 1,
  "first_name": "john",
  "last_name": "doe",
  "gender": "man",
  "date_of_birth": "1990-01-01",
  "info": "This is a test profile.",
  "avatar": "http://minio-theater/avatars/1_avatar.jpg"
}
```
  - **Status Code**: `201 Created`

---

### **4. Full List of Possible Errors**
| **Error Type**                      | **Message**                                         | **HTTP Status** |
|--------------------------------------|-----------------------------------------------------|-----------------|
| **Missing Token**                    | `"Authorization header is missing"`                 | `401 Unauthorized` |
| **Invalid Token Format**              | `"Invalid Authorization header format. Expected 'Bearer <token>'"` | `401 Unauthorized` |
| **Expired Token**                     | `"Token has expired."`                              | `401 Unauthorized` |
| **Unauthorized Profile Creation**      | `"You don't have permission to edit this profile."` | `403 Forbidden` |
| **User Not Found or Not Active**       | `"User not found or not active."`                  | `401 Unauthorized` |
| **Profile Already Exists**             | `"User already has a profile."`                    | `400 Bad Request` |
| **Avatar Upload Failed**               | `"Failed to upload avatar. Please try again later."` | `500 Internal Server Error` |

---

### **5. Next Steps**
1. **Implement `schemas/profiles.py`**:
   - Define validation rules for profile creation using `pydantic` and custom validation functions.
2. **Implement `routes/profiles.py`**:
   - Implement token validation, authorization, database storage, and avatar upload logic.

This implementation will complete the **user profile management** functionality within the **Movie Theater API**.

### **Tips and Guidance**

If you’re unsure about the expected behavior or need clarification, **refer to the provided test suite**. Running the tests will:

- Show the expected logic and flow for each endpoint.
- Help you identify edge cases and handle errors correctly.
- Ensure your implementation aligns with the project's requirements.

### **Running Tests**

#### **1️⃣ Running Unit and Integration Tests (Without Docker)**
You can run the unit and integration tests **directly** using `pytest`:

```bash
pytest src/tests/test_integration/
```
This will execute **only the integration tests**, ensuring that your API logic functions correctly **without spinning up Docker containers**.

#### **2️⃣ Running End-to-End (E2E) Tests**
To run the full **E2E test suite**, you need to start the test environment using Docker:

```bash
docker-compose -f docker-compose-tests.yml up --build
```
This will spin up all necessary services (database, MinIO, MailHog, FastAPI instance) and execute the **end-to-end tests** inside the test container.

### **Test Results**
- The test logs will **highlight any failures** and discrepancies between your implementation and expected behavior.
- Use the error messages from the test output to **fix issues and adjust your code accordingly**.

By following these steps, you can ensure your implementation is correct and fully aligned with the **Movie Theater API** project requirements.

