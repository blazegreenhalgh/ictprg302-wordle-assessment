with open("sources/all_words.txt") as file:
    all_words = file.read().splitlines()
    for word in all_words:
        word.strip()

with open("sources/target_words.txt") as file:
    target_words = file.read().splitlines()
    for target_word in target_words:
        target_word.strip()

print(all_words[0:5])
print(target_words[0:5])

# Blaze Greenhalgh, 20043918, 30/03/2025
def score_guess(guess, target):
    """ This functions takes two strings (guess, target) and determines if each character from one matches in value and position with the other.
    1 = Value match, 2 = Value and Position match. A list is returned with items equal to the length of the target string."""
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

# # Arrange
# guess = "world"
# target = "hello"
#
# # Act
# print(score_guess(guess, target))


