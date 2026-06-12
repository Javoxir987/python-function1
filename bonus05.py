def is_palindrome(text):
    clean_text = text.lower()
    reversed_text = clean_text[::-1]
    
    if clean_text == reversed_text:
        return True
    else:
        return False

print(is_palindrome("Non"))
print(is_palindrome("Python"))