#### this is an ai translation based on my other project name slotomania ####
import random
import os

# File to store the high score
SCORE_FILE = "high_score.txt"

# Function to simulate sound effects (with text)
def sound_effect(effect):
    if effect == "spin":
        os.system('clear')
        print("🎰 Spinning the reels... 🌀 Let's see how quickly the casino can take your money!")
    elif effect == "win":
        os.system('clear')
        print("✨ Ding ding ding! A rare win! The casino must have let its guard down! ✨")
    elif effect == "lose":
        os.system('clear')
        print("💸 Another spin, another donation to the casino's vault! 💸")
    elif effect == "jackpot":
        os.system('clear')
        print("🎉 JACKPOT!!! Enjoy it while it lasts, because it won’t happen again! 🎉")
    elif effect == "bonus":
        os.system('clear')
        print("🌟 BONUS ROUND! The casino's algorithm probably glitched! 🌟")

# Function to spin the reels
def spin_reels():
    symbols = ["🍒", "🍋", "🔔", "🍀", "💎", "7️⃣", "💰", "⭐"]
    reels = [random.choice(symbols) for _ in range(3)]
    print(" ".join(reels))
    return reels

# Function to check winnings
def check_winnings(reels, bet):
    payout = 0
    if reels[0] == reels[1] == reels[2]:
        if reels[0] == "💰":
            payout = bet * 10
            sound_effect("jackpot")
            print(f"The casino's rigged system must be malfunctioning! You hit the 💰💰💰 jackpot! You won {payout} coins!")
        else:
            payout = bet * 5
            sound_effect("win")
            print(f"All three symbols match! You won {payout} coins!")
    elif reels[0] == reels[1] or reels[1] == reels[2] or reels[0] == reels[2]:
        if "💰" in reels:
            payout = bet * 3
            sound_effect("win")
            print(f"You matched two symbols, one is 💰! You won {payout} coins!")
        else:
            payout = bet * 2
            sound_effect("win")
            print(f"Two symbols match! A small win to keep you playing. You won {payout} coins!")
    else:
        sound_effect("lose")
        print(f"No match, as expected. You lost {bet} coins!")

    # Bonus round trigger
    if reels == ["⭐", "⭐", "⭐"]:
        trigger_bonus_round(bet)
    
    return payout

# Function to trigger a bonus round
def trigger_bonus_round(bet):
    sound_effect("bonus")
    print("Welcome to the BONUS ROUND! Enjoy it while you can!")
    bonus_spin = spin_reels()
    sound_effect("win")
    print(f"You won an extra {bet * 5} coins in the bonus round!")
    return bet * 5

# Function to update and display high scores
def update_high_score(balance):
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "r") as file:
            high_score = int(file.read())
    else:
        high_score = 0

    if balance > high_score:
        high_score = balance
        with open(SCORE_FILE, "w") as file:
            file.write(str(high_score))
        print(f"🏆 New High Score! You reached {high_score} coins!")
    return high_score

# Function to load the high score from file
def load_high_score():
    os.system('clear')
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "r") as file:
            return int(file.read())
    return 0

# Main game loop
def play_slot_machine():
    high_score = load_high_score()
    balance = 100  # Starting balance
    progressive_jackpot = 500  # Progressive jackpot starting amount

    print(f"Welcome to the Casino! You start with {balance} coins. Let's see how long you can last!")

    while True:
        print(f"Your current balance is {balance} coins.")
        try:
            bet = int(input(f"Place your bet (minimum 1 coin, max {balance}): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if bet > balance or bet <= 0:
            print("Invalid bet. You can't bet more than your balance or less than 1 coin.")
            continue

        sound_effect("spin")
        reels = spin_reels()
        payout = check_winnings(reels, bet)
        balance += payout - bet
        progressive_jackpot += bet // 10

        high_score = update_high_score(balance)

        if balance <= 0:
            sound_effect("lose")
            os.system('clear')
            print("You're out of coins! The casino wins again.")
            break

        print(f"Current Progressive Jackpot: {progressive_jackpot} coins.")
        play_again = input("Do you want to play again? (y/n): ").lower()

        if play_again != 'y':
            print(f"Smart move! Walking away with {balance} coins. Your highest score was {high_score} coins.")
            break

    print("Thank you for playing!")

# Run the game
if __name__ == "__main__":
    play_slot_machine()
