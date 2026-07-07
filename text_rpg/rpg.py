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
    
# Functions must be like machines.
def attack(monster_hp, player_attack):
    #global monster_hp 
    
    monster_hp -= player_attack
    
    if monster_hp < 0:
        monster_hp = 0
        
    print("You attacked the Goblin!")
    
    print(f"Goblin HP: {monster_hp}/{monster_max_hp}")
    
    if monster_hp == 0:
        print("You defeated the Goblin!")
        
    return monster_hp

def heal(player_hp, player_max_hp):
    #global player_hp
    
    player_hp += 20
    
    if player_hp > player_max_hp:
        player_hp = player_max_hp
        
    print("You healed yourself!")
    print(f"Player HP: {player_hp}/{player_max_hp}")
    
    return player_hp
    
def monster_turn(player_hp, monster_attack):
    #global player_hp
    
    player_hp -= monster_attack
    
    if player_hp < 0:
        player_hp = 0
        
    print("The Goblin attacked you!")
    print(f"Player HP: {player_hp}/{player_max_hp}")
    
    if player_hp == 0:
        print("You have been defeated by the Goblin!")
    
    return player_hp

while player_hp > 0 and monster_hp > 0:   
        
        display_stats()
                
        print()
        print("Choose your action:")
        print("1. Attack")
        print("2. Heal")
        print("3. Run")

        choice = input("Enter your choice (1-3):")

        if choice == "1":
            monster_hp = attack(monster_hp, player_attack)
            
            if monster_hp > 0:
                player_hp = monster_turn(player_hp, monster_attack)
            
            
        elif choice == "2":
            player_hp = heal(player_hp, player_max_hp)
            
            if monster_hp > 0:
                player_hp = monster_turn(player_hp, monster_attack)
            
        elif choice == "3":
            print("You chose Run!")
            break
            
        else:
            print("Invalid choice!")
        
        #if monster_hp > 0:    
        #    player_hp = monster_turn(player_hp, monster_attack)
            
if player_hp == 0:
    print("Game Over! You have been defeated.")
    
elif monster_hp == 0:
    print("Congratulations! You have defeated the Goblin!")
    
else:
    print("You ran away from the battle.")
    

        

        
