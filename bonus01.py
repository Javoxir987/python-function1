def check_balance(balance):
    print("Sizning balansingiz:", balance, "so'm")

def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    if amount <= balance:
        return balance - amount
    else:
        print("Mablag' yetarli emas.")
        return balance

my_balance = 50000
my_balance = deposit(my_balance, 20000)
my_balance = withdraw(my_balance, 30000)
check_balance(my_balance)