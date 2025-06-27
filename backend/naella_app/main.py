from fastapi import FastAPI, HTTPException, status, Body
from pydantic import BaseModel, field_validator
from supabase import create_client, Client
from .models.models import User
from .utils import write_user_to_csv, generate_user_id
import csv
import os

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Missing supabase access information")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


app = FastAPI()


# TODO: move the class to the models.py
class UserCreateRequest(BaseModel):
    name: str
    last_name: str
    gender: str
    age: int
    height: int
    current_weight: float
    ideal_weight: float
    physical_activity_score: float

    @field_validator("age")
    def age_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError("Age must be a positive integer")
        return value


# Suggested by copilot maybe check what ios the standard validators. Do it in the front end?
class SignUpRequest(BaseModel):
    email: str
    password: str

    @field_validator("email")
    def email_must_be_valid(cls, value):
        if "@" not in value or "." not in value:
            raise ValueError("Invalid email format")
        return value

    @field_validator("password")
    def password_must_not_be_empty(cls, value):
        if not value:
            raise ValueError("Password cannot be empty")
        return value


@app.post("/api/auth/sign-up", status_code=status.HTTP_201_CREATED)
async def sign_up(request: SignUpRequest = Body(...)):
    """
    Endpoint to handle user sign-up and creation in supabase.
    """
    try:
        response = supabase.auth.sign_up(
            {
                "email": request.email,
                "password": request.password,
            }
        )
        if response.get("user"):
            return {"message": "User created successfully"}
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=response.get("error", "Failed to create user"),
            )

    except Exception as e:
        print(f"Error during sign-up: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )


# @app.post("/users", response_model=User)
# async def create_user(user: UserCreateRequest):
#     """
#     Create a new user and calculate their nutritional needs.
#     """
#     user_id = generate_user_id()
#     user = User.from_user_input(
#         name=user.name,
#         last_name=user.last_name,
#         id=user_id,
#         gender=user.gender,
#         age=user.age,
#         height=user.height,
#         current_weight=user.current_weight,
#         ideal_weight=user.ideal_weight,
#         physical_activity_score=user.physical_activity_score,
#     )
#     try:
#         if write_user_to_csv(user):
#             return {"message": "User created successfully", "user": user.__dict__}

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
async def health_check():
    """
    Health check endpoint to verify if the service is running.
    """
    return {"status": "ok"}
