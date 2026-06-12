def calculate_bmi(weight, height):
    return weight / (height * height)

def bmi_status(bmi):
    if bmi < 18.5:
        return "Vazn yetishmovchiligi"
    elif bmi < 25.0:
        return "Normal vazn"
    elif bmi < 30.0:
        return "Ortiqcha vazn"
    else:
        return "Semizlik"

current_bmi = calculate_bmi(70, 1.75)
print("Sizning indeksingiz:", current_bmi)
print("Holatingiz:", bmi_status(current_bmi))