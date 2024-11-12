'''
Goals:
1 ~ done
2 ~ done
3 ~ done
4 ~ done
5 ~ done
*6 ~ done
7 ~ done
*8 ~ done
9 ~ done
'''

import random, time

BALANCE = 2000
ANTE_AMOUNT = random.randint(100, 300)

WIN_MULTIPLIER = 7

user_wins = 0
user_losts = 0
user_ties = 0
total_rounds = 0

bluff_lines = [
    "You're in trouble now!",
    "I've seen better cards, but I might get lucky.",
    "Think twice before betting more!",
    "Let's see how you handle this!",
    "I might just win this one!",
    "I'm feeling lucky today!",
    "You're not ready for what's coming!",
    "I've got a winning hand—maybe.",
    "You should fold while you still can!",
    "Don't say I didn't warn you!",
    "My hand is better than it looks!",
    "Feeling brave? You shouldn't be!",
    "You won't believe this hand if I win!",
    "I bet you didn't see this coming!",
    "The odds are in my favor this time!",
    "I hope you're ready to lose!",
    "I've got a sneaky feeling about this one.",
    "Ready to be surprised?",
    "You might want to think twice before calling me!",
    "I'm about to turn the tables!"
]

def deal_cards():
    deck = [f"{rank}{suit}" for rank in '23456789tJQKA' for suit in '♠♥♦♣']
    random.shuffle(deck)
    player_hand = [deck.pop() for _ in range(7)]
    bot_hand = [deck.pop() for _ in range(7)]

    return player_hand, bot_hand

def get_ante():
    global BALANCE, ANTE_AMOUNT

    BALANCE -= ANTE_AMOUNT
    print(f"\nYou posted an Ante of: ${ANTE_AMOUNT}. Remaining money: ${BALANCE}.")

def reveal_cards(player_hand, round_number):
    displayed_hand = [
        card if index < round_number + 3 else "?" 
        for index, card in enumerate(player_hand)
    ]
    print(f"Your hand: {displayed_hand}")

def get_check():
    global bet_amount
    bet_amount = 0

def get_bet():
    global BALANCE, bet_amount

    while True:
        bet_amount = input("How much do you want to bet? $")
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if 1 <= bet_amount <= BALANCE:
                BALANCE -= bet_amount
                break
            else:
                print(f"Amount must be between: $1 - ${BALANCE}")
        else:
            print("Please enter a valid number.")

def get_fold():
    global user_losts

    print("You folded. The bot won the round.")
    user_losts += 1
    time.sleep(1.25)
    print()

def bot_phrase():
    return random.choice(bluff_lines)

def evaluate_hand(hand):
    score = sum(['23456789tJQKA'.index(card[0]) + 1 for card in hand])
    return score

def get_deciding(player_hand, bot_hand):
    global BALANCE, WIN_MULTIPLIER, user_wins, user_losts, user_ties, bet_amount

    player_score = evaluate_hand(player_hand)
    bot_score = evaluate_hand(bot_hand)
    print(f"\nYour hand: {player_hand}")
    print(f"Bot's hand: {bot_hand}")

    if player_score > bot_score:
        print(f"You win! Your score: {player_score}, Bot's score: {bot_score}.")
        if bet_amount == 0:
            bet_amount = 750
        BALANCE += bet_amount * 2
        user_wins += 1 * WIN_MULTIPLIER

    elif player_score == bot_score:
        print(f"It's a tie! Your score: {player_score}, Bot's score: {bot_score}.")
        BALANCE += bet_amount
        user_ties += 1

    else:
        print(f"You lost! Your score: {player_score}, Bot's score: {bot_score}.")
        user_losts += 1

# Main code:
def street():
    global BALANCE, action

    print()

    while True:
        print(f"Curent balance: ${BALANCE}.")
        action = input("Do you want to (c)heck, (b)et, or (f)old? ").lower()
        if action in ["check", "c"]:
            get_check()
            break

        elif action in ["bet", "b"]:
            if BALANCE <= 0:
                print("You don't have enough money to bet, you need to CHECK.")
                continue
            else:
                get_bet()
                break

        elif action in ["fold", "f"]:
            get_fold()
            return False 
        
        else:
            print("Invalid action.")

    return True 

def main():
    global total_rounds, action

    print("Welcome to Seven Card Stud!")
    time.sleep(1)

    while BALANCE > 0:
        total_rounds += 1
        print(f"\nRound {total_rounds}: You have ${BALANCE}.")
        get_ante()

        print("Dealing cards...")
        player_hand, bot_hand = deal_cards()
        time.sleep(2)

        for round_number in range(4):
            if round_number > 0:
                print(f"\nRevealing card {round_number + 2}: {player_hand[round_number + 2]}")
            reveal_cards(player_hand, round_number)
            time.sleep(2)

            if not street(): 
                break

        if action != "f" or action != "fold":
            time.sleep(1)
            print("\nBot's hand: [?, ?, ?, ?, ?, ?, ?]")
            print(f"Bot says: {bot_phrase()}")
            
            print("Final showdown!")
            time.sleep(5)
            get_deciding(player_hand, bot_hand)
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

    print("\n* SCS Stats *")
    print(f"You left with: ${BALANCE}.")
    print(f"You won: {user_wins} times.")
    print(f"You lost: {user_losts} times.")
    print(f"You tied: {user_ties} times.")
    print(f"Total rounds played: {total_rounds}.")


# main()