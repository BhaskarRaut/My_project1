"""
Number Guessing Game
--------------------
How to Play:
- The computer picks a number (1-100). Guess it!
- After each guess, you'll see: "Too High" or "Too Low".
- The game ends when you guess correctly.
- Your attempts will be counted.
- Play multiple rounds; best score is saved.

Features:
- Functions for clean code.
- Error handling for invalid inputs.
- High score tracking.
"""

import random

def menu():
    print("\n===== Number Guessing Game =====")
    print("1. Play")
    print("2. High Score")
    print("3. Exit")
    print("================================")

def get_choice():
    while True:
        c = input("Enter choice (1-3): ")
        if c in ["1", "2", "3"]:
            return c
        print("Invalid! Enter 1, 2, or 3.")

def play(hs):
    num = random.randint(1, 100)
    tries = 0
    
    print("\nI picked a number (1-100). Guess it!")
    
    while True:
        try:
            g = int(input("Your guess: "))
            if not 1 <= g <= 100:
                print("Enter a number between 1 and 100.")
                continue
        except ValueError:
            print("Invalid! Enter a number.")
            continue
        
        tries += 1
        
        if g < num:
            print("Too Low!")
        elif g > num:
            print("Too High!")
        else:
            print(f"🎉 Correct! You guessed in {tries} tries.")
            if hs is None or tries < hs:
                hs = tries
                print("🎯 New High Score!")
            break
    return hs

def show_score(hs):
    """Show current high score."""
    if hs is None:
        print("\nNo high score yet. Play a game!")
    else:
        print(f"\n🏆 High Score: {hs} tries.")

def main():
    hs = None
    while True:
        menu()
        c = get_choice()
        if c == "1":
            hs = play(hs)
        elif c == "2":
            show_score(hs)
        else:
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
