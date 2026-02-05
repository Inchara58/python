import random
import time

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def intro():
    slow_print("You wake up in a dark forest.")
    slow_print("The trees whisper, and two paths lie ahead.\n")

def choose_path():
    while True:
        choice = input("Do you go LEFT or RIGHT? ").lower()
        if choice in ["left", "right"]:
            return choice
        print("Choose 'left' or 'right'.")

def encounter_enemy():
    enemies = ["wolf", "bandit", "giant spider"]
    enemy = random.choice(enemies)
    slow_print(f"A wild {enemy} appears!")
    action = input("Do you FIGHT or RUN? ").lower()

    if action == "fight":
        if random.random() > 0.4:
            slow_print(f"You defeated the {enemy}!")
            return True
        else:
            slow_print(f"The {enemy} overpowers you...")
            return False
    else:
        slow_print("You escape safely, but feel weaker.")
        return True

def treasure_room():
    gold = random.randint(10, 100)
    slow_print(f"You find a chest with {gold} gold coins!")
    return gold

def game():
    intro()
    health = 100
    gold = 0

    path = choose_path()
    slow_print(f"You take the {path} path...\n")

    for _ in range(3):
        if not encounter_enemy():
            health -= 40
        if health <= 0:
            slow_print("You have fallen. Game Over.")
            return

    gold += treasure_room()
    slow_print(f"You escape the forest with {health} health and {gold} gold!")
    slow_print("🎉 You win!")

if __name__ == "__main__":
    game()
