# Blaze Greenhalgh, 20043918, 30/03/2025
def score_guess(guess, target):
    score = [0] * len(target)
    guess_letters = list(guess)
    target_letters = list(target)

    # Finding correct pos chars first
    for guess_index, guess_letter in enumerate(guess_letters):
        for target_index, target_letter in enumerate(target_letters):
            if guess_letter == target_letter and guess_index == target_index:
                score[guess_index] = 2
                # Replace duplicates with incorrect value after correct pos is found
                for i in range(len(guess_letters)):
                    if guess_letter in guess_letters[i]:
                        guess_letters[i] = " " 

    # Finding incorrect pos chars after finding correct pos
    for guess_index, guess_letter in enumerate(guess_letters):
        for target_index, target_letter in enumerate(target_letters):
            if guess_letter == target_letter and score[guess_index] != 2:
                score[guess_index] = 1




