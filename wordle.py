# Blaze Greenhalgh, 20043918, 30/03/2025
def score_guess(guess, target):
    score = [0] * len(target)
    if guess == target:
        score = [2] * len(target)
        return score
    return score

    # score = []
    # for letter in target:
    #     score.append(0)

guess_word = "world"
target_word = "hello"

print(score_guess(guess_word, target_word))

