import random

# HANGMAN WORD GUESSING GAME

WORDS = [
    "python",
    "computer",
    "keyboard",
    "internet",
    "programming"
]

MAX_WRONG_GUESSES = 6

# Game Title:

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
# MENU:

def main():
    while True:
        show_title()

        print("\n1. Start Game")
        print("2. Instructions")
        print("3. Exit")

        choice = input("\nChoose an option (1-3): ").strip()

        if choice == "1":
            print("Game will be added soon.")

        elif choice == "2":
            show_instructions
            

        elif choice == "3":
            print("\nThank you for playing!")
            break

        else:
            print("\nInvalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()