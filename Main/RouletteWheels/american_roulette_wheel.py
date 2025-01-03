import random, time

MAX_NUMBER_WHEEL = 36
BALANCE = 2500

WIN_MULTIPLIER = 7

user_wins = 0
user_losts = 0
total_rounds = 0

def spin_roulette():
    return random.choice([0, "00"] + list(range(1, MAX_NUMBER_WHEEL + 1)))

def get_bet():
    global BALANCE, bet

    while True:
        bet = input("What would you like to bet? $")
        if bet.isdigit():
            bet = int(bet)
            if 1 <= bet <= BALANCE:
                break
            else:
                print(f"Amount must be between: $1 - ${BALANCE}.")
        else:
            print("Please enter a number next time.")

def guess_win_number():
    global number_bet

    while True:
        number_bet = input(f"Enter the number you want to be on (0-{MAX_NUMBER_WHEEL}/00): ")
        if number_bet == "00":
            print()
            break
        elif number_bet.isdigit():
            number_bet = int(number_bet)
            if 0 <= number_bet <= MAX_NUMBER_WHEEL:
                print()
                break
            else:
                print(f"Please enter a number between: 0 - {MAX_NUMBER_WHEEL} or 00.")
        else:
            print("Please enter a number next time.")

def get_win():
    global BALANCE, bet, winnings, user_wins

    winnings = bet * 5
    BALANCE += winnings
    print(f"Congratulations! You won ${winnings}.")
    print()
    user_wins += 1 * WIN_MULTIPLIER

def get_lost():
    global BALANCE, bet, user_losts

    BALANCE -= bet
    print(f"Sorry, you lost your bet of ${bet}.")
    print()
    user_losts += 1

# Main code:
def main():
    global BALANCE, total_rounds

    print("Welcome to American Roulette Wheel!")
    print()
    time.sleep(1)

    while BALANCE > 0:
        total_rounds += 1
        print(f"Round {total_rounds}: Current balance is: ${BALANCE}")
        print()

        get_bet()
        guess_win_number()

        winning_number = spin_roulette()
        print(f"The winning number is: {winning_number}.")

        if str(winning_number) == str(number_bet):
            get_win()
        else:
            get_lost()
        time.sleep(1)

        while True:
            answer = input("Enter 'Y' to play again (Q to quit): ")
            if answer.upper() == "Q":
                break
            elif answer.upper() == "Y":
                print()
                time.sleep(1)
                break
            else:
                print("Invalid answer.")

        if answer.upper() == "Q":
            break

    print("\n* ARW Stats *")
    print(f"You left with: ${BALANCE}.")
    print(f"You won: {user_wins} times.")
    print(f"You lost: {user_losts} times.")
    print(f"The total rounds were: {total_rounds}.")
    time.sleep(2)


# main()
