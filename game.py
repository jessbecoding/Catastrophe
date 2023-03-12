import sys
import time
import random


class Hero:
    def __init__(hero_name, name, health, swordAD, punchAD, gold):
        hero_name.name = name
        hero_name.health = health
        hero_name.swordAD = swordAD
        hero_name.punchAD = punchAD
        hero_name.gold = gold
        hero_name.items = []

    def takeDamage(hero_name, lucipurr):
        hero_name.health -= lucipurr.attack
        print(f"{hero_name.name}'s health is now {hero_name.health}.")

    def swordAttack(hero_name, lucipurr):
        lucipurr.health -= hero_name.swordAD
        print(f"{lucipurr.name}'s health is now {lucipurr.health}")

    def punchAttack(hero_name, lucipurr):
        lucipurr.health -= hero_name.punchAD
        print(f"{lucipurr.name}'s health is now {lucipurr.health}")

    def dodge(hero_name, lucipurr):
        if random.random() < .5:
            print("""
            You dodge and roll, just as Lucipurr's paw swipes past your neck. You hear the "wooshing" sound as it travels.
            """)
        else:
            print("""
            You sense the attack coming and try to dodge, but it's too little too late.
            """)
            lucipurr.villanAttack(hero_name)

    def addItem(hero_name, itm):
        hero_name.items.append(itm)

    def addGold(hero_name, gold):
        hero_name.gold -= gold

    def spendMoney(hero_name, gold):
        hero_name.gold += gold

    def useItem(hero_name, i):
        hero_name.items.remove(i)

    def usePotion(hero_name):
        for item in hero_name.items:
            if item == "Potion":
                hero_name.health == 50
                print(f"{hero_name.name}'s health is now {hero_name.health}")
            else:
                print("You do not have a potion in your inventory!")


class Villan:
    def __init__(villan_name, name, health, attack):
        villan_name.name = name
        villan_name.health = health
        villan_name.attack = attack

    def villanTakeDamagePunch(villan_name, hero_name):
        villan_name.health -= hero_name.punchAD
        print(f"{villan_name.name}'s health is now {villan_name.health}.")

    def villanTakeDamageSword(villan_name, hero_name):
        villan_name.health -= hero_name.swordAD
        print(f"{villan_name.name}'s health is now {villan_name.health}.")

    def villanAttack(villan_name, hero_name):
        hero_name.health -= villan_name.attack
        print(f"{hero_name.name}'s health is now {hero_name.health}")


lucipurr = Villan("Lucipurr", 40, 20)

# typing_speed = 80 #wpm
# def print(str):
#     for letter in str:
#         sys.stdout.write(letter)
#         sys.stdout.flush()
#         time.sleep(random.random()*10.0/typing_speed)

# def print(str):
#     for letter in str:
#         sys.stdout.write(letter)
#         sys.stdout.flush()
#         time.sleep(random.random()*20.0/typing_speed)


def hero_stats(hero_name):
    print(f"""
Your name: {hero_name.name}
HP: {hero_name.health}
AP: {hero_name.attack}
""")


def displayInventory(hero_name):
    for item in hero_name.items:
        print(item)
    print(f"You have {hero_name.gold} gold.")


def combat_menu(lucipurr, hero_name):
    urAlive = True
    shieldPass = False
    while urAlive:
        if (lucipurr.health > 0) and (hero_name.health > 0):
            combatchoice = ''
            combatchoice = input("""
        What would you like to do?
            1. Block
            2. Attack
            3. Dodge
            4. Heal
        """)
            if (combatchoice == '1' and shieldPass == False):
                if "Shield" in hero_name.items:
                    print("""
                        You heave your sturdy shield in front of you, just in the knick of time! Lucipurr's outstretched claws make contact with the shield, buying you time to parry.
                    """)
                    hero_name.useItem("Shield")
                    print("Your shield has been destroyed!")
                    shieldPass = True
                else:
                    print("""
                    You throw your arms over your face, but it's all for naught. All 5 of Lucipurr's sharp claws tear into you. YOU DIED.
                    """)
                    urAlive = False
                    break
            if (combatchoice == '1' and shieldPass == True):
                print("Your trusty shield was destroyed and all you have to defend yourself is your hands.You throw your arms over your face, but it's all for naught. All 5 of Lucipurr's sharp claws tear into you. YOU DIED.")
                urAlive = False
                break
            elif (combatchoice == '2'):
                if (shieldPass == False) and ("Sword" not in hero_name.items):
                    print("""
                    You ball your hands into fists and wind back your arm with all that you have. Before you can make a connection, Lucipurr's monster paw meets your fist in a block. She smiles a wicked smile before all 5 of her sharp claws tear into you. YOU DIED.
                    """)
                    urAlive = False
                    break
                elif (shieldPass == False) and ("Sword" in hero_name.items):
                    print("""
                    You unsheath your sword and lunge forward with a powerful thrust. Lucipurr sees this coming from a mile away and easily dodges. With feline speed, she loops around and takes you out with all 5 of her sharp claws. YOU DIED.
                    """)
                    urAlive = False
                    break
                while lucipurr.health > 0:
                    if (shieldPass == True) and ("Sword" not in hero_name.items):
                        print("""
                        You swing your arm with a powerful punch. Lucipurr laughs at your arm gains. She's barely been impacted.
                        """)
                        lucipurr.villanTakeDamagePunch(hero_name)
                        break
                    if (shieldPass == True) and ("Sword" in hero_name.items):
                        print("""
                        You lunge forward with a powerful thrust of your blade. Lucipurr's eyes widen as the blade makes contact.
                        """)
                        lucipurr.villanTakeDamagePunch(hero_name)
                        break
            elif (combatchoice == '3'):
                hero_name.dodge(lucipurr)
            elif (combatchoice == '4'):
                while (shieldPass == True) and ("Potion" in hero_name.items):
                    print("""
                    You quickly grab the potion that the villargers gave you and bite the cork off. You slam the tiny vile down your throat. Feeling better already!
                    """)
                    hero_name.usePotion()
                    break
                else:
                    print(
                        "You reach into your satchel to grab the potion. Lucipurr takes advantage of your moment of distraction. You've been fillet'd.")
                    urAlive = False
                    break
        if (lucipurr.health == 0):
            print('Lucipurr has been DEFEATED!')
            print('You win')
            break
        if (hero_name.health == 0):
            print("You have been defeated!")
            

def player_menu(hero_name):
    menuchoice = input("""
Please make a selection:
    1. Hero Stats
    2. Items
    3. Back to Start
    4. Quit
    """)
    if (menuchoice == '1'):
        hero_stats(hero_name)
        player_menu(hero_name)
    elif (menuchoice == '2'):
        displayInventory(hero_name)
        player_menu(hero_name)
    elif (menuchoice == '3'):
        starting_point(hero_name)
    elif (menuchoice == '4'):
        print("Bye!")
        quit
    elif (menuchoice != '1', '2', '3', '4'):
        print("Please select a valid option")
        player_menu(hero_name)


hero_name = input()


def create_hero(hero_name):
    hero_name = input("Hello, Hero! What is your name?\n")
    hero_name = Hero(hero_name, 50, 20, 10, 0)
    print(f"Thank you, {hero_name.name}. We're so glad you're here.\n")
    print("Lucipurr, the troublemaking cat, has been terrorizing Our Town and we need your help! Lucipurr is located in her lair at the end of the forest. Please, take this. It's dangerous to go alone. \n")
    gold = 0
    hero_name.addItem("Potion")
    print("""
    A potion has been added to your inventory.
    """)
    print("Now, go! The fate of Town is in your hands. \n")
    print("""
    -------------------------------
    | ~* C A T A S T R O P H E *~ |
    -------------------------------
    """)
    starting_point(hero_name)


def starting_point(hero_name):
    startingchoice = input("""
You follow the path out of Cloud City toward the dense forest of her outskirts. Through the forest is the way to Lucipurr's Lair. At the entrance to the trees, there's The Last Chance shop. What would you like to do?
    1. Enter the forest
    2. Shop at The Last Chance
    3. View Player Menu
""")
    if (startingchoice == '1'):
        intoTheForest(hero_name)
    if (startingchoice == '2'):
        theMoneyPouch(hero_name)
    elif (startingchoice == '3'):
        player_menu(hero_name)


def luciLair(lucipurr, hero_name):
    fightchoice = input("""
You traverse the rugged forest and finally come to a stop outside of Lucipurr's Lair. There is a giant heavy door cracked slightly ajar.
Would you like to open it? Y or N
""").upper()
    if (fightchoice == "Y"):
        print("You slowly widen the opening and step inside. Your eyes adjust to the light for a shadowy figure, perched for an attack. You only have a moment to react!")
        combat_menu(lucipurr, hero_name)
    if (fightchoice == "N"):
        print("Really?! You're giving up now?! Get back in there!!")
        luciLair()


def theMoneyPouch(hero_name):
    moneychoice = input("""
You head toward The Last Chance but abruptly trip over something in your path. What would you like to do?
    1. Investigate what tripped me
    2. Ignore and head for shop
    3. Player menu
""")
    if (moneychoice == '1'):
        print("You bend down and pick up the leather sack that tripped you. It's heavy.\n")
        hero_name.addGold(10)
        print("10 gold has been added to your inventory")
        shopchoice = input("""
What would you like to do?
    1. Talk to Shopkeep
    2. Player Menu
""")
        if (shopchoice == '1'):
            shop(hero_name)
        if (shopchoice == '2'):
            player_menu(hero_name)


def shop(hero_name):
    print("The shopkeep greets you warmly and sells you a shield for 10 gold.\n")
    hero_name.addItem("Shield")
    print("A shield has been added to your inventory.\n")
    hero_name.spendMoney(10)
    print("10 gold has been removed from your inventory.\n")
    shopexit = input("""
What would you like to do?
    1. Continue to Lair
    2. Player Menu
""")
    if (shopexit == '1'):
        intoTheForest(hero_name)
    elif (shopexit == '2'):
        player_menu(hero_name)


def intoTheForest(hero_name):
    forestchoice = input("""
You gather your courage and head into the brush, which soon thickens to a dark canopy of trees above your head. Even through the dim lighting, you make out a way to a small clearing, just barely visable through the branches. What would you like to do?
    1. Investigate the clearing
    2. Continue forward to Lucipurr's Lair
    3. Player Menu
""")
    if (forestchoice == '1'):
        chestchoice = input("""
You push your way past some brush and stumble into the clearing, which appears to be a small meadow.
There is a wooden chest tucked between two trees on the far end. 
What would you like to do?
    1. Investigate the chest
    2. Go Back
    3. Player Menu
""")
        if (chestchoice == '1'):
            print(f"""
    Once you get to the chest, you can see that it's wood with ornate gold embelishments. Enscribed on the lid is... {hero_name.name}? That can't be right.
    You're compelled to open the chest by some innate force. Somehow, it seems larger on the inside. A glimmer at the bottom catches your eye. Is that a sword?
    """)
            swordchoice = input("Grab sword? Y or N\n").upper()
            if (swordchoice == 'Y'):
                print("You reach down a full arm's length into the chest and pull the sword from below. Despite its size, you're able to bring it out with ease.\n")
                hero_name.addItem("Sword")
                print("The sword has been added to your inventory.")
                swordexit = input("""
What would you like to do?
    1. Go back
    2. Player Menu
""")
                if (swordexit == '1'):
                    intoTheForest(hero_name)
                elif (swordexit == '2'):
                    player_menu(hero_name)
        elif (chestchoice == '2'):
            luciLair(lucipurr, hero_name)
        elif (chestchoice == '3'):
            intoTheForest(hero_name)
    elif (forestchoice == '2'):
        luciLair(lucipurr, hero_name)
    elif (forestchoice == '3'):
        player_menu(hero_name)


create_hero(hero_name)
