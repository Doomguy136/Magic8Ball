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
    user_input = str()
    while user_input != "q":
        print("Ask me a question! or (q)uit")
        user_input = input()
        if user_input == "q":
            print("Goodbye!")
            break

        answer = random.choice(magicAnswers)
        print(answer)


if __name__ == "__main__":
    magicAnswers = getMagicAnswers()
    main(magicAnswers)
