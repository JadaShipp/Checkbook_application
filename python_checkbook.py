# python checkbook
print()
print()
print("Salutations! Welcome to your checkbook.")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()
print()

print("Please make a choice from the following options:")

print("To check your balance, type 1")
print("To make a withdrawl, type 2")
print("To make a deposit, type 3")
print("To exit this application, type 4")


def display_balance():
    user_choice = input("Type choice here : ")
    while (user_choice.isdigit() == False  
        or int(user_choice) > 5 
        or int(user_choice < 0)):   
        print(f"{user_choice} is an invalid input. Please input a choice from the menu")
    user_choice = input("Type choice here : ")
    return user_choice

display_balance()


with open("transactions.txt", "r") as f:
    contents = f.read()
    print(contents)

def deposit():
    amount = float(input("How much would you like to deposit? "))
    current_balance = 0
    print(f"Your new balance is now {amount + current_balance}")
deposit()

def withdraw():
     amount = float(input("How much would you like to withdraw? "))
     current_balance = 0
     print(f"Your new balance is now {current_balance - amount}")
withdraw()

user_choice = user_choice = input("Type choice here : ")
    while (user_choice.isdigit() == False  
        or int(user_choice) > 5 
        or int(user_choice < 0)): 