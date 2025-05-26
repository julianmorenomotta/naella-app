from fastapi import FastAPI, HTTPException
from .models.models import User
from .utils import write_user_to_csv, generate_user_id
import csv

app = FastAPI()


@app.post("/users")
async def create_user(
    name: str,
    last_name: str,
    gender: str,
    age: int,
    height: float,
    current_weight: float,
    ideal_weight: float,
    fisical_activity_score: float,
):
    """
    Create a new user and calculate their nutritional needs.
    """
    user_id = generate_user_id()
    user = User(
        name=name,
        last_name=last_name,
        id=user_id,
        gender=gender,
        age=age,
        height=height,
        current_weight=current_weight,
        ideal_weight=ideal_weight,
        fisical_activity_score=fisical_activity_score,
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
