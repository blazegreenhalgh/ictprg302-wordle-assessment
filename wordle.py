import random

with open("sources/all_words.txt") as file:
    all_words = file.read().splitlines()
    for word in all_words:
        word.strip()

with open("sources/target_words.txt") as file:
    target_words = file.read().splitlines()
    for word in target_words:
        word.strip()

format_colours = {
    "green": {"start": '\x1b[6;30;42m', "end": '\x1b[0m'},
    "yellow": {"start": "\33[43m", "end": "\33[0m"}
}

def score_guess(guess, target):
    """ This functions takes two strings (guess, target) and determines if each character from one matches in value and position with the other.
    1 = Value match, 2 = Value and Position match. A list is returned with items equal to the length of the target string."""
    score = [0] * len(target)
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
    formatted_guess = list(guess)
    for i, letter in enumerate(formatted_guess):
        if score[i] == 1:
            formatted_guess[i] = f"{format_colours['yellow']['start']} {letter.upper()} {format_colours['yellow']['end']}"
        elif score[i] == 2:
            formatted_guess[i] = f"{format_colours["green"]["start"]} {letter.upper()} {format_colours["green"]["end"]}"
        else:
            formatted_guess[i] = f" {letter.upper()} "
    return formatted_guess


def play():
    print("\n--------------------")
    print("Welcome to CLI Wordle!")
    # TODO: Make 'CLI Wordle' have different colours per letter
    print("You have 6 attempts to guess the secret word!\n")
    print(f"{format_colours['yellow']['start']}   {format_colours['yellow']['end']} = Correct letter, wrong position")
    print(f"{format_colours['green']['start']}   {format_colours['green']['end']} = Correct letter, correct position")
    print("--------------------\n")
    target_word = random.choice(target_words).upper()
    attempts = 6
    print("What is your 5-letter guess?")
    while True:
        print(f"{attempts} Attempts remaining...")
        input_guess = input("> ").lower()
        if input_guess == "help":
            help_message(target_word)
            continue
        if len(input_guess) < len(target_word):
            print(f"Too short! Must be {len(target_word)} letters!")
            continue
        if len(input_guess) > len(target_word):
            print(f"Too long! Must be {len(target_word)} letters!")
            continue
        if input_guess not in all_words:
            print("Not a valid word!")
            continue
        score = score_guess(input_guess, target_word)
        print(*format_score(score, input_guess))
        if score == [2, 2, 2, 2, 2]:
            print("You guessed the target word! 🎉\n")
            end_game()
            break

        attempts -= 1
        if attempts == 0:
            print("\n--------------------")
            print("You lost!")
            print(f"The word was {format_colours['green']['start']} {target_word} {format_colours['green']['end']}")
            print("--------------------\n")
            end_game()
            break


def help_message(target):
    print("\n--------------------")
    print(f"I'll give you a hint: {target}")
    print("--------------------\n")



def end_game():
    print("Would you like to play again?")
    input_restart = input("> ").strip().lower()
    if input_restart[0] == 'y':
        play()
    else:
        print("Thanks for playing!")




play()

