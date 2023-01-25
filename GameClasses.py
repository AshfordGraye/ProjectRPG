from TypewriterText import *
import random
import time

# CHARACTER CLASSES - USED FOR PLAYER AND ENEMIES

class Player():
    
    name = ""
    
    job = ""
    soldier = ""
    scientist = ""
    medic = ""
    officer = ""

    hpmax = 1000
    hp = hpmax
    mpmax = 100
    mp = mpmax

    phystr = 10
    phydef = 10
    magstr = 10
    magdef = 10

    phyweapons = []
    physequip = ['none']
    magweapons = []
    magequip = ['none']
    items = []

    moves = {}
    misschance = random.randint (1,100)
    playerturn = False
    
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
    
    def StatsMenu():
        GMnarrate.write(f'''
Your current stats are:
    Health:                 {Player.hp}/{Player.hpmax}

    Physical Strength:      {Player.phystr}
    Physical Defense:       {Player.phydef}
    Magetek Strength:       {Player.magstr}
    Magetek Defense:        {Player.magdef}

You currently have the following equipped:
    Physical Weapon:        {Player.physequip}
    Magetek Weapon:         {Player.magequip}
        ''')

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

class Enemy():
    
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

##### BATTLE CLASSES - BASE BATTLE CLASS DETERMINES HOW THEY WORK, SUBCLASSES DEETERMINE THE DIFFICULTY (AND EVENTUALLY WHO)

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
        global playerhp
        global enemyhp
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

class LowLvlBadGuy(Battle):
    
    @staticmethod
    def StartFight():
        Enemy.level = 1
        LowLvlBadGuy.Fight()