from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
from .models.models import User
from .utils import write_user_to_csv, generate_user_id
import csv

app = FastAPI()


class UserCreateRequest(BaseModel):
    name: str
    last_name: str
    gender: str
    age: int
    height: int
    current_weight: float
    ideal_weight: float
    fisical_activity_score: float

    @field_validator("age")
    def age_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError("Age must be a positive integer")
        return value


@app.post("/users")
async def create_user(user: UserCreateRequest):
    """
    Create a new user and calculate their nutritional needs.
    """
    user_id = generate_user_id()
    user = User(
        name=user.name,
        last_name=user.last_name,
        id=user_id,
        gender=user.gender,
        age=user.age,
        height=user.height,
        current_weight=user.current_weight,
        ideal_weight=user.ideal_weight,
        fisical_activity_score=user.fisical_activity_score,
    )
    try:
        if write_user_to_csv(user):
            return {"message": "User created successfully", "user": user.__dict__}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
async def health_check():
    """
    Health check endpoint to verify if the service is running.
    """
    return {"status": "ok"}
