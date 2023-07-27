import random


def getMagicAnswers():
    try:
        file = open("magicAnswers.txt", "r")
        magicAnswers = file.readlines()
        file.close()
    except FileNotFoundError:
        print("magicAnswers not found, creating magicAnswers.txt in this directory")
        backup = open("magicAnswers.txt", "w")
        backup.write(defaultAnswers)
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


defaultAnswers = ('''It is certain
It is decidedly so
Yes
Reply hazy try again
Ask again later
Concentrate and ask again
My reply is no
Outlook not so good
Very doubtful
''')

if __name__ == "__main__":
    answers = getMagicAnswers()
    main(answers)
