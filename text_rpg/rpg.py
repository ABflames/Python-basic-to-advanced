print("=" * 40)
print("WELCOME TO THE RPG GAME !")
print("=" * 40)
print()

player_name = input("Enter your name: ")
print(f"Welcome, {player_name}!")

player_hp = 100
player_max_hp = 100
player_mana = 30
player_attack = 20

monster_name = "Goblin"
monster_hp = 60
monster_max_hp = 60
monster_attack = 12

print("\n----- PLAYER -----")
print(f"Name: {player_name}")
print(f"HP: {player_hp}/{player_max_hp}")
print(f"Mana: {player_mana}")
print(f"Attack: {player_attack}")

print("\n----- MONSTER -----")
print(f"Name: {monster_name}")
print(f"HP: {monster_hp}/{monster_max_hp}")
print(f"Attack: {monster_attack}")