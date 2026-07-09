import random

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

goblin = {
    "name": "Goblin",
    "hp": 60,
    "max_hp": 60,
    "attack": 12
}

wolf = {
    "name": "Wolf",
    "hp": 50,
    "max_hp": 50,
    "attack": 15
}

zombie = {
    "name": "Zombie",
    "hp": 80,
    "max_hp": 80,
    "attack": 8
}

orc = {
    "name": "Orc",
    "hp": 100,
    "max_hp": 100,
    "attack": 18
}

monsters = [
    goblin,
    wolf,
    zombie,
    orc
]

monster = random.choice(monsters)

print(f"\nA wild {monster['name']} appeared!")

def display_stats():
    print()
    print("----- PLAYER -----")
    print(f"Name: {player_name}")
    print(f"HP: {player_hp}/{player_max_hp}")
    print(f"Mana: {player_mana}")
    print(f"Attack: {player_attack}")
    print()
    print("----- MONSTER -----")
    print(f"Name: {monster['name']}")
    print(f"HP: {monster['hp']}/{monster['max_hp']}")
    print(f"Attack: {monster['attack']}")
    
# Functions must be like machines.
def attack(monster, player_attack): 
    #global monster_hp 
    
    monster['hp'] -= player_attack
    
    if monster['hp'] < 0:
        monster['hp'] = 0
        
    print(f"You attacked the {monster['name']}!")
    
    print(f"{monster['name']} HP: {monster['hp']}/{monster['max_hp']}")
    
    if monster['hp'] == 0:
        print(f"You defeated the {monster['name']}!")
        
    attack(monster, player_attack)

def heal(player_hp, player_max_hp):
    #global player_hp
    
    player_hp += 20
    
    if player_hp > player_max_hp:
        player_hp = player_max_hp
        
    print("You healed yourself!")
    print(f"Player HP: {player_hp}/{player_max_hp}")
    
    return player_hp
    
def monster_turn(player_hp, monster):
    #global player_hp
    
    player_hp -= monster['attack']
    
    if player_hp < 0:
        player_hp = 0
        
    print(f"The {monster['name']} attacked you!")
    print(f"Player HP: {player_hp}/{player_max_hp}")
    
    if player_hp == 0:
        print(f"You have been defeated by the {monster['name']}!")
    
    return player_hp

while player_hp > 0 and monster['hp'] > 0:   
        
        display_stats()
                
        print()
        print("Choose your action:")
        print("1. Attack")
        print("2. Heal")
        print("3. Run")

        choice = input("Enter your choice (1-3):")

        if choice == "1":
            monster['hp'] = attack(monster, player_attack)
            
            if monster['hp'] > 0:
                player_hp = monster_turn(player_hp, monster)
            
            
        elif choice == "2":
            player_hp = heal(player_hp, player_max_hp)
            
            if monster['hp'] > 0:
                player_hp = monster_turn(player_hp, monster)
            
        elif choice == "3":
            print("You ran away from battle!")
            break
            
        else:
            print("Invalid choice!")
        
        #if monster['hp'] > 0:    
        #    player_hp = monster_turn(player_hp, monster['attack'])
            
if player_hp == 0:
    print("Game Over! You have been defeated.")
    
elif monster['hp'] == 0:
    print(f"Congratulations! You have defeated the {monster['name']}!")
    
else:
    print("You ran away from the battle.")
    

        

        
