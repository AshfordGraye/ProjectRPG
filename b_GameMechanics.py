import random
from os import system, name
from time import sleep
from x_TypewriterText import *
from x_ItemList import *
from x_WeaponList import *

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

def PressEnterToGoBack():
    GMtalk.write ("Press Enter to go back")
    input()
    ClearScreen()
######################################
######################################
##### SECTION1 - DISPLAY SCREENS #####
######################################
######################################

####################################
##### SECTION 1A -  LocationS #####
####################################

# Location CLASS PROVIDES FRAMEWORK FOR LOCATION OBJECTS TO DISPLAY INFORMATION CONSISTENTLY
class Location:
    currentLocation = ""
    holdLocation = ""
    lastLocation = ""
    name = ""
    firstvisit = ""
    describe1 = ""
    describe2 = ""
    option1 = ""
    option2 = ""
    option3 = ""
    travel1 = ""
    travel2 = ""
    travel3 = ""
    selectoption1 = ""
    selectoption2 = ""
    selectoption3 = ""
    selecttravel1 = ""
    selecttravel2 = ""
    selecttravel3 = ""

    def Display():
        ScreenTitle.write (f"{Location.name}\n")
        if Location.firstvisit:
            Location.describe1()
        else:
            Location.describe2()
        Location.lastLocation = Location.holdLocation
        MenuTitle.write ("Travel Menu")
        PlayerInput.write (f"0: Go back to where I was")
        PlayerInput.write (f"1: {Location.travel1}")
        PlayerInput.write (f"2: {Location.travel2}")
        PlayerInput.write (f"3: {Location.travel3}")
        MenuTitle.write ("Action Menu")
        PlayerInput.write (f"4: {Location.option1}")
        PlayerInput.write (f"5: {Location.option2}")
        PlayerInput.write (f"6: {Location.option3}")
        MenuTitle.write ("Player Menu")
        PlayerInput.write (f"7: Check Items")
        PlayerInput.write (f"8: Check Weapons")
        PlayerInput.write (f"9: Check Stats")
        print ()
        Location.Selection()

# FACILITATES PLAYER SELECTION IN THE NAV SCREEN
    def Selection():
        GMtalk.write ("What would you like to do?   \n")
        selection = input()
        print()
        if selection == "0":
            if Location.lastLocation == "":
                Location.InvalidChoice()
            else:
                ClearScreen()
                Location.firstvisit = False
                Location.holdLocation = Location.currentLocation

                Location.lastLocation()   
        elif selection == "1":
            if Location.travel1 == "":
                Location.InvalidChoice()
            else:
                ClearScreen()
                Location.firstvisit = False
                Location.holdLocation = Location.currentLocation
                print ("location held")
                Location.selecttravel1()
        elif selection == "2":
            if Location.travel2 == "":
                Location.InvalidChoice()
            else:
                ClearScreen()
                Location.firstvisit = False
                Location.holdLocation = Location.currentLocation
                Location.selecttravel2()
        elif selection == "3":
            if Location.travel3 == "":
                Location.InvalidChoice()
            else:
                ClearScreen()
                Location.firstvisit = False
                Location.holdLocation = Location.currentLocation
                Location.selecttravel3()
        elif selection == "4":
            if Location.option1 == "":
                Location.InvalidChoice()
            else:
                ClearScreen()
                Location.selectoption1()
        elif selection == "5":
            if Location.option2 == "":
                Location.InvalidChoice()
            else:
                ClearScreen()
                Location.selectoption2()
        elif selection == "6":
            if Location.option3 == "":
                Location.InvalidChoice()
            else:
                ClearScreen()
                Location.selectoption3()
        elif selection == "7":
            PlayerScreens.ItemScreen()
            input ("Press Enter to go back")
            ClearScreen()
            Location.Display()
        elif selection == "8":
            PlayerScreens.WeaponScreen()
            input ("Press Enter to go back")
            ClearScreen()
            Location.Display()
        elif selection == "9":
            PlayerScreens.StatScreen()
            input ("Press Enter to go back")
            ClearScreen()
            Location.Display()
        else:
            Location.InvalidChoice()
    
    def InvalidChoice():
        GMtalk.write ("That won't work here... Try something else.")
        input("Press Enter to go back")
        ClearScreen()
        Location.Display()

###################################
##### SECTION 1B - NPCS #####
###################################

# NPC SCREEN PROVIDES FRAMEWORK FOR WHEN PLAYER HAS SELECTED TO INTERACT WITH AN NPC ON THE NAV SCREEN
# class NPC:
#     def __init__(self, name, firstvisit, gmintro1, gmintro2, inventory, option1, option2, option3):
#     firstvisit = True
#     name = ""
#     gmintro1 = ""
#     gmintro2 = ""
#     inventory = []
#     option1 = "-"
#     option2 = "-"
#     option3 = "-"
    
class NPC:
    def __init__(self, name, firstvisit, gmintro1, gmintro2, inventory, option1, option2, option3, select1, select2, select3):
        self.name = name
        self.firstvisit = firstvisit
        self.gmintro1 = gmintro1
        self.gmintro2 = gmintro2
        self.inventory = inventory
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.select1 = select1
        self.select2 = select2
        self.select3 = select3

    def Display():
        ScreenTitle.write (f"{NPC.name}    \n")
        if NPC.firstvisit:
            NPC.gmintro1()
        else:
            NPC.gmintro2()
        MenuTitle.write ("NPC Menu")
        PlayerInput.write (f"0: Leave this conversation")
        PlayerInput.write (f"1: {NPC.option1}")
        PlayerInput.write (f"2: {NPC.option2}")
        PlayerInput.write (f"3: {NPC.option3}")
        print ()
        NPC.Selection()

    def SaleDisplay():
        ScreenTitle.write (f"{NPC.name}    \n")
        if NPC.inventory == []:
            GMnarrate.write ("The Vendor shakes hs head...")
            NPCtalk.write ("I'm afraid I've got nothing else in stock. Be sure to coe back and try again later.")
            PressEnterToGoBack()
            ClearScreen()
            NPC.Display()
        else:
            listitem = 0
            for elem in NPC.inventory:
                listitem += 1
                GMtalk.write (f"{listitem}: {elem}   \n")
        Interactions.VendorChooseItem
        GMtalk.write (f"Your currently have {Player.cash} credits on you. Enter the number for what you'd like to buy and see it's price. If you're not interested, enter 0.")
        selection = int(input())
        if selection == 0:
            NPCtalk.write ("No worries - later now.")
            PressEnterToGoBack()
            ClearScreen()
            NPC.Display()
        elif selection in range (1,listitem+1):
            selecteditem = NPC.inventory[selection-1]
            selecteditemposition = NPC.inventory.index(selecteditem)
            ClearScreen()
            NPCtalk.write (f"That there {selecteditem.name} is worth {selecteditem.value} credits. You sure? No buybacks!   \n")
            PlayerInput.write ("1: I'm sure")
            PlayerInput.write ("2: Let me look again")
            confirmsale = int(input())
            if Player.cash >= selecteditem.cost:
                if confirmsale == 1:
                    boughtitem = NPC.inventory.pop(selecteditemposition)
                    Player.cash -= boughtitem.cost
                    GMnarrate.write (f"You acquired a {boughtitem.name}! You now have {Player.cash} credits left.")
                    Player.items.append(boughtitem)
                    PressEnterToGoBack()
                    ClearScreen()
                    NPC.SaleDisplay()
                elif confirmsale == 2:
                    NPCtalk.write ("Alright, have another look.")
                    NPC.SaleDisplay()
                else:
                    NPCtalk.write ("What? I didn't quite catch that. Let me show you again")
                    GMtalk.write (input("Press Enter to go back"))
                    NPC.SaleDisplay()
            else:
                Interactions.VendorNoMoney()
                NPC.SaleDisplay()
        else:
            NPC.InvalidChoice()
    
    def Selection():
        selection = input("What would you like to do?   \n")
        print()
        if selection == "0":
            ClearScreen()
            NPC.firstvisit = False
            Location.currentLocation()
        elif selection == "1":
            if NPC.select1 == "":
                NPC.InvalidChoice()
            else:
                ClearScreen()
                NPC.select1()
        elif selection == "2":
            if NPC.select2 == "":
                NPC.InvalidChoice()
            else:
                ClearScreen()
                NPC.select2()
        elif selection == "3":
            if NPC.select3 == "":
                NPC.InvalidChoice()
            else:
                ClearScreen()
                NPC.select3()
        else:
            NPC.InvalidChoice()




    def InvalidChoice():
        GMtalk.write ("That won't work here... Try something else.")
        input("Press Enter to go back")
        ClearScreen()
        NPC.Display()

# FACILITATES PLAYER SELECTION IN THE NPC SCREEN
# class NPCselect:

#     option1 = "NPC1"
#     option2 = "NPC2"
#     option3 = "NPC3"

#     def init():

#         selection = input("What would you like to do?   \n")
#         print()
#         if selection == "0":
#             ClearScreen()
#             NPC.firstvisit = False
#             Location.currentLocation()
#         elif selection == "1":
#             if NPC.select1 == "":
#                 NPCselect.InvalidChoice()
#             else:
#                 ClearScreen()
#                 NPC.select1()
#         elif selection == "2":
#             if NPC.select2 == "":
#                 NPCselect.InvalidChoice()
#             else:
#                 ClearScreen()
#                 NPC.select2()
#         elif selection == "3":
#             if NPC.select3 == "":
#                 NPCselect.InvalidChoice()
#             else:
#                 ClearScreen()
#                 NPC.select3()
#         else:
#             NPCselect.InvalidChoice()
    
#     def InvalidChoice():
#         GMtalk.write ("That won't work here... Try something else.")
#         input("Press Enter to go back")
#         ClearScreen()
#         NPC.Display()





######################################
##### SECTION 1C - PLAYERSCREENS #####
######################################

class PlayerScreens:
    def StatScreen():
        ClearScreen()
        GMnarrate.write(f'''
Your current stats are:
    Health:                 {Player.hp}/{Player.hpmax}

    Physical Strength:      {Player.phystr}
    Physical Defense:       {Player.phydef}
    Magetek Strength:       {Player.magstr}
    Magetek Defense:        {Player.magdef}
    ''')
        

    def WeaponScreen():
        ClearScreen()
        GMnarrate.write (f'''
You currently have the following equipped:
    Physical Weapon:        {Player.physequip}
    Armatek Weapon:         {Player.magequip}
    ''')

    def ItemScreen():
        ClearScreen()
        if Player.items == []:
            GMnarrate.write("You do not have anything in your inventory right now.  \n")
        else:
            GMnarrate.write ("You currently have the following in your inventory:   \n")
            listitem = 0
            for elem in Player.items:
                listitem += 1
                GMtalk.write (f"{listitem}: {elem}   \n")


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
    
    cash = 200

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

        Player.cash = 0
        
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
# class XXXXX(NPC):
#     firstvisit = True
#     def init():
#         NPC.name = "XXXXX"
#         if XXXXX.firstvisit:
#             NPC.firstvisit = True
#             NPC.gmintro1 = Story.GMIntroTest1
#
#             XXXXX.firstvisit = False
#         else:
#             NPC.gmintro2 = Story.GMIntroTest2
#
#         NPC.option1 = "-"
#         NPC.option2 = "-"
#         NPC.option3 = "-"
#         NPC.select1 = ""
#         NPC.select2 = ""
#         NPC.select3 = ""
#         NPC.Display()

class Porter (NPC):
    firstvisit = True
    localinventory = []
    def init():
        NPC.name = "Skytrain Dock porter"
        if Porter.firstvisit:
            NPC.firstvisit = True
            NPC.gmintro1 = Story.GMIntroTest1
            Porter.firstvisit = False
        else:
            NPC.gmintro2 = Story.GMIntroTest2
        NPC.option1 = "-"
        NPC.option2 = "-"
        NPC.option3 = "-"
        NPC.select1 = ""
        NPC.select2 = ""
        NPC.select3 = ""
        NPC.Display()

class HomelessGuy(NPC):
    firstvisit = True
    localinventory = []
    def init():
        NPC.name = "Homeless Guy"
        if HomelessGuy.firstvisit:
            NPC.firstvisit = True
            NPC.gmintro1 = Story.GMIntroTest1
            HomelessGuy.firstvisit = False
        else:
            NPC.gmintro2 = Story.GMIntroTest2
        NPC.option1 = "-"
        NPC.option2 = "-"
        NPC.option3 = "-"
        NPC.select1 = ""
        NPC.select2 = ""
        NPC.select3 = ""
        NPC.Display()

class Medic(NPC):
    firstvisit = True
    localinventory = []
    def init():
        NPC.name = "Medic"
        if Medic.firstvisit:
            NPC.firstvisit = True
            NPC.gmintro1 = Story.GMIntroTest1
            Medic.firstvisit = False
        else:
            NPC.gmintro2 = Story.GMIntroTest2
        NPC.option1 = "I'm hurt, can you help?"
        NPC.option2 = "What's that droid for?"
        NPC.option3 = "-"
        NPC.select1 = ""
        NPC.select2 = ""
        NPC.select3 = ""
        NPC.Display()

class FieldDroid(NPC):
    firstvisit = True
    localinventory = []
    def init():
        NPC.name = "Field Droid"
        if FieldDroid.firstvisit:
            NPC.firstvisit = True
            NPC.gmintro1 = Story.GMIntroTest1
            FieldDroid.firstvisit = False
        else:
            NPC.gmintro2 = Story.GMIntroTest2
        NPC.option1 = "Instruct Droid to fix you up"
        NPC.option2 = "-"
        NPC.option3 = "-"
        NPC.select1 = ""
        NPC.select2 = ""
        NPC.select3 = ""
        NPC.Display()

class VendorPhys (NPC):
    firstvisit = True
    localinventory = []
    def init():
        NPC.name = "Store - Iron Will"
        if VendorPhys.firstvisit:
            NPC.firstvisit = True
            NPC.gmintro1 = Interactions.VendorGreeting
            VendorPhys.firstvisit = False
        else:
            NPC.gmintro2 = Interactions.VendorGreeting
        NPC.option1 = "-"
        NPC.option2 = "-"
        NPC.option3 = "-"
        NPC.select1 = ""
        NPC.select2 = ""
        NPC.select3 = ""
        NPC.Display()

class VendorMag (NPC):
    firstvisit = True
    localinventory = []
    def init():
        NPC.name = "Store - Technomancy"
        if VendorMag.firstvisit:
            NPC.firstvisit = True
            NPC.gmintro1 = Interactions.VendorGreeting
            VendorMag.firstvisit = False
        else:
            NPC.gmintro2 = Interactions.VendorGreeting
        NPC.option1 = "-"
        NPC.option2 = "-"
        NPC.option3 = "-"
        NPC.select1 = ""
        NPC.select2 = ""
        NPC.select3 = ""
        NPC.Display()

class VendorItem (NPC):
    firstvisit = True
    localinventory = [Potion, HiPotion]
    def init():
        NPC.name = "Store - Going Alone"
        if VendorItem.firstvisit:
            NPC.firstvisit = True
            NPC.gmintro1 = Interactions.VendorGreeting
            VendorItem.firstvisit = False
        else:
            NPC.gmintro2 = Interactions.VendorGreeting
        NPC.inventory = VendorItem.localinventory
        NPC.option1 = "View wares"
        NPC.option2 = "-"
        NPC.option3 = "-"
        NPC.select1 = NPC.SaleDisplay
        NPC.select2 = ""
        NPC.select3 = ""
        NPC.Display()



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
# class XXXXX (Location):
#     def init():
#         Location.currentLocation = XXXXX.init
#         if XXXXX.firstvisit:
#             Location.firstvisit = True
#             XXXXX.firstvisit = False
#         Location.describe1 = Story.GMLocationTest1
#         Location.describe2 = Story.GMLocationTest2
#         Location.name = "XXXXX"
#         Location.option1 = "-"
#         Location.option2 = "-"
#         Location.option3 = "-"
#         Location.travel1 = "-"
#         Location.travel2 = "-"
#         Location.travel3 = "-"
#         Location.selectoption1 = "-"
#         Location.selectoption2 = "-"
#         Location.selectoption3 = "-"
#         Location.selecttravel1 = "-"
#         Location.selecttravel2 = "-"
#         Location.selecttravel3 = "-"
#         Location.Display()


class Train (Location): 
    firstvisit = True
    def init():
        Location.currentLocation = Train.init
        if Train.firstvisit:
            Location.firstvisit = True
            Train.firstvisit = False
        Location.describe1 = Story.GMLocationTest1
        Location.describe2 = Story.GMLocationTest2
        Location.name = "Skytrain"
        Location.travel1 = "Leave the Skytrain"
        Location.travel2 = "-"
        Location.travel3 = "-"
        Location.option1 = "-"
        Location.option2 = "-"
        Location.option3 = "-"
        Location.selecttravel1 = Station.init
        Location.Display()

class Station (Location):
    firstvisit = True
    def init():
        Location.currentLocation = Station.init
        if Station.firstvisit:
            Location.firstvisit = True
            Station.firstvisit = False
        Location.describe1 = Story.GMLocationTest1
        Location.describe2 = Story.GMLocationTest2
        Location.name = "Skytrain Dock Station"
        Location.travel1 = "Board the Skytrain"
        Location.travel2 = "-"
        Location.travel3 = "Head to the Power Station"
        Location.option1 = "Talk to the Dock Porter"
        Location.option2 = "Approach the homeless guy"
        Location.option3 = "-"
        Location.selecttravel1 = Train.init
        Location.selecttravel2 = ""
        Location.selecttravel3 = PowerStation.init
        Location.selectoption1 = Porter.init
        Location.selectoption2 = HomelessGuy.init
        Location.selectoption3 = ""
        Location.Display()

class PowerStation (Location):
    firstvisit = True
    def init():
        Location.currentLocation = PowerStation.init
        if PowerStation.firstvisit:
            Location.firstvisit = True
            PowerStation.firstvisit = False
        Location.describe1 = Story.GMLocationTest1
        Location.describe2 = Story.GMLocationTest2
        Location.name = "Old Power Station - Grounds"
        Location.travel1 = "Visit the Medic Station"
        Location.travel2 = "Visit the makeshift Bazaar in the Station lobby"
        Location.travel3 = "Head to the Skytrain Station"
        Location.option1 = "-"
        Location.option2 = "-"
        Location.option3 = "-"
        Location.selecttravel1 = MedicStation.init
        Location.selecttravel2 = Bazaar.init
        Location.selecttravel3 = Station.init
        Location.selectoption1 = ""
        Location.selectoption2 = ""
        Location.selectoption3 = ""
        Location.Display()

class MedicStation (Location):
    firstvisit = True
    def init():
        Location.currentLocation = MedicStation.init
        if MedicStation.firstvisit:
            Location.firstvisit = True
            MedicStation.firstvisit = False
        Location.describe1 = Story.GMLocationTest1
        Location.describe2 = Story.GMLocationTest2
        Location.name = "Old Power Station - Medic's Area"
        Location.travel1 = "-"
        Location.travel2 = "-"
        Location.travel3 = "-"
        Location.option1 = "Talk to the Medic"
        Location.option2 = "Approach the Field Droid"
        Location.option3 = "-"
        Location.selecttravel1 = ""
        Location.selecttravel2 = ""
        Location.selecttravel3 = ""
        Location.selectoption1 = Medic.init
        Location.selectoption2 = FieldDroid.init
        Location.selectoption3 = ""
        Location.Display()

class Bazaar (Location):
    firstvisit = True
    def init():
        Location.currentLocation = Bazaar.init
        if Bazaar.firstvisit:
            Location.firstvisit = True
            Bazaar.firstvisit = False
        Location.describe1 = Story.GMLocationTest1
        Location.describe2 = Story.GMLocationTest2
        Location.name = "Old Power Station - Makeshift Bazaar"
        Location.travel1 = "-"
        Location.travel2 = "-"
        Location.travel3 = "-"
        Location.option1 = "Talk to the Magetek Vendor"
        Location.option2 = "Talk to the Physical Vendor"
        Location.option3 = "Talk to the Item Vendor"
        Location.selecttravel1 = ""
        Location.selecttravel2 = ""
        Location.selecttravel3 = ""
        Location.selectoption1 = VendorMag.init
        Location.selectoption2 = VendorPhys.init
        Location.selectoption3 = VendorItem.init
        Location.Display()

class StationFloor (Location):
    firstvisit = True
    def init():
        Location.currentLocation = StationFloor.init
        if StationFloor.firstvisit:
            Location.firstvisit = True
            StationFloor.firstvisit = False
        Location.describe1 = Story.GMLocationTest1
        Location.describe2 = Story.GMLocationTest2
        Location.name = "Old Power Station - Work Floor"
        Location.travel1 = "-"
        Location.travel2 = "-"
        Location.travel3 = "-"
        Location.option1 = "Approach the Arena Cage"
        Location.option2 = "-"
        Location.option3 = "-"
        Location.selecttravel1 = ""
        Location.selecttravel2 = ""
        Location.selecttravel3 = ""
        Location.selectoption1 = ""
        Location.selectoption2 = ""
        Location.selectoption3 = ""
        Location.Display()

#####################################
#####################################
##### SECTION5 - STORY ELEMENTS #####
#####################################
#####################################

class Interactions:

# VENDORS

    def VendorGreeting():
        greeting = random.randint(1,3)
        if greeting == 1:
            GMnarrate.write ("You are greeted with a friendly smile \n")
            NPCtalk.write ("Well howdy there! What can I get ya \n")
        elif greeting == 2:
            GMnarrate.write ("You are quickly examined, presumably for trouble, before being greeted    \n")
            NPCtalk.write ("Hey there, how can I help you?  \n")
        else:
            GMnarrate.write ("The individual looks at you with a vacant expression... they look like they've been here a while  \n")
            NPCtalk.write ("Hey, uhh... what's up?  \n")

    def VendorChooseItem():
        option = random.randint(1,4)
        if option == 1:
            NPCtalk.write ("So what'll it be  \n?")
        elif option ==2:
            NPCtalk.write ("Anything take your fancy?  \n")
        elif option == 3:
            NPCtalk.write ("What catches your eye there?  \n")
        else:
            NPCtalk.write ("Got some good stuff for sale!  \n")

    def VendorNoMoney():
        greeting = random.randint(1,13)
        if greeting in range (1,5):
            GMnarrate.write ("The Vendor shakes their head...  \n")
            NPCtalk.write ("No creds, no goods I'm afraid... maybe come back when you've got something for me  \n")
        elif greeting in range (5,10):
            GMnarrate.write ("The Vendor glances at you with an annoyed expression  \n")
            NPCtalk.write ("... and what exactly are you going to be paying me with? Come on now.  \n")
        else:
            GMnarrate.write ("The Vendor looks kind of angry, perhaps you upset them…  \n")
            NPCtalk.write ("Do I look like a damn charity to you? Get outta here until you've got soemthing WORTH MY TIME!!!  \n")
        PressEnterToGoBack()




class Story:
    
    def GMLocationTest1():
        GMnarrate.write ("First Location Test \n")
    
    def GMLocationTest2():
        GMnarrate.write ("Second Location Test \n")
    
    def GMIntroTest1():
        GMnarrate.write ("First Introduction Test \n")
    
    def GMIntroTest2():
        GMnarrate.write ("Second Introduction Test \n")

    def NPCspeechtest1():
        NPCtalk.write ("First NPC Interaction Test \n")

    def NPCspeechtest2():
        NPCtalk.write ("Second NPC Interaction Test \n")

    def StoryTest1():
        GMnarrate.write ("STORY EXAMPLE 1 \n")
    
    def StoryTest2():
        GMnarrate.write ("STORY EXAMPLE 2 \n")








