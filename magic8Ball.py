import random


def getMagicAnswers():
    try:
        file = open("magicAnswers.txt", "r")
        magicAnswers = file.readlines()
    except FileNotFoundError:
        print("magicAnswers not found, creating magicAnswers.txt in this directory")
        backup = open("magicAnswers.txt", "w")
        backup.write('''It is certain
It is decidedly so
Yes
Reply hazy try again
Ask again later
Concentrate and ask again
My reply is no
Outlook not so good
Very doubtful
''')
        backup.close()
        backup = open("magicAnswers.txt", "r")
        magicAnswers = backup.readlines()
        return magicAnswers
    return magicAnswers


def main(magicAnswers):
    userInput = str()
    while userInput != "q":
        print("Ask me a question! or (q)uit")
        userInput = input()
        if userInput.lower() == "q":
            print("Goodbye!")
            break

        answer = random.choice(magicAnswers)
        print(answer)


if __name__ == "__main__":
    magicAnswers = getMagicAnswers()
    main(magicAnswers)
