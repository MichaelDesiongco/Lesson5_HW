# 1 

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try: 
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

def calculator():
    print("Select an operation: ")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    operation = input("Enter the number corresponding to the operation: ")

    if operation not in ['1','2','3','4']:
        print("Invalid operation try again.")
        return
    
    try: 
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    
    if operation == '1':
        print(f"The result is: {add(num1,num2)}")
    elif operation == '2':
        print(f"The result is: {subtract(num1, num2)}")
    elif operation == '3':
        print(f"The result is: {multiply(num1,num2)}")
    elif operation == '4':
        print(f"The result is: {divide(num1,num2)}")

calculator()


# 2

shopping_list = []

def add_item(item):
    global shopping_list
    shopping_list.append(item)

def remove_item(item):
    global shopping_list
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from your list.")
    else:
        print(f"{item} is not in your list.")

def print_list():
    global shopping_list
    if shopping_list:
        print("\nYour Shopping list: ")
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")
        print()
    else:
        print("Your shopping list is currently empty.")
    
def shopping_list_manager():
    while True:
        action = input("Choose an action: [A]dd item, [R]emove item, [D]isplay item, [Q]uit: ").upper()
        if action == 'A':
            item = input("Enter the item to add to your shopping list: ")
            add_item(item)
            print(f"{item} has been added to your shopping list.")
        elif action == 'R':
            item = input("Enter the item you want to remove from your shopping list: ")
            remove_item(item)
        elif action == 'D':
            print_list()
        elif action == 'Q':
            break
        else:
            print("Invalid action. Please choose again.")

shopping_list_manager()

