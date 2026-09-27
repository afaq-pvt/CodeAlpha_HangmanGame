import random


# ==============================
# HANGMAN WORD GUESSING GAME
# ==============================

WORDS = [
    "python",
    "computer",
    "keyboard",
    "internet",
    "programming"
]

MAX_WRONG_GUESSES = 6


def show_title():
    print("\n" + "=" * 40)
    print("         HANGMAN WORD GAME")
    print("=" * 40)


def show_instructions():
    print("\nHOW TO PLAY")
    print("-" * 40)
    print("1. The computer selects a secret word.")
    print("2. Guess one letter at a time.")
    print("3. Correct letters are revealed.")
    print("4. Each wrong guess costs one life.")
    print("5. You have 6 incorrect guesses.")
    print("6. Guess the word before lives run out.")
    print("-" * 40)


def display_word(word, guessed_letters):
    result = []

    for letter in word:
        if letter in guessed_letters:
            result.append(letter)
        else:
            result.append("_")

    return " ".join(result)


def calculate_score(wrong_guesses):
    return (MAX_WRONG_GUESSES - wrong_guesses) * 100


def play_game():
    word = random.choice(WORDS)
    guessed_letters = []
    wrong_guesses = 0

    while wrong_guesses < MAX_WRONG_GUESSES:
        print("\n" + "-" * 40)
        print("Word:", display_word(word, guessed_letters))

        if guessed_letters:
            print(
                "Guessed letters:",
                ", ".join(sorted(guessed_letters))
            )
        else:
            print("Guessed letters: None")

        print(
            "Wrong guesses:",
            wrong_guesses,
            "/",
            MAX_WRONG_GUESSES
        )
        print("Remaining lives:",
              MAX_WRONG_GUESSES - wrong_guesses)

        guess = input("\nEnter a letter: ").strip().lower()

        if len(guess) != 1:
            print("Please enter exactly ONE letter.")
            continue

        if guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter an English letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct! The letter is in the word.")
        else:
            wrong_guesses += 1
            print("Wrong guess! Try another letter.")

        if all(letter in guessed_letters for letter in word):
            print("\n" + "=" * 40)
            print("             YOU WON!")
            print("=" * 40)
            print("The secret word was:", word)
            print("Wrong guesses:", wrong_guesses)
            print("Your score:",
                  calculate_score(wrong_guesses))
            print("=" * 40)
            return True

    print("\n" + "=" * 40)
    print("             GAME OVER")
    print("=" * 40)
    print("The secret word was:", word)
    print("You have used all your lives.")
    print("=" * 40)

    return False


def main():
    while True:
        show_title()

        print("\n1. Start Game")
        print("2. Instructions")
        print("3. Exit")

        choice = input("\nChoose an option (1-3): ").strip()

        if choice == "1":
            play_game()

            play_again = input(
                "\nDo you want to play again? (y/n): "
            ).strip().lower()

            if play_again != "y":
                print("\nThank you for playing!")
                break

        elif choice == "2":
            show_instructions()

        elif choice == "3":
            print("\nThank you for playing!")
            break

        else:
            print("\nInvalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()