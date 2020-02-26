# python checkbook

def get_balance():
    transactions = get_transactions()
    total = 0
    for transaction in transactions:
        transaction = transaction.replace("\n","")
        transaction = float(transaction)
        total = total + transaction
    return total

def get_transactions():
    with open("transactions.txt", "r") as f:
        balance = f.readlines()
        return(balance)

def withdraw():
    amount = -1*float(input("How much would you like to withdraw? "))
    print()
    with open("transactions.txt", "a") as f:
        f.write(f"\n{amount}")
        return amount

def deposit():
    amount = float(input("How much would you like to deposit? "))
    print()
    with open("transactions.txt", "a") as f:
        f.write(f"\n{amount}")
        return amount


print()
print()
print("Salutations! Welcome to your checkbook.")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()
print()

while True:
    print()
    print("Please make a choice from the following options:")

    print("To check your balance, type 1")
    print("To make a withdrawl, type 2")
    print("To make a deposit, type 3")
    print("To exit this application, type 4")


    user_choice = input("Type choice here : ")
    while user_choice.isdigit() == False or int(user_choice) > 5 or int(user_choice) < 0:
        print(f"{user_choice} is an invalid input. Please input a choice from the menu")
        user_choice = input("Type choice here : ")
    print()
    user_choice = int(user_choice)
    if user_choice == 1:
        print(f"Your current balance is ${get_balance()}")
    elif user_choice == 2:
        print(f"Your account has been debited ${withdraw()}")
    elif user_choice == 3:
        print(f"You have just deposited ${deposit()}")
    elif user_choice == 4:
        user_choice = input("Are you sure you want to exit? Type Y or Yes. ")
        wants_to_stop = user_choice.lower() in ["y", "yes"]
        if wants_to_stop:
            break 