# I want to use this to validat the input and stop users from being able to input a string. 
# I also considered simply exiting the app if a string in input vs. forcing a valid input but that feels a little hacky
    # while user_choice.isdigit() == False:
    #     print("Invalid. Input must be a number")
    #     user_choice = input("Type choice here : ")



def get_balance():
    f = open("transactions_list.txt", "r")
    transactions = f.readlines()                                                                                                                                                                      
    total = 0
    for transaction in transactions:
        transaction = transaction.replace("\n","")
        transaction = float(transaction)
        total = total + transaction
    return total

def get_transactions():
    with open("transactions_list.txt", "a") as f:
        balance = f.readlines()
        return balance

def withdraw():
    amount = float(input("How much would you like to withdraw? "))
    print()
    with open("transactions_list.txt", "a") as f:
        f.write(f"\n{amount}")
        return amount

def deposit():
    amount = input("How much would you like to deposit? ")
    print()
    while amount.isdigit() == False:
        print(f"{amount} is an invalid choice. Please input a number ")
        amount = input("Input here ")
        amount = float(amount)
        with open("transactions_list.txt", "a") as f:
            f.write(f"\n{amount}")
            return amount

# def deposit():
#     amount = float(input("How much would you like to deposit? "))
#     print()
#     with open("transactions_list.txt", "a") as f:
#         f.write(f"\n{amount}")
#         return amount


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

    print()
    print()

    while user_choice.isdigit() == False or int(user_choice) >= 5 or int(user_choice) < 0:
        print(f"{user_choice} is an invalid choice. Please input a choice from the menu")
        user_choice = input("Type choice here : ")


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