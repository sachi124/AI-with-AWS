import random

def play_game():
    print("\n🎮 Number Guessing Game")
    print("1. Easy   (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard   (1-500, 5 attempts)")

    choice = input("\nChoose difficulty: ")

    if choice == "1":
        maximum = 50
        attempts = 10
    elif choice == "2":
        maximum = 100
        attempts = 7
    elif choice == "3":
        maximum = 500
        attempts = 5
    else:
        print("Invalid choice!")
        return

    secret_number = random.randint(1, maximum)

    print(f"\nI have selected a number between 1 and {maximum}.")
    print(f"You have {attempts} attempts.")

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"\nAttempt {attempt}: Enter your guess: "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        if guess == secret_number:
            score = (attempts - attempt + 1) * 10
            print(f"🎉 Correct! The number was {secret_number}.")
            print(f"🏆 Your score: {score}")
            break

        elif guess < secret_number:
            print("📈 Too low!")

        else:
            print("📉 Too high!")

    else:
        print(f"\n😢 Game over! The number was {secret_number}.")


while True:
    play_game()

    again = input("\nDo you want to play again? (y/n): ").lower()

    if again != "y":
        print("Thanks for playing! 👋")
        break