import random
def Main():
    while True:
        first=True
        guess=None
        Total=0
        limit=7
        print("Welcome to the number Guessing game!")
        print(f"You will guess a random number in {limit} amount of tries")
        while True:
            while True:
                try:
                    lower=int(input("Now enter the lower end of the range: "))
                    break
                except ValueError:
                    print("Enter a valid number")

            while True:
                try:
                    upper=int(input("Now enter the upper end of the range: "))
                    break
                except ValueError:
                    print("Enter a valid number")
            if first:
                try:
                    number_to_guess=random.randint(lower,upper)
                    first=False
                    break
                except ValueError:
                    print("Enter a valid range")
        while True:
            if Total==limit:
                print(f"You have ran out of tries the number was {number_to_guess}")
                ans=input("Do you wish to play again(Y/N)? ")
                if ans=="Y":
                    continue
                else:
                    break
            while True:
                try:
                    guess=int(input("Now enter your guess: "))
                    Total=Total+1
                    break
                except ValueError:
                    print("Enter a valid guess")
                    continue

            if guess==number_to_guess:
                print(f"Congratulations on guessing the correct number {number_to_guess} in {Total} tries!")
                ans=input("Do you wish to play again(Y/N)? ")
                if ans=="Y":
                    continue
                else:
                    break
            if guess<number_to_guess:
                print("The guess is to low")
                continue
            else:
                print("The guess is too high")
                continue
Main()