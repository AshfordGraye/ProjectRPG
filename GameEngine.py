import collections
import random
from os import system, name
from time import sleep
from x_Typewriter_Text import *
from x_Items_And_Weapons import *

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
    GMtalk.write ("\nPress Enter to continue")
    input()
    ClearScreen()

def PressEnterToGoBack():
    GMtalk.write ("\nPress Enter to go back")
    input()
    ClearScreen()

def InvalidChoice():
    GMtalk.write ("That won't work here... you'll have to try something else.")
    PressEnterToGoBack()

def CountDown():
    timer = 5
    while timer >= 5:
        GMtalk.write(f"{timer}...")
        timer -= 1
        sleep(1)
    ClearScreen()

#############################################
##### SECTION - OBJECT CLASS CREATION #####
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
        MainCharacter.currentlocation = self.Area
        MainCharacter.lastlocation = MainCharacter.holdlocation
        WorldBuilding.LocationUpdate()
        if self.firstvisit:
            self.describe1()
            print()
        else:
            self.describe2()
            print()
        ScreenTitle.write (f"{self.name}\n")
        MenuTitle.write ("Travel Menu")
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
        elif selection == "1":
            if self.selecttravel1 == "-":
                self.InvalidChoice()
            else:
                ClearScreen()
                self.firstvisit = False
                MainCharacter.holdlocation = MainCharacter.currentlocation
                self.selecttravel1()
        elif selection == "2":
            if self.selecttravel2 == "-":
                self.InvalidChoice()
            else:
                ClearScreen()
                self.firstvisit = False
                MainCharacter.holdlocation = MainCharacter.currentlocation
                self.selecttravel2()
        elif selection == "3":
            if self.selecttravel3 == "-":
                self.InvalidChoice()
            else:
                ClearScreen()
                self.firstvisit = False
                MainCharacter.holdlocation = MainCharacter.currentlocation
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
            MainCharacter.PlayerSelectItems()
            PressEnterToGoBack()
            self.Area()
        elif selection == "8":
            MainCharacter.ShowWeapons()
            PressEnterToGoBack()
            self.Area()
        elif selection == "9":
            MainCharacter.ShowStats()
            PressEnterToGoBack()
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
        if self.name != "":
            self.items = collections.Counter()

    job = ""

    credits = ""

    hpmax = ""
    hp = ""
    apmax = ""
    mp = apmax

    phystr = ""
    phydef = ""
    armstr = ""
    armdef = ""

    phyweapons = []
    physequip = []
    armweapons = []
    armequip = []

    moveset = []
    menuselect = ""
    movechoice = ""

    selectedtarget = ""

    def MenuSelection(self):
        print()
        self.menuselect = (input())
        try:
            self.menuselectint = int(self.menuselect)
        except ValueError:
            self.menuselectint = 0
        print()

# PLAYER CHARACTER SUBCLASS IS CONTROLLABLE BY THE PLAYER
class Player(Character):

    def __init__(self, name):
        self.name = name
        if self.name == "Player":
            self.currentlocation = ""
            self.holdlocation = ""
            self.lastlocation = ""
            self.combatlocation = False

            self.credits = 200
            
            self.job = ""

            self.hpmax = 1000
            self.hp = 1000
            self.apmax = 100
            self.ap = 100

            self.phystr = 10
            self.phydef = 10
            self.armstr = 10
            self.armdef = 10

            self.phyweapons = []
            self.physequip = [BareKnuckles]
            self.armweapons = []
            self.armequip = []

            self.items = collections.Counter()
            
            self.items[Potion] += 2
            self.items[HiPotion] += 2
            self.items[Grenade] += 2
            

            self.moveset = [Attack, Punches, "-", ListItems]
            self.arenawins = 0
            self.arenaroundcomplete = False

            self.handholding = ""


    def Naming(self):
        PlayerInput.write("Enter your name:")
        self.name = "Player"
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

    # NON COMBAT EQUIPMENT FUNCTIONS

    def ShowStats(self):
        ClearScreen()
        MenuTitle.write("Credits:")
        GMtalk.write(f"{MainCharacter.credits}  \n")
        for elem in BattleSystem.party:
            MenuTitle.write(f"{elem.name} Vitals:")
            #for health
            if elem.hp > (elem.hpmax /100 * 25):
                print (f' {type.fg_silver}HP:{type.reset}   {type.fg_green}{elem.hp}/{elem.hpmax}{type.reset}')
            elif elem.hp <= (elem.hpmax /100 * 25):
                print (f' {type.fg_silver}HP:{type.reset}   {type.fg_red}{elem.hp}{type.reset}/{type.fg_green}{elem.hpmax}{type.reset}')
            #for ap
            if elem.ap > (elem.apmax /100 * 25):
                print (f' {type.fg_silver}MP:{type.reset}   {type.fg_green}{elem.ap}/{elem.apmax}{type.reset}')
            elif elem.ap <= (elem.apmax /100 *25):
                print (f' {type.fg_silver}MP:{type.reset}   {type.fg_red}{elem.ap}{type.reset}/{type.fg_green}{elem.apmax}{type.reset}\n')
            print()
            MenuTitle.write(f"{elem.name} Stats:")
            GMtalk.write(f" Physical Strength:   {elem.phystr}")
            GMtalk.write(f" Physical Defense:    {elem.phydef}")
            GMtalk.write(f" Armatek Strength:    {elem.armstr}")
            GMtalk.write(f" Armatek Defense:     {elem.armdef}")
        
    def ShowWeapons(self):
        ClearScreen()
        MenuTitle.write ("Equipment Menu:   \n")
        MenuTitle.write("Physical Weapon:")
        if len(self.physequip) == 0:
            GMtalk.write("You do not have a weapon equipped.    \n")
        else:
            GMtalk.write(f"{self.physequip[0]}  \n")
        MenuTitle.write("Armatek Gear")
        if len(self.armequip) == 0:
            GMtalk.write("You do not have any gear equipped.    \n")
        else:
            GMtalk.write(f"{self.armequip[0]}   \n") 
        self.ChangeEquipment()

    def ChangeEquipment(self):
        GMtalk.write("Would you like to change any of your current equipment?")
        PlayerInput.write ("1: Yes \n2: No")
        self.MenuSelection()
        if self.menuselect == "1":
            self.SelectEquipment()
        elif self.menuselect == "2":
            pass
        else:
            InvalidChoice()
            self.ShowWeapons()

    def SelectEquipment(self):
        listorder = 0
        GMtalk.write ("Select an equipment type to change")
        PlayerInput.write("0: Cancel    \n1: Physical Equipment \n2: Armatek")
        self.MenuSelection()
        if self.menuselect =="0":
            pass
        #if player selected physical weapons
        elif self.menuselect == "1":
            if len (self.phyweapons) == 0:
                GMtalk.write( "You do not have another weapon to equip. \n")
                PressEnterToGoBack()
                self.ShowWeapons()
            else:
                GMtalk.write("Select a weapon to equip.")
                for elem in self.phyweapons:
                    listorder += 1
                    PlayerInput.write(f"{listorder}: {elem}")
                self.MenuSelection()
                if self.menuselectint in range (1, listorder+1):
                    removeditem = self.physequip.pop (0)
                    # self.menuselect = int(self.menuselect)
                    selecteditem = self.phyweapons.pop (self.menuselectint-1)
                    self.phyweapons.append (removeditem)
                    self.physequip.append (selecteditem)
                    self.moveset[1] = self.physequip[0].special
                    GMtalk.write (f"You now have the {self.physequip[0].name} equipped. \nYou can now use the {self.moveset[1].name} ability!")
                else:
                    InvalidChoice()
                    self.ShowWeapons()
        #if player selected armatek
        elif self.menuselect == "2":
            if len (self.armweapons) == 0:
                GMtalk.write("You do not have any Armatek Gear to equip")
                PressEnterToGoBack()
                self.ShowWeapons()
            else:
                GMtalk.write("Select gear to equip.")
                for elem in self.armweapons:
                    listorder += 1
                    PlayerInput.write(f"{listorder}: {elem}")
                self.MenuSelection()
                if self.menuselectint in range (1,listorder+1):
                    if len (self.armequip) == 0:
                        # self.menuselect = int(self.menuselect)
                        selecteditem = self.armweapons.pop (self.menuselectint-1)
                        print (selecteditem.name)
                        self.armequip.append (selecteditem)
                        self.moveset[2] = self.armequip[0].special
                        GMtalk.write (f"You now have the {self.armequip[0].name} equipped. \nYou can now use the {self.moveset[2].name} ability!")
                    else:
                        removeditem = self.armequip.pop (0)
                        selecteditem = self.armweapons.pop (self.menuselectint-1)
                        self.armweapons.append (removeditem)
                        self.armequip.append (selecteditem)
                        self.moveset[1] = self.physequip[0].special
                        GMtalk.write (f"You now have the {self.physequip[0].name} equipped. \nYou can now use the {self.moveset[1].name} ability!")
                else:
                    InvalidChoice()
                    self.ShowWeapons()
        else:
            InvalidChoice()
            self.ShowWeapons()

    # COMBAT ABILITY AND ITEM FUNCTIONS - ITEM FUNCTIONS ARE DESIGNED TO WORK INSIDE AND OUTSIDE OF COMBAT
    def PlayerTurnDisplay(self):
        MenuTitle.write("Your Turn: \n")
        for elem in BattleSystem.enemies:
            if elem.hp > (elem.hpmax /100 *70):
                GMnarrate.write("The foe stands strong! Don't give up!   \n")
            elif elem.hp > (elem.hpmax /100 *30):
                GMnarrate.write("Your foe grows weaker! Keep it up!  \n")
            elif elem.hp <= (elem.hpmax /100 *30):
                GMnarrate.write("Your enemy grows weak! Almost there!    \n")

        MenuTitle.write (f"{self.name}:")
        if self.hp > (self.hpmax /100 * 25):
            print (f' {type.fg_orange}HP:{type.reset}   {type.fg_green}{self.hp}/{self.hpmax}{type.reset}')
        elif self.hp <= (self.hpmax /100 * 25):
            print (f' {type.fg_orange}HP:{type.reset}   {type.fg_red}{self.hp}{type.reset}/{type.fg_green}{self.hpmax}{type.reset}')
        
        if self.ap > (self.apmax /100 * 25):
            print (f' {type.fg_orange}MP:{type.reset}   {type.fg_green}{self.ap}/{self.apmax}{type.reset}')
        elif self.ap <= (self.apmax /100 *25):
            print (f' {type.fg_orange}MP:{type.reset}   {type.fg_red}{self.ap}{type.reset}/{type.fg_green}{self.apmax}{type.reset}\n')
        print()

    def PlayerSelectAbility(self):
        listmoves = 0 #to number the ability list dynamically 
        MenuTitle.write ("Select an option:")
        
        #this bit swaps out the standard attack move in move slot 0 with LimtBreak when health is below 10%
        if self.hp <= (self.hpmax/100*10):
            self.moveset [0] = LimitBreak
        else:
            self.moveset [0] = Attack
        
        # list the choices
        for elem in self.moveset:
            listmoves += 1
            PlayerInput.write (f" {listmoves}: {elem} \n")
        #get player selection
        self.MenuSelection()

        #check to see if selection is valid, then move to select the enemy 
        if self.menuselect in (str(i) for i in range(1, listmoves+1)):
            self.PlayerSelectAbilityTarget()
        else:
            InvalidChoice()
            BattleSystem.PlayerTurn()

    def PlayerSelectAbilityTarget(self):
        listofenemies = 0
        #autoselect if there's only one enemy cos duh...
        if len (BattleSystem.enemies) == 1:
            self.selectedtarget = BattleSystem.enemies[0]
            self.PlayerSelectAbilityTargetConfirmed()
        #if more than one, list and select in the same way as selecting an ability. Neat!
        else:
            GMtalk.write(f"Select an enemy to attack    \n")
            for elem in BattleSystem.enemies:
                listofenemies += 1
                PlayerInput.write (f" {listofenemies}: {elem.name}")
            self.playerenemychoice = int(input())
            if self.playerenemychoice in range (1, listofenemies+1):
                self.selectedtarget = BattleSystem.enemies[self.playerenemychoice-1]
                self.PlayerSelectAbilityTargetConfirmed()
            else:
                GMtalk.write ("Invalid Input")
                self.PlayerSelectAbilityTarget()

    def PlayerSelectAbilityTargetConfirmed(self):
            self.menuselect = int(self.menuselect)
            selectedmove = self.moveset[self.menuselect-1]
            #accuracycheck checks against the misschance of the selected move.
            if selectedmove == "-":
                InvalidChoice()
                BattleSystem.PlayerTurn()
            else:
                if selectedmove.apcost > self.ap:
                    GMtalk.write("You don't have enough AP for that right now!")
                    self.PlayerTurnDisplay()
                else:
                    self.ap -= selectedmove.apcost
                    for i in range (1,selectedmove.rounds+1):
                        accuracycheck = random.randint (1,100)
                        if accuracycheck in range (selectedmove.chancetomiss): # so if the accuracycheck falls within the misschance of the selected move, it misses.
                            GMnarrate.write  (f"You tried to use {selectedmove.name}, but missed!  \n")
                        else: #otherwise, it hits and so determines how damage or buffs work here base on the selected move effect value
                            if selectedmove.effect == "Physical":
                                damage = (self.phystr + selectedmove.damage + self.physequip[0].damage - self.selectedtarget.phydef)
                                self.selectedtarget.hp = (BattleSystem.selectedtarget.hp - damage)
                                GMnarrate.write (f"You used {selectedmove.name} to inflict {damage} damage. \n")
                                BattleSystem.CheckEnemyStatus()
                            
                            elif selectedmove.effect == "Scan":
                                self.selectedtarget.ShowCurrentStats()
                            
                            elif selectedmove.effect == "Items":
                                self.PlayerSelectItems()

                            elif selectedmove.effect == "Legendary":
                                if self.hp <= ((self.hpmax / 100) * 10):
                                    damage = (self.phystr * selectedmove.damage)
                                    self.selectedtarget.hp = (self.selectedtarget.hp - damage)
                                    GMnarrate.write (f"You used {selectedmove.name} to inflict {damage} damage. \n")
                                    BattleSystem.CheckEnemyStatus()
                                else:
                                    GMnarrate.write ("You can't use your Limit Break ability unless your health is below 10%!")
                                    PressEnterToGoBack()
                                    BattleSystem.PlayerTurn()
                            else:
                                pass

    def PlayerSelectItems(self):
        listitems = 0
        MenuTitle.write("Items:")
        PlayerInput.write ("\n0: Cancel   \n") 
        for count in self.items:
            listitems += 1
            PlayerInput.write(f"{listitems}: {self.items[count]} x {count}  \n")
        GMtalk.write ("Select an item to use:")
        self.MenuSelection()
        if self.menuselect == "0":
            if self.combatlocation == False:
                PressEnterToGoBack()
                self.currentlocation()
            PressEnterToGoBack()
            BattleSystem.PlayerTurn()
        elif self.menuselect in (str(n) for n in range(1,len(self.items)+1)):
            self.listofitems = list(self.items)
            self.listselection = int(self.menuselect)
            if self.listselection not in range (len(self.items)+1):
                InvalidChoice()
                self.PlayerSelectItems()
            self.itemselected = self.listofitems[self.listselection-1]
            if not self.combatlocation and self.itemselected.effect == "Physical":
                GMtalk.write ("You can't use that here!")
            else:
                self.PlayerSelectItemsTarget()
        else:
            InvalidChoice()
            self.PlayerSelectItems()

    def PlayerSelectItemsTarget(self):
        listoftargets = 0

        if self.itemselected.effect == "Healing":
            if len(BattleSystem.party) == 1:
                self.selectedtarget == BattleSystem.party[0]
                self.PlayerSelectItemsTargetConfirmed()
            else:
                MenuTitle.write("Targets:")
                for elem in BattleSystem.party:
                    listoftargets += 1
                    PlayerInput.write (f"{listoftargets}: {elem.name}")
                    self.MenuSelection()
                    self.selectedtarget = BattleSystem.enemies[self.menuselect-1]
                    self.PlayerSelectItemsTargetConfirmed()
        elif self.itemselected.effect in ("Physical" , "Armatek"):
            if len(BattleSystem.enemies) == 1:
                self.selectedtarget == BattleSystem.enemies[0]
                print("Target Selected")
                PressEnterToContinue()
                self.PlayerSelectItemsTargetConfirmed()
            else:
                MenuTitle.write("Targets:")
                for elem in BattleSystem.enemies:
                    listoftargets += 1
                    PlayerInput.write (f"{listoftargets}: {elem.name}")
                self.MenuSelection()
                self.selectedtarget = BattleSystem.enemies[self.menuselect-1]
                if self.selectedtarget in range (1,listoftargets+1):

                    self.PlayerSelectItemsTargetConfirmed()
                else:
                    InvalidChoice()
                    self.PlayerSelectItemsTarget()
                    
    def PlayerSelectItemsTargetConfirmed(self):

        if self.itemselected.effect == "Healing":
            self.hp += self.itemselected.damage
            GMtalk.write (f"{self.itemselected.name} used, {self.name} HP raised to {self.hp}!")
            if not self.combatlocation:
                self.items[self.itemselected] -= 1
                if self.items[self.itemselected] == 0:
                    del self.items[self.itemselected]
                PressEnterToGoBack()
                self.currentlocation()

        elif self.itemselected.effect == "Physical":
            damage = (self.itemselected.damage + self.selectedtarget.phydef)
            print (self.itemselected)
            self.selectedtarget.hp = (BattleSystem.selectedtarget.hp - damage)
            GMnarrate.write (f"You used {self.itemselected.name} to inflict {damage} damage. \n")
        else:
            PressEnterToGoBack()
            BattleSystem.PlayerTurn()

        self.items[self.itemselected] -= 1
        if self.items[self.itemselected] == 0:
            del self.items[self.itemselected]
        if MainCharacter.combatlocation:
            BattleSystem.CheckEnemyStatus()

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
        WorldBuilding.LocationUpdate()
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
        self.MenuSelection()
        if self.menuselect in [str(n) for n in range (1,4)]:
            self.firstmeet = False
        if self.menuselect == "0":
            ClearScreen()
            MainCharacter.currentlocation()
        elif self.menuselect == "1":
            if self.talkselect1 == "":
                self.InvalidChoice()
            else:
                ClearScreen()
                self.talkselect1()
        elif self.menuselect == "2":
            if self.talkselect2 == "":
                self.InvalidChoice()
            else:
                ClearScreen()
                self.talkselect2()
        elif self.menuselect == "3":
            if self.talkselect3 == "":
                InvalidChoice()
            else:
                ClearScreen()
                self.talkselect3()
        else:
            self.InvalidChoice()

    def InvalidChoice(self):
        InvalidChoice()
        self.Talk()

# VENDORS ARE AN NPC SUBCLASS TO DIFFERENTIATE BETWEEN CONVERSATIONS AND COMMERCE
class Vendor (NPC): 
    
    def SaleDisplay(self):
        ScreenTitle.write (f"{self.name}    \n")
        if len (self.items) == 0:
            GMnarrate.write ("The Vendor shakes hs head...  \n")
            NPCtalk.write ("I'm afraid I've got nothing else in stock. Be sure to coe back and try again later.")
            PressEnterToGoBack()
            self.Talk()
        else:
            Interactions.VendorPresentItems()
            listitem = 0
            PlayerInput.write ("0: Cancel   \n")
            for count in self.items:
                listitem += 1
                PlayerInput.write (f"{listitem}: {self.items[count]} x {count}  \n : {count.value} credits  \n")
        GMtalk.write (f"You currently have {MainCharacter.credits} credits.")
        self.MenuSelection()
        if self.menuselect == "0":
            NPCtalk.write ("No worries - later now.")
            PressEnterToGoBack()
            self.Talk()
        else:
            pass
        
        if self.menuselectint in range (1,listitem+1):
            itemsforsale = list(self.items)
            selecteditem = itemsforsale[self.menuselectint-1]
            NPCtalk.write (f"You sure about that {selecteditem.name}?. The developer hasn't programmed me to buy it back!   \n")
            PlayerInput.write ("1: I'm sure")
            PlayerInput.write ("2: Let me look again")
            self.MenuSelection()
            if self.menuselect == "1":
                if MainCharacter.credits >= selecteditem.value:
                        boughtitem = selecteditem
                        MainCharacter.credits -= boughtitem.value
                        GMnarrate.write (f"You acquired a {boughtitem.name}! You now have {MainCharacter.credits} credits left.")

                        x = isinstance (selecteditem, Item)
                        y = isinstance (selecteditem, Weapon)
                        z = isinstance (selecteditem, Armatek)

                        if x:
                            MainCharacter.items[boughtitem] += 1
                        elif y:
                            MainCharacter.phyweapons.append(boughtitem)
                        elif z:
                            MainCharacter.armweapons.append(boughtitem)

                        self.items[boughtitem] -= 1
                        if self.items[boughtitem] == 0:
                            del self.items[boughtitem]
                        PressEnterToGoBack()
                        ClearScreen()
                        self.SaleDisplay()
                else:
                    Interactions.VendorNoMoney()
                    self.SaleDisplay()
            elif self.menuselect == "2":
                NPCtalk.write ("No worries - have a look at what I have.")
                PressEnterToGoBack()
                self.SaleDisplay()
            else:
                NPCtalk.write ("What? I didn't quite catch that. Have another look and let me know if you need anything.    \n")
                InvalidChoice()
                self.SaleDisplay()
        else:
            NPCtalk.write ("What? I didn't quite catch that.    \n")
            InvalidChoice()
            self.SaleDisplay()

# MEDICS ARE AN NPC SUBCLASS TO KEEP HEALING OPTIONS SEPERATE, JUST FOR ORGANISATION REALLY.
class Medic (NPC):
    def Healing(self):
        if self.name == "Medic":
            Interactions.MedicHealing()
        elif self.name == "Field Droid":
            Interactions.FieldDroidHealing()

# ENEMY CHARACTERS ARE USED IN COMBAT
class Enemy(Character):

    def __init__(self, name):
        
        self.name = name

        if self.name == "Vagrant":
            self.job = "Vagrant"
            self.hpmax = 250
            self.hp = 250
            self.phystr = 5
            self.phydef = 5
            self.armstr = 5
            self.armdef = 5
            self.moveset = [Lunge, KnifeCuts]
        elif self.name == "Bouncer":
            self.job = "Bouncer"
            self.hpmax = 350
            self.hp = 350
            self.phystr = 12
            self.phydef = 10
            self.armstr = 10
            self.armdef = 8
            self.moveset = [Punches, StrongFist]
        elif self.name == "Docker":
            self.job = "Docker"
            self.hpmax = 250
            self.hp = 250
            self.phystr = 10
            self.phydef = 10
            self.armstr = 12
            self.armdef = 8
            self.moveset = [AnchorStrike, LoaderFist]
        elif self.name == "Officer":
            self.job = "Officer"
            self.hpmax = 450
            self.hp = 450
            self.phystr = 10
            self.phydef = 10
            self.armstr = 8
            self.armdef = 14
            self.moveset = [PistolShot, ArmaScopeShot]
        elif self.name == "Assassin":
            self.job = "Assassin"
            self.hpmax = 450
            self.hp = 450
            self.phystr = 14
            self.phydef = 8
            self.armstr = 10
            self.armdef = 10
            self.moveset = [VibraSwordSlice, VibraSwordSlashes]


    def MoveSelect(self):
        misschance = random.randint (1,100)
        self.movechoice = self.moveset [(random.randint (1,len(self.moveset)))-1]
        if misschance in range (1,self.movechoice.chancetomiss+1):
            GMnarrate.write (f"The {self.name} tried to attack, but missed!  \n")
        else:
            Enemy.DamageCalculation(self)

    def DamageCalculation(self):
        target = BattleSystem.party[random.randint(1,len(BattleSystem.party))-1]
        if self.movechoice.effect == "Physical":
            totaldamage = (self.movechoice.damage + self.phystr - target.phydef)
            target.hp -= totaldamage
        elif self.movechoice.effect == "Armatek":
            totaldamage = (self.movechoice.damage + self.armstr - target.armdef)
            target.hp -= totaldamage
        GMnarrate.write (f"{self.name} used {self.movechoice.name} for {totaldamage} damage \n")

    def ShowCurrentStats(self):
        MenuTitle.write (f"{self.name}  \n")
        MenuTitle.write ("HP:"); GMtalk.write(f"{self.hp}/{self.hpmax}  \n")

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
MainCharacter = Player ("Player")

# NPC CHARACTERS
TutorialCharacter = NPC("Tutorial NPC")
DockPorter = NPC ("Skytrain Dock Porter")
HomelessGuy = NPC ("Homeless Guy")
PowerStationBoss = NPC ("Power Station Boss")

# STORE VENDORS 
VendorItem = Vendor("Item Vendor")
VendorPhysical = Vendor ("Physical Equipment Vendor")
VendorArmatek = Vendor ("Armatek Equipment Vendor")

# MEDIIIIIIIC!!!!!
MedicFella = Medic ("Medic")
FieldDroid = Medic ("Field Droid")

# ENEMY CHARACTERS
Vagrant = Enemy ("Vagrant")
Bouncer = Enemy ("Bouncer")
Docker = Enemy ("Docker")
Officer = Enemy ("Officer")
Assassin = Enemy ("Assassin")

############################
############################
##### SECTION - COMBAT #####
############################
############################

# BATTLE SYSTEM INITIATES TURN BASED COMBAT USING THE PLAYER AND ENEMY FUNCTIONS
class BattleSystem:
    
    #
    battlestart = True
    #enemy list gets populated at battle start and selectedtarget is populated when a player selectes an enemy to attack
    party = [MainCharacter]
    enemies = []
    selectedtarget = ""

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
        if MainCharacter.hp <= 0:
            StoryEvent.EndTheGame()
        else:
            PressEnterToContinue()

#player turn!
    def PlayerTurn():
        for elem in BattleSystem.party:
            elem.PlayerTurnDisplay()
            elem.PlayerSelectAbility()
        # BattleSystem.CheckForVictory()
        Player.playerturn = not Player.playerturn
        PressEnterToContinue()

#now enemy is selected, move is confirmed. 
    def PlayerSelectAbilityTargetConfirmed():
            BattleSystem.playermovechoice = int(BattleSystem.playermovechoice)
            selectedmove = Player.moveset[BattleSystem.playermovechoice-1]
            #accuracycheck checks against the misschance of the selected move.
            accuracycheck = random.randint (1,100)
            if accuracycheck in range (selectedmove.misschance): # so if the accuracycheck falls within the misschance of the selected move, it misses.
                GMnarrate.write  ("You missed!  \n")
            else: #otherwise, it hits and so determines how damage or buffs work here base on the selected move effect value
                if selectedmove.effect == "Physical":
                    damage = (Player.phystr + selectedmove.damage - BattleSystem.selectedtarget.phydef)
                    BattleSystem.selectedtarget.hp = (BattleSystem.selectedtarget.hp - damage)
                    GMnarrate.write (f"You used {selectedmove.name} to inflict {damage} damage. \n")
                    BattleSystem.CheckEnemyStatus()
                elif selectedmove.effect == "Legendary":
                    if Player.hp <= ((Player.hpmax / 100) * 10):
                        damage = (Player.phystr * selectedmove.damage)
                        BattleSystem.selectedtarget.hp = (BattleSystem.selectedtarget.hp - damage)
                        GMnarrate.write (f"You used {selectedmove.name} to inflict {damage} damage. \n")
                        BattleSystem.CheckEnemyStatus()
                    else:
                        GMnarrate.write ("You can't use your Limit Break ability unless your health is below 10%!")
                        PressEnterToGoBack()
                        BattleSystem.PlayerTurn()

#check to see if enemy is dead after attacking
    def CheckEnemyStatus():
        if BattleSystem.selectedtarget.hp <= 0:
            GMnarrate.write (f"{BattleSystem.selectedtarget.name} is down!")
            BattleSystem.enemies.remove (BattleSystem.selectedtarget)
            BattleSystem.PlayerCheckVictory()

#checks to see if all enemies are down 
    def PlayerCheckVictory():
            if len(BattleSystem.enemies) == 0:
                Battles.FightWon()
                

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
            MainCharacter.combatlocation = True
            if len (BattleSystem.enemies) == 1:
                BattleSystem.selectedtarget = BattleSystem.enemies[0]
                # GMnarrate.write (f"An enemy {BattleSystem.selectedtarget.job} appeared!  \n")
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

# BATTLES CLASS LOADS IN ENEMIES FOR DIFFERENT KINDS OF FIGHTS, ALSO FACILITATES THE ARENA ROUNDS FUNCTIONALITY :)
class Battles:

# FOR AT THE BEGINNING AND END OF ARENA BATTLES

    def FightWon():
        if MainCharacter.currentlocation == PowerStationArena.Area:
            Battles.ArenaVictory()
        else:
            print (MainCharacter.currentlocation)
            GMnarrate.write("You won the battle!")
    
    def ArenaFightStart():
        if MainCharacter.arenaroundcomplete == False:
            if MainCharacter.arenawins == 0:
                BattleSystem.enemies = [Vagrant]
                BattleSystem.battlestart = True
                BattleSystem.Fight()
            elif MainCharacter.arenawins == 1:
                BattleSystem.enemies = [Bouncer]
                BattleSystem.battlestart = True
                BattleSystem.Fight()
            elif MainCharacter.arenawins == 2:
                BattleSystem.enemies = [Docker]
                BattleSystem.battlestart = True
                BattleSystem.Fight()
            elif MainCharacter.arenawins == 3:
                BattleSystem.enemies = [Officer]
                BattleSystem.battlestart = True
                BattleSystem.Fight()            
            elif MainCharacter.arenawins == 4: 
                BattleSystem.enemies = [Assassin]
                BattleSystem.battlestart = True
                BattleSystem.Fight()
            else:
                pass
        else:
            GMnarrate.write ("There's nobody for you to fight right now")
            PressEnterToContinue()
            MainCharacter.currentlocation()

    def ArenaVictory():
        MainCharacter.arenawins += 1
        MainCharacter.arenaroundcomplete = True
        if MainCharacter.arenawins == 1:
            StoryEvent.FirstArenaWin()
        elif MainCharacter.arenawins == 2:
            StoryEvent.SecondArenaWin()
        PressEnterToContinue()
        MainCharacter.combatlocation = False
        MainCharacter.currentlocation()


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
        if MainCharacter.currentlocation == TutorialWorld.Area:
            if TutorialCharacter.firstmeet:
                TutorialWorld.describe2 = LocationIntroduction.TutorialWorld1
                TutorialWorld.travel1 = "Go to another location"
            elif not TutorialCharacter.firstmeet:
                TutorialWorld.firstvisit = False
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
        PowerStationGrounds.travel1 = "-"
        PowerStationGrounds.travel2 = "Visit the Bazaar"
        PowerStationGrounds.travel3 = "Head to the Skytrain Dock"
        PowerStationGrounds.option1 = "Talk to the Station Boss"
        PowerStationGrounds.option2 = "Approach the Medic Station"
        PowerStationGrounds.option3 = "-"
        PowerStationGrounds.selecttravel1 = "-"
        PowerStationGrounds.selecttravel2 = PowerStationBazaar.Area
        PowerStationGrounds.selecttravel3 = SkytrainDock.Area
        PowerStationGrounds.selectoption1 = PowerStationBoss.Talk
        PowerStationGrounds.selectoption2 = PowerStationMedicArea.Area
        PowerStationGrounds.selectoption3 = "-"

        PowerStationMedicArea.describe1 = LocationIntroduction.PowerStationMedicArea1
        PowerStationMedicArea.describe2 = LocationIntroduction.PowerStationMedicArea2
        PowerStationMedicArea.travel1 = "-"
        PowerStationMedicArea.travel2 = "-"
        PowerStationMedicArea.travel3 = "Back to the Power Station Entrance"
        PowerStationMedicArea.option1 = "Talk to the Medic"
        PowerStationMedicArea.option2 = "Approach the Field Droid"
        PowerStationMedicArea.option3 = "-"
        PowerStationMedicArea.selecttravel1 = "-"
        PowerStationMedicArea.selecttravel2 = "-"
        PowerStationMedicArea.selecttravel3 = PowerStationGrounds.Area
        PowerStationMedicArea.selectoption1 = MedicFella.Talk
        PowerStationMedicArea.selectoption2 = FieldDroid.Talk
        PowerStationMedicArea.selectoption3 = "-"
        if FieldDroid.droidclearancegranted == True:
            FieldDroid.talkoption1 = "Do you need me to grant access each time I visit?"
            FieldDroid.talkselect1 = Interactions.FieldDroidAlreadyCleared
            FieldDroid.talkoption2 = "Can you fix me up?"
            FieldDroid.talkselect2 = FieldDroid.Healing

        PowerStationBazaar.describe1 = LocationIntroduction.PowerStationBazaar1
        PowerStationBazaar.describe2 = LocationIntroduction.PowerStationBazaar2
        PowerStationBazaar.travel1 = "Go back to the Power Station entrance"
        PowerStationBazaar.travel2 = "-"
        PowerStationBazaar.travel3 = "-"
        PowerStationBazaar.option1 = "Approach the Items stall"
        PowerStationBazaar.option2 = "Talk to the Weapons trader"
        PowerStationBazaar.option3 = "Examine the Armatek stand"
        PowerStationBazaar.selecttravel1 = PowerStationGrounds.Area
        PowerStationBazaar.selecttravel2 = "-"
        PowerStationBazaar.selecttravel3 = "-"
        PowerStationBazaar.selectoption1 = VendorItem.Talk
        PowerStationBazaar.selectoption2 = VendorPhysical.Talk
        PowerStationBazaar.selectoption3 = VendorArmatek.Talk
        
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

        MedicFella.gmintro1 = Interactions.Medic1
        MedicFella.gmintro2 = Interactions.Medic2
        MedicFella.talkoption1 = "Can you fix me up?"
        MedicFella.talkoption2 = "What's that droid over there?"
        MedicFella.talkoption3 = ""
        MedicFella.talkselect1 = MedicFella.Healing
        MedicFella.talkselect2 = Interactions.MedicAskAboutDroid
        MedicFella.talkselect3 = ""
        MedicFella.askedaboutdroid = False


        FieldDroid.gmintro1 = Interactions.FieldDroid1
        FieldDroid.gmintro2 = Interactions.FieldDroid2
        FieldDroid.talkoption1 = "What clearance do you need to work?"
        FieldDroid.talkoption2 = ""
        FieldDroid.talkoption3 = ""
        FieldDroid.talkselect1 = Interactions.FieldDroidQuestion
        FieldDroid.talkselect2 = ""
        FieldDroid.talkselect3 = ""
        FieldDroid.droidclearancegranted = False


        PowerStationBoss.gmintro1 = Interactions.PowerStationBoss1
        PowerStationBoss.gmintro2 = Interactions.PowerStationBoss2
        PowerStationBoss.talkoption1 = "I need to get into the fights"
        PowerStationBoss.talkoption2 = ""
        PowerStationBoss.talkoption3 = ""
        PowerStationBoss.talkselect1 = Interactions.PowerStationBossConfirmArena
        PowerStationBoss.talkselect2 = ""
        PowerStationBoss.talkselect3 = ""

        VendorItem.gmintro1 = Interactions.VendorGreeting
        VendorItem.gmintro2 = Interactions.VendorGreeting
        VendorItem.talkoption1 = ""
        VendorItem.talkoption2 = ""
        VendorItem.talkoption3 = "Show me what you're selling"
        VendorItem.talkselect1 = ""
        VendorItem.talkselect2 = ""
        VendorItem.talkselect3 = VendorItem.SaleDisplay

        VendorPhysical.gmintro1 = Interactions.VendorGreeting
        VendorPhysical.gmintro2 = Interactions.VendorGreeting
        VendorPhysical.talkoption1 = ""
        VendorPhysical.talkoption2 = ""
        VendorPhysical.talkoption3 = "I need a better weapon"
        VendorPhysical.talkselect1 = ""
        VendorPhysical.talkselect2 = ""
        VendorPhysical.talkselect3 = VendorPhysical.SaleDisplay

        VendorArmatek.gmintro1 = Interactions.VendorGreeting
        VendorArmatek.gmintro2 = Interactions.VendorGreeting
        VendorArmatek.talkoption1 = ""
        VendorArmatek.talkoption2 = ""
        VendorArmatek.talkoption3 = "I'm looking for some new hardware"
        VendorArmatek.talkselect1 = ""
        VendorArmatek.talkselect2 = ""
        VendorArmatek.talkselect3 = VendorArmatek.SaleDisplay
        
    def ThisFunctionTookGodSixWholeDays():
        WorldBuilding.NPCUpdate()
        WorldBuilding.LocationUpdate()

############################
############################
##### SECTION - EVENTS #####
############################
############################

# LOCATION INTRODUCTION FUNCTIONS ARE LOADED BY INDIVIDUAL AREAS WHEN THEY LOAD. 
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

# STORY EVENT FUNCTIONS RUN AT KEY POINTS IN THE GAME. THEY CAN BE CALLED WHENEVER NEEDED, USUALLY BY THE WORLDBUILDING FUNCTION WHEN CERTAIN PARAMTERS ARE MET 
class StoryEvent:
    
    #runs at the start of the game to kick everything off
    def StartTheGame():
        MenuTitle.write("Project RPG        \n")
        GMtalk.write(f"Welcome, {MainCharacter.name} - to Project RPG   \nI am the Game Master of this world and will be your guide on your adventure.  \n")
        GMtalk.write("If you have never played the game before, I can show you tutorial segments throughout the game to assist you. \nOr, if you'd prefer, I can disable the tutorial elements for you. \n")
        PlayerInput.write ("Please select your preference:  \n1: Tutorials on  \n2: Tutorials off   \n")
        answer = input ()
        print()
        if answer == "1":
            Player.handholding = True
            GMtalk.write (f"Okay {MainCharacter.name} - Let's start with the basics.  \nFrom time to time I'll appear whenever new information about how the game becomes needed.   \n")
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
        TutorialWorld.Area()

    def Introduction_AboardTheSkytrain():
        GMnarrate.write("Story beat goes here. This is where our player character meets a stranger who gifts them their first items. Main character does have inventory for now")
        PressEnterToContinue()
        Train.Area()

    def FirstArenaWin():
        print ("FIRST MATCH COMPLETE")
        VendorItem.items[Potion] += 1
        VendorItem.items[HiPotion] += 1
        VendorArmatek.items[ScanningGlove] += 1
        VendorPhysical.items[Knife] += 1
    
    def SecondArenaWin():
        print ("SECOND MATCH COMPLETE")
        VendorItem.items[Potion] += 5
        VendorItem.items[HiPotion] += 5
        VendorArmatek.items[ArmaGauntlet] += 1

# SELF EXPLANATORY
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

# NPC INTERACTIONS ARE LOADED BY INDIVIDUAL NPCS WHEN YOU'RE HAVING A CHAT. EACH CHARACTER GETS ITS OWN GREETING FUNCTION AND THEN EXTRAS IF NECESSARY TO KEEP A CONVERSATION GOING.
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
        GMnarrate.write("The NPC chuckles at your brusque response  \n")
        NPCtalk.write("What you do now mate, is get on with the story! Bloke calling himself Game Master will take care of you from here.   \n")
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
    
    def Medic1():
        GMnarrate.write ("MEDIC PLACEHOLDER DESCRIPTION 1")
    def Medic2():
        GMnarrate.write ("MEDIC PLACEHOLDER DESCRIPTION 2")
        MedicFella.Healing
    def MedicAskAboutDroid():
        if MedicFella.askedaboutdroid == False:
            GMnarrate.write("STORY BEAT ABOUT DROID ORIGIN  \n")
            NPCtalk.write("NPC speech goes here for story beat.")
            MedicFella.askedaboutdroid = True
            PressEnterToGoBack()
            MedicFella.Talk()
        else:
            GMnarrate.write("CONFIRMS STORY BEAT DONE  \n")
            NPCtalk.write("We already spoke about the droid.")
            PressEnterToGoBack()
            MedicFella.Talk()
    def MedicHealing():
        if MainCharacter.ap < (MainCharacter.apmax/100*70):
            MainCharacter.ap = (MainCharacter.apmax/100*70)
        else:
            pass
        if MainCharacter.hp < (MainCharacter.hpmax/100*70):
            MainCharacter.hp = (MainCharacter.hpmax/100*70)
            GMnarrate.write("After the medic has finished examining you and administering some kind of injected formula, you can feel some of your pain begin to ease   \n")
            NPCtalk.write("That's as much as I can do for you. Maybe the droid can help you out further,if you can get the damned thign to work.    \n")
            GMtalk.write(f"{MainCharacter.name} health restored to {MainCharacter.hp}/{MainCharacter.hpmax}")
            PressEnterToGoBack()
            MedicFella.Talk()
        else:
            GMnarrate.write("The old medic looks you over:  \n")
            NPCtalk.write("I'm araid I can't patch you up any further than you are, if you can figure out how that old droid works, it might help you better.   \n")
            PressEnterToGoBack()
            MedicFella.Talk()

    def FieldDroid1():
        GMnarrate.write ("The Field Droid moves slowly around the Medic's station. It doesn't seem like it belongs here.    \n")
        NPCtalk.write("VALID AUTHORISATION REQUIRED FOR USE! BZZT")
    def FieldDroid2():
        GMnarrate.write("The Field Droid clicks it's chrome 'head' toward you:  \n ")
        if FieldDroid.droidclearancegranted == False:
            NPCtalk.write("VALID AUTHORISATION REQUIRED FOR USE! BZZT.")
        elif FieldDroid.droidclearancegranted == True:
            NPCtalk.write("DOES PRESENT COMBATANT REQUIRE ASSISTANCE?")  
    def FieldDroidQuestion():
        if MedicFella.askedaboutdroid == False and FieldDroid.droidclearancegranted == False:
            GMnarrate.write ("The Field Droid simply repeats itself: \n")
            NPCtalk.write ("VALID AUTHORISATION REQUIRED FOR USE! BZZT.")
            PressEnterToGoBack()
            FieldDroid.Talk()
        elif MedicFella.askedaboutdroid == True and FieldDroid.droidclearancegranted == False:
            GMnarrate.write ("The Field Droid notices your approach: \n")
            NPCtalk.write ("VALID AUTHORISATION REQUIRED FOR USE! BZZT.")
            if MainCharacter.job == "Medic":
                Interactions.FieldDroidClearanceGranted()
                FieldDroid.droidclearancegranted = True
                print (FieldDroid.droidclearancegranted)
                FieldDroid.Talk()
            else:
                GMnarrate.write ("This thing looks familiar from your time in the military, but only the Medics had authorisation to use them off-base. You try reciting your old rank and service number, to no avail. The droid responds:")
                NPCtalk.write("NON MEDICAL PERSONNEL ARE RESTRICTED FROM ACCESSING THIS UNIT AT THIS TIME.")
                PressEnterToGoBack()
    def FieldDroidClearanceGranted():
        print()
        GMnarrate.write ("Remembering what the old medic mentioned earlier, you recite your former military rank and service number to the droid.   \nAfter a moment, the droid sputters a response:    \n")
        NPCtalk.write ("BZT... CLEARANCE... GRANTED. \n")
        GMnarrate.write ("With some surprise at your success, you examine the droid more closely. You definitely used these during the war. They weren't perfect, but miles better than the field dressings you could provide. ")
        PressEnterToGoBack()
    def FieldDroidAlreadyCleared():
        GMnarrate.write ("The droid looks directly at you. It's optic lenses feel like they're staring straight through you.    \n")
        NPCtalk.write("NEGATIVE. SINGULAR ACCESS REQUIRED. MEDICAL ASSISTANCE NOT REQUESTED. CEASING INTERACTION.")
        PressEnterToGoBack()
        FieldDroid.Talk()
    def FieldDroidHealing():
        if MainCharacter.ap < (MainCharacter.apmax/100*85):
            MainCharacter.ap = (MainCharacter.apmax/100*85)
        else:
            pass
        if MainCharacter.hp < (MainCharacter.hpmax/100*85):
            MainCharacter.hp = (MainCharacter.hpmax/100*85)
            GMnarrate.write("The medical droid looks you over with a myriad of old tools - hardly cutting edge now, but it's more capable than the old medic.   \n")
            NPCtalk.write("COMBATANT RESTORED TO ACCEPTABLE CONDITION. REST TIME - NOT APPLICABLE. REPORT TO YOUR SENIOR OFFICER FOR FURTHER ORDERS, SOLDIER. \n")
            GMtalk.write(f"{MainCharacter.name} health restored to {MainCharacter.hp}/{MainCharacter.hpmax}")
            PressEnterToGoBack()
            FieldDroid.Talk()
        else:
            GMnarrate.write ("The droid examines you with it's array of (somewhat rusted) equipment - the years since the war have not been kind to this droid. It finally looks at you and barks a response:   \n")
            NPCtalk.write("COMBATANT CONDITION WITHIN ACCEPTABLE PARAMETERS. NO FURTHER ACTION REQUIRED. CEASING INTERACTION.")
            PressEnterToGoBack()
            FieldDroid.Talk()

    def PowerStationBoss1():
        GMnarrate.write ("POWER STATION BOSS PLACEHOLDER DESCRIPTION 1")
    def PowerStationBoss2():
        if MainCharacter.arenawins == 0:
            GMnarrate.write("The Boss Man asks")
            NPCtalk.write("You sure you wanna go in?")
        elif MainCharacter.arenawins == 1:
            GMnarrate.write("The Boss Man asks")
            NPCtalk.write("You won one round - let's see how you handle someone capable.") 
        elif MainCharacter.arenawins == 2:
            GMnarrate.write ("The Boss looks almost amused - it must be a while since he saw anyone winning fights here.")
            NPCtalk.write ("Alright then, you've got something. I've got something better...")
        elif MainCharacter.arenawins == 3:
                    GMnarrate.write ("The Boss is pleased with you - perhaps he's been making more money from this than usual.")
                    NPCtalk.write ("Right, I figure you for an ex military sort - I've got someone you might know this time")
        elif MainCharacter.arenawins == 4:
                    GMnarrate.write ("For once the Boss isn't beaming at you - he may not have banked on anyone ever getting this far.")
                    NPCtalk.write ("Got a special surprise for you... can't have you winning too many times or you'll start to make us look bad. ")
    def PowerStationBossConfirmArena():
        PowerStationBoss.talkoption1 = "Yes"
        PowerStationBoss.talkoption2 = "No, I'll come back later."
        PowerStationBoss.talkselect1 = Interactions.PowerStationBossArenaConfirmed
        PowerStationBoss.talkselect2 = MainCharacter.currentlocation
        PowerStationBoss.Talk()    
    def PowerStationBossArenaConfirmed():
        MainCharacter.holdlocation = MainCharacter.currentlocation
        MainCharacter.arenaroundcomplete = False
        PowerStationArena.Area()

    def VendorGreeting():
        greeting = random.randint(1,3)
        if greeting == 1:
            GMnarrate.write ("You are greeted with a friendly smile \n")
            NPCtalk.write ("Well howdy there! What can I get ya")
        elif greeting == 2:
            GMnarrate.write ("You are quickly examined, presumably for trouble, before being greeted    \n")
            NPCtalk.write ("Hey there, how can I help you?")
        else:
            GMnarrate.write ("The individual looks at you with a vacant expression... they look like they've been here a while  \n")
            NPCtalk.write ("Hey, uhh... what's up?")
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
            NPCtalk.write ("Do I look like a damn charity to you? Get the hell outta here until you've got soemthing WORTH MY TIME!!!  \n")
        PressEnterToGoBack()
x