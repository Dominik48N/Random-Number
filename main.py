import random


def generateRandomNumber():
    return random.randint(int(minimum), int(maximum))


if __name__ == "__main__":
    print("Please enter the minimum and maximum number for the random generator.")

    minimum = input("What should the minimum number be? ")
    maximum = input("What should the maximum number be? ")

    if minimum.strip().isdigit():

        if maximum.strip().isdigit():

            if minimum > maximum:
                print("The maximum number must be higher than the minimum number.")
            else:
                print("The random number between " + minimum + " and " + maximum + " is",
                      int(generateRandomNumber()))
        else:
            print("Please enter a number as maximum.")

    else:
        print("Please enter a number as a minimum.")
