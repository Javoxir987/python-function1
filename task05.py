def check_guess(secret, guess):
    return secret == guess

def print_result(is_correct):
    if is_correct:
        print("Tabriklaymiz! Togri topdingiz.")
    else:
        print("Xato! Qaytadan urinib ko'ring.")

sirli_son = 7
taxmin = int(input("1 dan 10 gacha bo'lgan sirli sonni taxmin qiling: "))

natija = check_guess(sirli_son, taxmin)
print_result(natija)