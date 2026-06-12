def calculate_age(birth_year, current_year):
    age = current_year - birth_year
    return age

birth_year = int(input("Tug'ilgan yilingizni kiriting: "))
current_year = 2026

yosh = calculate_age(birth_year, current_year)
print(f"Sizning yoshingiz: {yosh} da.")

if yosh >= 18:
    print("Siz balogatga yetgansiz.")
else:
    print("Siz balogatga yetmagansiz.")