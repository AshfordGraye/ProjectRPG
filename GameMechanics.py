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

######################################
######################################
##### SECTION1 - DISPLAY SCREENS #####
######################################
######################################

####################################
##### SECTION 1A -  NAVSCREENS #####
####################################

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
            NavScreen.describe1()
        else:
            NavScreen.describe2()
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

###################################
##### SECTION 1B - NPCSCREENS #####
###################################

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
            NPCscreen.gmintro1()
            NPCscreen.greeting1()
        else:
            NPCscreen.gmintro2()
            NPCscreen.greeting2()
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

######################################
##### SECTION 1C - PLAYERSCREENS #####
######################################

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


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################


####################################
####################################
######  SECTION2 - CHARACTERS  ######
####################################
####################################

class Character:
    
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
    playerturn = False

####################################
######  SECTIION 2A - PLAYER  ######
####################################

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
      
#############################
##### SECTION 2B - NPCS #####
#############################

    #EXAMPLE FRAMEWORK FOR FUTURE NPC ADDITIONS
# class XXXXX(NPCscreen):
#     firstvisit = True
#     def init():
#         NPCscreen.name = "XXXXX"
#         if XXXXX.firstvisit:
#             NPCscreen.firstvisit = True
#             NPCscreen.gmintro1 = Story.GMIntroTest1
#             NPCscreen.greeting1 = Story.NPCInteractTest1
#             XXXXX.firstvisit = False
#         else:
#             NPCscreen.gmintro2 = Story.GMIntroTest2
#             NPCscreen.greeting2 = Story.NPCInteractTest2
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
            NPCscreen.firstvisit = True
            NPCscreen.gmintro1 = Story.GMIntroTest1
            NPCscreen.greeting1 = Story.NPCInteractTest1
            Porter.firstvisit = False
        else:
            NPCscreen.gmintro2 = Story.GMIntroTest2
            NPCscreen.greeting2 = Story.NPCInteractTest2
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
            NPCscreen.gmintro1 = Story.GMIntroTest1
            NPCscreen.greeting1 = Story.NPCInteractTest1
            HomelessGuy.firstvisit = False
        else:
            NPCscreen.gmintro2 = Story.GMIntroTest2
            NPCscreen.greeting2 = Story.NPCInteractTest2
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
            NPCscreen.firstvisit = True
            NPCscreen.gmintro1 = Story.GMIntroTest1
            NPCscreen.greeting1 = Story.NPCInteractTest1
            Medic.firstvisit = False
        else:
            NPCscreen.gmintro2 = Story.GMIntroTest2
            NPCscreen.greeting2 = Story.NPCInteractTest2
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
            NPCscreen.firstvisit = True
            NPCscreen.gmintro1 = Story.GMIntroTest1
            NPCscreen.greeting1 = Story.NPCInteractTest1
            VendorPhys.firstvisit = False
        else:
            NPCscreen.gmintro2 = Story.GMIntroTest2
            NPCscreen.greeting2 = Story.NPCInteractTest2
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
            NPCscreen.firstvisit = True
            NPCscreen.gmintro1 = Story.GMIntroTest1
            NPCscreen.greeting1 = Story.NPCInteractTest1
            VendorMag.firstvisit = False
        else:
            NPCscreen.gmintro2 = Story.GMIntroTest2
            NPCscreen.greeting2 = Story.NPCInteractTest2
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
            NPCscreen.firstvisit = True
            NPCscreen.gmintro1 = Story.GMIntroTest1
            NPCscreen.greeting1 = Story.NPCInteractTest1
            VendorItem.firstvisit = False
        else:
            NPCscreen.gmintro2 = Story.GMIntroTest2
            NPCscreen.greeting2 = Story.NPCInteractTest2
        NPCscreen.option1 = "-"
        NPCscreen.option2 = "-"
        NPCscreen.option3 = "-"
        NPCselect.option1 = ""
        NPCselect.option2 = ""
        NPCselect.option3 = ""
        NPCscreen.Display()


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################


####################################
####################################
##### SECTION3 - BATTLE SYSTEM #####
####################################
####################################

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

##################################
###### SECTION 3B - ENEMIES ######
##################################

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
  

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################


##################################
##################################
##### SECTION4 - LOCATIONS #######
##################################
##################################

    # FRAMEWORK FOR FUTURE LOCATIOON ADDITIONS
# class XXXXX (NavScreen):
#     def init():
#         NavScreen.currentNavScreen = XXXXX.init
#         if XXXXX.firstvisit:
#             NavScreen.firstvisit = True
#             XXXXX.firstvisit = False
#         NavScreen.describe1 = Story.GMLocationTest1
#         NavScreen.describe2 = Story.GMLocationTest2
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
        NavScreen.describe1 = Story.GMLocationTest1
        NavScreen.describe2 = Story.GMLocationTest2
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
        NavScreen.describe1 = Story.GMLocationTest1
        NavScreen.describe2 = Story.GMLocationTest2
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
        NavScreen.describe1 = Story.GMLocationTest1
        NavScreen.describe2 = Story.GMLocationTest2
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
        NavScreen.describe1 = Story.GMLocationTest1
        NavScreen.describe2 = Story.GMLocationTest2
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
        NavScreen.describe1 = Story.GMLocationTest1
        NavScreen.describe2 = Story.GMLocationTest2
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
        NavScreen.describe1 = Story.GMLocationTest1
        NavScreen.describe2 = Story.GMLocationTest2
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

#####################################
#####################################
##### SECTION5 - STORY ELEMENTS #####
#####################################
#####################################

class Story:
    
    def GMLocationTest1():
        GMnarrate.write ("First Location Test \n")
    
    def GMLocationTest2():
        GMnarrate.write ("Second Location Test \n")
    
    def GMIntroTest1():
        GMnarrate.write ("First Introduction Test \n")
    
    def GMIntroTest2():
        GMnarrate.write ("Second Introduction Test \n")

    def NPCInteractTest1():
        NPCtalk.write ("First NPC Interaction Test \n")

    def NPCInteractTest2():
        NPCtalk.write ("Second NPC Interaction Test \n")

    def StoryTest1():
        GMnarrate.write ("STORY EXAMPLE 1 \n")
    
    def StoryTest2():
        GMnarrate.write ("STORY EXAMPLE 2 \n")