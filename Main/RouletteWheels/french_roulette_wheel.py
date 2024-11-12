'''
Goals:
1 ~ Done
2 ~ Done
3 ~ Done
4 ~ Done
5 ~ Done
*6 ~ Done
7 ~ Done
*8 ~ Done
9 ~ Done
'''

import random, time

MAX_NUMBER_WHEEL = 36
BALANCE = 2500

WIN_MULTIPLIER = 3

user_wins = 0
user_losts = 0
user_partages = 0
total_rounds = 0

la_partage_and_en_prison_explained = {
    "la partage": "recover half",
    "en prison": "keep your bet"
}

def spin_roulette():
    return random.randint(0, MAX_NUMBER_WHEEL) # retrun 0: to test the special part :)

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
        number_bet = input(f"Enter the number you want to be on (0-{MAX_NUMBER_WHEEL}): ")
        if number_bet.isdigit():
            number_bet = int(number_bet)
            if 0 <= number_bet <= MAX_NUMBER_WHEEL:
                print()
                break
            else:
                print(f"Please enter a number between: 0 - {MAX_NUMBER_WHEEL}.")
        else:
            print("Please enter a number next time.")

def get_win():
    global BALANCE, bet, winnings, user_wins, WIN_MULTIPLIER
    
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

def la_partage_and_en_prison():
    global BALANCE, WIN_MULTIPLIER, la_partage_and_en_prison_explained, bet, number_bet, winnings, user_wins, user_losts, user_partages

    print("You hitted 0!")
    time.sleep(1)
    print()
    for key, value in la_partage_and_en_prison_explained.items():
        print(f"{key.title()}: {value.capitalize()}")
    print()

    while True:
        option = input("Do you want to use (l)a partage or (e)n prison? ").lower()
        if option in ["la partage", "l"]:
            BALANCE += bet / 2
            print("You recover half of your bet.")
            time.sleep(0.75)
            user_partages += 1
            print()
            break

        elif option in ["en prison", "e"]:
            print("Your bet will stay for the next spin.")
            time.sleep(0.75)

            next_spin = spin_roulette()
            print(f"\nThe next winning number is: {next_spin}")

            if next_spin == number_bet:
                winnings = bet * 5
                BALANCE += winnings
                print(f"Congratulations! You won ${winnings}.")
                print()
                user_wins += 1 * WIN_MULTIPLIER
                break
            else:
                BALANCE -= bet
                print(f"Sorry, you lost your bet of ${bet}.")
                print()
                user_losts += 1
                break

# Main code:
def main():
    global BALANCE, total_rounds
    print("Welcome to French Roulette Wheel!")
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

        if winning_number == number_bet:
            get_win()
        elif winning_number == 0:
            la_partage_and_en_prison()
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

    print("\n* FRW Stats *")
    print(f"You left with: ${BALANCE}.")
    print(f"You won: {user_wins} times.")
    print(f"You lost: {user_losts} times.")
    print(f"La Partage usages: {user_partages} times.")
    print(f"The total rounds were: {total_rounds}.")
    time.sleep(2)


# main()