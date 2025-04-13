# TODO: Implement achievements
# TODO: Implement Hot seat 2-player mode (P1 sets word, P2 guesses)

import random

with open("sources/all_words.txt") as file:
    all_words = file.read().splitlines()

with open("sources/target_words.txt") as file:
    target_words = file.read().splitlines()


format_colours = {
    "green": {"start": '\x1b[6;30;42m', "end": '\x1b[0m'},
    "yellow": {"start": "\33[43m", "end": "\33[0m"}
}

game_running = True

def is_winner(score, target):
    if score == [2] * len(target):
        return True

def score_guess(guess, target):
    """Determines if each character from one matches in value and position with the other.
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
    return ' '.join(formatted_guess)

def append_grid(score, grid):
    share_row = []
    for number in score:
        if number == 2:
            share_row.append("🟩")
        if number == 1:
            share_row.append("🟨")
        if number == 0:
            share_row.append("⬜")
    string_share_row = ' '.join(share_row)
    grid.append(f"{string_share_row}")
    grid = '\n'.join(grid)
    return grid

def append_guess_history(guess, guesses):
    guesses.append(guess)
    guesses = '\n'.join(guesses)
    return guesses


def is_valid_guess(guess, target):
    if guess == "help":
        help_message(target)
        return False
    if len(guess) < len(target):
        print(f"Too short! Must be {len(target)} letters!")
        return False
    if len(guess) > len(target):
        print(f"Too long! Must be {len(target)} letters!")
        return False
    if guess not in all_words:
        print("Not a valid word!")
        return False
    else:
        return True


def track_average_scores(total_attempts, remaining_attempts):
    with open("sources/scores.txt", 'a') as file:
        file.write(f"{total_attempts - remaining_attempts} ")
    with open("sources/scores.txt") as file:
        scores = file.read().split()
    for i, score in enumerate(scores):
        scores[i] = int(score)
    average_score = round(sum(scores)) / len(scores) 
    return average_score

def play():
    print("\n--------------------")
    print("Welcome to CLI Wordle!")
    print("You have 6 attempts to guess the secret word!")
    print("--------------------")
    target_word = random.choice(target_words).upper()
    attempts = 6
    grid = []
    guess_history = []
    print(f"What is your {len(target_word)} letter guess?")
    while True:
        print(f"{attempts} Attempts remaining...")
        input_guess = input("> ").lower()
        if is_valid_guess(input_guess, target_word):
            score = score_guess(input_guess, target_word)
            formatted_grid = append_grid(score, grid)
            attempts -= 1
            if is_winner(score, target_word):
                print(formatted_grid)
                remaining_attempts = attempts
                attempts = 6
                print(f"You guessed the target word: {format_colours['green']['start']} {target_word} {format_colours['green']['end']} 🎉")
                print(f"On average, you take {track_average_scores(attempts, remaining_attempts)} attempts to guess the word.\n")
                break
            formatted_guess = format_score(score, input_guess)
            guess_total = append_guess_history(formatted_guess, guess_history)
            print(guess_total)
            if attempts == 0:
                print("\n--------------------")
                print("You lost!")
                print(f"The word was {format_colours['green']['start']} {target_word} {format_colours['green']['end']}")
                print("--------------------\n")
                break
    end_game(game_running)

def help_message(target):
    print("\n--------------------")
    print(f"{format_colours['yellow']['start']}   {format_colours['yellow']['end']} = Correct letter, wrong position")
    print(f"{format_colours['green']['start']}   {format_colours['green']['end']} = Correct letter, correct position")
    print(f"I'll give you a hint: {target}")
    print("--------------------\n")




def end_game(boolean):
    global game_running
    print("Would you like to play again?")
    input_restart = input("> ").strip().lower()
    if input_restart[0] == 'y':
        game_running = True
    else:
        print("Thanks for playing!")
        game_running = False
       # open('sources/scores.txt', 'w').close()
       # with open('sources/scores.txt', 'w') as file:
        #    file.write('0')


while game_running is True:
    play()

