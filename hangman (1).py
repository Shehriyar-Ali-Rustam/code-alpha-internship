import random

# Dictionary of words with corresponding hints
words_with_hints = {
    "python": "A popular programming language.",
    "developer": "A person who writes computer software.",
    "hangman": "A classic word-guessing game.",
    "programmer": "Another term for a software developer.",
    "technology": "The application of scientific knowledge for practical purposes."
}

# Hangman stages represented as ASCII art
hangman_stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

# Randomly select a word from the dictionary
selected_word, hint = random.choice(list(words_with_hints.items()))

# Variables to track the game state
guessed_word = ["_"] * len(selected_word)  # Display the guessed word with underscores
incorrect_guesses = 0  # Count the number of incorrect guesses
max_incorrect_guesses = len(hangman_stages) - 1  # Maximum allowed incorrect guesses
guessed_letters = []  # Keep track of guessed letters

print("Welcome to Hangman!")
print(f"Hint: {hint}")
print("Guess the word, one letter at a time.\n")

while incorrect_guesses < max_incorrect_guesses and "_" in guessed_word:
    print(hangman_stages[incorrect_guesses])
    print("Word: ", " ".join(guessed_word))
    print(f"Incorrect guesses: {incorrect_guesses}/{max_incorrect_guesses}")
    print("Guessed letters: ", " ".join(guessed_letters))

    # Get player's guess
    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter. Try again.\n")
    elif guess in selected_word:
        # Correct guess: Update the guessed word
        for i, letter in enumerate(selected_word):
            if letter == guess:
                guessed_word[i] = guess
        guessed_letters.append(guess)
        print("Good guess!\n")
    else:
        # Incorrect guess: Increase the count of incorrect guesses
        incorrect_guesses += 1
        guessed_letters.append(guess)
        print("Wrong guess. Try again.\n")

# Check if the player has won or lost
if "_" not in guessed_word:
    print("Congratulations! You've guessed the word:", selected_word)
else:
    print(hangman_stages[incorrect_guesses])
    print("You've run out of guesses. The word was:", selected_word)

print("Game Over!")
