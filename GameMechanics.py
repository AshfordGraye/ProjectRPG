import random
from os import system, name
from time import sleep
from TypewriterText import *

############################
##### GLOBAL FUNCTIONS #####
############################
def ClearScreen():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

######################
##### NAVSCREENS #####
######################

# NAVSCREEN CLASS PROVIDES FRAMEWORK FOR NavScreen SUBCLASSES TO DISPLAY INFORMATION CONSISTENTLY
class NavScreen:

    firstvisit = True
    currentNavScreen = ""
    holdNavScreen = ""
    lastNavScreen = ""
    describe1 = ""
    describe2 = ""
    name = ""
    option1 = "-"
    option2 = "-"
    option3 = "-"
    travel1 = "-"
    travel2 = "-"
    travel3 = "-"    
    
    def Display():
        ScreenTitle.write (f"{NavScreen.name}\n")
        if NavScreen.firstvisit:
            GMnarrate.write (f"{NavScreen.describe1}\n")
        else:
            GMnarrate.write (f"{NavScreen.describe2}\n")
        NavScreen.lastNavScreen = NavScreen.holdNavScreen
        MenuTitle.write ("Travel Menu")
        PlayerInput.write (f"0: Go back to where I was")
        PlayerInput.write (f"1: {NavScreen.travel1}")
        PlayerInput.write (f"2: {NavScreen.travel2}")
        PlayerInput.write (f"3: {NavScreen.travel3}")
        MenuTitle.write ("Action Menu")
        PlayerInput.write (f"4: {NavScreen.option1}")
        PlayerInput.write (f"5: {NavScreen.option2}")
        PlayerInput.write (f"6: {NavScreen.option3}")
        MenuTitle.write ("Player Menu")
        PlayerInput.write (f"7: Check Items")
        PlayerInput.write (f"8: Check Weapons")
        PlayerInput.write (f"9: Check Stats")
        print ()
        NavSelect.init()

# FACILITATES PLAYER SELECTION IN THE NAV SCREEN
class NavSelect:

    travel1 = ""
    travel2 = ""
    travel3 = ""
    option1 = ""
    option2 = ""
    option3 = ""

    def init():

        selection = input("What would you like to do?   \n")
        print()
        if selection == "0":
            if NavScreen.lastNavScreen == "":
                NavSelect.InvalidChoice()
            else:
                ClearScreen()
                NavScreen.firstvisit = False
                NavScreen.holdNavScreen = NavScreen.currentNavScreen
                NavScreen.lastNavScreen()   
        elif selection == "1":
            if NavSelect.travel1 == "":
                NavSelect.InvalidChoice()
            else:
                ClearScreen()
                NavScreen.firstvisit = False
                NavScreen.holdNavScreen = NavScreen.currentNavScreen
                NavSelect.travel1()
        elif selection == "2":
            if NavSelect.travel2 == "":
                NavSelect.InvalidChoice()
            else:
                ClearScreen()
                NavScreen.firstvisit = False
                NavScreen.holdNavScreen = NavScreen.currentNavScreen
                NavSelect.travel2()
        elif selection == "3":
            if NavSelect.travel3 == "":
                NavSelect.InvalidChoice()
            else:
                ClearScreen()
                NavScreen.firstvisit = False
                NavScreen.holdNavScreen = NavScreen.currentNavScreen
                NavSelect.travel3()
        elif selection == "4":
            if NavSelect.option1 == "":
                NavSelect.InvalidChoice()
            else:
                ClearScreen()
                NavSelect.option1()
        elif selection == "5":
            if NavSelect.option2 == "":
                NavSelect.InvalidChoice()
            else:
                ClearScreen()
                NavSelect.option2()
        elif selection == "6":
            if NavSelect.option3 == "":
                NavSelect.InvalidChoice()
            else:
                ClearScreen()
                NavSelect.option3()
        elif selection == "7":
            PlayerScreens.ItemScreen()
            input ("Press Enter to go back")
            ClearScreen()
            NavScreen.Display()
        elif selection == "8":
            PlayerScreens.WeaponScreen()
            input ("Press Enter to go back")
            ClearScreen()
            NavScreen.Display()
        elif selection == "9":
            PlayerScreens.StatScreen()
            input ("Press Enter to go back")
            ClearScreen()
            NavScreen.Display()
        else:
            NavSelect.InvalidChoice()
    
    def InvalidChoice():
        GMtalk.write ("That won't work here... Try something else.")
        input("Press Enter to go back")
        ClearScreen()
        NavScreen.Display()

######################
##### NPCSCREENS #####
######################

# NPC SCREEN PROVIDES FRAMEWORK FOR WHEN PLAYER HAS SELECTED TO INTERACT WITH AN NPC ON THE NAV SCREEN
class NPCscreen:

    firstvisit = True
    name = ""
    gmintro1 = ""
    gmintro2 = ""
    greeting1 = ""
    greeting2 = ""
    items = {}
    option1 = "-"
    option2 = "-"
    option3 = "-"
    
    def Display():
        ScreenTitle.write (f"{NPCscreen.name}    \n")
        if NPCscreen.firstvisit:
            GMnarrate.write(f"{NPCscreen.gmintro1} \n")
            NPCtalk.write (f'{NPCscreen.greeting1}  \n')
        else:
            GMnarrate.write (f"{NPCscreen.gmintro2}\n")
            NPCtalk.write (f'{NPCscreen.greeting2}  \n')
        MenuTitle.write ("NPCscreen Menu")
        PlayerInput.write (f"0: Leave this conversation")
        PlayerInput.write (f"1: {NPCscreen.option1}")
        PlayerInput.write (f"2: {NPCscreen.option2}")
        PlayerInput.write (f"3: {NPCscreen.option3}")
        MenuTitle.write ("Player Menu")
        PlayerInput.write (f"7: Check Items")
        PlayerInput.write (f"8: Check Weapons")
        PlayerInput.write (f"9: Check Stats")
        print ()
        NPCselect.init()

# FACILITATES PLAYER SELECTION IN THE NPC SCREEN
class NPCselect:

    option1 = "NPCscreen1"
    option2 = "NPCscreen2"
    option3 = "NPCscreen3"

    def init():

        selection = input("What would you like to do?   \n")
        print()
        if selection == "0":
            ClearScreen()
            NPCscreen.firstvisit = False
            NavScreen.currentNavScreen()
        elif selection == "1":
            if NPCselect.option1 == "":
                NPCselect.InvalidChoice()
            else:
                ClearScreen()
                NPCselect.option1()
        elif selection == "2":
            if NPCselect.option2 == "":
                NPCselect.InvalidChoice()
            else:
                ClearScreen()
                NPCselect.option2()
        elif selection == "3":
            if NPCselect.option3 == "":
                NPCselect.InvalidChoice()
            else:
                ClearScreen()
                NPCselect.option3()
        elif selection == "7":
            PlayerScreens.ItemScreen
            input ("Press Enter to go back")
            ClearScreen()
            NPCscreen.Display()
        elif selection == "8":
            PlayerScreens.WeaponScreen
            input ("Press Enter to go back")
            ClearScreen()
            NPCscreen.Display()
        elif selection == "9":
            PlayerScreens.StatScreen
            input ("Press Enter to go back")
            ClearScreen()
            NPCscreen.Display()
        else:
            NPCselect.InvalidChoice()
    
    def InvalidChoice():
        GMtalk.write ("That won't work here... Try something else.")
        input("Press Enter to go back")
        ClearScreen()
        NPCscreen.Display()

###################################
###################################
##### SECTION - BATTLE SYSTEM #####
###################################
###################################

# BATTLE CLASS WILL DETERMINE BATTLE SEQUENCING AND BEHAVIOURS
class Battle():
    battlestart = True
    #runs at the start to determine who goes first 
    @staticmethod
    def FirstStrike():
        cointoss = random.randint(1,2)
        if cointoss == 1:
            Player.playerturn = True
            GMnarrate.write(f'You move fast for the first strike!   \n')
            Player.BattlePhase()
        elif cointoss == 2:
            Player.playerturn = False
            GMnarrate.write(f'Your opponent strikes first!   \n')
            Enemy.BattlePhase()
    
    @staticmethod
    def PlayerVictory():

        GMtalk.write (f'\nDecide quickly: yes or no?\n')
        answer = input(("")) ; print("\n")
        if answer.lower() in ("no"):
            GMnarrate.write ("Your enemy stumbles to his feet and braces himself, steadying his weapon with renewed vigor. He has a cold steel in his eye... this could be his last chance to survive. \n")
            time.sleep(1)
            GMtalk.write (f'Brace Yourself! \n')
            time.sleep(1)
            Enemy.hp = Enemy.hpmax /100 *60
            Battle.FirstStrike()
        elif answer.lower() in ("yes"):
            GMnarrate.write ("With a final swing of your weapon, you dispatch your foe's soul to the gods. May they have more mercy than you did... \n")
            time.sleep(1)
            GMnarrate.write ("It was a harsh ordeal, but you have emerged victorious, and earned your freedom. Well done, warrior. \n")
            time.sleep(1)
            GMnarrate.write("Thank you for playing. The game will close itself in five seconds. \n")
            time.sleep(5)
            quit()
        else: 
            GMtalk.write ("your mind is racing...  but you must focus! \n")
            Battle.PlayerVictory()

    @staticmethod
    def EnemyVictory():
        global firsthit
        global playerturn
        
        GMnarrate.write ("You feel shattered and broken... but do you have the strength to go on? You must decide, one way or the other... \n")
        GMtalk.write (f"He won't wait long... Yes or No? \n")
        answer = input(str("")) ; print()
        if answer.lower() in ("yes"):
            firsthit = True
            playerturn = False
            GMnarrate.write ("Your enemy, allowing a brief show of his military honour, allows you a moment to stand and steady your weapon. Take this chance - it could be your last. \n")
            time.sleep(1)
            GMtalk.write ("Brace Yourself! \n")
            time.sleep(1)
            Player.Reset()
            Battle.FirstStrike()
        elif answer.lower() in ("no"):
            GMnarrate.write("You enemy looks upon you with disdain.\n")
            time.sleep(1)
            NPCtalk.write (f"'hm... pathetic. I had expected more of you.' \n")
            time.sleep(1)
            GMnarrate.write ("With a final thrust of his weapon, your foe dispatches your dream of freedom to the gods - and your soul with it.\n")
            time.sleep(1)
            GMnarrate.write("Thank you for playing. The app will close itself in five seconds\n")
            time.sleep(5)
            quit()
        else:
            GMtalk.write ("Your mind is racing... focus! \n")
            Battle.EnemyVictory()

    @staticmethod
    def CheckForVictory():
        if Player.hp <= 0:
            Player.hp = 0
            GMnarrate.write (f'Seeing an opening, the enemy rushes forward and strikes you with a vicious fury, knocking you to the ground. He stands above you and bellows for the crowd: \n')
            time.sleep(1)
            NPCtalk.write (f"   'ARE YOU DEFEATED ALREADY?!'\n")
            time.sleep(1)
            Battle.EnemyVictory()
        elif Enemy.hp <= 0:
            Enemy.hp = 0
            GMnarrate.write ("Your enemy stumbles back, and then falls to the ground.\n")
            time.sleep(1)
            GMnarrate.write ("You look down at your enemy - do you strike him down and finish the task?")
            time.sleep(1)
            Battle.PlayerVictory()
    

    @staticmethod
    def Fight():
        
        #NEED TO RESET BATTLEBEGINS AT THE END OF THE FIGHT 
        if Battle.battlestart == True:
            Battle.battlestart = False
            Enemy.SetDifficulty()
            GMnarrate.write (f"An enemy {Enemy.job} appeared!")
            Battle.FirstStrike()
        if Player.playerturn == True:
            Player.BattlePhase()
            Battle.Fight()    
        elif Player.playerturn == False:
            Enemy.BattlePhase()
            Battle.Fight()

        Battle.CheckForVictory()
        Battle.Fight()

# INITIALISES NEW BATTLE BASED ON ENEMY TYPE
class LowLvlBadGuy(Battle):
    
    @staticmethod
    def StartFight():
        Enemy.level = 1
        LowLvlBadGuy.Fight()

######################
#### PLAYER  INFO ####
######################

class PlayerScreens:
    def StatScreen():
        
        GMnarrate.write(f'''
Your current stats are:
    Health:                 {Player.hp}/{Player.hpmax}

    Physical Strength:      {Player.phystr}
    Physical Defense:       {Player.phydef}
    Magetek Strength:       {Player.magstr}
    Magetek Defense:        {Player.magdef}
    ''')
        

    def WeaponScreen():
        GMnarrate.write (f'''
You currently have the following equipped:
    Physical Weapon:        {Player.physequip}
    Magetek Weapon:         {Player.magequip}
    ''')

    def ItemScreen():
        GMnarrate.write (f'''
You currently have the following in your inventory:
    {Player.items}
    ''')

####################################
####################################
######  SECTION - CHARACTERS  ######
####################################
####################################

class Character():
    
    name = ""
    
    job = ""
    soldier = ""
    scientist = ""
    medic = ""
    officer = ""

    hpmax = ""
    hp = hpmax
    mpmax = ""
    mp = mpmax

    phystr = ""
    phydef = ""
    magstr = ""
    magdef = ""

    phyweapons = ""
    physequip = ""
    magweapons = ""
    magequip = ""
    items = ""

    moves = ""
    misschance = random.randint (1,100)
    turn = False

######################
######  PLAYER  ######
######################

class Player (Character):

    def init():
        Player.name = ""
        
        Player.job = ""
        Player.soldier = ""
        Player.scientist = ""
        Player.medic = ""
        Player.officer = ""

        Player.hpmax = 1000
        Player.hp = Player.hpmax
        Player.mpmax = 100
        Player.mp = Player.mpmax

        Player.phystr = 10
        Player.phydef = 10
        Player.magstr = 10
        Player.magdef = 10

        Player.phyweapons = []
        Player.physequip = ['none']
        Player.magweapons = []
        Player.magequip = ['none']
        Player.items = []

        Player.moves = {}

    @staticmethod
    def Naming():
        PlayerInput.write("Enter your name:")
        Player.name = "Player"
        print ()
    
    @staticmethod
    def ClassChoice():
        GMtalk.write ('''
Different roles will affect your how strong your Physical and Magetek abilities are, and how well you can defend against them. 
As you progress in the game you will have the option of usig different weapons and items that also influence these stats.

Remember, your enemies will have strengths and weaknesses too!
    ''')
        PlayerInput.write ('''
What was your role in the military? Enter a role number to view it's stats.

    1: Soldier
    2: Scientist
    3: Medic
    4: Officer''')

        ############################################################################################################

        viewclass = "1"

        if viewclass.lower() == "1":
            Player.job = "Soldier"
            Player.phystr += (Player.phystr /100 *30)
            Player.magdef -= (Player.magdef /100 *30)
            Player.moves = {"Attack": random.randint(25,35) + Player.phystr}
            GMnarrate.write (f'''
A former {Player.job}, you fought in the Alliance Army as a Shock Trooper.
The Army's excellent training has given you great strength when fighting. 

Your stats will be:
{Player.phystr} Physical Strength
{Player.phydef} Physical Defense
{Player.magstr} Magetek Strength
{Player.magdef} Magetek Defense
    ''')
            PlayerInput.write ('''
Would you like to select this class, or view another?
    1: Select Role
    2: Go Back to select another Role''')
            roleselect = "1"
            if roleselect == "1":
                print ("selected")
            elif roleselect == "2":
                GMtalk.write ("Okay, this section of the tutorial will restart so you can choose another class.")
                Player.job = ""
                Player.phystr = 10
                Player.phydef = 10
                Player.magstr = 10
                Player.magdef = 10
                Player.ClassChoice()
            else:
                GMtalk.write ("Please enter the number of your selection")

        ############################################################################################################

        elif viewclass.lower() == "2":
            Player.job = "Scientist"
            Player.magstr += (Player.magstr /100 *30)
            Player.phydef -= (Player.phydef /100 *30)
            Player.moves = {"Attack": random.randint(25,35) + Player.phystr}
            GMnarrate.write (f'''
A former {Player.job}, you designed weaponry to be used against the enemy.
Your knowledge of Magetek gives you an advantage when using Magetek abilities.

Your stats will be:
{Player.phystr} Physical Strength
{Player.phydef} Physical Defense
{Player.magstr} Magetek Strength
{Player.magdef} Magetek Defense
    ''')
            PlayerInput.write ('''
Would you like to select this class, or view another?
    1: Select Role
    2: Go Back to select another Role''')
            roleselect = str(input("\n"))
            if roleselect == "1":
                print ("selected")
            elif roleselect == "2":
                GMtalk.write ("Okay, this section of the tutorial will restart so you can choose another class.")
                Player.job = ""
                Player.phystr = 10
                Player.phydef = 10
                Player.magstr = 10
                Player.magdef = 10
                Player.ClassChoice()
            else:
                GMtalk.write ("Please enter the number of your selection")


        ############################################################################################################

        elif viewclass.lower() == "3":
            Player.job = "Medic"
            Player.phydef += (Player.phydef /100 *30)
            Player.phystr -= (Player.phystr /100 *30)
            Player.moves = {"Attack": random.randint(25,35) + Player.phystr}
            GMnarrate.write (f'''
A former {Player.job} you served and saved alongside you solder brothers. 
Your hardiness earned in battle has given you stronger physical defense.

Your stats will be:
{Player.phystr} Physical Strength
{Player.phydef} Physical Defense
{Player.magstr} Magetek Strength
{Player.magdef} Magetek Defense
    ''')
            PlayerInput.write ('''
Would you like to select this class, or view another?
    1: Select Role
    2: Go Back to select another Role''')
            roleselect = str(input("\n"))
            if roleselect == "1":
                print ("selected")
            elif roleselect == "2":
                GMtalk.write ("Okay, this section of the tutorial will restart so you can choose another class.")
                Player.job = ""
                Player.phystr = 10
                Player.phydef = 10
                Player.magstr = 10
                Player.magdef = 10
                Player.ClassChoice()
            else:
                GMtalk.write ("Please enter the number of your selection")


        ############################################################################################################

        elif viewclass.lower() == "4":
            Player.job = "Officer"
            Player.magdef += (Player.magdef /100 *30)
            Player.magstr -= (Player.magstr /100 *30)
            Player.moves = {"Attack": random.randint(25,35) + Player.phystr}
            GMnarrate.write (f'''
A former {Player.job} in the Alliance Navy, you commanded SkyCruiser fleets against the Commonwealth.
Your officer's training gave you increased defense against Magetek abilities. 

Your stats will be:
{Player.phystr} Physical Strength
{Player.phydef} Physical Defense
{Player.magstr} Magetek Strength
{Player.magdef} Magetek Defense
    ''')
            PlayerInput.write ('''
Would you like to select this class, or view another?
    1: Select Role
    2: Go Back to select another Role''')
            roleselect = str(input("\n"))
            if roleselect == "1":
                print ("selected")
            elif roleselect == "2":
                GMtalk.write ("Okay, this section of the tutorial will restart so you can choose another class.")
                Player.job = ""
                Player.phystr = 10
                Player.phydef = 10
                Player.magstr = 10
                Player.magdef = 10
                Player.ClassChoice()
            else:
                GMtalk.write ("Please enter the number of your selection")
    


    @staticmethod
    def AbilitySelect():
        MenuTitle.write ("Select an option:")
        PlayerInput.write('''
 1: Attack
 2: Limit Break
        ''')
        movechoice = input("")
        if movechoice == "1":
            if Player.misschance in range (1,90):
                damage = Player.moves["Attack"]
                Enemy.hp = Enemy.hp - damage
                GMnarrate.write (f"You used 'Attack' to inflict {damage} damage.")
            elif Player.misschance in range (90,101):
                GMnarrate.write  ("You tried to attack with your weapon, but missed!")
        else:
            GMtalk.write ("Invalid Input")
            Player.AbilitySelect()

    @staticmethod
    def StatsDisplay():
        if Enemy.hp > (Enemy.hpmax /100 *70):
            GMnarrate.write("The foe stands strong! Don't give up!   \n")
        elif Enemy.hp > (Enemy.hpmax /100 *30):
            GMnarrate.write("Your foe grows weaker! Keep it up!  \n")
        elif Enemy.hp <= (Enemy.hpmax /100 *30):
            GMnarrate.write("your enemy grows weak! Almost there!    \n")

        MenuTitle.write (f"{Player.name} Status:")
        if Player.hp > (Player.hpmax /100 * 25):
            print (f' {type.fg_orange}HP:{type.reset}   {type.fg_green}{Player.hp}/{Player.hpmax}{type.reset}')
        elif Player.hp <= (Player.hpmax /100 * 25):
            print (f' {type.fg_orange}HP:{type.reset}   {type.fg_red}{Player.hp}{type.reset}/{type.fg_green}{Player.hpmax}{type.reset}')
        
        if Player.mp > (Player.mpmax /100 * 25):
            print (f' {type.fg_orange}MP:{type.reset}   {type.fg_green}{Player.mp}/{Player.mp}{type.reset}')
        elif Player.mp <= (Player.mpmax /100 *25):
            print (f' {type.fg_orange}MP:{type.reset}   {type.fg_red}{Player.mp}{type.reset}/{type.fg_green}{Player.mpmax}{type.reset}\n')
        print()
        
        MenuTitle.write (f"{Enemy.job} Status")
        if (Enemy.hp > Enemy.hpmax/100 *25):
            print (f' {type.fg_orange}HP:{type.reset}   {type.fg_green}{Enemy.hp}/{Enemy.hpmax}{type.reset}')
        if (Enemy.hp <= Enemy.hpmax /100 *25):
            print (f' {type.fg_orange}HP:{type.reset}   {type.fg_red}{Enemy.hp}{type.reset}/{type.fg_orange}{Enemy.hpmax}{type.reset}')
        print()

    @staticmethod
    def BattlePhase():
        Player.StatsDisplay()
        Player.AbilitySelect()
        Player.playerturn = not Player.playerturn

    @staticmethod
    def Reset():
        Player.hp = Player.hpmax
        Player.mp = Player.mpmax

######################
###### BAD GUYS ######
######################

class Enemy(Character):

    level = ""
    job = ""

    hpmax = 500
    hp = hpmax

    phystr = 10
    phydef = 10
    magstr = 10
    magdef = 10


    misschance = ""
    damadj = ""
    magadj = ""
    moves = ""
    movechoice = ""

    @staticmethod
    def SetDifficulty():
        if Enemy.level == 1:
            Enemy.job = "Enemy"
            Enemy.hpmax += (Enemy.hpmax /100 *10)
            Enemy.hp = Enemy.hpmax
            Enemy.phystr += (Enemy.phystr /100 *10)
            Enemy.phydef += (Enemy.phydef /100 *10)
            Enemy.magstr += (Enemy.magstr /100 *10)
            Enemy.magdef += (Enemy.magdef /100 *10)

        elif Enemy.level == 2:
            Enemy.job = "Brute"
            Enemy.hpmax += (Enemy.hpmax /100 *20)
            Enemy.hp = Enemy.hpmax
            Enemy.phystr += (Enemy.phystr /100 *75)
            Enemy.phydef += (Enemy.phydef /100 *75)
            Enemy.magstr += (Enemy.magstr /100 *75)
            Enemy.magdef += (Enemy.magdef /100 *75)

        elif Enemy.level == 3:
            Enemy.job = "Elite"
            Enemy.hpmax += (Enemy.hpmax /100 *150)
            Enemy.hp = Enemy.hpmax
            Enemy.phystr += (Enemy.phystr /100 *150)
            Enemy.phydef += (Enemy.phydef /100 *150)
            Enemy.magstr += (Enemy.magstr /100 *150)
            Enemy.magdef += (Enemy.magdef /100 *150)

        elif Enemy.level == 4:
            Enemy.job = "Boss"
            Enemy.hpmax += (Enemy.hpmax /100 *200)
            Enemy.hp = Enemy.hpmax
            Enemy.phystr += (Enemy.phystr /100 *200)
            Enemy.phydef += (Enemy.phydef /100 *200)
            Enemy.magstr += (Enemy.magstr /100 *200)
            Enemy.magdef += (Enemy.magdef /100 *200)
        Enemy.damadj = (Enemy.phystr - Player.phydef)
        Enemy.magadj = (Enemy.magstr - Player.magdef)

    @staticmethod
    def ResetDifficulty():
        Enemy.level = ""
        Enemy.job = ""
        
        Enemy.hpmax = 500
        Enemy.hp = Enemy.hpmax
        
        Enemy.phystr = 10
        Enemy.phydef = 10
        Enemy.magstr = 10
        Enemy.magdef = 10

        Enemy.damadj = ""
        Enemy.magadj = ""
    
    @staticmethod
    def MoveDamage():
        Enemy.moves = {
                "Attack": random.randint(25,35) + Enemy.damadj,
                "Strong Attack": random.randint(35,50) + Enemy.damadj
                    }


    @staticmethod
    def BattlePhase():
        Enemy.MoveDamage()
        Enemy.misschance = random.randint (1,100)
        Enemy.movechoice = random.randint (1,5)
        if Enemy.level == 1:
            Enemy.movechoice = random.randint(1,5)
            if Enemy.movechoice in range (1,4):
                if Enemy.misschance in range (1,90):
                    damage = Enemy.moves["Attack"]
                    Player.hp -= Enemy.moves["Attack"]
                    GMnarrate.write (f'The {Enemy.job} swiped at you with a broken bottle, causing {damage} damage')
                elif Enemy.misschance in range (90,101):
                    GMnarrate.write (f"The {Enemy.job} tried to attack you, but missed!")    
            elif Enemy.movechoice in range (5,6):
                damage = Enemy.moves["Strong Attack"]
                Player.hp -= Enemy.moves["Strong Attack"]
                Player.hp -= Enemy.moves["Attack"]
                GMnarrate.write (f'The {Enemy.job} made a strong lunge at you with its weapon, causing {damage} damage')
        Player.playerturn = not Player.playerturn
        
################
##### NPCS #####
################

    #EXAMPLE FRAMEWORK FOR FUTURE NPC ADDITIONS
# class XXXXX(NPCscreen):
#     firstvisit = True
#     def init():
#         NPCscreen.name = "XXXXX"
#         if XXXXX.firstvisit:
#             NPCscreen.gmintro1 = "GMINTRO1"
#             NPCscreen.greeting1 = "NPCGREETING1"
#         else:
#             NPCscreen.gmintro2 = "GMINTRO2"
#             NPCscreen.greeting2 = "NPCGREETING2"
#         NPCscreen.option1 = "-"
#         NPCscreen.option2 = "-"
#         NPCscreen.option3 = "-"
#         NPCselect.option1 = ""
#         NPCselect.option2 = ""
#         NPCselect.option3 = ""
#         NPCscreen.Display()

class Porter (NPCscreen):
    firstvisit = True
    def init():
        NPCscreen.name = "Skytrain Dock porter"
        if Porter.firstvisit:
            NPCscreen.gmintro1 = "GMINTRO1"
            NPCscreen.greeting1 = "NPCGREETING1"
        else:
            NPCscreen.gmintro2 = "GMINTRO2"
            NPCscreen.greeting2 = "NPCGREETING2"
        NPCscreen.option1 = "-"
        NPCscreen.option2 = "-"
        NPCscreen.option3 = "-"
        NPCselect.option1 = ""
        NPCselect.option2 = ""
        NPCselect.option3 = ""
        NPCscreen.Display()

class HomelessGuy(NPCscreen):
    firstvisit = True
    def init():
        NPCscreen.name = "Homeless Guy"
        if HomelessGuy.firstvisit:
            NPCscreen.firstvisit = True
            NPCscreen.gmintro1 = "GMINTRO1"
            NPCscreen.greeting1 = "NPCGREETING1"
            HomelessGuy.firstvisit = False
        else:
            NPCscreen.gmintro2 = "GMINTRO2"
            NPCscreen.greeting2 = "NPCGREETING2"
        NPCscreen.option1 = "-"
        NPCscreen.option2 = "-"
        NPCscreen.option3 = "-"
        NPCselect.option1 = ""
        NPCselect.option2 = ""
        NPCselect.option3 = ""
        NPCscreen.Display()

class Medic(NPCscreen):
    firstvisit = True
    def init():
        NPCscreen.name = "Medic"
        if Medic.firstvisit:
            NPCscreen.gmintro1 = "The Medic greets you"
            NPCscreen.greeting1 = "Hey there, nice to meet you"
        else:
            NPCscreen.gmintro2 = " The Medic now says"
            NPCscreen.greeting2 = "Nice to see you again!"
        NPCscreen.option1 = "I'm hurt, can you help?"
        NPCscreen.option2 = "What's that droid for?"
        NPCscreen.option3 = "-"
        NPCselect.option1 = Story.Medic1
        NPCscreen.Display()

class VendorPhys (NPCscreen):
    firstvisit = True
    def init():
        NPCscreen.name = "Store - Iron Will"
        if VendorPhys.firstvisit:
            NPCscreen.gmintro1 = "GMINTRO1"
            NPCscreen.greeting1 = "NPCGREETING1"
        else:
            NPCscreen.gmintro2 = "GMINTRO2"
            NPCscreen.greeting2 = "NPCGREETING2"
        NPCscreen.option1 = "-"
        NPCscreen.option2 = "-"
        NPCscreen.option3 = "-"
        NPCselect.option1 = ""
        NPCselect.option2 = ""
        NPCselect.option3 = ""
        NPCscreen.Display()

class VendorMag (NPCscreen):
    firstvisit = True
    def init():
        NPCscreen.name = "Store - Technomancy"
        if VendorMag.firstvisit:
            NPCscreen.gmintro1 = "GMINTRO1"
            NPCscreen.greeting1 = "NPCGREETING1"
        else:
            NPCscreen.gmintro2 = "GMINTRO2"
            NPCscreen.greeting2 = "NPCGREETING2"
        NPCscreen.option1 = "-"
        NPCscreen.option2 = "-"
        NPCscreen.option3 = "-"
        NPCselect.option1 = ""
        NPCselect.option2 = ""
        NPCselect.option3 = ""
        NPCscreen.Display()

class VendorItem (NPCscreen):
    firstvisit = True
    def init():
        NPCscreen.name = "Store - Going Alone"
        if VendorItem.firstvisit:
            NPCscreen.gmintro1 = "GMINTRO1"
            NPCscreen.greeting1 = "NPCGREETING1"
        else:
            NPCscreen.gmintro2 = "GMINTRO2"
            NPCscreen.greeting2 = "NPCGREETING2"
        NPCscreen.option1 = "-"
        NPCscreen.option2 = "-"
        NPCscreen.option3 = "-"
        NPCselect.option1 = ""
        NPCselect.option2 = ""
        NPCselect.option3 = ""
        NPCscreen.Display()

##########################
##########################
##### STORY ELEMENTS #####
##########################
##########################

class Story():

    @staticmethod
    def Introduction():
        GMtalk.write (f'''
    Welcome, Player - to Project RPG. Shortly, you will be free to explore the city of Piston, meet its inhabitants, and find your way to the fighting tournament to earn your fortune. 
    But first, a little about how the game works.

    In the game world, you will be presented with menus that looks like this:
        ''')
        time.sleep(0.5)
        Tutorial.__init__()
        Tutorial.Screen()
        time.sleep(1)
        GMtalk.write ('''
    Whenever you see a list like the one above, just enter the number of the option you wish to select. It's that easy!

    Further hints like will appear like this as the game continues. 
    There will be another tutorial section when you enter a battle for the first time. Until then, enjoy the game!
        ''')
        time.sleep(2)
   
    @staticmethod
    def StoryBegins():

        GMnarrate.write ('''
You're riding the skytrain to Piston, a city on the Southern Alliance's edge. You served the Alliance during it's last war against the Northern Commonwealth. 
The Empire won, but you were cast aside afterwards, just like the rest of the conscriptions.
Now you're barely getting by - but an underground fight tournament in Piston may give you just enough fortune to start the new life you deserve...
While looking out the brass port hole you notice the stranger opposite peering at you through his goggles. After meeting your eyes, he introduces himself with a familiar Pistonian drawl:
        ''')
        NPCtalk.write ('''
    'Well hey there friend, Armish Cornwall's the name - Who do I got the pleasure of acquantancin' today?'
        ''')
        Player.Naming()
        NPCtalk.write (f'''
    'Howdy, {Player.name} - a pleasure. You go' dat stern look about yer feller, one only an Alliance vet could git. 
    I were a low rank soldier in the war, how'd they git you to serve?'
        ''')
        Player.ClassChoice()
        if Player.job == "Soldier":
            NPCtalk.write ('''
    Well I'll be, I had feelings yer might be a brother in arms
        ''')
        elif Player.job == "Scientist":
            NPCtalk.write ('''
    Shoot, you one o' dem fancy science types huh?
    Well I'm grateful fer the tech you nerds done worked up fer us!
        ''')
        elif Player.job == "Medic":
            NPCtalk.write ('''
    Hell, you boys were all whut kept us going some days... thank you, brother.
        ''')
        elif Player.job == "Officer":
            NPCtalk.write ('''
    Officer, huh... higher ups always lookin' down on us rank and file...
    I suppose yer orders kept us alive.
        ''')
        GMnarrate.write ("Armish leans back in his chair and studies you")
        NPCtalk.write ('''
    ... Yer never been ter Piston, have yer? Rough place, no Alliance peacekeepers around this far out. I gotta spare knife. Not much, but it's better than yer fists. A healing salve too, in case someone manages to get too close.
    ''')
        GMnarrate.write ('''
Armish hands you a knife. The blade is serrated, but rusted. Handle seems sturdy enough.
He also hands you a healing salve. Looks like a standard spray applicator.
        ''')
        Player.phyweapons.append("Knife")
        Player.items.append ("Healing Salve")
        GMtalk.write ('''
    A Knife has been added to your weapons list.
    A Healing Salve has been added to your items list.
        ''')
        GMnarrate.write ('''
Armish looks out the window. You are nearing Piston now, the gleaming metal superstructures piercing the clouds you are now descending towards.
He stands to leave and turns to you:
        ''')
        NPCtalk.write (f'''
    It were good makin' yer acquaintanceship the day, friend - maybe we'll see each other round the way.
    Stay safe, now, {Player.name}.
        ''')
        GMnarrate.write (f'''
After watching Armish leave, you look around the skytrain cabin. 
The battered leather seats haven't been fixed in years, and the once polished brass has started to rust in places.
You glance out of the port hole one last time at the incoming city - the skytrain is on it's landing approach. 
You turn and walk through the rusted cabin door into the skytrain's passenger corridor...
        ''')

    def Medic1():
        NPCtalk.write ("howdy!")

#####################
#####################
##### LOCATIONS #####
#####################
#####################

    # FRAMEWORK FOR FUTURE LOCATIOON ADDITIONS
# class XXXXX (NavScreen):
#     def init():
#         NavScreen.currentNavScreen = XXXXX.init
#         if XXXXX.firstvisit:
#             NavScreen.firstvisit = True
#             XXXXX.firstvisit = False
#         NavScreen.describe1 = ""
#         NavScreen.describe2 = ""
#         NavScreen.name = "XXXXX"
#         NavScreen.option1 = "-"
#         NavScreen.option2 = "-"
#         NavScreen.option3 = "-"
#         NavScreen.travel1 = "-"
#         NavScreen.travel2 = "-"
#         NavScreen.travel3 = "-"
#         NavScreen.Display()

class Tutorial (NavScreen):
    def init():
        NavScreen.currentNavScreen = Tutorial.init
        if Tutorial.firstvisit:
            NavScreen.firstvisit = True
            Tutorial.firstvisit = False
        NavScreen.describe1 = "A description of your NavScreen and the world around you"
        NavScreen.describe2 = "Another description of your NavScreen and the world around you"
        NavScreen.name = "The name of your NavScreen"
        NavScreen.option1 = "Talk to NPC"
        NavScreen.option2 = "Look at item of interest"
        NavScreen.option3 = "-"
        NavScreen.travel1 = "Go in that direction"
        NavScreen.travel2 = "Go in the other direction"
        NavScreen.travel3 = "-"
        NavScreen.Display()

# EDIT THIS SUBCLASS TO ADD A HIDDEN ITEM AFTER LEAVING FOR THE FIRST TIME
class Train (NavScreen): 
    firstvisit = True
    def init():
        NavScreen.currentNavScreen = Train.init
        if Train.firstvisit:
            NavScreen.firstvisit = True
            Train.firstvisit = False
        NavScreen.describe1 = "You are in a Skytrain cabin. The battered leather seats haven't been fixed in years, and the once polished brass has started to rust in places."
        NavScreen.describe2 = "Once again you enter the Skytrain and find a cabin."
        NavScreen.name = "Skytrain"
        NavScreen.travel1 = "Leave the Skytrain"
        NavScreen.travel2 = "-"
        NavScreen.travel3 = "-"
        NavScreen.option1 = "-"
        NavScreen.option2 = "-"
        NavScreen.option3 = "-"
        NavSelect.travel1 = Station.init
        NavScreen.Display()

class Station (NavScreen):
    firstvisit = True
    def init():
        NavScreen.currentNavScreen = Station.init
        if Station.firstvisit:
            NavScreen.firstvisit = True
            Station.firstvisit = False
        NavScreen.describe1 = "You step off the Skytrain onto the Station dock. It stinks of smoke and diesel, and you can barely see in the smog."
        NavScreen.describe2 = "Back at the station, you see the magnificent Skytrain docked - they always amazed you, as a boy you had never imagined they would one day take off from the rails."
        NavScreen.name = "Skytrain Dock Station"
        NavScreen.travel1 = "Proceed to the Power Station"
        NavScreen.travel2 = "-"
        NavScreen.travel3 = "-"
        NavScreen.option1 = "Talk to the Dock Porter"
        NavScreen.option2 = "Approach the homeless guy"
        NavScreen.option3 = "-"
        NavSelect.travel1 = PowerStation.init
        NavSelect.travel2 = ""
        NavSelect.travel3 = ""
        NavSelect.option1 = Porter.init
        NavSelect.option2 = HomelessGuy.init
        NavSelect.option3 = ""
        NavScreen.Display()

class PowerStation (NavScreen):
    firstvisit = True
    def init():
        NavScreen.currentNavScreen = PowerStation.init
        if PowerStation.firstvisit:
            NavScreen.firstvisit = True
            PowerStation.firstvisit = False
        NavScreen.describe1 = "The hulking mass of concrete, steel and towering chimneys stands before you"
        NavScreen.describe2 = "You stand in the grounds of the old Power Station"
        NavScreen.name = "Old Power Station - Grounds"
        NavScreen.travel1 = "Visit the Medic Station"
        NavScreen.travel2 = "Visit the makeshift Bazaar in the Station lobby"
        NavScreen.travel3 = "Head up to the Power Station workfloor"
        NavScreen.option1 = "-"
        NavScreen.option2 = "-"
        NavScreen.option3 = "-"
        NavSelect.travel1 = MedicStation.init
        NavSelect.travel2 = Bazaar.init
        NavSelect.travel3 = StationFloor.init
        NavSelect.option1 = ""
        NavSelect.option2 = ""
        NavSelect.option3 = ""
        NavScreen.Display()

class MedicStation (NavScreen):
    firstvisit = True
    def init():
        NavScreen.currentNavScreen = MedicStation.init
        if MedicStation.firstvisit:
            NavScreen.firstvisit = True
            MedicStation.firstvisit = False
        NavScreen.describe1 = "The Medic's Station area seems to be staffed only by an old man and a beaten up droid."
        NavScreen.describe2 = "The Medic sits in the corner. You hear the beeps and whirs of the Field Droid busying itself around the area."
        NavScreen.name = "Old Power Station - Medic's Area"
        NavScreen.travel1 = "-"
        NavScreen.travel2 = "-"
        NavScreen.travel3 = "-"
        NavScreen.option1 = "Talk to the Medic"
        NavScreen.option2 = "Approach the Field Droid"
        NavScreen.option3 = "-"
        NavSelect.travel1 = ""
        NavSelect.travel2 = ""
        NavSelect.travel3 = ""
        NavSelect.option1 = Medic.init
        NavSelect.option2 = ""
        NavSelect.option3 = ""
        NavScreen.Display()

class Bazaar (NavScreen):
    firstvisit = True
    def init():
        NavScreen.currentNavScreen = Bazaar.init
        if Bazaar.firstvisit:
            NavScreen.firstvisit = True
            Bazaar.firstvisit = False
        NavScreen.describe1 = "You enter the Bazaar"
        NavScreen.describe2 = "The bazaar are is full of people"
        NavScreen.name = "Old Power Station - Makeshift Bazaar"
        NavScreen.travel1 = "-"
        NavScreen.travel2 = "-"
        NavScreen.travel3 = "-"
        NavScreen.option1 = "Talk to the Magetek Vendor"
        NavScreen.option2 = "Talk to the Physical Vendor"
        NavScreen.option3 = "Talk to the Item Vendor"
        NavSelect.travel1 = ""
        NavSelect.travel2 = ""
        NavSelect.travel3 = ""
        NavSelect.option1 = VendorMag.init
        NavSelect.option2 = VendorPhys.init
        NavSelect.option3 = VendorItem.init
        NavScreen.Display()

class StationFloor (NavScreen):
    firstvisit = True
    def init():
        NavScreen.currentNavScreen = StationFloor.init
        if StationFloor.firstvisit:
            NavScreen.firstvisit = True
            StationFloor.firstvisit = False
        NavScreen.describe1 = "You enter the Power Station Floor"
        NavScreen.describe2 = "Once again into the Arena area... here goes. "
        NavScreen.name = "Old Power Station - Work Floor"
        NavScreen.travel1 = "-"
        NavScreen.travel2 = "-"
        NavScreen.travel3 = "-"
        NavScreen.option1 = "Approach the Arena Cage"
        NavScreen.option2 = "-"
        NavScreen.option3 = "-"
        NavSelect.travel1 = ""
        NavSelect.travel2 = ""
        NavSelect.travel3 = ""
        NavSelect.option1 = ""
        NavSelect.option2 = ""
        NavSelect.option3 = ""
        NavScreen.Display()