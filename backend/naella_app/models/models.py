class User:
    def __init__(
        self,
        name,
        gender,
        age,
        height,
        current_weight,
        ideal_weight,
        fisical_activity_score,
    ):
        self.name = name
        self.gender = gender
        self.age = age
        self.height = height
        self.current_weight = current_weight
        self.ideal_weight = ideal_weight
        self.fisical_activity_score = fisical_activity_score
        self.bmr = self.calculate_bmr()
        self.calories = self.calculate_calories()
        self.protein = self.calculate_protein()
        self.carbohydrates = self.calculate_carbohydrates()
        self.fats = self.calculate_fats()

    def calculate_bmr(self):
        bmr = 9.99 * self.ideal_weight + 6.25 * self.height - 4.92 * self.age
        return bmr - 161

    def calculate_calories(self):
        return self.bmr * self.fisical_activity_score

    def calculate_protein(self):
        return self.calories * 0.25 / 4

    def calculate_carbohydrates(self):
        return self.calories * 0.35 / 4

    def calculate_fats(self):
        return self.calories * 0.40 / 9
