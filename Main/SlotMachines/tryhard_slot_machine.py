import random, time

WIN_MULTIPLIER = 7

user_wins = 0
user_misses = 0
user_losts = 0
total_rounds = 0

symbols = ["🍌", "🍒", "🍀", "💎", "👑", "🍉"]

def spin_slot_machine():
    return [random.choice(symbols) for _ in range(5)]

def check_win(spin_result):
    if len(set(spin_result)) == 1:
        return "win"
    elif len(set(spin_result)) == 2:
        return "near_miss"
    else:
        return "lose"

# Main code
def main():
    global user_losts, user_wins, user_misses, total_rounds

    print("Welcome to Tryhard Slot Machine!")
    print()
    time.sleep(1)

    while True:
        total_rounds += 1
        playing = input(f"Round {total_rounds}: Press Enter to spin the slot machine...")
        spin_result = spin_slot_machine()
        print(" | ".join(spin_result))
        
        result = check_win(spin_result)
        
        if result == "win":
            print("Congratulations! You won!")
            user_wins += 1 * WIN_MULTIPLIER
        elif result == "near_miss":
            print("So close! You were just one symbol away from winning!")
            user_misses += 1
        else:
            print("Sorry, you lost. Try again!")
            user_losts += 1
        
        while True:
            answer = input("\nEnter 'Y' to play again (Q to quit): ")
            if answer.upper() == "Q":
                break
            elif answer.upper() == "Y":
                break
            else:
                print("Invalid answer.")

        if answer.upper() == "Q":
            break
        
    print("\n* TSM Stats *")
    print(f"You won: {user_wins} times.")
    print(f"You lost: {user_losts} times.")
    print(f"You miss: {user_misses} times.")
    print(f"The total rounds were: {total_rounds}.")
    time.sleep(2)


# main()
