# age_validator.py
# Karm Patel 
# ICE 3 
# Description: Making the class of Agevalidator. 

class AgeValidator:
    def validate_age(self, age):
        # Rule: Age must be an integer
        if not isinstance(age, int):
            raise TypeError("Age must be an integer.")

        MIN_AGE = 18
        MAX_AGE = 65

        return MIN_AGE <= age <= MAX_AGE