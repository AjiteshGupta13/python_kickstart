import random

def get_random_word():
    words = ['python', 'developer', 'jumble', 'learning', 'project', 'school', 'keyboard']
    return random.choice(words)

def jumble_word(word):
    return ''.join(random.sample(word, len(word)))

def play_game():
    print("Welcome to Jumble Game")
    score = 0
    play = True

    while play:
        original_word = get_random_word()
        jumbled_word = jumble_word(original_word)

        print(f"\nJumbled word: {jumbled_word}")
        guess = input("Guess the word: ").lower()

        if guess == original_word:
            print("VERY NICE!")
            score += 1
        else:
            print(f"Wrong! The correct word was: {original_word}")

        again = input("Do you want to play again? (y/n): ").lower()
        if again != "y":
            play = False

    print("\nYour final score was:", score)

if __name__ == "__main__":
    play_game()
