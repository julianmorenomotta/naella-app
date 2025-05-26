class User:
    def __init__(
        self,
        id,
        name,
        last_name,
        gender,
        age,
        height,
        current_weight,
        ideal_weight,
        fisical_activity_score,
    ):
        self.name = name
        self.last_name = last_name
        self.id = id
        self.gender = gender
        self.age = age
        self.height = height
        self.current_weight = current_weight
        self.ideal_weight = ideal_weight
        self.fisical_activity_score = fisical_activity_score
        self.bmr = self.calculate_bmr()
        self.calories = self.calculate_calories()
        self.protein = self.calculate_protein()
        self.carbs = self.calculate_carbs()
        self.fats = self.calculate_fats()

    def calculate_bmr(self):
        bmr = (9.99 * self.ideal_weight) + (6.25 * self.height) - (4.92 * self.age)
        bmr = bmr - 161
        return bmr

    def calculate_calories(self):
        return self.bmr * self.fisical_activity_score

    def calculate_protein(self):
        return self.calories * 0.25 / 4

    def calculate_carbs(self):
        return self.calories * 0.35 / 4

    def calculate_fats(self):
        return self.calories * 0.40 / 9
