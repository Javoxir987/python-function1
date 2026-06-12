def calculate_tax(salary):
    if salary > 5000000:
        return salary * 0.20
    else:
        return salary * 0.13

def calculate_net_salary(salary):
    tax = calculate_tax(salary)
    return salary - tax

salary_amount = 6000000
print("Soliq miqdori:", calculate_tax(salary_amount))
print("Qo'lga tegadigan maosh:", calculate_net_salary(salary_amount))