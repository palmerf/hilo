import random


def main():
    print("Welcome to the HI - LO game")

    num = random.randint(1, 100)

    guess = -1

    while guess != num:
        guess = int(input("Guess a number between 1 & 100: "))

        if guess == num:
            print("Got it: The number is {}".format(num))
        elif guess < num:
            print("Too low!")
        else:
            print("Too high!")


if __name__ == '__main__':
    main()
