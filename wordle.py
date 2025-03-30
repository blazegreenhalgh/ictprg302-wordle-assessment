# Blaze Greenhalgh, 20043918, 30/03/2025
def score_guess(guess, target):
    score = [0] * len(target)
    if guess == target:
        score = [2] * len(target)
        return score
    return score