def get_grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 75 <= score < 90:
        return 'B'
    elif 60 <= score < 75:
        return 'C'
    elif 0 <= score < 60:
        return 'F'
    else:
        return "Noto'g'ri ball kiritildi!"

ball = int(input("Ballingizni kiriting (0-100): "))
baho = get_grade(ball)
print(f"Sizning bahoingiz: {baho}")