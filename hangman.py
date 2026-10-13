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
#Intructions Menu  
def show_instructions():
    print("\n" + "=" * 40)
    print("HOW TO PLAY")
    print("=" * 40)
    print("1. The computer selects a secret word.")
    print("2. Guess one letter at a time.")
    print("3. Correct letters are revealed.")
    print("4. Each wrong guess costs one life.")
    print("5. You have 6 incorrect guesses.")
    print("6. Guess the word before lives run out.")
    print("=" * 40)
def calculate_score(wrong_guesses):
    return (MAX_WRONG_GUESSES - wrong_guesses) * 100

def choose_word():
    return random.choice(WORDS)

def display_word(word, guessed_letters):
    result = []

    for letter in word:
        if letter in guessed_letters:
            result.append(letter)
        else:
            result.append("_")

    return " ".join(result)
def play_game():
    word = choose_word()
    guessed_letters = []
    wrong_guesses = 0

    print("\nThe game has started!")

    while wrong_guesses < MAX_WRONG_GUESSES:
        print("\nWord:", display_word(word, guessed_letters))

        guess = input("Enter a letter: ").strip().lower()

        if len(guess) != 1 or guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter one valid English letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")
        else:
            print("Wrong guess!")
            wrong_guesses += 1
            print("Wrong guesses:", wrong_guesses)
            print("Lives remaining:", MAX_WRONG_GUESSES - wrong_guesses) 

        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            print("Your score:", calculate_score(wrong_guesses))
            return True

    print("\nGame Over! You ran out of lives.")
    print("The correct word was:", word)
    print("Your score: 0")
    return False
    
# MENU:

def main():
    while True:
        show_title()

        print("\n1. Start Game")
        print("2. Instructions")
        print("3. Exit")

        choice = input("\nChoose an option (1-3): ").strip()

        if choice == "1":
           play_game()

           play_again = input("\nDo you want to play again? (y/n): ").strip().lower()

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