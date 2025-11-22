# Word Puzzle Project - BYU W04
# Author: Tunde Femi
# This program allows the user to guess a secret word and receive hints.

# ------------------------------
# 1. SECRET WORD
# ------------------------------
secret_word = "python"   # You may change this for testing
word_length = len(secret_word)

# ------------------------------
# 2. INITIAL HINT (Underscores)
# ------------------------------
initial_hint = "_ " * word_length
print("Welcome to the Word Puzzle!")
print("Here is your hint:")
print(initial_hint)

# ------------------------------
# 3. GUESSING LOOP
# ------------------------------
guess_count = 0
guess = ""

while guess != secret_word:
    guess = input("\nPlease enter your guess: ")

    # Count every guess attempt
    guess_count += 1

    # ------------------------------
    # 4. VERIFY GUESS LENGTH
    # ------------------------------
    if len(guess) != word_length:
        print(f"Your guess must be {word_length} letters long.")
        continue  # Skip hint generation, restart loop

    # ------------------------------
    # 5. GENERATE HINT FOR THE GUESS
    # RULES:
    #  _ -> letter NOT in secret word
    #  lowercase -> letter in word but wrong position
    #  UPPERCASE -> letter in correct position
    # ------------------------------
    hint = ""

    for i in range(word_length):
        if guess[i] == secret_word[i]:
            hint += guess[i].upper()
        elif guess[i] in secret_word:
            hint += guess[i].lower()
        else:
            hint += "_"

    print("Hint:", hint)

# ------------------------------
# 6. GAME COMPLETED
# ------------------------------
print("\nCongratulations! You guessed the word!")
print(f"Total guesses: {guess_count}")
