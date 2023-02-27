import random
from os import system, name
from time import sleep
from x_TypewriterText import *
from x_ItemList import *
from x_WeaponList import *
from x_AbilityList import *
from EnemyAbilities import *



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

def PressEnterToContinue():
    GMtalk.write ("Press Enter to continue")
    input()
    ClearScreen()

def PressEnterToGoBack():
    GMtalk.write ("Press Enter to go back")
    input()
    ClearScreen()

def InvalidChoice():
    GMtalk.write ("That won't work here... you'll have to try something else.")
    PressEnterToGoBack()

def CountDown():
    timer = 5
    while timer >= 4:
        GMtalk.write(f"{timer}...")
        timer -= 1
        sleep(1)
    ClearScreen()



#############################################
##### SECTION 1 - OBJECT CLASS CREATION #####
#############################################

# LOCATION CLASS PROVIDES VARIABLES AND FUNCTIONS FOR LOCATIONS TO DISPLAY INFORMATION CONSISTENTLY
class Location:
    
    def __init__(self, name):
        self.name = name
    firstvisit = True
    describe1 = ""
    describe2 = ""
    option1 = "-"
    option2 = "-"
    option3 = "-"
    travel1 = "-"
    travel2 = "-"
    travel3 = "-"
    selectoption1 = "-"
    selectoption2 = "-"
    selectoption3 = "-"
    selecttravel1 = "-"
    selecttravel2 = "-"
    selecttravel3 = "-"

    # LOADS WHEN A LOCATION IS TRAVELLED TO - DISPLAYS LOCATION INFO AND SORTS TRAVEL BACK TO PREVIOUS  
    def Area (self):
        WorldBuilding.LocationUpdate()
        if self.firstvisit:
            self.describe1()
            print()
        else:
            self.describe2()
            print()
        PlayerOne.currentlocation = self.Area
        PlayerOne.lastlocation = PlayerOne.holdlocation
        ScreenTitle.write (f"{self.name}\n")
        MenuTitle.write ("Travel Menu")
        PlayerInput.write (f"0: Go back to where I was")
        PlayerInput.write (f"1: {self.travel1}")
        PlayerInput.write (f"2: {self.travel2}")
        PlayerInput.write (f"3: {self.travel3}")
        MenuTitle.write ("Action Menu")
        PlayerInput.write (f"4: {self.option1}")
        PlayerInput.write (f"5: {self.option2}")
        PlayerInput.write (f"6: {self.option3}")
        MenuTitle.write ("Player Menu")
        PlayerInput.write (f"7: Check Items")
        PlayerInput.write (f"8: Check Weapons")
        PlayerInput.write (f"9: Check Stats")
        print ()
        self.Selection()

    # FACILITATES PLAYER SELECTION IN THE NAV SCREEN
    def Selection(self):
        GMtalk.write ("What would you like to do?   \n")
        selection = input()
        if selection in range (1,7):
            self.firstvisit = False
        print()
        if selection == "0":
            if PlayerOne.lastlocation == "":
                self.InvalidChoice()
            else:
                ClearScreen()
                self.firstvisit = False
                PlayerOne.holdlocation = PlayerOne.currentlocation

                PlayerOne.lastlocation()   
        elif selection == "1":
            if self.selecttravel1 == "-":
                self.InvalidChoice()
            else:
                ClearScreen()
                self.firstvisit = False
                PlayerOne.holdlocation = PlayerOne.currentlocation
                self.selecttravel1()
        elif selection == "2":
            if self.selecttravel2 == "-":
                self.InvalidChoice()
            else:
                ClearScreen()
                self.firstvisit = False
                PlayerOne.holdlocation = PlayerOne.currentlocation
                self.selecttravel2()
        elif selection == "3":
            if self.selecttravel3 == "-":
                self.InvalidChoice()
            else:
                ClearScreen()
                self.firstvisit = False
                PlayerOne.holdlocation = PlayerOne.currentlocation
                self.selecttravel3()
        elif selection == "4":
            if self.selectoption1 == "-":
                self.InvalidChoice()
            else:
                ClearScreen()
                self.selectoption1()
        elif selection == "5":
            if self.selectoption2 == "-":
                self.InvalidChoice()
            else:
                ClearScreen()
                self.selectoption2()
        elif selection == "6":
            if self.selectoption3 == "-":
                self.InvalidChoice()
            else:
                ClearScreen()
                self.selectoption3()
        elif selection == "7":
            Player.ShowItems()
            input ("Press Enter to go back")
            ClearScreen()
            self.Area()
        elif selection == "8":
            Player.ShowWeapons()
            input ("Press Enter to go back")
            ClearScreen()
            self.Area()
        elif selection == "9":
            Player.ShowStats()
            input ("Press Enter to go back")
            ClearScreen()
            self.Area()
        else:
            self.InvalidChoice()
    
    # SELF EXPLANATORY  
    def InvalidChoice(self):
        InvalidChoice()
        self.Area()

# MAIN CHARACTER CLASS WITH VARIABLES NECESSARY FOR ALL CHARACTERS
class Character:
    
    def __init__(self, name):
        self.name = name

    job = ""

    cash = ""

    hpmax = ""
    hp = hpmax
    mpmax = ""
    mp = mpmax

    phystr = ""
    phydef = ""
    armstr = ""
    armdef = ""

    phyweapons = []
    physequip = []
    armweapons = []
    armequip = []
    
    items = []

    moveset = []

# PLAYER CHARACTER SUBCLASS IS CONTROLLABLE BY THE PLAYER
class Player(Character):

    currentlocation = ""
    holdlocation = ""
    lastlocation = ""

    cash = 200
    
    job = ""

    hpmax = 1000
    hp = 101
    mpmax = 100
    mp = mpmax

    phystr = 10
    phydef = 10
    armstr = 10
    armdef = 10

    phyweapons = [BareKnuckles]
    physequip = [BareKnuckles]
    armweapons = []
    armequip = []
    
    items = []

    moves = [Attack]
    arenawins = 0
    arenaroundcomplete = False

    handholding = ""
    menuselect = ""
    

    def MenuSelection():
        GMtalk.write("What would you like to do?    \n")
        Player.menuselect = input ()

    def Naming():
        PlayerInput.write("Enter your name:")
        Player.name = "Player"
        print ()
    
    def ClassChoice():
        GMtalk.write ('''
Different roles will affect your how strong your Physical and Armatek abilities are, and how well you can defend against them. 
As you progress in the game you will have the option of usig different weapons and items that also influence these stats.

Remember, your enemies will have strengths and weaknesses too!
    ''')
        PlayerInput.write ('''
What was your role in the military? Enter a role number to view it's stats.

    1: Soldier
    2: Scientist
    3: Medic
    4: Officer''')


        viewclass = "1"

        if viewclass.lower() == "1":
            Player.job = "Soldier"
            Player.phystr += (Player.phystr /100 *30)
            Player.armdef -= (Player.armdef /100 *30)
            Player.moves = {"Attack": random.randint(25,35) + Player.phystr}
            GMnarrate.write (f'''
A former {Player.job}, you fought in the Alliance Army as a Shock Trooper.
The Army's excellent training has given you great strength when fighting. 

Your stats will be:
{Player.phystr} Physical Strength
{Player.phydef} Physical Defense
{Player.armstr} Armatek Strength
{Player.armdef} Armatek Defense
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
                Player.armstr = 10
                Player.armdef = 10
                Player.ClassChoice()
            else:
                GMtalk.write ("Please enter the number of your selection")

        elif viewclass.lower() == "2":
            Player.job = "Scientist"
            Player.armstr += (Player.armstr /100 *30)
            Player.phydef -= (Player.phydef /100 *30)
            Player.moves = {"Attack": random.randint(25,35) + Player.phystr}
            GMnarrate.write (f'''
A former {Player.job}, you designed weaponry to be used against the enemy.
Your knowledge of Armatek gives you an advantage when using Armatek abilities.

Your stats will be:
{Player.phystr} Physical Strength
{Player.phydef} Physical Defense
{Player.armstr} Armatek Strength
{Player.armdef} Armatek Defense
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
                Player.armstr = 10
                Player.armdef = 10
                Player.ClassChoice()
            else:
                GMtalk.write ("Please enter the number of your selection")

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
{Player.armstr} Armatek Strength
{Player.armdef} Armatek Defense
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
                Player.armstr = 10
                Player.armdef = 10
                Player.ClassChoice()
            else:
                GMtalk.write ("Please enter the number of your selection")

        elif viewclass.lower() == "4":
            Player.job = "Officer"
            Player.armdef += (Player.armdef /100 *30)
            Player.armstr -= (Player.armstr /100 *30)
            Player.moves = {"Attack": random.randint(25,35) + Player.phystr}
            GMnarrate.write (f'''
A former {Player.job} in the Alliance Navy, you commanded SkyCruiser fleets against the Commonwealth.
Your officer's training gave you increased defense against Armatek abilities. 

Your stats will be:
{Player.phystr} Physical Strength
{Player.phydef} Physical Defense
{Player.armstr} Armatek Strength
{Player.armdef} Armatek Defense
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
                Player.armstr = 10
                Player.armdef = 10
                Player.ClassChoice()
            else:
                GMtalk.write ("Please enter the number of your selection")
    
    def Reset():
        Player.hp = Player.hpmax
        Player.mp = Player.mpmax

    def ShowStats():
        ClearScreen()
        GMnarrate.write(f'''
Your current stats are:
    Health:                 {Player.hp}/{Player.hpmax}

    Physical Strength:      {Player.phystr}
    Physical Defense:       {Player.phydef}
    Armatek Strength:       {Player.armstr}
    Armatek Defense:        {Player.armdef}
    ''')
        
    def ShowWeapons():
        ClearScreen()
        GMtalk.write ("You currently have the following equipped:")
        if len(PlayerOne.physequip) == 0:
            GMnarrate.write("Physical Weaponry:     You do not have a weapon equipped.")
        else:
            GMnarrate.write(f"Physical Weapon:       {PlayerOne.physequip[0]}")
        if len(PlayerOne.armequip) == 0:
            GMnarrate.write("Armatek Equipment:     You do not have any Armatek equipped.")
        else:
            GMnarrate.write(f"Armatek Equipment:     {PlayerOne.armequip[0]}")

    def ShowItems():
        ClearScreen()
        if Player.items == []:
            GMnarrate.write("You do not have anything in your inventory right now.  \n")
        else:
            GMnarrate.write ("You currently have the following in your inventory:   \n")
            listitem = 0
            for elem in Player.items:
                listitem += 1
                GMtalk.write (f"{listitem}: {elem}   \n")


    def ChangeEquipment(self):
        GMtalk.write("Would you like to change any of your current equipment?")
        self.MenuSelection()
        
        
# NPC CHARACTER SUBCLASS CAN BE INTERACTED WITH BY THE PLAYER TO TRIGGER CONVERSATIONS AND EVENTS
class NPC(Character):
    
    firstmeet = True
    gmintro1 = ""
    gmintro2 = ""
    talkoption1 = ""
    talkoption2 = ""
    talkoption3 = ""
    talkselect1 = ""
    talkselect2 = ""
    talkselect3 = ""

    def Talk(self):
        if self.firstmeet:
            self.gmintro1()
        else:
            self.gmintro2()
        MenuTitle.write (f"\n{self.name}")
        PlayerInput.write (f"0: Leave this conversation")
        PlayerInput.write (f"1: {self.talkoption1}")
        PlayerInput.write (f"2: {self.talkoption2}")
        PlayerInput.write (f"3: {self.talkoption3}")
        print ()
        self.TalkSelection()

    def TalkSelection(self):
        Player.MenuSelection()
        print (Player.menuselect)
        if Player.menuselect in [str(n) for n in range (1,4)]:
            self.firstmeet = False
        if Player.menuselect == "0":
            ClearScreen()
            PlayerOne.currentlocation()
        elif Player.menuselect == "1":
            if self.talkselect1 == "":
                NPC.InvalidChoice()
            else:
                ClearScreen()
                self.talkselect1()
        elif Player.menuselect == "2":
            if self.talkselect2 == "":
                NPC.InvalidChoice()
            else:
                ClearScreen()
                self.talkselect2()
        elif Player.menuselect == "3":
            if self.talkselect3 == "":
                NPC.InvalidChoice()
            else:
                ClearScreen()
                self.talkselect3()
        else:
            print("messup")
            self.InvalidChoice()

    def InvalidChoice(self):
        InvalidChoice()
        self.Talk()

# VENDORS ARE AN NPC SUBCLASS TO DIFFERENTIATE BETWEEN CONVERSATIONS AND COMMERCE
class Vendor (NPC):

    def SaleDisplay():
        ScreenTitle.write (f"{NPC.name}    \n")
        if NPC.inventory == []:
            GMnarrate.write ("The Vendor shakes hs head...")
            NPCtalk.write ("I'm afraid I've got nothing else in stock. Be sure to coe back and try again later.")
            PressEnterToGoBack()
            ClearScreen()
            NPC.Display()
        else:
            Interactions.VendorPresentItems()
            listitem = 0
            for elem in NPC.inventory:
                listitem += 1
                GMtalk.write (f"{listitem}: {elem}   \n")
        GMtalk.write (f"Your currently have {Player.cash} credits on you. Enter the number for what you'd like to buy and see it's price. If you're not interested, enter 0.")
        selection = int(input())
        if selection == 0:
            ClearScreen()
            NPCtalk.write ("No worries - later now. \n")
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

# ENEMY CHARACTERS ARE USED IN COMBAT
class Enemy(Character):

    def __init__(self, name, level):
        
        self.name = name
        self.level = level

        if level == 1:
            self.job = "Vagrant"
            self.hpmax = 250
            self.hp = 250
            self.phystr = 5
            self.phydef = 5
            self.armstr = 5
            self.armdef = 5
            self.moves = [Lunge]
            self.movechoice = ""

    def MoveSelect(self):
        misschance = random.randint (1,100)
        movechoice = random.randint (1,10)
        if self.level == 1:
            if movechoice in range (1,5) and misschance in range (1,90):
                self.moveselection = Lunge
                Enemy.DamageCalculation(self)
            elif movechoice in range (5,11) and misschance in range (1,90):
                self.moveselection = Lunge
                Enemy.DamageCalculation(self)
            else:
                GMnarrate.write (f"The {self.name} tried to attack, but missed!  \n")


    def DamageCalculation(self):
        if self.moveselection.effect == "SinglePhysical":
            totaldamage = (self.moveselection.damage + self.phystr - Player.phydef)
            Player.hp -= totaldamage
        GMnarrate.write (f"{self.name} used {self.moveselection.name} for {totaldamage} damage \n")

# VENDORS ARE AN NPC SUBCLASS TO DIFFERENTIATE BETWEEN CONVERSATIONS AND COMMERCE


#######################################
###### SECTION - OBJECT CREATION ######
#######################################

#  NOW THE PREVIOUS SECTION TOOK CARE OF CREATING THE OBJECT CLASSES, WE'LL CREATE THE OBJECTS IN THEIR OWN SUBSECTIONS HERE

# LOCATIONS
TutorialWorld = Location("The name of your current location")
Train = Location("Skytrain")
SkytrainDock = Location("Skytrain Dock")
PowerStationGrounds = Location("Power Station - Grounds")
PowerStationMedicArea = Location("Power Station - Medic's Station")
PowerStationBazaar = Location("PowerStation - Bazaar")
PowerStationArena = Location("Power Station - Arena")

# PLAYABLE CHARACTERS
PlayerOne = Player ("Ash")

# NPC CHARACTERS
TutorialCharacter = NPC("Tutorial NPC")
DockPorter = NPC ("Skytrain Dock Porter")
HomelessGuy = NPC ("Homeless Guy")
PowerStationBoss = NPC ("Power Station Boss")

# STORE VENDORS 
VendorItem = Vendor("Item Vendor")
VendorPhysical = Vendor ("Physical Equipment Vendor")
VendorArmatek = Vendor ("Armatek Equipment Vendor")


# ENEMY CHARACTERS
Vagrant = Enemy ("Vagrant", 1)
Vagrant2 = Enemy ("Vagrant 2", 1)


############################
############################
##### SECTION - COMBAT #####
############################
############################

# BATTLE SYSTEM ITSELF DOES ALL THE LEGWORK 
class BattleSystem:
    
    #
    battlestart = True
    #enemy list gets populated at battle start and selectedenemy is populated when a player selectes an enemy to attack
    enemies = []
    selectedenemy = ""

    #variables for listing and selection of abilities across functions
    playermovelist = 0
    playermovechoice = 0
    playerenemychoice = 0

#what goes on during the enemy turn 
    def EnemyTurn():
        MenuTitle.write ("Enemy Turn:   \n")
        for elem in BattleSystem.enemies:
            elem.MoveSelect()
        # BattleSystem.CheckForVictory()
        Player.playerturn = not Player.playerturn
        if Player.hp <= 0:
            StoryEvent.EndTheGame()
        else:
            PressEnterToContinue()

#player turn!
    def PlayerTurn():
        for elem in BattleSystem.enemies:
            print (elem.job, elem.hp)
        BattleSystem.PlayerTurnDisplay()
        BattleSystem.PlayerAbilitySelect()
        # BattleSystem.CheckForVictory()
        Player.playerturn = not Player.playerturn
        PressEnterToContinue()

# displays player stats on screen during player turn 
    def PlayerTurnDisplay():
        MenuTitle.write("Your Turn: \n")
        for elem in BattleSystem.enemies:
            if elem.hp > (elem.hpmax /100 *70):
                GMnarrate.write("The foe stands strong! Don't give up!   \n")
            elif elem.hp > (elem.hpmax /100 *30):
                GMnarrate.write("Your foe grows weaker! Keep it up!  \n")
            elif elem.hp <= (elem.hpmax /100 *30):
                GMnarrate.write("Your enemy grows weak! Almost there!    \n")

        MenuTitle.write (f"{PlayerOne.name}:")
        if PlayerOne.hp > (PlayerOne.hpmax /100 * 25):
            print (f' {type.fg_orange}HP:{type.reset}   {type.fg_green}{PlayerOne.hp}/{PlayerOne.hpmax}{type.reset}')
        elif PlayerOne.hp <= (PlayerOne.hpmax /100 * 25):
            print (f' {type.fg_orange}HP:{type.reset}   {type.fg_red}{PlayerOne.hp}{type.reset}/{type.fg_green}{PlayerOne.hpmax}{type.reset}')
        
        if PlayerOne.mp > (PlayerOne.mpmax /100 * 25):
            print (f' {type.fg_orange}MP:{type.reset}   {type.fg_green}{Player.mp}/{Player.mp}{type.reset}')
        elif PlayerOne.mp <= (PlayerOne.mpmax /100 *25):
            print (f' {type.fg_orange}MP:{type.reset}   {type.fg_red}{PlayerOne.mp}{type.reset}/{type.fg_green}{PlayerOne.mpmax}{type.reset}\n')
        print()
        

        # KEEP THIS TO INSERT AS SCAN ABILITY LATER:

        # MenuTitle.write (f"{Enemy.job} Status")
        # if (Enemy.hp > Enemy.hpmax/100 *25):
        #     print (f' {type.fg_orange}HP:{type.reset}   {type.fg_green}{Enemy.hp}/{Enemy.hpmax}{type.reset}')
        # if (Enemy.hp <= Enemy.hpmax /100 *25):
        #     print (f' {type.fg_orange}HP:{type.reset}   {type.fg_red}{Enemy.hp}{type.reset}/{type.fg_orange}{Enemy.hpmax}{type.reset}')
        # print()

# how player selects abilities
    def PlayerAbilitySelect():
        listmoves = 0 #to number the ability list dynamically 
        MenuTitle.write ("Select an option:")
        
        #this bit swaps out the standard attack move in move slot 0 with LimtBreak when health is below 10%
        if Player.hp <= (Player.hpmax/100*10):
            Player.moves [0] = LimitBreak
        else:
            Player.moves [0] = Attack
        
        # list the choices
        for elem in Player.moves:
            listmoves += 1
            PlayerInput.write (f" {listmoves}: {elem} \n")
        #get player selection - try statement takes care of blank inputs. 
        
        BattleSystem.playermovechoice = input()
        #check to see if selection is valid, then move to select the enemy 
        if BattleSystem.playermovechoice in [str(n) for n in range (1, listmoves+1)]:
            BattleSystem.PlayerSelectEnemy()
        else:
            InvalidChoice()
            BattleSystem.PlayerTurn()

#get selectin!
    def PlayerSelectEnemy():
        listofenemies = 0
        #autoselect if there's only one enemy cos duh...
        if len (BattleSystem.enemies) == 1:
            BattleSystem.selectedenemy = BattleSystem.enemies[0]
            BattleSystem.PlayerMoveConfirmed()
        #if more than one, list and select in the same way as selecting an ability. Neat!
        else:
            GMtalk.write(f"Select an enemy to attack    \n")
            for elem in BattleSystem.enemies:
                listofenemies += 1
                PlayerInput.write (f" {listofenemies}: {elem.name}")
            BattleSystem.playerenemychoice = int(input())
            if BattleSystem.playerenemychoice in range (1, listofenemies+1):
                BattleSystem.selectedenemy = BattleSystem.enemies[BattleSystem.playerenemychoice-1]
                BattleSystem.PlayerMoveConfirmed()
            else:
                GMtalk.write ("Invalid Input")
                BattleSystem.PlayerSelectEnemy()

#now enemy is selected, move is confirmed. 
    def PlayerMoveConfirmed():
            BattleSystem.playermovechoice = int(BattleSystem.playermovechoice)
            selectedmove = Player.moves[BattleSystem.playermovechoice-1]
            #accuracycheck checks against the misschance of the selected move.
            accuracycheck = random.randint (1,100)
            if accuracycheck in range (selectedmove.misschance): # so if the accuracycheck falls within the misschance of the selected move, it misses.
                GMnarrate.write  ("You missed!  \n")
            else: #otherwise, it hits and so determines how damage or buffs work here base on the selected move effect value
                if selectedmove.effect == "Physical":
                    damage = (Player.phystr + selectedmove.damage - BattleSystem.selectedenemy.phydef)
                    BattleSystem.selectedenemy.hp = (BattleSystem.selectedenemy.hp - damage)
                    GMnarrate.write (f"You used {selectedmove.name} to inflict {damage} damage. \n")
                    BattleSystem.CheckEnemyStatus()
                elif selectedmove.effect == "Legendary":
                    if Player.hp <= ((Player.hpmax / 100) * 10):
                        damage = (Player.phystr * selectedmove.damage)
                        BattleSystem.selectedenemy.hp = (BattleSystem.selectedenemy.hp - damage)
                        GMnarrate.write (f"You used {selectedmove.name} to inflict {damage} damage. \n")
                        BattleSystem.CheckEnemyStatus()
                    else:
                        GMnarrate.write ("You can't use your Limit Break ability unless your health is below 10%!")
                        PressEnterToGoBack()
                        BattleSystem.PlayerTurn()

#check to see if enemy is dead after attacking
    def CheckEnemyStatus():
        if BattleSystem.selectedenemy.hp <= 0:
            GMnarrate.write (f"{BattleSystem.selectedenemy.name} is down!")
            BattleSystem.enemies.remove (BattleSystem.selectedenemy)
            BattleSystem.PlayerCheckVictory()

#checks to see if all enemies are down 
    def PlayerCheckVictory():
            if len(BattleSystem.enemies) == 0:
                Player.arenawins += 1
                Player.arenaroundcomplete = True
                Battles.ArenaVictory()

#runs at battle start to determine who goes first
    def FirstStrike():
        cointoss = random.randint(1,2)
        if cointoss == 1:
            Player.playerturn = True
            GMnarrate.write(f'You move fast for the first strike!   \n')
            BattleSystem.PlayerTurn()
        elif cointoss == 2:
            Player.playerturn = False
            GMnarrate.write(f'Your opponent strikes first!   \n')
            BattleSystem.EnemyTurn()

#runs the fight sequence in a loop until victory is confirmed... one way or the other... mwahahahaha lel ya might ded.
    def Fight():
        #NEED TO RESET BATTLEBEGINS AT THE END OF THE FIGHT 
        if BattleSystem.battlestart == True:
            BattleSystem.battlestart = False
            if len (BattleSystem.enemies) == 1:
                BattleSystem.selectedenemy = BattleSystem.enemies[0]
                # GMnarrate.write (f"An enemy {BattleSystem.selectedenemy.job} appeared!  \n")
                BattleSystem.FirstStrike()
            else:
                GMnarrate.write (f"Multiple Enemies!")
                BattleSystem.FirstStrike()
        if Player.playerturn == True:
            BattleSystem.PlayerTurn()
            BattleSystem.Fight()    
        elif Player.playerturn == False:
            BattleSystem.EnemyTurn()
            BattleSystem.Fight()

# BATTLES CLASS LOADS IN ENEMIES FOR DIFFERENT KINDS OF FIGHTS, ALSO FACILITATES THE ARENA ROUNDS FUNCTIONALITY ;)
class Battles:

# FOR AT THE BEGINNING AND END OF ARENA BATTLES

    def ArenaFightStart():
        if Player.arenaroundcomplete:
            GMnarrate.write ("There's nobody for you to fight right now")
            PressEnterToContinue()
            PlayerOne.currentlocation()
        else:
            if Player.arenawins == 0:
                BattleSystem.enemies = [Vagrant]
                BattleSystem.battlestart = True
                Player.arenaroundcomplete = False
                BattleSystem.Fight()

    def ArenaVictory():
        if Player.arenawins == 1:
            print ("FIRST MATCH COMPLETE")
            PressEnterToContinue()
            PlayerOne.currentlocation()

###################################
###################################
##### SECTION - WORLDBUILDING #####
###################################
###################################

# THIS SECTION EXISTS TO POPULATE ALL OF THE CREATED OBJECTS WITH THEIR OWN VALUES. IT WILL LOAD AT THE START OF RUNTIME AND CHECKED WHENEVER A LOCATION IS LOADED TO ALLOW FOR VARIANCE DURING GAMEPLAY

# WORLDBUILDING CLASS FUNCTIONS ARE FOR ORGANISATION - EACH FUNCTION POPULATES ITS OWN SET OF INFORMATION. FINAL FUNCTION IS USED TO CALL ALL PREVIOUS FUNCTIONS AT ONCE AT THE START OF RUNTIME.
class WorldBuilding:
    
    # updates location objects
    def LocationUpdate():

        # FRAMEWORK FOR FUTURE LOCATION CREATION

        # xinfo.describe1 = BoilerplateSpeech.GMLocationTest1
        # xinfo.describe2 = BoilerplateSpeech.GMLocationTest2
        # xinfo.travel1 = "-"
        # xinfo.travel2 = "-"
        # xinfo.travel3 = "-"
        # xinfo.option1 = "-"
        # xinfo.option2 = "-"
        # xinfo.option3 = "-"
        # xinfo.selecttravel1 = "-"
        # xinfo.selecttravel2 = "-"
        # xinfo.selecttravel3 = "-"
        # xinfo.selectoption1 = "-"
        # xinfo.selectoption2 = "-"
        # xinfo.selectoption3 = "-"

        #LOCATION INFORMATION LIST TO POPULATE LOCATION INFO - THIS WAY LETS US CHANGE STUFF EASILY LATER
        
        TutorialWorld.describe1 = LocationIntroduction.TutorialWorld1
        TutorialWorld.describe2 = LocationIntroduction.TutorialWorld2
        TutorialWorld.travel2 = "-"
        TutorialWorld.travel3 = "-"
        TutorialWorld.option1 = "Talk to an NPC"
        TutorialWorld.selecttravel1 = "-"
        TutorialWorld.option2 = "-"
        TutorialWorld.option3 = "-"
        TutorialWorld.selecttravel2 = "-"
        TutorialWorld.selecttravel3 = "-"
        TutorialWorld.selectoption1 = TutorialCharacter.Talk
        TutorialWorld.selectoption2 = "-"
        TutorialWorld.selectoption3 = "-"
        if PlayerOne.currentlocation == TutorialWorld.Area:
            if TutorialCharacter.firstmeet:
                TutorialWorld.describe2 = LocationIntroduction.TutorialWorld1
                TutorialWorld.travel1 = "Go to another location"
            elif not TutorialCharacter.firstmeet:
                TutorialWorld.describe2 = LocationIntroduction.TutorialWorld2
                TutorialWorld.travel1 = "Continue the story"
                TutorialWorld.selecttravel1 = StoryEvent.Introduction_AboardTheSkytrain

        Train.describe1 = LocationIntroduction.Train1
        Train.describe2 = LocationIntroduction.Train1
        Train.travel1 = "Leave the Skytrain"
        Train.travel2 = "-"
        Train.travel3 = "-"
        Train.option1 = "-"
        Train.option2 = "-"
        Train.option3 = "-"
        Train.selecttravel1 = SkytrainDock.Area
        Train.selecttravel2 = "-"
        Train.selecttravel3 = "-"
        Train.selectoption1 = "-"
        Train.selectoption2 = "-"
        Train.selectoption3 = "-"
        
        SkytrainDock.describe1 = LocationIntroduction.SkytrainDock1
        SkytrainDock.describe2 = LocationIntroduction.SkytrainDock2
        SkytrainDock.travel1 = "Board the Skytrain"
        SkytrainDock.travel2 = "-"
        SkytrainDock.travel3 = "Head to the Power Station"
        SkytrainDock.option1 = "Talk to the dock porter"
        SkytrainDock.option2 = "Approach the homeless guy"
        SkytrainDock.option3 = "-"
        SkytrainDock.selecttravel1 = Train.Area
        SkytrainDock.selecttravel2 = "-"
        SkytrainDock.selecttravel3 = PowerStationGrounds.Area
        SkytrainDock.selectoption1 = DockPorter.Talk
        SkytrainDock.selectoption2 = HomelessGuy.Talk
        SkytrainDock.selectoption3 = "-"

        PowerStationGrounds.describe1 = LocationIntroduction.PowerStationGrounds1
        PowerStationGrounds.describe2 = LocationIntroduction.PowerStationGrounds2
        PowerStationGrounds.travel1 = "Visit the Area"
        PowerStationGrounds.travel2 = "Visit the Bazaar"
        PowerStationGrounds.travel3 = "Head to the Skytrain Dock"
        PowerStationGrounds.option1 = "Talk to the Station Boss"
        PowerStationGrounds.option2 = "-"
        PowerStationGrounds.option3 = "-"
        PowerStationGrounds.selecttravel1 = PowerStationMedicArea.Area
        PowerStationGrounds.selecttravel2 = PowerStationBazaar.Area
        PowerStationGrounds.selecttravel3 = SkytrainDock.Area
        PowerStationGrounds.selectoption1 = PowerStationBoss.Talk
        PowerStationGrounds.selectoption2 = "-"
        PowerStationGrounds.selectoption3 = "-"

        
        PowerStationMedicArea.describe1 = LocationIntroduction.PowerStationMedicArea1
        PowerStationMedicArea.describe2 = LocationIntroduction.PowerStationMedicArea2
        PowerStationMedicArea.travel1 = "-"
        PowerStationMedicArea.travel2 = "-"
        PowerStationMedicArea.travel3 = "-"
        PowerStationMedicArea.option1 = "Talk to the Medic"
        PowerStationMedicArea.option2 = "Approach the Field Droid"
        PowerStationMedicArea.option3 = "-"
        PowerStationMedicArea.selecttravel1 = "-"
        PowerStationMedicArea.selecttravel2 = "-"
        PowerStationMedicArea.selecttravel3 = "-"
        PowerStationMedicArea.selectoption1 = "-"
        PowerStationMedicArea.selectoption2 = "-"
        PowerStationMedicArea.selectoption3 = "-"

        PowerStationBazaar.describe1 = LocationIntroduction.PowerStationBazaar1
        PowerStationBazaar.describe2 = LocationIntroduction.PowerStationBazaar2
        PowerStationBazaar.travel1 = "-"
        PowerStationBazaar.travel2 = "-"
        PowerStationBazaar.travel3 = "-"
        PowerStationBazaar.option1 = "-"
        PowerStationBazaar.option2 = "-"
        PowerStationBazaar.option3 = "-"
        PowerStationBazaar.selecttravel1 = "-"
        PowerStationBazaar.selecttravel2 = "-"
        PowerStationBazaar.selecttravel3 = "-"
        PowerStationBazaar.selectoption1 = "-"
        PowerStationBazaar.selectoption2 = "-"
        PowerStationBazaar.selectoption3 = "-"
        
        PowerStationArena.describe1 = LocationIntroduction.PowerStationArena1
        PowerStationArena.describe2 = LocationIntroduction.PowerStationArena2
        PowerStationArena.travel1 = "Head back to the Power Station entrance"
        PowerStationArena.travel2 = "-"
        PowerStationArena.travel3 = "-"
        PowerStationArena.option1 = "Approach the Arena Cage"
        PowerStationArena.option2 = "-"
        PowerStationArena.option3 = "-"
        PowerStationArena.selecttravel1 = PowerStationGrounds.Area
        PowerStationArena.selecttravel2 = "-"
        PowerStationArena.selecttravel3 = "-"
        PowerStationArena.selectoption1 = Battles.ArenaFightStart
        PowerStationArena.selectoption2 = "-"
        PowerStationArena.selectoption3 = "-"

    def NPCUpdate():

        # FRAMEWORK FOR FUTURE NPC INFO ADDITION AT RUNTIME 
        # xinfo.gmintro1 = ""
        # xinfo.gmintro2 = ""
        # xinfo.talkoption1 = ""
        # xinfo.talkoption2 = ""
        # xinfo.talkoption3 = ""
        # xinfo.talkselect1 = ""
        # xinfo.talkselect2 = ""
        # xinfo.talkselect3 = ""

        TutorialCharacter.gmintro1 = Interactions.TutorialCharacterGreet1
        TutorialCharacter.gmintro2 = Interactions.TutorialCharacterGreet2
        TutorialCharacter.talkoption1 = "Yeah that's great - what do I do now?"
        TutorialCharacter.talkoption2 = ""
        TutorialCharacter.talkoption3 = ""
        TutorialCharacter.talkselect1 = Interactions.TutorialCharacter_WhatNext
        TutorialCharacter.talkselect2 = ""
        TutorialCharacter.talkselect3 = ""

        DockPorter.gmintro1 = Interactions.DockPorter1
        DockPorter.gmintro2 = Interactions.DockPorter2
        DockPorter.talkoption1 = ""
        DockPorter.talkoption2 = ""
        DockPorter.talkoption3 = ""
        DockPorter.talkselect1 = ""
        DockPorter.talkselect2 = ""
        DockPorter.talkselect3 = ""

        HomelessGuy.gmintro1 = Interactions.HomelessGuy1
        HomelessGuy.gmintro2 = Interactions.HomelessGuy2
        HomelessGuy.talkoption1 = ""
        HomelessGuy.talkoption2 = ""
        HomelessGuy.talkoption3 = ""
        HomelessGuy.talkselect1 = ""
        HomelessGuy.talkselect2 = ""
        HomelessGuy.talkselect3 = ""

        PowerStationBoss.gmintro1 = Interactions.PowerStationBoss1
        PowerStationBoss.gmintro2 = Interactions.PowerStationBoss2
        PowerStationBoss.talkoption1 = "I need to get into the fights"
        PowerStationBoss.talkoption2 = ""
        PowerStationBoss.talkoption3 = ""
        PowerStationBoss.talkselect1 = Interactions.PowerStationBossConfirmArena
        PowerStationBoss.talkselect2 = ""
        PowerStationBoss.talkselect3 = ""

    def VendorUpdate():
        VendorItem.items = [Potion, HiPotion]
    
    def ThisFunctionTookGodSixWholeDays():
        WorldBuilding.LocationUpdate()
        WorldBuilding.NPCUpdate()
        WorldBuilding.VendorUpdate()

############################
############################
##### SECTION - EVENTS #####
############################
############################

# GM_NARRATE CLASSES ARE FOR ORGANISATION OF GAME MASTER NARRATION FOR DIFFERENT OBJECTS - STORY, LOCATIONS, CHARACTER INTRODUCTIONS, ETC
class LocationIntroduction:
    
    # def xxxxx 1():
    #     GMnarrate.write ("xxxxx PLACEHOLDER DESCRIPTION 1")
    # def xxxxx 2():
    #     GMnarrate.write ("xxxxx PLACEHOLDER DESCRIPTION 2")

    def TutorialWorld1():
        GMtalk.write("In order to select something, just type in the number of the list item and hit enter. It's that easy! If a listed item shows a '-' symbol, there's nothing to select there.")
        GMtalk.write("First, let's try talking to an NPC. Try selecting the option for 'Talk to an NPC' from the menu.\n")
        GMnarrate.write("This is how I will narrate the scene to you, with my words appearing like this.")
    def TutorialWorld2():
        GMtalk.write("Sometimes, the options available to you will change. See below? That first option will now allow you to continue the story.  \nAlso, you can check your current inventory, equipped items and current stats anytime you're travelling around the world. You can try that now, or continue forward with the story\n")
        GMnarrate.write("Welcome Back to the tutorial area.")

    def Train1():
        GMnarrate.write ("SKYTRAIN PLACEHOLDER DESCRIPTION 1")
    def Train2():
        GMnarrate.write ("SKYTRAIN PLACEHOLDER DESCRIPTION 2")

    def SkytrainDock1():
        GMnarrate.write("SKYTRAIN DOCK PLACEHOLDER DESCRIPTION 1")
    def SkytrainDock2():
        GMnarrate.write("SKYTRAIN DOCK PLACEHOLDER DESCRIPTION 2")

    def PowerStationGrounds1():
        GMnarrate.write ("POWER STATION GROUNDS PLACEHOLDER DESCRIPTION 1")
    def PowerStationGrounds2():
        GMnarrate.write ("POWER STATION GROUNDS PLACEHOLDER DESCRIPTION 2")

    def PowerStationMedicArea1():
        GMnarrate.write ("POWER STATION MEDIC AREA PLACEHOLDER DESCRIPTION 1")
    def PowerStationMedicArea2():
        GMnarrate.write ("POWER STATION MEDIC AREA PLACEHOLDER DESCRIPTION 2")

    def PowerStationBazaar1():
        GMnarrate.write ("POWER STATION BAZAAR PLACEHOLDER DESCRIPTION 1")
    def PowerStationBazaar2():
        GMnarrate.write ("POWER STATION BAZAAR PLACEHOLDER DESCRIPTION 2")

    def PowerStationArena1():
        GMnarrate.write ("POWER STATION ARENA PLACEHOLDER DESCRIPTION 1")
    def PowerStationArena2():
        GMnarrate.write ("POWER STATION ARENA PLACEHOLDER DESCRIPTION 2")


class StoryEvent:
    
    #runs at the start of the game to kick everything off
    def StartTheGame():
        MenuTitle.write("Project RPG        \n")
        GMtalk.write(f"Welcome, {PlayerOne.name} - to Project RPG   \nI am the Game Master of this world and will be your guide on your adventure.  \n")
        GMtalk.write("If you have never played the game before, I can show you tutorial segments throughout the game to assist you. \nOr, if you'd prefer, I can disable the tutorial elements for you. \n")
        PlayerInput.write ("Please select your preference:  \n1: Tutorials on  \n2: Tutorials off   \n")
        answer = input ()
        print()
        if answer == "1":
            Player.handholding = True
            GMtalk.write (f"No worries - We'll start with a quick overview.  \nFrom time to time I'll appear whenever new information about how the game becomes needed.\nOkay {PlayerOne.name} - Let's start with the basics.   \n\n")
            PressEnterToContinue()
            StoryEvent.IntroductionTutorial()
        elif answer == "2":
            Player.handholding = False
            GMtalk.write ("Alright, let's jump right into the story. Starting in")
            CountDown()
            StoryEvent.Introduction_AboardTheSkytrain()
        else:
            InvalidChoice()
            StoryEvent.StartTheGame()
    
    # runs when the player dies to end the game. 
    def EndTheGame():
        GMnarrate.write("With a final blow, your enemy dispatches your soul to the next life.   \n\n")
        GMtalk.write("Would you like to start again?")
        PlayerInput.write("1: Yes   \n2: No \n")
        selection = input("")
        print()
        if selection == "1":
            GMtalk.write ("Okay, the game will start again in   \n")
            CountDown()
            StoryEvent.StartTheGame()
        elif selection == "2":
            GMtalk.write ("Thank you for playing. The game will close itself in \n")
            CountDown()
            quit()
        else:
            InvalidChoice()
            StoryEvent.EndTheGame()

    def IntroductionTutorial():
        if Player.handholding:
            GMtalk.write(f"When I'm talking to you directly, my words will appear like this. When you visit somewhere, you'll see a screen like the one about to appear below.")
        TutorialWorld.Area()

    def Introduction_AboardTheSkytrain():
        GMnarrate.write("Story beat goes here. This is where our player character meets a stranger who gifts them a healing salve and a power glove armatek weapon")
        PlayerOne.armweapons.append (PowerFist)
        print (PlayerOne.armweapons)
        PressEnterToContinue()
        Train.Area()


class BoilerplateSpeech:
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



# NPC INTERACTIONS ARE FOR WHEN YOU'RE HAVING A CHAT.
class Interactions:



    def TutorialCharacterGreet1():
        GMtalk.write("When talking to NPCs, You'll see an introduction by me and a greeting from the NPC. Selecting conversation options is the same as before.\n")
        GMnarrate.write ("The NPC greets you:")
        NPCtalk.write("Hey, when NPCs are talking to you - our speech will appear like this!")
    def TutorialCharacterGreet2():
        NPCtalk.write ("What're you doing back here? I told you already, bloke calling himself Game Master will take you from the here.")
        PressEnterToContinue()
        TutorialWorld.Area()

    def TutorialCharacter_WhatNext():
        GMnarrate.write("The NPC chuckles at your brusque response")
        NPCtalk.write("What you do now mate, is get on with the story! Bloke calling himself Game Master will take care of you from here.")
        PressEnterToContinue()
        TutorialWorld.Area()
    
    def DockPorter1():
        GMnarrate.write ("DOCK PORTER PLACEHOLDER DESCRIPTION 1")
    def DockPorter2():
        GMnarrate.write ("DOCK PORTER PLACEHOLDER DESCRIPTION 2")

    def HomelessGuy1():
        GMnarrate.write ("HOMELESS GUY PLACEHOLDER DESCRIPTION 1")
    def HomelessGuy2():
        GMnarrate.write ("HOMELESS GUY PLACEHOLDER DESCRIPTION 2")
    
    def PowerStationBoss1():
        GMnarrate.write ("POWER STATION BOSS PLACEHOLDER DESCRIPTION 1")
    def PowerStationBoss2():
        GMnarrate.write ("POWER STATION BOSS PLACEHOLDER DESCRIPTION 2")
    
    def PowerStationBossConfirmArena():
        GMnarrate.write("The Boss Man asks")
        NPCtalk.write("You sure you wanna go in?")
        PowerStationBoss.talkoption1 = "Yes"
        PowerStationBoss.talkoption2 = "No, I'll come back later."
        PowerStationBoss.talkselect1 = Interactions.PowerStationBossArenaConfirmed
        PowerStationBoss.talkselect2 = PlayerOne.currentlocation
        PowerStationBoss.Talk()
    
    def PowerStationBossArenaConfirmed():
        PlayerOne.holdlocation = PlayerOne.currentlocation
        PowerStationArena.Area()

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

    def VendorPresentItems():
        option = random.randint(1,4)
        if option == 1:
            NPCtalk.write ("So what'll it be?  \n")
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
