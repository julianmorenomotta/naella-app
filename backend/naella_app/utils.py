import csv
import uuid
from .models.models import User
from dotenv import load_dotenv
import os
import logging

load_dotenv()

FILEPATH = os.environ.get("DATABASE_LOCAL_FILEPATH")


def write_user_to_csv(user: User):
    if not os.path.exists(FILEPATH):
        generate_csv_file(FILEPATH)

    logging.info(f"Writing user {user.id} to CSV file {FILEPATH}")
    with open(FILEPATH, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                user.id,
                user.last_name,
                user.name,
                user.gender,
                user.age,
                user.height,
                user.current_weight,
                user.ideal_weight,
                user.physical_activity_score,
                user.bmr,
                user.calories,
                user.protein,
                user.carbs,
                user.fats,
            ]
        )
    return True


def generate_user_id():
    """
    Generate a unique user ID.
    """
    user_id = str(uuid.uuid4())
    return user_id


def get_exisiting_ids():
    """
    Get existing user IDs from the CSV file.
    """
    existing_ids = set()
    try:
        with open(FILEPATH, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    existing_ids.add(row[0])
    except FileNotFoundError:
        print(f"File {FILEPATH} not found. Creating csv file...")
        generate_csv_file()
    return existing_ids


def generate_csv_file(filepath):
    """
    Generate the CSV file with headers if it does not exist.
    """
    logging.warning(f"Generating CSV file at {filepath} with headers.")
    with open(filepath, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                "id",
                "last_name",
                "name",
                "gender",
                "age",
                "height",
                "current_weight",
                "ideal_weight",
                "fisical_activity_score",
                "bmr",
                "calories",
                "protein",
                "carbs",
                "fats",
            ]
        )
    print(f"CSV file {filepath} created with headers.")
