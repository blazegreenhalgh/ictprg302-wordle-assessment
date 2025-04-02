def help_message():
    attempts = 6
    print("<< Welcome to CLI Wordle! >>")
    print("You have 6 attempts to guess the secret word!")


import random

with open("sources/all_words.txt") as file:
    all_words = file.read().splitlines()
    for word in all_words:
        word.strip()

with open("sources/target_words.txt") as file:
    target_words = file.read().splitlines()
    for target_word in target_words:
        target_word.strip()

target_word = random.choice(target_words)
score = [0] * len(target_word)


def score_guess(guess, target):
    """ This functions takes two strings (guess, target) and determines if each character from one matches in value and position with the other.
    1 = Value match, 2 = Value and Position match. A list is returned with items equal to the length of the target string."""
    guess_letters = list(guess.lower())
    target_letters = list(target.lower())
    # Finding correct pos chars first
    for guess_index, guess_letter in enumerate(guess_letters):
        if guess_letter == target_letters[guess_index]:
            score[guess_index] = 2
            # Replace duplicates with incorrect value after correct pos is found
            target_letters[guess_index] = None
            guess_letters[guess_index] = None


    # Finding incorrect pos chars after finding correct pos
    for guess_index, guess_letter in enumerate(guess_letters):
        if guess_letter in target_letters and guess_letter is not None:
            score[guess_index] = 1
            # Replace duplicates with incorrect value after correct pos is found
            target_index = target_letters.index(guess_letter)
            target_letters[target_index] = None

    return score

def format_score(score, guess):
    yellow = {"start": "\33[43m", "end": "\33[0m"}
    green = {"start": '\x1b[6;30;42m', "end": '\x1b[0m'}
    formatted_guess = list(guess)
    for i, letter in enumerate(formatted_guess):
        if score[i] == 1:
            formatted_guess[i] = f"{yellow["start"]} {letter} {yellow["end"]}"
        elif score[i] == 2:
            formatted_guess[i] = f"{green["start"]} {letter} {green["end"]}"
        else:
            formatted_guess[i] = f" {letter} "
    return formatted_guess






def guess():
    while True:
        attempts = 6
        print(f"{attempts} Attempts remaining...")
        print("What is your 5-letter guess?")
        input_guess = input("> ").lower()
        if len(input_guess) < 5:
            print("Too short! Must be 5 letters!")
            continue
        if len(input_guess) > 5:
            print("Too long! Must be 5 letters!")
            continue
        score = score_guess(input_guess, target_word)
        print(*format_score(score, input_guess))

help_message()
guess()




# guess = "bca"
# target = "bba"
#
# print("FINAL SCORE: ", score_guess(guess, target))



