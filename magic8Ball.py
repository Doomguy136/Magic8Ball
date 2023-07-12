import random
import sys


def getMagicAnswers():
    try:
        file = open("magicAnswers.txt", "r")
        magicAnswers = file.readlines()
    except FileNotFoundError:
        print("Make sure you have the magicAnswers.txt in this folder!")
        sys.exit()
    return magicAnswers


def main(magicAnswers):
    userInput = str()
    while userInput != "q":
        print("Ask me a question! or (q)uit")
        userInput = input()
        if userInput == "q":
            print("Goodbye!")
            break

        answer = random.choice(magicAnswers)
        print(answer)


if __name__ == "__main__":
    magicAnswers = getMagicAnswers()
    main(magicAnswers)
