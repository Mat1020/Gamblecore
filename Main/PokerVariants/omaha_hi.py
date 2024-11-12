import random, time

BALANCE = 2000

WIN_MULTIPLIER = 1

user_wins = 0
user_losts = 0
user_ties = 0
total_rounds = 0

bluff_lines = [
    "My cards are looking good.",
    "You missed your chance to fold.",
    "I'm all in for this round!",
    "I doubt you can outplay me.",
    "I've got the best hand possible.",
    "This round is mine to take.",
    "Luck is on my side today.",
    "I hold a couple of pairs.",
    "You should feel uneasy.",
    "I know my strategy well.",
    "Your tells are easy to spot.",
    "This table belongs to me.",
    "A bluffer can't fool another.",
    "I'm completely unfazed.",
    "I have the top hand here.",
]

def deal_cards():
    deck = [f"{rank}{suit}" for rank in '23456789tJQKA' for suit in '♠♥♦♣']
    random.shuffle(deck)
    return deck[:4], deck[4:8]

def get_bet():
    global BALANCE, bet_amount

    while True:
        bet_amount = input("How much do you want to bet? $")
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if 1 <= bet_amount <= BALANCE:
                break
            else:
                print(f"Amount must be between: $1 - ${BALANCE}")
        else:
            print("Please enter a number next time.")

def go_all_in():
    global BALANCE, bet_amount

    bet_amount = BALANCE
    BALANCE -= bet_amount
    print(f"You went all in (${bet_amount})!")

def get_fold():
    global user_losts

    print("You folded. You gave the win away to the Bot.")
    user_losts += 1
    time.sleep(1.25)

def bot_phrase():
    return random.choice(bluff_lines)

def get_deciding():
    global BALANCE, bet_amount, player_score, bot_score, user_wins, user_losts, user_ties, WIN_MULTIPLIER

    player_score = random.randint(1, 10)
    bot_score = random.randint(1, 10)
        
    if player_score > bot_score:
        print(f"You win! Your score: {player_score}, Bot's score: {bot_score}.")
        BALANCE += bet_amount * 2
        user_wins += 1 * WIN_MULTIPLIER

    elif player_score == bot_score:
        print(f"It's a tie! Your score: {player_score}, Bot's score: {bot_score}.")
        BALANCE += bet_amount
        user_ties += 1

    else:
        print(f"You lost! Your score: {player_score}, Bot's score: {bot_score}.")
        BALANCE -= bet_amount
        user_losts += 1

# Main code:
def main():
    global total_rounds

    print("Welcome to Omaha Hi!")
    time.sleep(1)

    while BALANCE > 0:
        total_rounds += 1

        print(f"\nRound {total_rounds}: You have ${BALANCE}.")
        print("\nDealing cards...")

        player_hand, bot_hand = deal_cards()
        print(f"Your hand: {player_hand}")

        action = input("\nDo you want to (b)et, go (a)ll in, or (f)old? ").lower()
        if action in ["bet", "b"]:
            get_bet()

        elif action in ["fold", "f"]:
            get_fold()
            continue
            
        elif action in ["all in", "a"]:
            go_all_in()
            
        else:
            print("Invalid action.")
            continue

        time.sleep(1)
        print(f"\nBot's hand: {bot_hand}")
        print(f"Bot says: {bot_phrase()}")

        print("Deciding...")
        time.sleep(5)
        get_deciding()
        time.sleep(1.25)
        print()

        while True:
            answer = input("Enter 'Y' to play again (Q to quit): ")
            if answer.upper() == "Q":
                break
            elif answer.upper() == "Y":
                break
            else:
                print("Invalid answer.")

        if answer.upper() == "Q":
            break

    print("\n* OH Stats *")
    print(f"You left with: ${BALANCE}.")
    print(f"You won: {user_wins} times.")
    print(f"You lost: {user_losts} times.")
    print(f"You tied: {user_ties} times.")
    print(f"The total rounds played: {total_rounds}.")
    time.sleep(2)


# main()
