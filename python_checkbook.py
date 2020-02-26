# python checkbook

def get_balance():
    with open("transactions.txt", "r") as f:
        balance = f.readlines()
        return(balance)

def withdraw():
    amount = -1*float(input("How much would you like to withdraw? "))
    with open("transactions.txt", "a") as f:
        f.write(f"\n{amount}")
        return amount

def deposit():
    amount = float(input("How much would you like to deposit? "))
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

    #         user_choice = input("Do you want to continue? Type y or Yes. ")
    #         wants_to_stop = user_choice.lower() not in ["y", "yes"]
    #         if wants_to_stop:
    #             break

    user_choice = input("Type choice here : ")
    while user_choice.isdigit() == False or int(user_choice) > 5 or int(user_choice) < 0:
        print(f"{user_choice} is an invalid input. Please input a choice from the menu")
        user_choice = input("Type choice here : ")
    user_choice = int(user_choice)
    if user_choice == 1:
        print(get_balance())
    elif user_choice == 2:
        withdraw()
    elif user_choice == 3:
        deposit()
    elif user_choice == 4:
        user_choice = input("Do you want to continue? Type y or Yes. ")
        wants_to_stop = user_choice.lower() not in ["y", "yes"]
        if wants_to_stop:
            break


# def get_balance():
#      with open("transactions.txt", "r") as f:
#          balance = f.readlines()
#          return(balance)


# def withdraw():
#     amount = float(input("How much would you like to withdraw? "))
#     current_balance = 0
#     print(f"Your new balance is now {current_balance - amount}")
# withdraw()

# def deposit():
#     amount = float(input("How much would you like to deposit? "))
#     current_balance = 0
#     print(f"Your new balance is now {amount + current_balance}")
# deposit() 