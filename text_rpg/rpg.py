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

def display_stats():
    print()
    print("----- PLAYER -----")
    print(f"Name: {player_name}")
    print(f"HP: {player_hp}/{player_max_hp}")
    print(f"Mana: {player_mana}")
    print(f"Attack: {player_attack}")
    print()
    print("----- MONSTER -----")
    print(f"Name: {monster_name}")
    print(f"HP: {monster_hp}/{monster_max_hp}")
    print(f"Attack: {monster_attack}")
    

def attack():
    global monster_hp 
    #monster_hp = attack(monster_hp, player_attack)
    monster_hp -= player_attack
    
    if monster_hp < 0:
        monster_hp = 0
        
    print("You attacked the Goblin!")
    
    print(f"Goblin HP: {monster_hp}/{monster_max_hp}")
    
def heal():
    global player_hp
    
    player_hp += 20
    
    if player_hp > player_max_hp:
        player_hp = player_max_hp
        
    print("You healed yourself!")
    print(f"Player HP: {player_hp}/{player_max_hp}")
    
    
display_stats()
        
        
print()
print("Choose your action:")
print("1. Attack")
print("2. Heal")
print("3. Run")

choice = input("Enter your choice (1-3):")

if choice == "1":
    print("You chose Attack!")
    attack()
    
elif choice == "2":
    print("You chose Heal!")
    heal()
    
elif choice == "3":
    print("You chose Run!")
    
else:
    print("Invalid choice!")
    

        

        
