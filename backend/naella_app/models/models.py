from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    last_name: str
    gender: str
    age: int
    height: float
    current_weight: float
    ideal_weight: float
    physical_activity_score: float
    bmr: float
    calories: float
    protein: float
    carbs: float
    fats: float

    @classmethod
    def from_user_input(
        cls,
        id,
        name,
        last_name,
        gender,
        age,
        height,
        current_weight,
        ideal_weight,
        physical_activity_score,
    ):
        bmr = (9.99 * ideal_weight) + (6.25 * height) - (4.92 * age) - 161
        calories = bmr * physical_activity_score
        protein = calories * 0.25 / 4
        carbs = calories * 0.35 / 4
        fats = calories * 0.4 / 9
        return cls(
            id=id,
            name=name,
            last_name=last_name,
            gender=gender,
            age=age,
            height=height,
            current_weight=current_weight,
            ideal_weight=ideal_weight,
            physical_activity_score=physical_activity_score,
            bmr=bmr,
            calories=calories,
            protein=protein,
            carbs=carbs,
            fats=fats,
        )
