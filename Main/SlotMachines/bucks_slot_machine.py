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

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

WIN_MULTIPLIER = 3

user_wins = 0
user_losts = 0
total_rounds = 0

symbol_count = {
    "🍀": 2,
    "💎": 4,
    "🪙": 6,
    "🍒": 8,
    "🍌": 10
}

symbol_value = {
    "🍀": 6,
    "💎": 5,
    "🪙": 4,
    "🍒": 3,
    "🍌": 2
}

def check_winnings(columns, lines, bet, values):
    global user_wins, user_losts

    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0] [line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount


def get_number_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines


def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                print()
                break
            else:
                print(f"Amount must be between: ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount

# Main code:
def spin(balance):
    global user_wins, user_losts, WIN_MULTIPLIER

    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    time.sleep(1)

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won: ${winnings}.")

    if winnings > 0:
        print(f"You won on line:", * winning_lines)
        user_wins += 1 * WIN_MULTIPLIER
    else:
        print("You won on line: none")
        user_losts += 1

    return winnings - total_bet

def main():
    global total_rounds

    print("Welcome to Bucks Slot Machine!")
    print()
    time.sleep(1)

    balance = deposit()
    while True:
        total_rounds += 1
        print(f"Round {total_rounds}: Current balance is: ${balance}")
        print()
        balance += spin(balance)
        print()

        while True:
            answer = input("Enter 'Y' to play again (Q to quit): ")
            if answer.upper() == "Q":
                break
            elif answer.upper() == "Y":
                print()
                break
            else:
                print("Invalid answer.")

        if answer.upper() == "Q":
            break

    print("\n* BSM Stats *")
    print(f"You left with: ${balance}.")
    print(f"You won: {user_wins} times.")
    print(f"You lost: {user_losts} times.")
    print(f"The total rounds were: {total_rounds}.")
    time.sleep(2)


# main()