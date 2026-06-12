def is_valid_phone_number(phone):
    return phone.isdigit() and len(phone) == 9

raqam = input("Telefon raqamingizni kiriting: ")

if is_valid_phone_number(raqam):
    print("Telefon raqami togri kiritildi.")
else:
    print("Xato! Raqam faqat 9 ta raqamdan iborat bolishi kerak.")