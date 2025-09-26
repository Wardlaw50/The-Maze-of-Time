# ———————— Imports ———————— #

import sys  # For exit functions
import time # For sleep functions



# ———————— Functions ———————— #


# typewriter function
def typewriter(text, delay):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Intro sequence function
def intro():
    typewriter(f"\n————————————————————————————————\n  Welcome to {gamename}\n————————————————————————————————", 0.01)
    time.sleep(1)
    print("\n ——— Gameplay Information ———", flush=True)
    time.sleep(0.6)
    print(" ——— The \">\" symbol indicates when player input is expected.", flush=True)
    time.sleep(0.6)
    print(" ——— The \"*\" symbol indicates when an item is in use.", flush=True)
    time.sleep(0.6)
    print(" ——— When answering a riddle, there is no need to write \"a\", \"an\", or \"the\" before your answer.", flush=True)
    time.sleep(0.6)
    print(" ——— \"(Y/N)\" inputs accept all of the following:", flush=True)
    time.sleep(0.6)
    print(" ——— For yes: (y, Y, yes, Yes, YES)", flush=True)
    time.sleep(0.6)
    print(" ——— For no: (n, N, no, No, NO)", flush=True)
    time.sleep(1.2)

    while True:
        if input("\n> Press [Enter] to start the game ") == "":
            break

    time.sleep(0.75)
    print("\n. ", end="", flush="False")
    time.sleep(0.75)
    print(". ", end="", flush="False")
    time.sleep(0.75)
    print(".\n", end="", flush="False")
    time.sleep(0.75)

    typewriter("\nHer parents kissed her goodnight and put her to sleep, but when the morning came, she was gone.", 0)
    typewriter("No one knew where she had disappeared, only that she had been dreaming for so long trapped in a world between time and shadow.", 0)
    typewriter("The parents searched endlessly, but no one could give them any answers.", 0)
    typewriter("People whispered of small cases, others vanishing the same way, but the truth remained hidden.", 0)
    typewriter("Then, one night, a wanderer came to their door. He spoke of realms beyond dreams, of strange riddles and monsters.", 0)
    typewriter("Still, no one believed him until he secretly broke into an ancient chamber and uncovered the truth: a hidden doorway \ninto the Maze of Time, the place where their daughter was lost, waiting to be found.", 0)
    time.sleep(2)
    typewriter("\nThe wanderer leads you to the rift within the cave. Will you brave the journey ahead to save your daughter?\n", 0)

# function for calling riddles
def riddle_room(level, path):
    if level == 1:
        print("\nThe door creaks to life before bestowing upon you a riddle.")
        time.sleep(0.75)
        Response = input("\"I shine in the night but fade in the day. What am I?\"\n> ")
    elif level == 2:
        Response = input(f"\nThe wind picks up, carrying {path} thoughts to you. \n\"I follow you everywhere, but disappear in darkness. What am I?\"\n> ")
    elif level == 3:
        Response = input("\nCracks in the ground whisper a question to you.\n\"The more you take from me, the bigger I become. What am I?\"\n> ")
    elif level == 4:
        if path == "focus":
            Response = input("\nSummoned by the runes, a stone being emerges with a question.\n\"I have no beginning, no end; I flow forever. What am I?\"\n> ")
        else:
            Response = input("\nAfter trial an error, you make out a message.\n\"I have no beginning, no end; I flow forever. What am I?\"\n> ")
    elif level == 5:
        Response = input("\n\"I don't exist in darkeness, yet I never cast a shadow. What am I?\"\n> ")
    elif level == 6: 
        Response = input("\n\"I speak without a mouth; and vanish when silence falls. What am I?\"\n> ")
    else:
        print(f"Unexpected argument value: {level}")
    return Response.strip().lower().capitalize()

# function for when user does NOT want to save their child
def badParent_exe():
    print("\n...seriously?? Parents these day... *tut tut*. Very well then.", flush=True)
    time.sleep(7)
    print("What are you waiting for? The game to end? Close it yourself.", flush=True)
    time.sleep(7)
    print("You know... with (Ctrl + c)?? Hurry up, I don't have all day.", flush=True)
    time.sleep(7)
    print("Last chance before I flood your terminal...", flush=True)
    time.sleep(5)
    print("3...", end="", flush=True)
    time.sleep(1)
    print("2...", end="", flush=True)
    time.sleep(1)
    print("1...", end="", flush=True)
    time.sleep(1)
    for i in range(2500):
        print(f"Shame on you, {character.name}. ", end="", flush=True)
        time.sleep(0.01)
    sys.exit()      # Exit game

# function for validating Y/N inputs
def ynCheck(i):             # "i" is short for input. saves time writing if statements.
    i = i.strip().lower()
    if i in ("y, yes"):
        return "yes"
    elif i in ("n , no"):
        return "no"         # user has chosen no
    else:
        return "undef"      # invalid input
    
# fight the golden door
def fightDoor():
    typewriter("\nDread approaches as you realise that your answer was wrong.", 0.01)
    if character.item == "Sword of Shadow":
        typewriter("* Your sword is missing from your holster. It has readied itself before you, commmanding you to weild it.", 0.01)
        while True:
            if input("\n> Press [Enter] to strike the door ") == "":
                break
        typewriter("\nThe sword floods you with feelings. Desire. Rage. Excitement.", 0.01)
        typewriter("With the combined power of countless deadly sins, you destroy the door. \nThe next passage awaits...\n", 0.01)
        return
    typewriter("Armed only with what you brough from home, you attempt to fight the door.", 0.01)
    time.sleep(0.75)
    print("\n. ", end="", flush="False")
    time.sleep(0.75)
    print(". ", end="", flush="False")
    time.sleep(0.75)
    print(".\n", end="", flush="False")
    time.sleep(0.75)
    typewriter("You make it out alive, though the battle was not without loss. \nYou won't be able to take a fight like that many more times.\n", 0.01)
    character.hp -= 1
        

# ———————— Variables and classes ———————— #

# Class object for storing player info
class character:
    def __init__(self, name, age, item, hp):
        self.name = name
        self.age = age
        self.item = item
        self.hp = hp

# Placeholder value for the player's chosen item
character.item = "placeholder"

character.hp = 4

# Variable for game name
gamename = "The Maze of Time"

# Track book uses
wisdomCharges = 3


# ———————— Main Code ———————— #

# Get player's Name
nameInput = input("\n> Enter your name: ")
nameInput = nameInput.strip().lower().capitalize()
print(f"So, your name is {nameInput}?")
while True:
    nameValid = ynCheck(input("> (Y/N): "))
    if nameValid == "yes":
        break
    elif nameValid == "no":
        print(f"Okay... {nameInput} is NOT your name then.")
        nameInput = input("> Please re-enter your name: ")
        print(f"Is your new name correct, {nameInput}?")
character.name = nameInput

# Get Player's Age
character.age = int(input("> Enter your age: ")) # Get user's age
if character.age < 18: # Check if user is under 18
    print("Must be 18 or over to play this game. Goodbye :)")
    sys.exit()         # Exit game


# Call on Intro Seqence function
intro()

Response = ynCheck(input("> (Yes/No): "))
while True:
    if Response == "no":
        badParent_exe()#
    elif Response == "yes":
        break
    else:
        Response = ynCheck(input("> (Yes/No): "))


print("\nFueled by adrenaline, you step through the rift and a blinding light envelopes you.") # Pause while being taken to the maze
time.sleep(0.75)
print("\n. ", end="", flush="False")
time.sleep(0.75)
print(". ", end="", flush="False")
time.sleep(0.75)
print(".\n", end="", flush="False")
time.sleep(0.75)


# Wake up in the maze
print("\nYou come to your senses and observe the rundown ancient city that has formed around you.\nIn your path lay 2 pedastals, shimmering with energy.\n")
time.sleep(0.75)
chapter2 = False
while chapter2 == False:
    if input("> Press [Enter] to move ahead ") == "": # User must press ENTER to progress to the pedestals
        chapter2 = True


# User chooses between the book and the sword
print("\nUpon the pedestals lie the Book of Wisdom and a Sword of Shadow.\nPick an item to help you on this journey: \n")
time.sleep(1)
while character.item not in ("Book of Wisdom, Sword of Shadow"):
    chosenItem = input("> (Book/Sword): ")
    if chosenItem.strip().lower() in ["b", "book", "book of wisdom"]:
        character.item = "Book of Wisdom"
        break
    elif chosenItem.strip().lower() in ["s", "sword", "sword of shadow"]:
        character.item = "Sword of Shadow"
        break
    else:
        chosenItem = input("> (Book/Sword): ")


# Tell user what they have taken
if character.item == "Book of Wisdom": # If they have selected the book:
    print("\n* You have equipped the Book of Wisdom. It glows brightly before bursting into dust; But its presence lingers.")
else:                        # If they have selected the sword:
    print("\nYou have selected the Sword of Shadows. But before you can pick it up, it levetates above and around you, holstering itself by your side.")


# First encounter
door = ("""
+---------+
|         |
|   ___   |
|  |   |  |
|  |   |  |
|  |___|  |
|         |
+---------+
""")
print(door)
print("In the distance you spy a Golden Door and head towards it.\n")
time.sleep(0.75)
while True:
    if input("> Press [Enter] to interact with the Door ") == "":
        break
if riddle_room(1, 0) == "Moon":
    print("\nThe door grumbles.")
    time.sleep(1.25)
    typewriter("\"Hmmm... ", 0.1)
    time.sleep(1.25)
    typewriter("your answer... ", 0.1)
    time.sleep(1.25)
    typewriter("pleases me.\"", 0.1)
    time.sleep(0.75)
    print("\nThe door opens and the light disappears. You feel pushed and the door closes behind you.")
    time.sleep(0.75)
else:
    if character.item == "Book of Wisdom" and wisdomCharges > 0:
        typewriter("\n* A familiar energy rushes over you; The books energy.\nIf you wish, you can revise your answer, but who knows what it will cost.", 0.01)
        time.sleep(1)
        seek = ynCheck(input("\nSeek knowledge from the book?\n> (Y/N): "))
        while True:
            if seek == "yes":
                typewriter("The book unleashes powerful psionic magic onto the door, changing your answer to \"Moon\".", 0.01)
                print("\nThe door grumbles.")
                time.sleep(1.25)
                typewriter("\"Hmmm... ", 0.1)
                time.sleep(1.25)
                typewriter("your answer... ", 0.1)
                time.sleep(1.25)
                typewriter("pleases me.\"", 0.1)
                time.sleep(0.75)
                print("\nThe door opens and the light disappears. You feel pushed and the door closes behind you.")
                time.sleep(0.75)
                typewriter("The book's presence feels lighter...", 0.1)
                wisdomCharges -= 1
                break
            elif seek == "no":
                fightDoor()
                break
            else:
                seek = ynCheck(input("> (Y/N): "))
    else:
        fightDoor()
                


# Second encounter
Glowinglantern =("""
   .---.
  /     \ 
  | (*) | 
  |     |
   \___/
    | |
    | | 

""")
print(Glowinglantern)
print("You enter a grey, misty, and foggy area. You are led across a bridge by blue lanterns which continuously \nreveals the path ahead. The road diverges and you are left with a choice.\nDo you take the left path illuminated by blue lanterns or the right path illuminated by a dull moonlight?\n")
time.sleep(0.75)

leftOrRight = input("> Pick your path (L/R): ")
while True:
    if leftOrRight in ["l", "L", "left", "Left", "LEFT"]:
        leftOrRight = "L"
        break
    elif leftOrRight in ["r", "R", "right", "Right", "RIGHT"]:
        leftOrRight = "R"
        break
    else:
        leftOrRight = input("> (L/R): ")
if leftOrRight == "L":
    path = "their"
    print("\nYou have taken the left path and follow the lanterns deeper into the forest.\nThe light from the lanterns flicker violently before going dark. Then, as the lanterns ignite once more, you notice markings on the ground.")
    time.sleep(1)
    while True:
        if input("\n> Press [Enter] ") == "":
            break
    if character.item == "Book of Wisdom":
        typewriter("\n* You feel pressure as the Book of Wisdom seeps knowledge into your head. \nYou begin to recognise the markings on the ground as a holding spell.", 0.03)
        typewriter("A holding spell that you are right in the center of.\n", 0.08)
    time.sleep(1)
    print("The lighting reveals 8 silhouettes surrounding you; They're mimicking you. \nThey spin and whisper before synchronising to give you your next riddle.")
    time.sleep(0.75)
    while True:
        if input("\n> Press [Enter] to hear your silhouettes ") == "":
            break
else:
    path = "Tree's"
    print("\nYou have taken the right path, curiously following the moonlight until you stumble to a great oak tree.\nAn intimidating but protective presence washes over you.")
    time.sleep(0.75)
    while True:
        if input("\n> Press [Enter] to interact with the Tree ") == "":
            break

time.sleep(0.45)
if riddle_room(2, path) == "Shadow":
    time.sleep(0.75)
    print("\nYou see some rocks before you at the bottom of the mountain and when you answer the riddle correctly the rocks open up to reveal the entrance to the cave.")
    while True:
        if input("\n> Press [Enter] to enter the cave ") == "":
            break
else:
    ("Incorrect.\nYour passage now costs you part of your life.")
    character.hp -= 1
    if character.hp < 1:
        print()
        typewriter("You Died.\n", 0.2)
        time.sleep(3)
        print("Resetting game", flush=True, end="")
        typewriter(". . .", 0.75)
        sys.exit()
    # TO DO: Write about the door opening and going into the next zone


# Third encounter
largeemptycaveenvironment = ("""
  /''''''\ 
 /        \ 
|          |
 \        /
  \______/

""")
print(largeemptycaveenvironment)
print("\nYou step into a wide stone courtyard, empty and silent.")
time.sleep(0.75)
print("The ground looks strange... each step you take leaves a deeper mark than the last.")
time.sleep(0.75)

while True:
    if input("\n> Press [Enter] to inspect the strange ground ") == "":
        break

if riddle_room(3, 0) == "Hole":
    time.sleep(0.75)
    print("\nThe floor trembles and forms a perfect circle that opens in the center.")
    print("Glowing runes spiral into a staircase, leading you safely into the next realm.\n")
else:
    print("Wrong!")
    time.sleep(0.5)
    print("The floor splits a part in to a vast pit!")
    print("From the depths rises a beast of dust and stone, roaring as it climbs out to attack!")
    time.sleep(1)
    typewriter("Your body is pelted with hundreds if not thousands of small rocks and and dust pellets.", 0.01)
    time.sleep(0.5)
    character.hp -= 1
    if character.hp < 1:
        print()
        typewriter("You Died.\n", 0.2)
        time.sleep(3)
        print("Resetting game", flush=True, end="")
        typewriter(". . .", 0.75)
        sys.exit()
    typewriter("...The pain you feel is spiritual in nature.\nYou are free to go, but you're not the same as you were.", 0.08)
    typewriter("The stone guardian is gone, and the underground is open for you now.")
           

 
 
# Fourth encounter
Floatinghourglasses =("""
\   /    \   /
 \ /      \ /
  X        X
 / \      / \ 
/   \    /   \ 

""")
print(Floatinghourglasses)
print("You descend beneath the earth into a chamber where countless hourglasses float.")
time.sleep(0.75)
print("Their sands flow upward and downward at once, and the room pulses like a hidden clock.")
time.sleep(0.75)
print("Glowing runes crawl across the walls in endless cycles; beginnings and endings blur together.")
time.sleep(0.75)
 
while True:
    if character.item == "Book of Wisdom":  
        print("* The Book's knowledge pierces your mind again and you recognise the powerful magic surrounding you.\nAs it disrupts the flow of time, it projects overlapping thoughts and whispers thoughout the realm.")  
        if input("\n> Press [Enter] focus on the magic ") == "":
            path = "focus"
            break
    else:
        if input("\n> Press [Enter] to try to read the runes ") == "":
            path = "read"

 
if riddle_room(4, path) == "Time":
    print("Correct")
    time.sleep(0.75)
    print("\nThe sands freeze, then fall, warmth spreads through the chamber, and the ceiling cracks open.")
    print("Daylight pours in. Time is restored. The Book of paths glows and guides you to the next realm.") # Paths? #
else:
    print("Incorrect.")
    typewriter("The levitating hourglasses freeze in place, as if offended by your being there.\nThe runes shift, and the aura changes. What was once tranquil is now potent.", 0.01)
    typewriter("Suddenly, your mind and body as split accross countless places and times.\nHaving been tossed around in a dimension that you were never supposed to see, you lose consciousness.", 0.01)
    character.hp -= 1
    if character.hp < 1:
        print()
        typewriter("You Died.\n", 0.2)
        time.sleep(3)
        print("Resetting game", flush=True, end="")
        typewriter(". . .", 0.75)
        sys.exit()
    else:
        time.sleep(1)
        print("By some miracle, your life was spared.")
        typewriter("Or was it...?", 0.08)
    
 
# Fifth encounter
FireSeaDragon =("""
    
           \||/
           |  @___oo
   /---\  / (__,,,,|
  /        \_(-'  )
  |      /   \_/\ 
  |     /      \ \    
  |  /\/        \ \ 
  \__/           \_/
""")
print(FireSeaDragon)
print("You step into a cavern where an underground sea burns with endless fire. The flames shift and swirl like wings beating across the waves.")
print("But the sea is not water —— it is burning with endless, cold soulfire flames twisting like living serpents.", flush=True)
time.sleep(0.75)
print("The pressure grows in the air, and suddenly the fire rises, shaping into a colossal SEA-FIRE DRAGON!", flush=True)
time.sleep(0.75)
print("Its horns blaze with embers, its eyes glow like molten gold, and its furnace heart rumbles with power.", flush=True)
time.sleep(0.75)

if character.item == "Book of Wisdom":
    print("The book warns you of danger at sunrise. Spend too long by this sea of dormant fire, and the light \nfrom the sun will ignite an endless raging heat, eager to consume you.")

while True:
    if input("\n> Press [Enter] to face the riddle ") == "":
        break
 
if riddle_room(5, 0) == "Fire":
    print("Correct")
    time.sleep(0.75)
    print("\nThe dragon lowers its massive head, acknowledging your answer.")
    print("Its furnace heart softens into golden light, and the flames of the sea rise as wings beneath you.")
    print("The Sea-Fire Dragon takes flight, carrying you across the burning sea into the next realm.")
else:
    print("Incorrect.")
    time.sleep(0.75)
    typewriter("The Sea-Fire Dragon, who just for a moment seemed dissapointed in your answer, grins as it eyes you up and down.\nIt's jaw unhinges like a snake and it darts towards you faster than you can react.", 0.01)
    character.hp -= 1
    if character.hp < 1:
        typewriter("Passing straight through you, it takes with it what was left of you.", 0.08)
        print()
        typewriter("You Died.\n", 0.2)
        time.sleep(3)
        print("Resetting game", flush=True, end="")
        typewriter(". . .", 0.75)
        sys.exit()

    else:
        typewriter("Passing straight through you, it takes even more of what it left of your spirit.\nHow much of you is still left in there?", 0.05)
 
# Sixth encounter
Echo =("""
~    ~~~    ~~~~~    ~~~   ~

 """)
print(Echo)
print("The passage winds into a shadowy cavern, its walls black and polished like glass.")
time.sleep(0.75)
print("Every step you take multiplies in sound —— one becomes ten, then a hundred, until whispers chase you.")
time.sleep(0.75)
print("The voices grow louder, filling the chamber as though the walls themselves are speaking.")
time.sleep(0.75)
 
while True:
    if input("\n> Press [Enter] to listen to the riddle ") == "":
        break
 
if riddle_room(6, 0) == "Echo":
    print("Correct")
    time.sleep(0.75)
    print("The whispers twist into screams the cavern walls and shatter.")
    print("Silver light fills the cavern, mending the black walls around you.")
    print("The echo lifts you as though on invisible wings , carrying  you to a  final  doorway that  shimmers ahead.")
else:
    print("Incorrect")
    typewriter("Silence falls.\nDeep into the cavern you feel a rumbling... and it's defintely not getting further away.", 0.1)
    time.sleep(0.75)
    typewriter("Sparks fly and an insurmounrable sound radiates throughout the caverns. The walls crack and and loose rocks fall.", 0.1)
    character.hp -= 1
    if character.hp < 1:
        print()
        typewriter("You Died.\n", 0.2)
        time.sleep(3)
        print("Resetting game", flush=True, end="")
        typewriter(". . .", 0.75)
        sys.exit()
    else:
        typewriter("Luck is certainly on your side. The crashing stops stops and your body remaain in-tact.", 0.01)
        print("The whispers twist into screams the cavern walls and shatter.")
        print("Silver light fills the cavern, mending the black walls around you.")
        print("The echo lifts you as though on invisible wings , carrying  you to a  final  doorway that  shimmers ahead.")

 # ---------- Final Monster Encounter ----------
print("\nThe cavern shakes as the air splits apart!")
time.sleep(1)
print("From the darkness emerges the FINAL MONSTER — the Phantom of Echoes!")
time.sleep(1.5)
print("It stares into your soul and whispers...")
time.sleep(1.5)
print("\"Every choice is a question… every answer is a wing.\"")
time.sleep(2)

print("\nThis becomes your clue. You ready your strength for the final battle.\n")

# Simple fight system
def final_fight():
    hp_player = 5
    hp_monster = 6
    while hp_player > 0 and hp_monster > 0:
        input("Press [Enter] to strike...")
        hp_monster -= 1
        print(f"You strike! Monster HP = {hp_monster}")
        if hp_monster <= 0:
            break
        print("The Phantom attacks!")
        hp_player -= 1
        print(f"Your HP = {hp_player}")
    return hp_player > 0

if final_fight():
    print("\n✨ You land the final blow! The Phantom shatters into silver dust.")
    print("You hear your child’s cry — you run forward and rescue them!")
    print("The Maze of Time collapses behind you as hope is restored forever.")
    print("YOU WIN!\n")
else:
    print("\n💀 The Phantom’s scream consumes you.")
    print("Your voice becomes one more echo in the Maze, and the child remains trapped…")
    print("GAME OVER.\n")
    sys.exit()









