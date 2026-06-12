def check_answer(user_answer, correct_answer):

    return user_answer.strip().lower() == correct_answer.lower()

def ask_question(question: str, correct_answer: str):
    print(f"Savol: {question}")
    javob = input("Sizning javobingiz: ")
    
    if check_answer(javob, correct_answer):
        print("Togri")
    else:
        print(f"Xato! Togri javob: {correct_answer} edi.")

ask_question("O'zbekistonning poytaxti qaysi shahar?", "Toshkent")
ask_question("Python dasturlash tili nechanchi yilda yaratilgan?", "1991")