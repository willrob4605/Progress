def main():
    while True:
        try:
            num1 = float(input("Enter your first number: "))
        except ValueError:
            print("Enter a valid input")
        else:
            break

    while True:
        print("\nChoose your operation:")
        print("1. +")
        print("2. -")
        print("3. /")
        print("4. *")
        print("5. quit")

        choice = input("Enter choice (1-5): ")
        if choice.lower() == "quit":
            print("Quitting")
            break

        try:
            choice_num = int(choice)
        except ValueError:
            print("Invalid input. Please enter a number or 'quit'.")
            continue

        if choice_num < 1 or choice_num > 5:
            print("Invalid Choice")
            continue
        if choice_num == 5:
            print("Quitting")
            break

        try:
            num2 = float(input("Enter next number: "))
        except ValueError:
            print("Enter a valid number")
            continue

        result = 0
        if choice_num == 1:
            result = num1 + num2
        elif choice_num == 2:
            result = num1 - num2
        elif choice_num == 3:
            try:
                result = num1 / num2
            except ZeroDivisionError:
                print("You cannot divide by zero.")
                continue
        elif choice_num == 4:
            result = num1 * num2
        else:
            print("Invalid choice.")
            continue

        print(f"The Result is {result}")
        print("1. Continue using the result")
        print("2. Start with a new first number")
        choice2 = input("Choose next step (1 or 2): ")

        if choice2 == '1':
            num1 = result
        else:
            while True:
                try:
                    num1 = float(input("Enter your new first number: "))
                except ValueError:
                    print("Enter a valid number")
                else:
                    break

main()