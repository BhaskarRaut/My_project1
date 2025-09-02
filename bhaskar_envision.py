"""
Number Guessing Game
--------------------
Rules:
- Computer secretly picks a number between 1 and 100.
- Player keeps guessing until they get it right.
- After each guess, feedback is given if it's higher or lower.
- Tracks number of attempts.
- Keeps a "best score" (fewer tries = better).
"""

import random

def show_menu():
    print("\n=== Number Guessing Game ===")
    print("1. Play a round")
    print("2. See High Score")
    print("3. Quit")
    print("(Psst... try 99)")
    print("============================")

def get_menu_choice():
    while True:
        choice = input("Pick 1, 2, or 3: ")
        if choice.strip() in ["1", "2", "3", "99"]:
            return choice
        else:
            print("Nope. That’s not one of the options.")

def play_round(best_score):
    secret_number = random.randint(1, 100)
    attempt_count = 0

    print("\nI’m thinking of a number between 1 and 100...")
    print("Can you crack it? Good luck! (You’ll need it 😏)")

    too_low_msgs = [
        "Too low... like my WiFi signal 😅",
        "Nope, bigger than that.",
        "You’re underestimating me.",
        "Try going higher 🚀!",
        "That’s under it. Think bigger!"
    ]
    too_high_msgs = [
        "Too high!",
        "Overshot it 🚀",
        "Bring it down a notch.",
        "Lower... lower...",
        "That guess flew too far. 🎈"
    ]

    while True:
        try:
            user_input = input("Your guess: ")
            guess = int(user_input)
        except ValueError:
            print("That doesn’t look like a number.")
            continue

        if guess < 1 or guess > 100:
            print("Numbers between 1 and 100 only.")
            continue

        attempt_count += 1

        
        if guess == 42:
            print("✨ 42 is the Answer to the Ultimate Question of Life, the Universe, and Everything... but not my number.")
        elif guess == 69:
            print("😏 Nice. But nope, that’s not it.")
        
        if guess < secret_number:
            print(random.choice(too_low_msgs))
        elif guess > secret_number:
            print(random.choice(too_high_msgs))
        else:
            if attempt_count == 1:
                print(f"🎯 UNBELIEVABLE! First try! You’re psychic. The number was {guess}.")
            else:
                print(f"\n🎉 Correct! {guess} in {attempt_count} tries.")
            
            if best_score is None or attempt_count < best_score:
                best_score = attempt_count
                print("🏆 New record!")
            else:
                print("Not your best run, but hey—it counts!")
            break

    return best_score

def show_high_score(best_score):
    if best_score is None:
        print("\nNo high score yet. Go make history!")
    else:
        print(f"\n🏆 Best so far: {best_score} tries.")

def secret_menu():
    print("\n🤫 You found the secret menu!")
    print("Here’s a random fun fact for you:")
    facts = [
        "Bananas are berries, but strawberries aren’t.",
        "Octopuses have three hearts.",
        "You can’t hum while holding your nose shut. (Go ahead, try it.)",
        "Sharks existed before trees."
    ]
    print("👉 " + random.choice(facts))

def main():
    best_score = None
    while True:
        show_menu()
        choice = get_menu_choice()
        
        if choice == "1":
            best_score = play_round(best_score)
        elif choice == "2":
            show_high_score(best_score)
        elif choice == "3":
            print("Alright, quitting. Thanks for playing 👋")
            break
        elif choice == "99":   
            secret_menu()

if __name__ == "__main__":
    main()


