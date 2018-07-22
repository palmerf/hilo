import random


def main():
    print("Welcome to the HI - LO game")

    num = random.randint(1, 100)

    correct = False

    while not correct:
        guess = int(input("Guess a number between 1 & 100: "))

        if guess == num:
            print("Got it: The number is {}".format(num))
            correct = True
        elif guess < num:
            print("Too low!")
        else:
            print("Too high!")


if __name__ == '__main__':
    main()
