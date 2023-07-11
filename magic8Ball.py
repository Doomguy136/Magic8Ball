import random

file = open("magicAnswers.txt", "r")
read = file.readlines()
magic_answers = []
for line in read:
    if line[-1] == "\n":
        magic_answers.append(line[:-1])
    else:
        magic_answers.append(line)
    


def main():
    user_input = str()
    while user_input != "q":
        print("Ask me a question! or (q)uit")
        user_input = input()
        if user_input == "q":
            print("Goodbye!")
            break

        answer = random.choice(magic_answers)
        print(answer)


if __name__ == "__main__":
    main()
