def c_to_f(celsius):
    return celsius * 1.8 + 32

def f_to_c(fahrenheit):
    return (fahrenheit - 32) / 1.8

c_harorat = 25
f_harorat = c_to_f(c_harorat)
print(f"{c_harorat}°C = {f_harorat}°F")

f_harorat_2 = 98.6
c_harorat_2 = f_to_c(f_harorat_2)
print(f"{f_harorat_2}°F = {c_harorat_2:.1f}°C")