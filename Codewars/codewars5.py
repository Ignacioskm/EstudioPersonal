# Write function bmi that calculates body mass index (bmi = weight / height2).
# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"
# if bmi > 30 return "Obese"

def bmi(weight, height):
    bmi = float(weight / (height * height))
    if bmi <= 18.5:
        condición = "Underweight"
    elif bmi <= 25:
        condición = "Normal"
    elif bmi <= 30:
        condición = "Overweight"
    elif bmi > 30:
        condición = "Obese"
    return f"{condición}, For weight = {weight} and height = {height}"

#Test
# print(bmi(80,1.80))