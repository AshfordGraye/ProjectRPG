import collections
import random
from os import system, name
from time import sleep
import os
import sys
import time

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
    timer = 3
    while timer > 0:
        GMtalk.write(f"{timer}...")
        timer -= 1
        sleep(1)
    ClearScreen()

##################################
##################################
##### SECTION - USABLE MOVES #####
##################################
##################################

# THIS SECTION IS FOR USABLE MOVES BY THE PLAYER AND ENEMIES - IT'S UP AT THE TOP BECAUSE CHARACTERS AND WEAPON ITEMS WON'T INITIALISE UNLESS THESE COME FIRST

# ABILITY CLASS ALLOWS FOR CREATION OF ABILITY OBJECTS THAT WILL BE HELD WITHIN WEAPON OBJECTS WHICH ALLOWS DYNAMIC ABILITY SWAPPING.
class Ability:
    def __init__(self, name, effect, damage, rounds, apcost, chancetomiss):
        self.name = name
        self.effect = effect
        self.damage = damage
        self.apcost = apcost
        self.rounds = rounds
        self.chancetomiss = chancetomiss

    def __repr__(self):
        if self.rounds > 1:
            return (f'''{self.name} - can hit {self.rounds} times.\n   AP: {self.apcost}''')
        else:
            return (f'''{self.name} \n   AP: {self.apcost}''')   

class AbilityEffects(Ability):
    def PhysicalDamage():
        totaleffect = (BattleSystem.movechoice.damage + BattleSystem.currentplayer.phystr - BattleSystem.selectedtarget.phydef)
        BattleSystem.selectedtarget.hp -= totaleffect
        GMnarrate.write (f"{BattleSystem.currentplayer.name} used {BattleSystem.movechoice.name} for {totaleffect} damage")
    
    def ArmatekDamage():
        totaleffect = (BattleSystem.movechoice.damage + BattleSystem.currentplayer.armstr - BattleSystem.selectedtarget.armdef)
        BattleSystem.selectedtarget.hp -= totaleffect
        GMnarrate.write (f"{BattleSystem.currentplayer.name} used {BattleSystem.movechoice.name} for {totaleffect} damage")

    def Scan():
        BattleSystem.selectedtarget.ShowCurrentStats()
    
    def Legendary():
        totaleffect = ((BattleSystem.currentplayer.phystr + BattleSystem.currentplayer.armstr) * 2) * 10
        GMnarrate.write (f"{BattleSystem.currentplayer.name} used {BattleSystem.movechoice.name} for {totaleffect} damage")

##################
# STANDARD MOVES #
##################

# CONTAINS ALL AVAILABLE FUNCTIONS FOR ABILITIES TO SAVE MEMORY
AbilityEffectsList = AbilityEffects

# ABILITIES ARE SHARED BETWEEN PLAYER AND ENEMY CHARACTERS. PLAYER ABIILITIES ARE EQUIPPED THROUGH WEAPONS, ENEMIES CAN JUST DO THEM.
Attack = Ability ("Attack", AbilityEffectsList.PhysicalDamage, 20, 1, 0, 10)
Punches = Ability ("Punches", AbilityEffectsList.PhysicalDamage, 15, 3, 15, 30)
Lunge = Ability ("Lunge", AbilityEffectsList.PhysicalDamage, 30, 1, 5, 20)
KnifeCuts = Ability ("Knife Cuts", AbilityEffectsList.PhysicalDamage, 25, 2, 10, 30)
AnchorStrike = Ability ("Anchor Strike", AbilityEffectsList.PhysicalDamage, 15, 1, 15, 15)
PistolShot = Ability ("Pistol Shot", AbilityEffectsList.PhysicalDamage, 60, 1, 10, 10)
VibraSwordSlice = Ability ("VibraSword Slice", AbilityEffectsList.PhysicalDamage, 40, 1, 20, 10)
VibraSwordSlashes = Ability ("VibraSword Slashes", AbilityEffectsList.PhysicalDamage, 25, 3, 30, 20)
ArmaFist = Ability ("Arma Fist", AbilityEffectsList.PhysicalDamage, 50, 1, 10, 10)

LoaderFist = Ability ("Loader Fist", AbilityEffectsList.ArmatekDamage, 25, 2,25, 30)
ArmaScopeShot = Ability ("ArmaScope Shot", AbilityEffectsList.ArmatekDamage, 40, 1,30, 1)

ArmaMechArmLow = Ability ("Pneumatic Fist", AbilityEffectsList.PhysicalDamage, 40, 1, 0, 10)
ArmaMechArmHigh = Ability ("Grand Slam", AbilityEffectsList.PhysicalDamage, 30, 2, 0, 20)
ArmaMechChestLow = Ability ("Arma Beam Blast", AbilityEffectsList.ArmatekDamage, 200, 1, 0, 50)
ArmaMechChestHigh = Ability ("Arma Beam Bomb", AbilityEffectsList.ArmatekDamage, 150, 1, 0, 50)

#################
# ARMATEK MOVES #
#################

# LIMIT BREAK IS FOR PLAYER ONLY, REPLACES STANDARD ATTACK WHEN HEALTH IS LOW
LimitBreak = Ability ("Limit Break", AbilityEffectsList.Legendary, 10, 1,0, 0)

# FAR LESS USEFUL THAN I'D LIKE... I SHOULD HAVE DONE SOME SORT OF SPECIAL ABILITIES SYSTEM WHERE WEAPON ABILTIES ARE EQUIPPED WITH WEAPONS AND ARMATEK ABILITES ARE ACQUIRED... MAYBE IN THE NEXT EDITION.
Scan = Ability ("Scan", AbilityEffectsList.Scan, 0, 1,5, 0)

################################################
################################################
##### SECTION - USABLE ITEMS AND EQUIPMENT #####
################################################
################################################
class Item:
    def __init__(self, name, effect, action, actionlevel, damage, hits, value):
        self.name = name
        self.effect = effect
        self.action = action
        self.actionlevel = actionlevel
        self.damage = damage
        self.hits = hits
        self.value = value
        self.totaleffect = self.actionlevel * self.damage

    def __repr__(self):
        return (f"{self.name} - {self.effect} effect for {self.damage} points")

class ItemEffects(Item): 
    
    def HPBuff():
        if ConsumableSystem.selectedtarget.hp == ConsumableSystem.selectedtarget.hpmax:
            GMtalk.write(f"{ConsumableSystem.selectedtarget.name} is already at full health!")
            PressEnterToGoBack()
            ConsumableSystem.ShowConsumables()
        else:
            pass
        ConsumableSystem.selectedtarget.hp += ConsumableSystem.selectedconsumable.totaleffect
        if ConsumableSystem.selectedtarget.hp > ConsumableSystem.selectedtarget.hpmax:
            ConsumableSystem.selectedtarget.hp = ConsumableSystem.selectedtarget.hpmax
        else:
            pass
        GMnarrate.write(f"{ConsumableSystem.selectedtarget.name} HP raised to {ConsumableSystem.selectedtarget.hp}")

    def APBuff():
        if ConsumableSystem.selectedtarget.ap == ConsumableSystem.selectedtarget.apmax:
            GMtalk.write(f"{ConsumableSystem.selectedtarget.name} is already at full health!")
        else:
            pass
        ConsumableSystem.selectedtarget.ap += ConsumableSystem.selectedconsumable.totaleffect
        if ConsumableSystem.selectedtarget.ap > ConsumableSystem.selectedtarget.apmax:
            ConsumableSystem.selectedtarget.ap = ConsumableSystem.selectedtarget.apmax
        else:
            pass
        GMnarrate.write(f"{ConsumableSystem.selectedtarget.name} AP raised to {ConsumableSystem.selectedtarget.ap}")

    def PhysicalDamage():
        BattleSystem.selectedtarget.hp -= (ConsumableSystem.selectedconsumable.totaleffect - BattleSystem.selectedtarget.phydef)
        GMnarrate.write(f"{ConsumableSystem.selectedconsumable.name} used on {BattleSystem.selectedtarget.name} to cause {ConsumableSystem.selectedconsumable.totaleffect} damage.")

    def ArmatekDamage():
        BattleSystem.selectedtarget.hp -= (ConsumableSystem.selectedconsumable.totaleffect - BattleSystem.selectedtarget.armdef)
        GMnarrate.write(f"{ConsumableSystem.selectedconsumable.name} used on {BattleSystem.selectedtarget.name} to cause {ConsumableSystem.selectedconsumable.totaleffect} damage.")

    def PhyDefBuff():
        BattleSystem.selectedtarget.phydef += (ConsumableSystem.selectedconsumable.totaleffect)
        GMnarrate.write(f"{ConsumableSystem.selectedconsumable.name} used on {BattleSystem.selectedtarget.name}. Permanently raised Physical Defense to {BattleSystem.selectedtarget.phydef}.")

    def PhyStrBuff():
        BattleSystem.selectedtarget.phystr += (ConsumableSystem.selectedconsumable.totaleffect)
        GMnarrate.write(f"{ConsumableSystem.selectedconsumable.name} used on {BattleSystem.selectedtarget.name}. Permanently raised Physical Strength to {BattleSystem.selectedtarget.phystr}.")

    def ArmDefBuff():
        BattleSystem.selectedtarget.armdef += (ConsumableSystem.selectedconsumable.totaleffect)
        GMnarrate.write(f"{ConsumableSystem.selectedconsumable.name} used on {BattleSystem.selectedtarget.name}. Permanently raised Armatek Defense to {BattleSystem.selectedtarget.armdef}.")

    def ArmStrBuff():
        BattleSystem.selectedtarget.armstr += (ConsumableSystem.selectedconsumable.totaleffect)
        GMnarrate.write(f"{ConsumableSystem.selectedconsumable.name} used on {BattleSystem.selectedtarget.name}. Permanently raised Armatek Strength to {BattleSystem.selectedtarget.armstr}.")

class Weapon:
    def __init__(self, name, effect, damage, special, value):
        self.name = name
        self.effect = effect
        self.damage = damage
        self.special = special
        self.value = value
    def __repr__(self):
        if self.special == "":
            return (f"{self.name} - {self.effect} weapon for {self.damage} points.")
        else:
            return (f"{self.name} - {self.effect} weapon for {self.damage} points. Gives abiility: {self.special.name} for {self.special.apcost} AP cost.")

class Armatek:
    def __init__(self, name, effect, damage, special, value):
        self.name = name
        self.effect = effect
        self.damage = damage
        self.special = special
        self.value = value
    def __repr__(self):
        if self.special == "":
            return (f"{self.name} - {self.effect} weapon for {self.damage} points.")
        else:
            return (f"{self.name} - {self.effect} weapon for {self.damage} points. Gives abiility: {self.special.name} for {self.special.apcost} AP cost.")



    # DEFENSIVE / BUFFS

# THIS OBJECT HOLDS ALL AVAILABLE ITEM EFFECT FUNCTIONS
ItemEffectsList = ItemEffects

##############
# BUFF ITEMS #
##############
HPup1 = Item ("Field Dressing", "HP Buff", ItemEffectsList.HPBuff, 1, 30, 1, 20)
HPup2 = Item ("Medkit", "HP Buff", ItemEffectsList.HPBuff, 2, 30, 1, 40)
HPup3 = Item ("Doctor's Kit", "HP Buff", ItemEffectsList.HPBuff, 3, 30, 1, 60)

APup1 = Item ("Adreno Shot", "AP Buff", ItemEffectsList.APBuff, 1, 20, 1, 20)
APup2 = Item ("Hi Adreno Shot", "AP Buff", ItemEffectsList.APBuff, 2, 20, 1, 20)
APup3 = Item ("Mega Adreno Shot", "AP Buff", ItemEffectsList.APBuff, 3, 20, 1, 60)


DefBooster = Item ("PhyDef Booster", "Physical Defense Buff", ItemEffectsList.PhyDefBuff, 1, 20, 1, 200)
StrBooster = Item ("PhyStr Booster", "Physical Strength Buff", ItemEffectsList.PhyStrBuff, 1, 20, 1, 200)
ArmDefBooster = Item ("ArmDef Booster", "Armatek Defense Buff", ItemEffectsList.ArmDefBuff, 1, 20, 1, 200)
ArmStrBooster = Item ("ArmStr Booster", "Armatek Strength Buff", ItemEffectsList.ArmStrBuff, 1, 20, 1, 200)

################
# DEBUFF ITEMS #
################
Grenade = Item ("Grenade", "Physical Damage", ItemEffectsList.PhysicalDamage, 1, 200, 1, 50)
Grenade2 = Item ("Hi Grenade", "Physical Damage", ItemEffectsList.PhysicalDamage, 1, 375, 1, 75)
Grenade3 = Item ("Mega Grenade", "Physical Damage", ItemEffectsList.PhysicalDamage, 1, 500, 1, 100)

ArmaGrenade = Item ("Arma Grenade", "Armatek Damage", ItemEffectsList.ArmatekDamage, 1, 200, 1, 50 )
ArmaGrenade2 = Item ("Hi Arma Grenade", "Armatek Damage", ItemEffectsList.ArmatekDamage, 1, 375, 1, 75 )
ArmaGrenade3 = Item ("Mega Arma Grenade", "Armatek Damage", ItemEffectsList.ArmatekDamage, 1, 500, 1, 100 )

###########
# WEAPONS #
###########
BareKnuckles = Weapon ("Bare Knuckles", "Physical", 10, Punches, 0)
Knife = Weapon ("Knife", "Physical", 15, KnifeCuts, 0)
Pistol = Weapon ("Pistol", "Physical", 50, PistolShot, 150)

###########
# ARMATEK #
###########
ScanningGlove = Armatek ("Scanning Glove", "Armatek", 0, Scan, 100)
ArmaGauntlet = Armatek ("Mecha Gauntlet", "Armatek", 18, ArmaFist, 10)
ArmaRifle = Armatek ("Arma Rifle", "Armatek", 30, ArmaScopeShot, 100)

################################
################################
##### SECTION - CHARACTERS #####
################################
################################

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
            self.activecombat = False
            self.combatarea = ""

            self.credits = 200
            
            self.job = ""

            self.hpmax = 500
            self.hp = 500
            self.apmax = 200
            self.ap = 200

            self.phystr = 10
            self.phydef = 10
            self.armstr = 10
            self.armdef = 10

            self.phyweapons = []
            self.physequip = [BareKnuckles]
            self.armweapons = []
            self.armequip = []

            self.items = collections.Counter()
            

            self.moveset = [Attack,Punches,"-"]
            self.arenawins = 0
            self.arenaroundcomplete = False

            self.handholding = ""
            self.equipmenttutorial = False
            self.statstutorial = False
            self.itemstutorial = False
            self.combattutorial = False


    def Naming(self):
        PlayerInput.write("Enter your name: \n")
        self.name = str(input())
        if self.name == "":
            self.Naming()
        else:
            pass
    
    def ClassChoice(self):
        GMtalk.write ('''
Different roles will affect your how strong your Physical and Armatek abilities are, and how well you can defend against them. 
The damage you deal and receive will be influenced by these stats. 

Remember, your enemies will have strengths and weaknesses too!
    ''')
        PlayerInput.write ('''
What was your role in the military? Enter a role number to view it's stats.

    1: Soldier
    2: Scientist
    3: Medic
    4: Officer''')


        DecisionMaker.MenuSelection()

        if DecisionMaker.menuselect == "1":
            self.job = "Soldier"
            GMnarrate.write ("A former Soldier, you fought in the Alliance Army as a Shock Trooper.The Army's excellent training has given you great strength when fighting.    \n")
            GMtalk.write ("Your stats will be:     \n13 Physical Strength        \n10 Physical Defense     \n10 Armatek Strength     \n8  Armatek Defense")  
            self.ClassChoiceConfirm()

        elif DecisionMaker.menuselect == "2":
            self.job = "Scientist"
            GMnarrate.write ("A former Scientist, you designed weaponry to be used against the enemy.   \nYour knowledge of Armatek gives you an advantage when using Armatek equipment.    \n")
            GMtalk.write ("Your stats will be:     \n10  Physical Strength        \n8  Physical Defense     \n13 Armatek Strength     \n10 Armatek Defense")  
            self.ClassChoiceConfirm()

        elif DecisionMaker.menuselect == "3":
            self.job = "Medic"
            GMnarrate.write ("A former Medic you served and saved alongside you soldier brothers.Your hardiness earned in battle has given you stronger physical defense.    \n")
            GMtalk.write ("Your stats will be:     \n8  Physical Strength        \n13 Physical Defense     \n10 Armatek Strength     \n10 Armatek Defense")
            self.ClassChoiceConfirm()

        elif DecisionMaker.menuselect == "4":
            self.job = "Officer"
            GMnarrate.write ("A former Officer in the Alliance Navy, you commanded SkyCruiser fleets against the Commonwealth. Your officer's training gave you increased defense against Armatek abilities.    \n")
            GMtalk.write ("Your stats will be:   \n10 Physical Strength    \n10 Physical Defense \n8  Armatek Strength \n13 Armatek Defense")
            self.ClassChoiceConfirm()
           
    def ClassChoiceConfirm(self):
                PlayerInput.write ('''
Would you like to select this class, or view another?
    1: Select Role
    2: Go Back to select another Role''')
                DecisionMaker.MenuSelection()
                if DecisionMaker.menuselect == "1":
                    if self.job == "Soldier":
                        self.phystr = 13
                        self.armdef = 8
                    elif self.job == "Scientist":
                        self.phydef = 8
                        self.armstr = 13
                    elif self.job == "Medic":
                        self.phydef = 13
                        self.phystr = 8
                    elif self.job == "Officer":
                        self.armdef = 13
                        self.armstr = 8
                    else:
                        pass
                elif DecisionMaker.menuselect == "2":
                    GMtalk.write ("Okay, this section of the tutorial will restart so you can choose another class.")
                    PressEnterToGoBack()
                    MainCharacter.ClassChoice()
                else:
                    GMtalk.write ("Please enter the number of your selection")
                    MainCharacter.ClassChoiceConfirm()

    # NON COMBAT EQUIPMENT FUNCTIONS

    def ShowStats(self):
        ClearScreen()
        if MainCharacter.handholding == True and MainCharacter.statstutorial == False:
            MainCharacter.statstutorial = True
            GMtalk.write('''
Here you can view your stats and how many credits you have. 
    Remember, there will be items you can acquire in the world to improve these stats...
        ''')
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
        if MainCharacter.handholding == True and MainCharacter.equipmenttutorial == False:
            GMtalk.write ('''
Welcome to the Equipment screen. From here, you will be able to view and change your equipped items.
    Items that you equip will change your abilities in combat. 
        You'll be able to see what the ability is and how much AP it costs when viewing the items.
            Selecting menu items here works the same as everywhere else.
                ''')
            MainCharacter.equipmenttutorial = True
        else:pass
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
        DecisionMaker.MenuSelection()
        if DecisionMaker.menuselect == "1":
            self.SelectEquipment()
        elif DecisionMaker.menuselect == "2":
            pass
        else:
            InvalidChoice()
            self.ShowWeapons()

    def SelectEquipment(self):
        listorder = 0
        GMtalk.write ("Select an equipment type to change")
        PlayerInput.write("0: Cancel    \n1: Physical Equipment \n2: Armatek")
        DecisionMaker.MenuSelection()
        if DecisionMaker.menuselect =="0":
            pass
        #if player selected physical weapons
        elif DecisionMaker.menuselect == "1":
            if len (self.phyweapons) == 0:
                GMtalk.write( "You do not have another weapon to equip. \n")
                PressEnterToGoBack()
                self.ShowWeapons()
            else:
                GMtalk.write("Select a weapon to equip.")
                for elem in self.phyweapons:
                    listorder += 1
                    PlayerInput.write(f"{listorder}: {elem}")
                DecisionMaker.MenuSelection()
                if DecisionMaker.menuselectint in range (1, listorder+1):
                    removeditem = self.physequip.pop (0)
                    # self.menuselect = int(self.menuselect)
                    selecteditem = self.phyweapons.pop (DecisionMaker.menuselectint-1)
                    self.phyweapons.append (removeditem)
                    self.physequip.append (selecteditem)
                    self.moveset[1] = self.physequip[0].special
                    GMtalk.write (f"You now have the {self.physequip[0].name} equipped. \nYou can now use the {self.moveset[1].name} ability!")
                else:
                    InvalidChoice()
                    self.ShowWeapons()
        #if player selected armatek
        elif DecisionMaker.menuselect == "2":
            if len (self.armweapons) == 0:
                GMtalk.write("You do not have any Armatek Gear to equip")
                PressEnterToGoBack()
                self.ShowWeapons()
            else:
                GMtalk.write("Select gear to equip.")
                for elem in self.armweapons:
                    listorder += 1
                    PlayerInput.write(f"{listorder}: {elem}")
                DecisionMaker.MenuSelection()
                if DecisionMaker.menuselectint in range (1,listorder+1):
                    if len (self.armequip) == 0:
                        # self.menuselect = int(self.menuselect)
                        selecteditem = self.armweapons.pop (DecisionMaker.menuselectint-1)
                        print (selecteditem.name)
                        self.armequip.append (selecteditem)
                        self.moveset[2] = self.armequip[0].special
                        GMtalk.write (f"You now have the {self.armequip[0].name} equipped. \nYou can now use the {self.moveset[2].name} ability!")
                    else:
                        removeditem = self.armequip.pop (0)
                        selecteditem = self.armweapons.pop (DecisionMaker.menuselectint-1)
                        self.armweapons.append (removeditem)
                        self.armequip.append (selecteditem)
                        self.moveset[2] = self.armequip[0].special
                        GMtalk.write (f"You now have the {self.armequip[0].name} equipped. \nYou can now use the {self.moveset[2].name} ability!")
                else:
                    InvalidChoice()
                    self.ShowWeapons()
        else:
            InvalidChoice()
            self.ShowWeapons()

    # COMBAT ABILITY AND ITEM FUNCTIONS - ITEM FUNCTIONS ARE DESIGNED TO WORK INSIDE AND OUTSIDE OF COMBAT
    def PlayerTurnDisplay(self):
        if MainCharacter.handholding == True and MainCharacter.combattutorial == False:
            MainCharacter.combattutorial = True
            GMtalk.write(f'''
Welcome to combat, {MainCharacter.name}... select your moves and items in combat the same way you would anywhere else.''')
        else:pass
        MenuTitle.write("Your Turn: \n")
        # for elem in BattleSystem.enemies:
        #     if elem.hp > (elem.hpmax /100 *70):
        #         GMnarrate.write("The foe stands strong! Don't give up!   \n")
        #     elif elem.hp > (elem.hpmax /100 *30):
        #         GMnarrate.write("Your foe grows weaker! Keep it up!  \n")
        #     elif elem.hp <= (elem.hpmax /100 *30):
        #         GMnarrate.write("Your enemy grows weak! Almost there!    \n")

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
        self.PlayerSelectAbility()

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
        listmoves+=1
        PlayerInput.write(f" {listmoves}: Items")
        #get player selection
        DecisionMaker.MenuSelection()

        #check to see if selection is valid, then move to select the enemy 
        if DecisionMaker.menuselectint in range(1, listmoves+1):
            if DecisionMaker.menuselectint == 4:
                ConsumableSystem.ShowConsumables()
            else:
                self.PlayerSelectAbilityTarget()
        else:
            InvalidChoice()
            BattleSystem.PlayerTurn()

    def PlayerSelectAbilityTarget(self):
        listofenemies = 0
        #autoselect if there's only one enemy cos duh...
        if len (BattleSystem.enemies) == 1:
            BattleSystem.selectedtarget = BattleSystem.enemies[0]
            self.PlayerSelectAbilityTargetConfirmed()
        #if more than one, list and select in the same way as selecting an ability. Neat!
        else:
            GMtalk.write(f"Select an enemy to attack    \n")
            for elem in BattleSystem.enemies:
                listofenemies += 1
                PlayerInput.write (f" {listofenemies}: {elem.name}")
            DecisionMaker.MenuSelection()
            if DecisionMaker.menuselectint in range (1, listofenemies+1):
                BattleSystem.selectedtarget = BattleSystem.enemies[DecisionMaker.menuselectint-1]
                self.PlayerSelectAbilityTargetConfirmed()
            else:
                GMtalk.write ("Invalid Input")
                self.PlayerSelectAbilityTarget()

    def PlayerSelectAbilityTargetConfirmed(self):
            BattleSystem.movechoice = self.moveset[DecisionMaker.menuselectint-1]
            #accuracycheck checks against the misschance of the selected move.
            if BattleSystem.movechoice == "-":
                InvalidChoice()
                BattleSystem.PlayerTurn()
            else:
                if BattleSystem.movechoice.apcost > self.ap:
                    GMtalk.write("You don't have enough AP for that right now!")
                    self.PlayerTurnDisplay()
                else:
                    self.ap -= BattleSystem.movechoice.apcost
                    for i in range (1,BattleSystem.movechoice.rounds+1):
                        accuracycheck = random.randint (1,100)
                        if accuracycheck in range (BattleSystem.movechoice.chancetomiss): # so if the accuracycheck falls within the misschance of the selected move, it misses.
                            GMnarrate.write  (f"You tried to use {BattleSystem.movechoice.name}, but missed!  \n")
                        else: #otherwise, it hits and so determines how damage or buffs work here base on the selected move effect value
                            BattleSystem.movechoice.effect()


                            # elif selectedmove.effect == "Armatek":
                            #     pass
                            
                            # elif selectedmove.effect == "Scan":
                            #     BattleSystem.selectedtarget.ShowCurrentStats()
                            
                            # elif selectedmove.effect == "Legendary":
                            #     if self.hp <= ((self.hpmax / 100) * 10):
                            #         damage = (self.phystr * selectedmove.damage)
                            #         BattleSystem.selectedtarget.hp -= damage
                            #         GMnarrate.write (f"You used {selectedmove.name} to inflict {damage} damage. \n")
                            #         BattleSystem.CheckEnemyStatus()
                            #     else:
                            #         GMnarrate.write ("You can't use your Limit Break ability unless your health is below 10%!")
                            #         PressEnterToGoBack()
                            #         BattleSystem.PlayerTurn()
                            
                            # else:
                            #     pass
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
        WorldBuilding.WorldUpdater()
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
        DecisionMaker.MenuSelection()
        if DecisionMaker.menuselectint in range (1,4):
            self.firstmeet = False
        if DecisionMaker.menuselect == "0":
            ClearScreen()
            MainCharacter.currentlocation()
        elif DecisionMaker.menuselect == "1":
            if self.talkselect1 == "":
                self.InvalidChoice()
            else:
                ClearScreen()
                self.talkselect1()
        elif DecisionMaker.menuselect == "2":
            if self.talkselect2 == "":
                self.InvalidChoice()
            else:
                ClearScreen()
                self.talkselect2()
        elif DecisionMaker.menuselect == "3":
            if self.talkselect3 == "":
                self.InvalidChoice()
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
            GMnarrate.write ("The Vendor shakes their head...  \n")
            NPCtalk.write ("I'm not selling anything else right now. Be sure to come back and try again later.")
            PressEnterToGoBack()
            MainCharacter.currentlocation()
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
            NPCtalk.write ('''
    No worries - later now.''')
            PressEnterToGoBack()
            MainCharacter.currentlocation()
        else:
            pass
        
        if self.menuselectint in range (1,listitem+1):
            itemsforsale = list(self.items)
            selecteditem = itemsforsale[self.menuselectint-1]
            NPCtalk.write (f'''
    You sure about that {selecteditem.name}?. The developer hasn't programmed me to buy it back!
    ''')
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
                NPCtalk.write ('''
    No worries - have a look at what I have''')
                PressEnterToGoBack()
                self.SaleDisplay()
            else:
                NPCtalk.write ('''
    What? I didn't quite catch that. Have another look and let me know if you need anything.''')
                InvalidChoice()
                self.SaleDisplay()
        else:
            NPCtalk.write ('''
    What? I didn't quite catch that.    ''')
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

    def __init__(self, name, job):
        
        self.name = name
        self.job = job

        if self.job == "Vagrant":
            self.hpmax = 80
            self.hp = 80
            self.phystr = 5
            self.phydef = 5
            self.armstr = 5
            self.armdef = 5
            self.moveset = [Lunge, KnifeCuts]
        elif self.job == "Bouncer":
            self.hpmax = 120
            self.hp = 120
            self.phystr = 12
            self.phydef = 10
            self.armstr = 10
            self.armdef = 8
            self.moveset = [Punches, ArmaFist]
        elif self.job == "Docker":
            self.hpmax = 150
            self.hp = 150
            self.phystr = 10
            self.phydef = 10
            self.armstr = 12
            self.armdef = 8
            self.moveset = [AnchorStrike, LoaderFist]
        elif self.job == "Officer":
            self.hpmax = 175
            self.hp = 175
            self.phystr = 10
            self.phydef = 10
            self.armstr = 8
            self.armdef = 14
            self.moveset = [PistolShot, ArmaScopeShot]
        elif self.job == "Assassin":
            self.hpmax = 200
            self.hp = 200
            self.phystr = 14
            self.phydef = 8
            self.armstr = 10
            self.armdef = 10
            self.moveset = [VibraSwordSlice, VibraSwordSlashes]
        elif self.job == "Arma Tank Arm":
            self.hpmax = 150
            self.hp = 150
            self.phystr = 18
            self.phydef = 18
            self.armstr = 15
            self.armdef = 15
            self.moveset = [ArmaMechArmLow, ArmaMechArmHigh]
        elif self.job == "Arma Tank Core":
            self.hpmax = 200
            self.hp = 200
            self.phystr = 20
            self.phydef = 20
            self.armstr = 20
            self.armdef = 20
            self.moveset = [ArmaMechChestLow, ArmaMechChestHigh]

    def MoveSelect(self):
        misschance = random.randint (1,100)
        BattleSystem.movechoice = self.moveset [(random.randint (1,len(self.moveset)))-1]
        if misschance in range (1,BattleSystem.movechoice.chancetomiss+1):
            GMnarrate.write (f"{self.name} tried to attack, but missed!")
        else:
            Enemy.DamageCalculation(self)

    def DamageCalculation(self):
        BattleSystem.selectedtarget = BattleSystem.party[random.randint(1,len(BattleSystem.party))-1]
        BattleSystem.movechoice.effect()

    def ShowCurrentStats(self):
        MenuTitle.write (f"{self.name}  \n")
        MenuTitle.write ("HP:"); GMtalk.write(f"{self.hp}/{self.hpmax}  \n")
        MenuTitle.write ("Physical Strength:");GMtalk.write(f"{self.phystr}  \n")
        MenuTitle.write ("Physical Defense: ");GMtalk.write(f"{self.phydef}  \n")
        MenuTitle.write ("Armatek Strength: ");GMtalk.write(f"{self.armstr}  \n")
        MenuTitle.write ("Armatek Defense:  ");GMtalk.write(f"{self.armdef}  \n")
        print()
        MenuTitle.write ("Abilities:        ")
        for elem in self.moveset:
            GMtalk.write (f"{elem}")

##############
# CHARACTERS #
##############

# PLAYABLE CHARACTERS

DecisionMaker = Player ("DecisionMaker") #THIS GUY EXISTS PURELY SO THAT DECISIONS ARE HANDED OFF INSTEAD OF RELYING ON SELF FOR CHARACTERS, MAKES LIFE EASIER FOR ME. 
MainCharacter = Player ("Player")

# NPC CHARACTERS
TutorialCharacter = NPC("Tutorial NPC")
DockPorter = NPC ("Skytrain Dock Porter")
HomelessGuy = NPC ("Homeless Guy")
PowerStationBoss = NPC ("Power Station Boss")

# STORE VENDORS 
VendorItem = Vendor("Item Vendor")
VendorWeapon = Vendor ("Physical Equipment Vendor")
VendorArmatek = Vendor ("Armatek Equipment Vendor")

# MEDIIIIIIIC!!!!!
MedicFella = Medic ("Medic")
FieldDroid = Medic ("Field Droid")

    # ENEMY CHARACTERS
Vagrant = Enemy ("Vagrant", "Vagrant")
Bouncer = Enemy ("Bouncer", "Bouncer")
Docker = Enemy ("Docker", "Docker")
Officer = Enemy ("Officer", "Officer")
Assassin = Enemy ("Assassin", "Assassin")
ArmaTankLeftArm = Enemy ("Arma Tank - Left Arm", "Arma Tank Arm")
ArmaTankRightArm = Enemy ("Arma Tank - Right Arm", "Arma Tank Arm")
ArmaTankCentre = Enemy ("Arma Tank - Centre", "Arma Tank Core")

################################
################################
##### SECTION - NAVIGATION #####
################################
################################

# THE LOCATION CLASS AND LOCATION OBJECTS SHOW INFORMATION ABOUT THE PLAYER'S LOCATION AND FACILITATE NAVIGATION
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
        WorldBuilding.WorldUpdater()
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
        DecisionMaker.MenuSelection()
        if DecisionMaker.menuselectint in range (1,10):
            self.firstvisit = False
        if DecisionMaker.menuselect == "1":
            if self.selecttravel1 == "-":
                self.InvalidChoice()
            else:
                ClearScreen()
                MainCharacter.holdlocation = MainCharacter.currentlocation
                self.selecttravel1()
        elif DecisionMaker.menuselect == "2":
            if self.selecttravel2 == "-":
                self.InvalidChoice()
            else:
                ClearScreen()
                MainCharacter.holdlocation = MainCharacter.currentlocation
                self.selecttravel2()
        elif DecisionMaker.menuselect == "3":
            if self.selecttravel3 == "-":
                self.InvalidChoice()
            else:
                ClearScreen()
                MainCharacter.holdlocation = MainCharacter.currentlocation
                self.selecttravel3()
        elif DecisionMaker.menuselect == "4":
            if self.selectoption1 == "-":
                self.InvalidChoice()
            else:
                ClearScreen()
                self.selectoption1()
        elif DecisionMaker.menuselect == "5":
            if self.selectoption2 == "-":
                self.InvalidChoice()
            else:
                ClearScreen()
                self.selectoption2()
        elif DecisionMaker.menuselect == "6":
            if self.selectoption3 == "-":
                self.InvalidChoice()
            else:
                ClearScreen()
                self.selectoption3()
        elif DecisionMaker.menuselect == "7":
            ConsumableSystem.ShowConsumables()
            PressEnterToGoBack()
            self.Area()
        elif DecisionMaker.menuselect == "8":
            MainCharacter.ShowWeapons()
            PressEnterToGoBack()
            self.Area()
        elif DecisionMaker.menuselect == "9":
            MainCharacter.ShowStats()
            PressEnterToGoBack()
            self.Area()
        else:
            self.InvalidChoice()
    
    # SELF EXPLANATORY  
    def InvalidChoice(self):
        InvalidChoice()
        self.Area()

#############
# LOCATIONS #
#############
TutorialWorld = Location("The name of your current location")
Train = Location("Skytrain")
# SkytrainDock =DecisionMaker.menuselect Location("Skytrain Dock")
PowerStationDock = Location("Power Station - Dock Area")
PowerStationMedicArea = Location("Power Station - Medic's Station")
PowerStationBazaar = Location("PowerStation - Bazaar")
PowerStationArena = Location("Power Station - Workfloor Arena")

#########################################
#########################################
##### SECTION - INTERACTIVE SYSTEMS #####
#########################################
#########################################

# BATTLE SYSTEM ALLOWS TURN BASED COMBAT USING THE PLAYER AND ENEMY FUNCTIONS
class BattleSystem:
    
    #
    battlestart = True
    activeturn = True
    #enemy list gets populated at battle start and selectedtarget is populated when a player selectes an enemy to attack
    party = [MainCharacter]
    enemies = []
    currentplayer = ""
    selectedtarget = ""
    movechoice = ""

#what goes on during the enemy turn 
    def EnemyTurn():
        MenuTitle.write ("Enemy Turn:   \n")
        for elem in BattleSystem.enemies:
            BattleSystem.currentplayer = elem
            BattleSystem.currentplayer.MoveSelect()
        # BattleSystem.CheckForVictory()
        BattleSystem.activeturn = not BattleSystem.activeturn
        if MainCharacter.hp <= 0:
            StoryEvent.EndTheGame()
        else:
            PressEnterToContinue()

#player turn!
    def PlayerTurn():
        for elem in BattleSystem.party:
            BattleSystem.currentplayer = elem
            BattleSystem.currentplayer.PlayerTurnDisplay()
            PressEnterToContinue()
        # BattleSystem.CheckForVictory()
        BattleSystem.activeturn = not BattleSystem.activeturn

#check to see if enemy is dead after attacking
    def CheckEnemyStatus():
        if BattleSystem.selectedtarget.hp <= 0:
            GMnarrate.write (f"{BattleSystem.selectedtarget.name} is down!")
            BattleSystem.enemies.remove (BattleSystem.selectedtarget)
            BattleSystem.PlayerCheckVictory()
        else: 
            pass

#checks to see if all enemies are down 
    def PlayerCheckVictory():
            if len(BattleSystem.enemies) == 0:
                PressEnterToContinue()
                Battles.FightWon()
                

#runs at battle start to determine who goes first
    def FirstStrike():
        cointoss = random.randint(1,2)
        if cointoss == 1:
            BattleSystem.activeturn = True
            GMnarrate.write(f'You move fast for the first strike!   \n')
            BattleSystem.PlayerTurn()
        elif cointoss == 2:
            BattleSystem.activeturn = False
            GMnarrate.write(f'Your opponent strikes first!   \n')
            BattleSystem.EnemyTurn()

#runs the fight sequence in a loop until victory is confirmed... one way or the other... mwahahahaha lel ya might ded.
    def Fight():
        if BattleSystem.battlestart == True:
            BattleSystem.battlestart = False
            MainCharacter.activecombat = True
            if len (BattleSystem.enemies) == 1:
                BattleSystem.selectedtarget = BattleSystem.enemies[0]
                BattleSystem.FirstStrike()
            else:
                GMnarrate.write (f"Multiple Enemies!")
                BattleSystem.FirstStrike()
        if BattleSystem.activeturn == True:
            BattleSystem.PlayerTurn()
            BattleSystem.Fight()    
        elif BattleSystem.activeturn == False:
            BattleSystem.EnemyTurn()
            BattleSystem.Fight()

# BATTLES CLASS LOADS IN ENEMIES FOR DIFFERENT KINDS OF FIGHTS,  FACILITATES THE ARENA ROUNDS FUNCTIONALITY :)
class Battles:

# FOR AT THE BEGINNING AND END OF ARENA BATTLES

    def FightWon():
        if MainCharacter.combatarea == "Arena":
            Battles.ArenaVictory()
        elif MainCharacter.combatarea == "FinalBoss":
            StoryEvent.HellOuttaDodge()
        else:
            GMnarrate.write ("You won the battle!")
    
    def ArenaFightStart():
        if MainCharacter.arenaroundcomplete == False:
            if MainCharacter.arenawins == 0:
                BattleSystem.enemies = [Docker]
            elif MainCharacter.arenawins == 1:
                BattleSystem.enemies = [Officer]
            elif MainCharacter.arenawins == 2:
                BattleSystem.enemies = [Assassin]
            else:
                pass
            MainCharacter.combatarea = "Arena"
            BattleSystem.battlestart = True
            BattleSystem.Fight()
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
        elif MainCharacter.arenawins == 3:
            StoryEvent.ThirdArenaWin()
        PressEnterToContinue()
        MainCharacter.activecombat = False
        MainCharacter.currentlocation()

    def FinalBossBattle():
        BattleSystem.enemies = [ArmaTankLeftArm, ArmaTankCentre, ArmaTankRightArm]
        MainCharacter.combatarea = "FinalBoss"
        BattleSystem.battlestart = True
        BattleSystem.Fight()

# CONSUMABLE SYSTEM ALLOWS USERS TO SELECT AND USE CONSUMABLE ITEMS IN OR OUT OF COMBAT.
class ConsumableSystem:
    
    listofitems = ""
    selectedconsumable = ""
    selectedtarget = ""
    
    def ShowConsumables():
        #list the consumable items available
        if MainCharacter.handholding == True and MainCharacter.itemstutorial == False:
            MainCharacter.itemstutorial = True
            GMtalk.write('''
Here, you can select and use items in or out of combat. 
    Remember though, you won't be able to use combat items when in the main game world!
    ''')
        listconsumables = 0
        MenuTitle.write("Items:")
        PlayerInput.write ("\n0: Cancel   \n") 
        for count in MainCharacter.items:
            listconsumables += 1
            PlayerInput.write(f"{listconsumables}: {MainCharacter.items[count]} x {count}  \n")
        #let player select consumable
        GMtalk.write ("Select an item to use:")
        DecisionMaker.MenuSelection()
        if DecisionMaker.menuselect == "0":
            #check if player is outside of combat - if so will return to player's current location. If in combat will restart player turn
            if MainCharacter.activecombat == False:
                PressEnterToGoBack()
                MainCharacter.currentlocation()
            else:
                PressEnterToGoBack()
                BattleSystem.currentplayer.PlayerTurnDisplay()
        #check to see if entered value is valid
        elif DecisionMaker.menuselectint in range(1,len(MainCharacter.items)+1):
            #cast count of items as a standard list, define the selection and then select the item in the list 
            ConsumableSystem.listofitems = list(MainCharacter.items)
            ConsumableSystem.selectedconsumable = ConsumableSystem.listofitems[DecisionMaker.menuselectint-1]
            #check to see if player is out of combat and if item is not a buff to reject usage of offensive items, otherwise move onto target selection.
            if not MainCharacter.activecombat and "Buff" not in ConsumableSystem.selectedconsumable.effect:
                GMtalk.write ("You can't use that here!")
            else:
                ConsumableSystem.SelectConsumableTarget()
        else:
            InvalidChoice()
            ConsumableSystem.ShowConsumables()
        
    def SelectConsumableTarget(): 
        listoftargets = 0
        #check to see if the item effect is a buff - if it is, it will be used against friendly characters. else, it will be used against enemy characters
        if "Buff" in ConsumableSystem.selectedconsumable.effect:
            
            #check to see if there's only one person in the party. if there is, it'll be selected automatically. if not it will list the party members and let the player choose one.
            if len(BattleSystem.party) == 1:
                BattleSystem.selectedtarget = BattleSystem.party[0]
                ConsumableSystem.selectedtarget = BattleSystem.selectedtarget
                ConsumableSystem.ConsumableTargetConfirmed()
            else:
                MenuTitle.write("Targets:")
                for elem in BattleSystem.party:
                    listoftargets += 1
                    PlayerInput.write (f"{listoftargets}: {elem.name}")
                    DecisionMaker.MenuSelection()
                    BattleSystem.selectedtarget = BattleSystem.enemies[DecisionMaker.menuselectint-1]
                    ConsumableSystem.selectedtarget = BattleSystem.selectedtarget
                    ConsumableSystem.ConsumableTargetConfirmed()
        else:
            #same check as just before but for enemies. one enemy is automatically selected, more than one will allow player selection of the target. 
            if len(BattleSystem.enemies) == 1:
                BattleSystem.selectedtarget = BattleSystem.enemies[0]
                ConsumableSystem.ConsumableTargetConfirmed()
            else:
                MenuTitle.write("Targets:")
                for elem in BattleSystem.enemies:
                    listoftargets += 1
                    PlayerInput.write (f"{listoftargets}: {elem.name}")
                DecisionMaker.MenuSelection()
                BattleSystem.selectedtarget = BattleSystem.enemies[DecisionMaker.menuselectint-1]
                if DecisionMaker.menuselectint in range (1,listoftargets+1):
                    ConsumableSystem.ConsumableTargetConfirmed()
                else:
                    InvalidChoice()
                    ConsumableSystem.SelectConsumableTarget()

    def ConsumableTargetConfirmed():
        #runs item action and removes one instance of the item from player inventory 
        ConsumableSystem.selectedconsumable.action()
        MainCharacter.items[ConsumableSystem.selectedconsumable] -= 1
        if MainCharacter.items[ConsumableSystem.selectedconsumable] == 0:
            del MainCharacter.items[ConsumableSystem.selectedconsumable]
        else:
            pass
        #check to see if in combat, if so will check enemy status, if not will continue.
        if MainCharacter.activecombat:
            BattleSystem.CheckEnemyStatus()
        else:
            pass

###################################
###################################
##### SECTION - WORLDBUILDING #####
###################################
###################################

# THIS SECTION EXISTS TO POPULATE ALL OF THE CREATED OBJECTS WITH THEIR OWN VALUES. IT WILL LOAD AT THE START OF RUNTIME AND CHECKED WHENEVER A LOCATION IS LOADED TO ALLOW FOR VARIANCE DURING GAMEPLAY

# WORLDBUILDING CLASS FUNCTIONS ARE FOR ORGANISATION - EACH FUNCTION POPULATES ITS OWN SET OF INFORMATION. FINAL FUNCTION IS USED TO CALL ALL PREVIOUS FUNCTIONS AT ONCE AT THE START OF RUNTIME.
class WorldBuilding:
    
    # updates location objects
    def LocationBuilder():

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
        
        Train.describe1 = LocationIntroduction.Train1
        Train.describe2 = LocationIntroduction.Train2
        Train.travel1 = "Leave the Skytrain"
        Train.travel2 = "-"
        Train.travel3 = "-"
        Train.option1 = "-"
        Train.option2 = "-"
        Train.option3 = "-"
        Train.selecttravel1 = PowerStationDock.Area
        Train.selecttravel2 = "-"
        Train.selecttravel3 = "-"
        Train.selectoption1 = "-"
        Train.selectoption2 = "-"
        Train.selectoption3 = "-"
        
        PowerStationDock.describe1 = LocationIntroduction.PowerStationDock1
        PowerStationDock.describe2 = LocationIntroduction.PowerStationDock2
        PowerStationDock.travel1 = "Approach the Field Infirmary"
        PowerStationDock.travel2 = "Visit the Makeshift Bazaar"
        PowerStationDock.travel3 = "Board the Skytrain"
        PowerStationDock.option1 = "-"
        PowerStationDock.option2 = "Talk to the Dock Porter"
        PowerStationDock.option3 = "Talk to the Homeless Guy"
        PowerStationDock.selecttravel1 = PowerStationMedicArea.Area
        PowerStationDock.selecttravel2 = PowerStationBazaar.Area
        PowerStationDock.selecttravel3 = Train.Area
        PowerStationDock.selectoption1 = "-"
        PowerStationDock.selectoption2 = DockPorter.Talk
        PowerStationDock.selectoption3 = HomelessGuy.Talk


        PowerStationMedicArea.describe1 = LocationIntroduction.PowerStationMedicArea1
        PowerStationMedicArea.describe2 = LocationIntroduction.PowerStationMedicArea2
        PowerStationMedicArea.travel1 = "-"
        PowerStationMedicArea.travel2 = "-"
        PowerStationMedicArea.travel3 = "Back to the Power Station Dock"
        PowerStationMedicArea.option1 = "Talk to the Medic"
        PowerStationMedicArea.option2 = "Approach the Field Droid"
        PowerStationMedicArea.option3 = "-"
        PowerStationMedicArea.selecttravel1 = "-"
        PowerStationMedicArea.selecttravel2 = "-"
        PowerStationMedicArea.selecttravel3 = PowerStationDock.Area
        PowerStationMedicArea.selectoption1 = MedicFella.Talk
        PowerStationMedicArea.selectoption2 = FieldDroid.Talk
        PowerStationMedicArea.selectoption3 = "-"

        PowerStationBazaar.describe1 = LocationIntroduction.PowerStationBazaar1
        PowerStationBazaar.describe2 = LocationIntroduction.PowerStationBazaar2
        PowerStationBazaar.travel1 = "Go back to the Power Station Dock"
        PowerStationBazaar.travel2 = "-"
        PowerStationBazaar.travel3 = "-"
        PowerStationBazaar.option1 = "Approach the Items stall"
        PowerStationBazaar.option2 = "Talk to the Weapons trader"
        PowerStationBazaar.option3 = "Examine the Armatek stand"
        PowerStationBazaar.selecttravel1 = PowerStationDock.Area
        PowerStationBazaar.selecttravel2 = "-"
        PowerStationBazaar.selecttravel3 = "-"
        PowerStationBazaar.selectoption1 = VendorItem.SaleDisplay
        PowerStationBazaar.selectoption2 = VendorWeapon.SaleDisplay
        PowerStationBazaar.selectoption3 = VendorArmatek.SaleDisplay
        
        PowerStationArena.describe1 = LocationIntroduction.PowerStationArena1
        PowerStationArena.describe2 = LocationIntroduction.PowerStationArena2
        PowerStationArena.travel1 = "Head back to the Power Station Dock"
        PowerStationArena.travel2 = "-"
        PowerStationArena.travel3 = "-"
        PowerStationArena.option1 = "Approach the Arena Cage"
        PowerStationArena.option2 = "-"
        PowerStationArena.option3 = "-"
        PowerStationArena.selecttravel1 = PowerStationDock.Area
        PowerStationArena.selecttravel2 = "-"
        PowerStationArena.selecttravel3 = "-"
        PowerStationArena.selectoption1 = Battles.ArenaFightStart
        PowerStationArena.selectoption2 = "-"
        PowerStationArena.selectoption3 = "-"

    def CharacterBuilder():

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
        TutorialCharacter.askedwhatnext = False

        DockPorter.gmintro1 = Interactions.DockPorter1
        DockPorter.gmintro2 = Interactions.DockPorter2
        DockPorter.talkoption1 = "Who are you?"
        DockPorter.talkoption2 = "What is this place?"
        DockPorter.talkoption3 = ""
        DockPorter.talkselect1 = Interactions.DockPorterWhoAreYou
        DockPorter.talkselect2 = Interactions.DockPorterWhatIsThisPlace
        DockPorter.talkselect3 = ""

        HomelessGuy.gmintro1 = Interactions.HomelessGuy1
        HomelessGuy.gmintro2 = Interactions.HomelessGuy2
        HomelessGuy.talkoption1 = "Who are you?"
        HomelessGuy.talkoption2 = ""
        HomelessGuy.talkoption3 = ""
        HomelessGuy.talkselect1 = Interactions.HomelessGuyWhoAreYou
        HomelessGuy.talkselect2 = ""
        HomelessGuy.talkselect3 = ""
        HomelessGuy.askedabouthimself = False
        HomelessGuy.askedaboutboss = False

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

        VendorItem.talkoption1 = ""
        VendorItem.talkoption2 = ""
        VendorItem.talkoption3 = "Show me what you're selling"
        VendorItem.talkselect1 = ""
        VendorItem.talkselect2 = ""
        VendorItem.talkselect3 = VendorItem.SaleDisplay
        VendorItem.items[HPup1] += 2
        VendorItem.items[APup1] += 2

        VendorWeapon.talkoption1 = ""
        VendorWeapon.talkoption2 = ""
        VendorWeapon.talkoption3 = "I need a better weapon"
        VendorWeapon.talkselect1 = ""
        VendorWeapon.talkselect2 = ""
        VendorWeapon.talkselect3 = VendorWeapon.SaleDisplay

        VendorArmatek.talkoption1 = ""
        VendorArmatek.talkoption2 = ""
        VendorArmatek.talkoption3 = "I'm looking for some new hardware"
        VendorArmatek.talkselect1 = ""
        VendorArmatek.talkselect2 = ""
        VendorArmatek.talkselect3 = VendorArmatek.SaleDisplay

    def WorldUpdater():
        if MainCharacter.currentlocation == TutorialWorld.Area:
            if TutorialCharacter.firstmeet:
                TutorialWorld.describe2 = LocationIntroduction.TutorialWorld1
                TutorialWorld.travel1 = "Go to another location"
            elif not TutorialCharacter.firstmeet:
                TutorialWorld.firstvisit = False
                TutorialWorld.describe2 = LocationIntroduction.TutorialWorld2
                TutorialWorld.travel1 = "Continue the story"
                TutorialWorld.selecttravel1 = StoryEvent.Introduction_AboardTheSkytrain
            else:pass
        
        elif MainCharacter.currentlocation == Train.Area:
            if MainCharacter.arenawins == 0:
                pass
            elif MainCharacter.arenawins == 3:
                StoryEvent.FinalBossIntro()
            elif MainCharacter.combatarea == "Final Boss":
                StoryEvent.HellOuttaDodge()
            else:pass
        
        elif MainCharacter.currentlocation == PowerStationDock.Area:
            if HomelessGuy.askedabouthimself == True:
                HomelessGuy.talkoption2 = "Who's the mean looking fella that keeps looking my way?"
                HomelessGuy.talkselect2 = Interactions.HomelessGuyAskAboutBoss
            if HomelessGuy.askedaboutboss == True:
                PowerStationDock.option1 = "Talk to the Station Boss"
                PowerStationDock.selectoption1 = PowerStationBoss.Talk
            if MainCharacter.arenawins == 5:
                PowerStationDock.option1 = "-"
                PowerStationDock.selectoption1 = "-"
            else:pass
        
        elif MainCharacter.currentlocation == PowerStationMedicArea.Area:
            if FieldDroid.droidclearancegranted == True:
                FieldDroid.talkoption1 = "Do you need me to grant access each time I visit?"
                FieldDroid.talkselect1 = Interactions.FieldDroidAlreadyCleared
                FieldDroid.talkoption2 = "Can you fix me up?"
                FieldDroid.talkselect2 = FieldDroid.Healing
            else:pass
        else:pass

    def ThisFunctionTookGodSixWholeDays():
        WorldBuilding.LocationBuilder()
        WorldBuilding.CharacterBuilder()

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
        GMtalk.write('''
First, let's try talking to an NPC. 
    Try selecting the option for 'Talk to an NPC' from the menu.
        You can try looking at the items, weapons or stats menus if you like
            Or if you prefer, I can explain those later.
                ''')
        GMnarrate.write("This is how I will narrate the scene to you, with my words appearing like this.")
    def TutorialWorld2():
        GMtalk.write("Sometimes, the options available to you will change. See below? That first option will now allow you to continue the story.  \nAlso, you can check your current inventory, equipped items and current stats anytime you're travelling around the world. You can try that now, or continue forward with the story\n")
        GMnarrate.write("Welcome Back to the tutorial area.")

    def Train1():
        GMnarrate.write ("Looking around the Skytrain, you can see the battered leather seats haven't been fixed in years, and the once polished brass has started to rust in places.")
    def Train2():
        GMnarrate.write ("The Skytrain vibrates under the power of it's huge engines. It isn't due to leave yet.")

    def PowerStationDock1():
        GMnarrate.write('''
You take a look around through the smoke and fog:
    There's an old Porter that looks to be keeping himself busy and a homeless guy loafing around near the tracks.
        A burly, mean looking guy is watching you from a distance. He doesn't look friendly.
            There's an old Field Station for medics from during the war and what looks to be a makeshift bazaar in the old vehicle compound area.
            ''')
    def PowerStationDock2():
        GMnarrate.write("The Dock area is full of acrid smoke from the Power Station and visiting Skytrains. There haven't been any personal vehicles around here since the war.")

    def PowerStationMedicArea1():
        GMnarrate.write ('''
An old man, dressed in a wartime Medic's uniform, is relaxing near the Field Tent. 
    An old Field Droid is wandering around by itself.''')
    def PowerStationMedicArea2():
        GMnarrate.write ("The old man smiles at your approach, the Field Droid barely notices you.")

    def PowerStationBazaar1():
        GMnarrate.write ('''
Entering the Bazaar area, you make out three stands:
    They looks to be selling Weapons, Armatek gear and other items.
        All the vendors look at you judgingly - they know you're broke and new here, for sure.
        ''')
    def PowerStationBazaar2():
        GMnarrate.write ("The Bazaar vendors tend to their stocks and busy themselves while glancing over to you, checking for any interest in their offerings.")

    def PowerStationArena1():
        GMnarrate.write ('''
You are shown the way to the Power Station workfloor.
    A large cage arena has been constructed in the centre
        ...last chance to go back now, or you can go forward and fight this round.''')
    def PowerStationArena2():
        GMnarrate.write ("The cage arena stands before you, large and imposing. The cage floor is dirtied with the dried blood and sweat of previous combatants.")

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
            MainCharacter.handholding = True
            GMtalk.write (f"Okay {MainCharacter.name} - Let's start with the basics.  \nFrom time to time I'll appear whenever new information about how the game becomes needed.   \n")
            PressEnterToContinue()
            StoryEvent.IntroductionTutorial()
        elif answer == "2":
            MainCharacter.handholding = False
            GMtalk.write ("Alright, let's jump right into the story. Starting in")
            CountDown()
            StoryEvent.Introduction_AboardTheSkytrain()
        else:
            InvalidChoice()
            StoryEvent.StartTheGame()
    
    # runs when the player dies to end the game. 
    def EndTheGame():
        GMnarrate.write("With a final blow, your enemy dispatches your soul to the next life.   \n\n")
        GMtalk.write("Thank you for playing. Sadly, you were not able to overcome the foes which awaited you in the Piston Power Station.")
        PressEnterToContinue()
        GMtalk.write ("The game will close itself in:")
        CountDown()
        quit()
    
    def IntroductionTutorial():
        TutorialWorld.Area()

    def Introduction_AboardTheSkytrain():

        GMnarrate.write ('''
You're riding the skytrain to Piston, a city on the Southern Alliance's edge. You served the Alliance during it's last war against the Northern Commonwealth. 
    The Empire won, but you were cast aside afterwards, just like the rest of the conscriptions.
        Now you're barely getting by - but an underground fight tournament in Piston may give you just enough fortune to start the new life you deserve...
            While looking out the brass port hole you notice the stranger opposite peering at you through his goggles. After meeting your eyes, he introduces himself with a familiar Pistonian drawl:
        ''')
        NPCtalk.write ('''
    Well hey there friend, Armish Cornwall's the name - Who do I got the pleasure of acquantancin' today?
        ''')
        MainCharacter.Naming()
        NPCtalk.write (f'''
    Howdy, {MainCharacter.name} - a pleasure. You go' dat stern look about yer feller, one only an Alliance vet could git. 
    I were a low rank soldier in the war, how'd they git you to serve?
        ''')
        MainCharacter.ClassChoice()
        if MainCharacter.job == "Soldier":
            NPCtalk.write ('''
    Well I'll be, I had feelings yer might be a brother in arms
        ''')
        elif MainCharacter.job == "Scientist":
            NPCtalk.write ('''
    Shoot, you one o' dem fancy science types huh?
    Well I'm grateful fer the tech you nerds done worked up fer us!
        ''')
        elif MainCharacter.job == "Medic":
            NPCtalk.write ('''
    Hell, you boys were all whut kept us going some days... thank you, brother.
        ''')
        elif MainCharacter.job == "Officer":
            NPCtalk.write ('''
    Officer, huh... higher ups always lookin' down on us rank and file...
    I suppose yer orders kept us alive.
        ''')
        else:
            pass
        GMnarrate.write ('''
Armish leans back in his chair and studies you''')
        NPCtalk.write ('''
    ... Yer never been ter Piston, have yer? Rough place, no Alliance peacekeepers around this far out. 
        I gotta spare knife. Not much, but it's better than yer fists. 
            A Field Dressing too, in case someone manages to get too close.''')
        GMnarrate.write ('''
Armish hands you a knife. The blade is serrated, but rusted. Handle seems sturdy enough.
The field dressing doesn't look used, at least.''')
        MainCharacter.phyweapons.append (Knife)
        MainCharacter.items[HPup1] += 1
        GMtalk.write ('''
    A Knife has been added to your weapons list.
    A Field Dressing has been added to your items list.''')
        GMnarrate.write ('''
Armish looks out the window. You are nearing Piston now, the gleaming metal superstructures piercing the clouds you are now descending towards.
He stands to leave and turns to you:''')
        NPCtalk.write (f'''
    It were good makin' yer acquaintanceship the day, friend - maybe we'll see each other round the way.
    Stay safe, now, {MainCharacter.name}.''')
        PressEnterToContinue()
        Train.Area()

    def ArenaVictory():
        MainCharacter.arenawins += 1
        MainCharacter.arenaroundcomplete = True
        if MainCharacter.arenawins == 1:
            StoryEvent.FirstArenaWin()
        elif MainCharacter.arenawins == 2:
            StoryEvent.SecondArenaWin()
        PressEnterToContinue()
        MainCharacter.activecombat = False
        MainCharacter.currentlocation()

    def FirstArenaWin():
        GMnarrate.write ('''
Your first ordeal was hard to handle, but you kept your wits and pulled through.
    A few of the onlookers look extra happy...
        ...maybe they tried their luck betting on the challenger for once.''')
        GMtalk.write ("As you leave, the cage guard hands you 500 credits in winnings")

        MainCharacter.credits += 500
        VendorItem.items[HPup1] += 2
        VendorItem.items[HPup2] += 2
        VendorItem.items[APup1] += 2
        VendorItem.items[APup2] += 2
        VendorArmatek.items[ArmaGauntlet] += 1
        VendorWeapon.items[Grenade] += 1
        VendorWeapon.items[Grenade2] += 1
        VendorWeapon.items[ArmaGrenade] += 1
        VendorWeapon.items[Pistol] += 1
    
    def SecondArenaWin():
        GMnarrate.write ('''
You're starting to feel worn... 
    ...but after three wins you can almost feel your goal coming into reach.
        Climbing back out of the cage, you can hear some of the crowd cheering you on.
            They're starting to root for you.''')
        GMtalk.write ("As you leave, the cage guard hands you 1000 credits in winnings")
        MainCharacter.credits += 600
        VendorItem.items[HPup1] += 2
        VendorItem.items[HPup2] += 2
        VendorItem.items[APup1] += 2
        VendorItem.items[APup2] += 2
        VendorWeapon.items[Grenade] += 2
        VendorWeapon.items[Grenade2] += 2
        VendorWeapon.items[ArmaGrenade] += 2
        VendorWeapon.items[ArmaGrenade2] +=1
        VendorArmatek.items[DefBooster] += 1
        VendorArmatek.items[StrBooster] += 1
        VendorArmatek.items[ScanningGlove] += 1

    def ThirdArenaWin():
        GMnarrate.write ('''
Battered and almost broken, you manage to climb out of the arena cage.
    The guard looks worried...''')
        NPCtalk.write ('''
    Look, I know you deserve to win, but you gotta get out of here.
        The boss is furious - he paid a fortune for this guy to kill you.
            I heard him saying something about a Mech - just run, stranger. Take your winnings and get the hell outta dodge.''')
        GMtalk.write ("As you leave, the cage guard hands you 2000 credits in winnings")
        MainCharacter.credits += 800
        VendorItem.items[HPup1] += 2
        VendorItem.items[HPup2] += 2
        VendorItem.items[HPup3] += 2
        VendorItem.items[APup1] += 2
        VendorItem.items[APup2] += 2
        VendorItem.items[APup3] += 2
        VendorWeapon.items[Grenade2] += 2
        VendorWeapon.items[Grenade3] += 2
        VendorWeapon.items[ArmaGrenade2] += 2
        VendorWeapon.items[ArmaGrenade3] +=2
        VendorArmatek.items[ArmDefBooster] += 1
        VendorArmatek.items [ArmStrBooster] += 1
        VendorArmatek.items [ArmaRifle] += 1

    def FinalBossIntro():
        GMnarrate.write ('''
As you attempt to board the Skytrain, you hear a familiar clanking of metal and gears behind you.
    This isn't good...
        Turning around, a sight you'd hoped long gone stands before you.
            A war-era Arma Mech, these things were what your side used to win the war.
                Three seperate mech sections commanded by individual pilots - this one looks old and worn, but fully operational.
                    The Station Boss roars out over the mech's comm speakers:''')
        NPCtalk.write ('''
    DO YOU HAVE ANY IDEA HOW MUCH YOU'VE COST ME, YOU LITTLE TWERP!?!
        YEARS OF THAT ARENA BRINGING IN MONEY, AND YOU JUST SHOW UP AND TAKE OUT MY BEST GUYS???
            WELL EAT THIS, COS I'M NOT LETTING YOU GET OUT OF HERE WITH MY GODDAMN MONEY!!!!''')
        GMnarrate.write ('''
Bracing yourself for the fight ahead, you pull together your remaining strength and ready your weapon...''')
        
        PressEnterToContinue()
        Battles.FinalBossBattle()

    def HellOuttaDodge():
        PressEnterToContinue()
        GMnarrate.write ("Goodness knows how but you managed to survive your encounter with the Arma Mech.")
        GMnarrate.write ("You scramble your way aboard the Skytrain once more with a sigh of relief. \nIt was a struggle but you managed to endure - and now you have enough money and equipment to kickstart your new life as a wandering mercenary.")
        GMtalk.write ("Thank you for playing. If you managed to get this far - well done!")
        PressEnterToContinue()
        GMtalk.write ("The game will close itself in")
        CountDown()
        quit()

# NPC INTERACTIONS ARE LOADED BY INDIVIDUAL NPCS WHEN YOU'RE HAVING A CHAT. EACH CHARACTER GETS ITS OWN GREETING FUNCTION AND THEN EXTRAS IF NECESSARY TO KEEP A CONVERSATION GOING.
class Interactions:

    def TutorialCharacterGreet1():
        GMtalk.write("When talking to NPCs, You'll see an introduction by me and a greeting from the NPC. Selecting conversation options is the same as before.\n")
        GMnarrate.write ("The NPC greets you:   \n")
        NPCtalk.write('''
    Hey, when NPCs are talking to you - our speech will appear like this!
    ''')
    def TutorialCharacterGreet2():
        if TutorialCharacter.askedwhatnext:
            NPCtalk.write ('''
    What're you doing back here? I told you already, bloke calling himself Game Master will take you from here.''')
            PressEnterToContinue()
            TutorialWorld.Area()
        else:
            Interactions.TutorialCharacterGreet1()
    def TutorialCharacter_WhatNext():
        GMnarrate.write('''
The NPC chuckles at your brusque response
        ''')
        NPCtalk.write('''
    What you do now mate, is get on with the story! Bloke calling himself Game Master will take care of you from here.
    ''')
        TutorialCharacter.askedwhatnext = True
        PressEnterToContinue()
        TutorialWorld.Area()
    
    def DockPorter1():
        GMnarrate.write ("The Dock Porter busies himself working a control panel on the side of the Skytrain's engine.")
    def DockPorter2():
        GMnarrate.write ("The Dock Porter looks hard at work")
    def DockPorterWhoAreYou():
        GMnarrate.write ("The Porter smiles at you")
        NPCtalk.write('''
    Oh, I'm the Porter here - I take care of servicin' the Skytrains that come through here. 
        There's not usually many people drop by here, so it's safe to work on the engines.
            Those guys holed up in the Power Station don't really bother us none. ''')
        PressEnterToGoBack()
        DockPorter.Talk()
    def DockPorterWhatIsThisPlace():
        GMnarrate.write("The Porter looks around at the abandoned waste of what used to be a stronghold during the war")
        NPCtalk.write('''
    Well see, this area round here used to be a Power Station before the war.
        After it got damaged by shelling, it was turned into a stronghold base for military supplies and troops
            Since the war ended it's just been left. A gang of guys holed up in there since, they keep to themselves mostly. 
                I still get paid to show up and fix the engines, so, I'm still here.''')
        PressEnterToGoBack()
        DockPorter.Talk()

    def HomelessGuy1():
        GMnarrate.write ("The old homeless man glances up at you from his destitute position on the ground")
    def HomelessGuy2():
        GMnarrate.write ("The old  guy is just loafing around...")
    def HomelessGuyWhoAreYou():
        if HomelessGuy.askedabouthimself == False:
            HomelessGuy.askedabouthimself = True
            GMnarrate.write("The man seems grateful for the attention, but doesn't seem much interested in talking.")
            NPCtalk.write ('''
    Ah'm just an old man, kid... Lost my ways a long time ago. I don't like to talk bout mah past...''')
            PressEnterToGoBack()
            HomelessGuy.Talk()
        else:
            GMnarrate.write ("The old man furrows his brow")
            NPCtalk.write ('''
    come on now, kid - I already said to leave me be bout mah past...''')
            PressEnterToGoBack()
            HomelessGuy.Talk()
    def HomelessGuyAskAboutBoss():
        if HomelessGuy.askedaboutboss == False:
            HomelessGuy.askedaboutboss = True
            GMnarrate.write ("The old man looks at you with a nervous expression")
            NPCtalk.write ('''
    He's the gang boss round here - him and his boys moved in at the end of the war, see. 
        I think they run some kind operation in there. Keep seein' folk goin' in, but not so many come out you get meh?''')
            PressEnterToGoBack()
            HomelessGuy.Talk()
        else:
            GMnarrate.write ("The old man looks at you quizzically")
            NPCtalk.write ("    Yer hearin' not so good, huh? He's BAD NEWS, kid. Just leave it alone, is mah advice...")
            PressEnterToGoBack()
            HomelessGuy.Talk()

    def Medic1():
        GMnarrate.write ("The Medic notices your arrival")
        NPCtalk.write ("Well, hey there!")
    def Medic2():
        GMnarrate.write ("The Medic waves to you")
        NPCtalk.write("Well, hey again there! You need some patching up?")
        MedicFella.Healing
    def MedicAskAboutDroid():
        if MedicFella.askedaboutdroid == False:
            GMnarrate.write("The Medic looks over at the old droid \n")
            NPCtalk.write('''
    That old useless lunk? Old war droid.
        It still works, or it reckons it does -
            - seems like it's stuck in it's wartime configuration, must be have been seperated from the military comm servers.
                If you got a real Medic's ID from back then, it might actually be of some use to you''')
            MedicFella.askedaboutdroid = True
            PressEnterToGoBack()
            MedicFella.Talk()
        else:
            GMnarrate.write("The Medic rolls his eyes at you  \n")
            NPCtalk.write('''
    I already done told you - 
        - damn thing won't work without a wartime Medic's ID''')
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
        GMnarrate.write ("The Power Station Boss looks at you with disdain. He doesn't think you can handle yourself, much less take on his challengers. \n")
        NPCtalk.write("    ...What do you want?")
    def PowerStationBoss2():
        if MainCharacter.arenawins == 0:
            GMnarrate.write("The Boss Man laughs at you  \n")
            NPCtalk.write("    You sure you wanna go in? These aren't playfights kid. If you lose, you die. Game Over, as they say, hehe...")
        elif MainCharacter.arenawins == 1:
            GMnarrate.write("The Boss Man looks at you with a smile  \n")
            NPCtalk.write("    Alright, you won one round - let's see how you handle someone capable.") 
        elif MainCharacter.arenawins == 2:
            GMnarrate.write ("The Boss looks almost amused - it must be a while since he saw anyone winning fights here.    \n")
            NPCtalk.write ("    Alright then, you've got something. I've got something better...")
        elif MainCharacter.arenawins == 3:
                    GMnarrate.write ("The Boss looks fairly pleased with himself. Like he knows something he shouldn't.  \n")
                    NPCtalk.write ("    Right, I figure you for an ex military sort - I've got someone that can take you on now")
        elif MainCharacter.arenawins == 4:
                    GMnarrate.write ("For once the Boss isn't beaming at you - he may not have banked on anyone ever getting this far.\n")
                    NPCtalk.write ("    Got a special surprise for you... can't have you winning too many times or you'll start to make us look bad. ")
    def PowerStationBossConfirmArena():
        PowerStationBoss.talkoption1 = "I'm ready."
        PowerStationBoss.talkoption2 = "No, I'll come back later."
        PowerStationBoss.talkselect1 = Interactions.PowerStationBossArenaConfirmed
        PowerStationBoss.talkselect2 = MainCharacter.currentlocation
        PowerStationBoss.Talk()    
    def PowerStationBossArenaConfirmed():
        MainCharacter.holdlocation = MainCharacter.currentlocation
        MainCharacter.arenaroundcomplete = False
        PowerStationArena.Area()

    def VendorPresentItems():
        option = random.randint(1,4)
        if option == 1:
            GMnarrate.write ("You are greeted with a friendly smile ")
            NPCtalk.write ('''
    Got some good stuff for sale!  \n''')
        elif option ==2:
            GMnarrate.write ("The Vendor looks over from whatever they're messing with    ")
            NPCtalk.write ('''
    Anything take your fancy?  \n''')
        elif option == 3:
            GMnarrate.write ("You are quickly examined, presumably for trouble, before being greeted    ")
            NPCtalk.write ('''
    What catches your eye there?  \n''')
        else:
            GMnarrate.write ("The individual looks at you with a vacant expression... they look like they've been here a while  ")
            NPCtalk.write ('''
    So what'll it be?  \n''')    
    def VendorNoMoney():
        greeting = random.randint(1,13)
        if greeting in range (1,5):
            GMnarrate.write ("The Vendor shakes their head...  \n")
            NPCtalk.write ('''
    No creds, no goods... come back when you've got something for me  \n''')
        elif greeting in range (5,10):
            GMnarrate.write ("The Vendor glances at you with an annoyed expression  \n")
            NPCtalk.write ('''
    ... and what exactly are you going to be paying me with? Come on now.  \n''')
        else:
            GMnarrate.write ("The Vendor looks kind of angry, perhaps you upset them…  \n")
            NPCtalk.write ('''
    Do I look like a damn charity to you? Get the hell outta here until you've got soemthing WORTH MY TIME!!!  \n''')
        PressEnterToGoBack()

####################################
####################################
##### SECTION - TEXT ANIMATION #####
####################################
####################################
        
class type():
    def write(text, speed=0.01):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()

            time.sleep(speed)

    print("")

    def clear():
        os.system('clear')
        
    def fg(r,g,b):
        return f'\033[38;2;{r};{g};{b}m'

    def bg(r,g,b):
        return f"\033[48;2;{r};{g};{b}m"

    fg_red = fg(242,78,78)
    fg_orange = fg(255,168,5)
    fg_yellow = fg(249,255,89)
    fg_lightgreen = '\033[92m'
    fg_green = fg(54,200,99)
    fg_lightblue = '\033[94m'
    fg_lightestblue = fg(128,128,255)
    fg_blue = '\033[34m'
    fg_purple = fg(151,71,255)
    fg_brown = fg(190,140,100)
    fg_black = fg(0,0,0)
    fg_silver = fg(191,191,191)

    bg_red = bg(255,0,69)
    bg_orange = bg(255,100,0)
    bg_yellow = bg(255,255,0)
    bg_lightgreen = '\033[102m'
    bg_green = bg(54,150,50)
    bg_lightblue = '\033[104m'
    bg_blue = '\033[44m'
    bg_purple = bg(151,50,250)
    bg_brown = bg(190,100,77)
    bg_silver = bg(163,163,163)

    bold = '\033[1m'
    dim = '\033[2m'
    italic = '\033[3m'
    underline = '\033[4m'
    reverse = '\033[7m'
    invisible = '\033[8m'
    crossover = '\033[9m'
    reset = '\033[0m'

class quicktype():
    def write(text, speed=0.0):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()

            time.sleep(speed)

    print("")

    def clear():
        os.system('clear')
    def fg(r,g,b):
        return f'\033[38;2;{r};{g};{b}m'

    def bg(r,g,b):
        return f"\033[48;2;{r};{g};{b}m"

    fg_red = fg(242,78,78)
    fg_orange = fg(255,168,5)
    fg_yellow = fg(249,255,89)
    fg_lightgreen = '\033[92m'
    fg_green = fg(54,200,99)
    fg_lightblue = '\033[94m'
    fg_lightestblue = fg(128,128,255)
    fg_blue = '\033[34m'
    fg_purple = fg(151,71,255)
    fg_brown = fg(190,140,100)
    fg_black = fg(0,0,0)
    fg_silver = fg(191,191,191)

    bg_red = bg(255,0,69)
    bg_orange = bg(255,100,0)
    bg_yellow = bg(255,255,0)
    bg_lightgreen = '\033[102m'
    bg_green = bg(54,150,50)
    bg_lightblue = '\033[104m'
    bg_blue = '\033[44m'
    bg_purple = bg(151,50,250)
    bg_brown = bg(190,100,77)
    bg_silver = bg(163,163,163)

    bold = '\033[1m'
    dim = '\033[2m'
    italic = '\033[3m'
    underline = '\033[4m'
    reverse = '\033[7m'
    invisible = '\033[8m'
    crossover = '\033[9m'
    reset = '\033[0m'

# These are message classes that format text automatically
class GMtalk(type):
    def write (mytext):
        type.write(f'{type.fg_silver}{type.italic}{mytext}{type.reset}\n')

class GMnarrate(type):
    def write (mytext):
        type.write(f'{type.fg_orange}{type.italic}{mytext}{type.reset}\n')

class NPCtalk(type):
    def write (mytext):
        type.write(f'{type.fg_green}{type.italic}{mytext}{type.reset}\n')

class PlayerInput(type):
    def write (mytext):
        quicktype.write(f'{type.fg_blue}{type.bold}{mytext}{type.reset}\n')

class ScreenTitle(type):
    def write (mytext):
        type.write(f'{type.bold}{mytext}{type.reset}\n')

class MenuTitle(type):
    def write(mytext):
        type.write(f'{type.fg_purple}{mytext}{type.reset}\n')

#######################
#######################
##### RUN ZE GAME #####
#######################
#######################

WorldBuilding.ThisFunctionTookGodSixWholeDays()
StoryEvent.StartTheGame()