# Blaze Greenhalgh, 20043918, 30/03/2025
def score_guess(guess, target):
    score = [0] * len(target)
    guess_letters = list(guess)
    target_letters = list(target)

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





