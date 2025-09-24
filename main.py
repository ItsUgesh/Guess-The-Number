import random
import logo_art
EASY_LEVEL_ATTEMPT = 10
HARD_LEVEL_ATTEMPT = 5


def set_level(level):
    if level == "easy":
        return EASY_LEVEL_ATTEMPT
    elif level == "hard":
        return HARD_LEVEL_ATTEMPT
    else:
        return


def check_answer(choosed_number, computer_guess, attempts,):
    if choosed_number > computer_guess:
        print("Your guess is too high ⬆️ ")
        return attempts - 1
    elif choosed_number < computer_guess:
        print("Your guess is too low ⬇️ ")
        return attempts - 1
    else:
        print(
            f"Congratulations!👋 You have guessed correctly! {choosed_number} is the right answer.")


def game():
    print(logo_art.logo)
    print("Let me think of a Number between 1 to 50 🤔")

    computer_guess = random.randint(1, 50)
    # print(computer_guess)
    level = input("Choose the LEVEL...Type 'easy' or 'hard' => ")
    attempts = set_level(level)
    if attempts != EASY_LEVEL_ATTEMPT and attempts != HARD_LEVEL_ATTEMPT:
        print("❌ There are no such levels. Try again")
        return
    choosed_number = 0
    while choosed_number != computer_guess:
        print(f"you have {attempts} numbers of attempts left")
        choosed_number = int(input("Enter your guess => "))
        attempts = check_answer(choosed_number, computer_guess, attempts,)

        if attempts == 0:
            print("❌ Sorry! You have ran out of the attempts. Please! try again")
            return
        elif choosed_number != computer_guess:
            print("Guess Again 🔄")


while True:
    game()
    again = input("\nDo you want to play again? (y/n): ").lower()
    if again != "y":
        print("Thanks for playing! 👋")
        break
