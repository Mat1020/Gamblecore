from SlotMachines import classic_slot_machine, bucks_slot_machine, tryhard_slot_machine
from RouletteWheels import french_roulette_wheel, american_roulette_wheel, european_roulette_wheel
from PokerVariants import texas_hold_em, omaha_hi, seven_card_stud, cantredraw
import time

TOTAL_GAMBLING_ARCADES = 3

TOTAL_SLOT_MACHINES = 3
TOTAL_ROULETTE_WHEELS = 3
TOTAL_POKER_VARIANTS = 4

gambling_arcades = {
    "slot machines": 1,
    "roulette wheels": 2,
    "poker variants": 3
}

slot_machines = {
    "classic slot machine": 1,
    "bucks slot machine": 2,
    "tryhard slot machine": 3
}

roulette_wheels = {
    "french roulette wheel": 1,
    "american roulette wheel": 2,
    "european roulette wheel": 3
}

poker_variants = {
    "texas hold em'": 1,
    "omaha hi": 2,
    "seven-card stud": 3,
    "five-card draw (cantredraw)": 4
}

def loop_gambling_arcades():
    for key, value in gambling_arcades.items():
        print(f"{key.title()}: {value}")
        time.sleep(0.25)

def loop_slot_machines():
    for key, value in slot_machines.items():
        print(f"{key.title()}: {value}")
        time.sleep(0.25)

def loop_roulette_wheels():
    for key, value in roulette_wheels.items():
        print(f"{key.title()}: {value}")
        time.sleep(0.25)

def loop_poker_variants():
    for key, value in poker_variants.items():
        print(f"{key.title()}: {value}")
        time.sleep(0.25)


def play_slot_machines():
    global play

    loop_slot_machines()
    while True:
        varation = input("Enter a Slot Machine number to play: #")
        if varation.isdigit():
            varation = int(varation)
            if 1 <= varation <= TOTAL_SLOT_MACHINES:
                for _ in range(2):
                    print()
                break
            else:
                print(f"Please enter a number between: #1 - #{TOTAL_SLOT_MACHINES}.")
        else:
            print("Please enter a number next time.")

    if varation == 1:
        classic_slot_machine.main()
    elif varation == 2:
        bucks_slot_machine.main()
    elif varation == 3:
        tryhard_slot_machine.main()

def play_roulette_wheels():
    global play

    loop_roulette_wheels()
    while True:
        varation = input("Enter a Roulette Wheel number to play: #")
        if varation.isdigit():
            varation = int(varation)
            if 1 <= varation <= TOTAL_ROULETTE_WHEELS:
                for _ in range(2):
                    print()
                break
            else:
                print(f"Please enter a number between: #1 - #{TOTAL_ROULETTE_WHEELS}.")
        else:
            print("Please enter a number next time.")

    if varation == 1:
        french_roulette_wheel.main()
    elif varation == 2:
        american_roulette_wheel.main()
    elif varation == 3:
        european_roulette_wheel.main()

def play_poker_variants():
    global play

    loop_poker_variants()
    while True:
        varation = input("Enter a Poker Variant number to play: #")
        if varation.isdigit():
            varation = int(varation)
            if 1 <= varation <= TOTAL_POKER_VARIANTS:
                for _ in range(2):
                    print()
                break
            else:
                print(f"Please enter a number between: #1 - #{TOTAL_POKER_VARIANTS}.")
        else:
            print("Please enter a number next time.")

    if varation == 1:
        texas_hold_em.main()
    elif varation == 2:
        omaha_hi.main()
    elif varation == 3:
        seven_card_stud.main()
    elif varation == 4:
        cantredraw.main()

# Main code:
def main():
    print("Welcome to Gamblecore!")
    print()
    time.sleep(1)

    loop_gambling_arcades()
    while True:
        play = input("Enter a Gambling Arcade number to look at: #")
        if play.isdigit():
            play = int(play)
            if 1 <= play <= TOTAL_GAMBLING_ARCADES:
                print()
                break
            else:
                print(f"Please enter a number between: #1 - #{TOTAL_GAMBLING_ARCADES}.")
        else:
            print("Please enter a number next time.")

    if play == 1:
        play_slot_machines()
        print("\nThank you for playing, goodbye!")
        quit()
    elif play == 2:
        play_roulette_wheels()
        print("\nThank you for playing, goodbye!")
        quit()
    elif play == 3:
        play_poker_variants()
        print("\nThank you for playing, goodbye!")
        quit()

main()