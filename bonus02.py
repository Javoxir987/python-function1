def is_strong_password(password):
    if len(password) < 8:
        return False
        
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            
    return has_digit

print(is_strong_password("Qwerty1234"))
print(is_strong_password("12345"))