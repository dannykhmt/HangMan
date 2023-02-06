# Write your code here
from random import choice
print("H A N G M A N")
nb_won = 0
nb_lost = 0

def convert(string):
    list1 = []
    list1[:0] = string
    return list1


def catch_error(string):
    if (len(string) > 1) or (len(string) == 0):
        print('Please, input a single letter.')
        return -1
    if not (string.isalpha()) or string.isupper():
        print('Please, enter a lowercase letter from the English alphabet.')
        return -1
    return 0


def menu():
    # function menu
    action = input("Type \"play\" to play the game, \"results\" to show the scoreboard, and \"exit\" to quit: ")
    return action


def main_module():
    my_list = ['python', 'java', 'swift', 'javascript']

    answer = choice(my_list)
    answer_hide = (len(answer)) * '-'
    word_list = convert(answer)
    nb_attempt = 7
    letters_guessed = []
    global nb_lost
    global nb_won


    while nb_attempt >= 0:

        print()
        print(answer_hide)

        my_input = input("Input a letter : ")
        err = catch_error(my_input)

        if err != -1:

            if my_input in letters_guessed:
                print("You've already guessed this letter.")

            letters_guessed.append(my_input)

            index = answer.find(my_input)
            indices = [index for index, element in enumerate(word_list) if element == my_input]

            if len(indices):
                for k in indices:
                    answer_hide = answer_hide[:k] + my_input + answer_hide[k + 1:]
            else:
                print("That letter doesn't appear in the word")
                nb_attempt = nb_attempt - 1

        if nb_attempt == -1:
            print("You lost!")
            nb_lost = nb_lost + 1
            return nb_lost

        if "-" not in answer_hide:
            print("You guessed the word " + answer_hide + "! ")
            print("You survived!")
            nb_won = nb_won + 1
            nb_attempt = -1
            return nb_won


again = True
while again:

    action = menu()

    if action == "play":
        main_module()

    if action == "results":
        print("You won: " + str(nb_won) + " times. ")
        print("You lost: " + str(nb_lost) + " times. ")

    if action == "exit":
        again = False
