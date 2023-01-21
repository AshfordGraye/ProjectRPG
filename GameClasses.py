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
        PlayerMsg.write ('''
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
            Narration.write (f'''
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
                PlayerMsg.write ("Okay, this section of the tutorial will restart so you can choose another class.")
                Player.job = ""
                Player.phystr = 10
                Player.phydef = 10
                Player.magstr = 10
                Player.magdef = 10
                Player.ClassChoice()
            else:
                PlayerMsg.write ("Please enter the number of your selection")

        ############################################################################################################

        elif viewclass.lower() == "2":
            Player.job = "Scientist"
            Player.magstr += (Player.magstr /100 *30)
            Player.phydef -= (Player.phydef /100 *30)
            Player.moves = {"Attack": random.randint(25,35) + Player.phystr}
            Narration.write (f'''
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
                PlayerMsg.write ("Okay, this section of the tutorial will restart so you can choose another class.")
                Player.job = ""
                Player.phystr = 10
                Player.phydef = 10
                Player.magstr = 10
                Player.magdef = 10
                Player.ClassChoice()
            else:
                PlayerMsg.write ("Please enter the number of your selection")


        ############################################################################################################

        elif viewclass.lower() == "3":
            Player.job = "Medic"
            Player.phydef += (Player.phydef /100 *30)
            Player.phystr -= (Player.phystr /100 *30)
            Player.moves = {"Attack": random.randint(25,35) + Player.phystr}
            Narration.write (f'''
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
                PlayerMsg.write ("Okay, this section of the tutorial will restart so you can choose another class.")
                Player.job = ""
                Player.phystr = 10
                Player.phydef = 10
                Player.magstr = 10
                Player.magdef = 10
                Player.ClassChoice()
            else:
                PlayerMsg.write ("Please enter the number of your selection")


        ############################################################################################################

        elif viewclass.lower() == "4":
            Player.job = "Officer"
            Player.magdef += (Player.magdef /100 *30)
            Player.magstr -= (Player.magstr /100 *30)
            Player.moves = {"Attack": random.randint(25,35) + Player.phystr}
            Narration.write (f'''
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
                PlayerMsg.write ("Okay, this section of the tutorial will restart so you can choose another class.")
                Player.job = ""
                Player.phystr = 10
                Player.phydef = 10
                Player.magstr = 10
                Player.magdef = 10
                Player.ClassChoice()
            else:
                PlayerMsg.write ("Please enter the number of your selection")
    
    def StatsMenu():
        Narration.write(f'''
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
                Narration.write (f"You used 'Attack' to inflict {damage} damage.")
            elif Player.misschance in range (90,101):
                Narration.write  ("You tried to attack with your weapon, but missed!")
        else:
            PlayerMsg.write ("Invalid Input")
            Player.AbilitySelect()

    @staticmethod
    def StatsDisplay():
        if Enemy.hp > (Enemy.hpmax /100 *70):
            Narration.write("The foe stands strong! Don't give up!   \n")
        elif Enemy.hp > (Enemy.hpmax /100 *30):
            Narration.write("Your foe grows weaker! Keep it up!  \n")
        elif Enemy.hp <= (Enemy.hpmax /100 *30):
            Narration.write("your enemy grows weak! Almost there!    \n")

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
                    Narration.write (f'The {Enemy.job} swiped at you with a broken bottle, causing {damage} damage')
                elif Enemy.misschance in range (90,101):
                    Narration.write (f"The {Enemy.job} tried to attack you, but missed!")    
            elif Enemy.movechoice in range (5,6):
                damage = Enemy.moves["Strong Attack"]
                Player.hp -= Enemy.moves["Strong Attack"]
                Player.hp -= Enemy.moves["Attack"]
                Narration.write (f'The {Enemy.job} made a strong lunge at you with its weapon, causing {damage} damage')
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
            Narration.write(f'You move fast for the first strike!   \n')
            Player.BattlePhase()
        elif cointoss == 2:
            Player.playerturn = False
            Narration.write(f'Your opponent strikes first!   \n')
            Enemy.BattlePhase()
    
    @staticmethod
    def PlayerVictory():

        PlayerMsg.write (f'\nDecide quickly: yes or no?\n')
        answer = input(("")) ; print("\n")
        if answer.lower() in ("no"):
            Narration.write ("Your enemy stumbles to his feet and braces himself, steadying his weapon with renewed vigor. He has a cold steel in his eye... this could be his last chance to survive. \n")
            time.sleep(1)
            PlayerMsg.write (f'Brace Yourself! \n')
            time.sleep(1)
            Enemy.hp = Enemy.hpmax /100 *60
            Battle.FirstStrike()
        elif answer.lower() in ("yes"):
            Narration.write ("With a final swing of your weapon, you dispatch your foe's soul to the gods. May they have more mercy than you did... \n")
            time.sleep(1)
            Narration.write ("It was a harsh ordeal, but you have emerged victorious, and earned your freedom. Well done, warrior. \n")
            time.sleep(1)
            Narration.write("Thank you for playing. The game will close itself in five seconds. \n")
            time.sleep(5)
            quit()
        else: 
            PlayerMsg.write ("your mind is racing...  but you must focus! \n")
            Battle.PlayerVictory()

    @staticmethod
    def EnemyVictory():
        global firsthit
        global playerturn
        
        Narration.write ("You feel shattered and broken... but do you have the strength to go on? You must decide, one way or the other... \n")
        PlayerMsg.write (f"He won't wait long... Yes or No? \n")
        answer = input(str("")) ; print()
        if answer.lower() in ("yes"):
            firsthit = True
            playerturn = False
            Narration.write ("Your enemy, allowing a brief show of his military honour, allows you a moment to stand and steady your weapon. Take this chance - it could be your last. \n")
            time.sleep(1)
            PlayerMsg.write ("Brace Yourself! \n")
            time.sleep(1)
            Player.Reset()
            Battle.FirstStrike()
        elif answer.lower() in ("no"):
            Narration.write("You enemy looks upon you with disdain.\n")
            time.sleep(1)
            foetalk.write (f"'hm... pathetic. I had expected more of you.' \n")
            time.sleep(1)
            Narration.write ("With a final thrust of his weapon, your foe dispatches your dream of freedom to the gods - and your soul with it.\n")
            time.sleep(1)
            Narration.write("Thank you for playing. The app will close itself in five seconds\n")
            time.sleep(5)
            quit()
        else:
            PlayerMsg.write ("Your mind is racing... focus! \n")
            Battle.EnemyVictory()

    @staticmethod
    def CheckForVictory():
        global playerhp
        global enemyhp
        if Player.hp <= 0:
            Player.hp = 0
            Narration.write (f'Seeing an opening, the enemy rushes forward and strikes you with a vicious fury, knocking you to the ground. He stands above you and bellows for the crowd: \n')
            time.sleep(1)
            foetalk.write (f"   'ARE YOU DEFEATED ALREADY?!'\n")
            time.sleep(1)
            Battle.EnemyVictory()
        elif Enemy.hp <= 0:
            Enemy.hp = 0
            Narration.write ("Your enemy stumbles back, and then falls to the ground.\n")
            time.sleep(1)
            Narration.write ("You look down at your enemy - do you strike him down and finish the task?")
            time.sleep(1)
            Battle.PlayerVictory()
    

    @staticmethod
    def Fight():
        
        #NEED TO RESET BATTLEBEGINS AT THE END OF THE FIGHT 
        if Battle.battlestart == True:
            Battle.battlestart = False
            Enemy.SetDifficulty()
            Narration.write (f"An enemy {Enemy.job} appeared!")
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

##### GAME FUNCTION CLASSES FOR USE IN THE GAME WORLD

class PlayerLocation():
    xPos = 0
    xLimit = 20
    yPos = 0
    yLimit = 20

class GameWorld():

    def TutorialLocation():
        Narration.write('''
    A description of your locationand the things around you.
        ''')
        MenuTitle.write("Action Menu")
        PlayerInput.write('''
    1: Talk to NPC
    2: Look at item of interest
    3: Talk to a different NPC
        ''')
        MenuTitle.write("Player Menu")
        PlayerInput.write('''
    4: Stats
    5: Items
    6: Equipment
        ''')
        MenuTitle.write("Travel Menu")
        PlayerInput.write('''
    7: Go in one direction
    8: Go in another direction
    9: Go in yet another direction
    0: Go back where I just came from
        ''')

    def TrainCarriage():
        PlayerLocation.xPos = 0
        PlayerLocation.yPos = 0
        Narration.write ('''
You have entered the skytrain passenger carriage. 
It is lined either side with battered leather seats, with a brass ringed port hole facing the outside world.
        ''')

    def TrainCorridor():
        Narration.write ("You have etered the skytrain passenger corridor")
        PlayerLocation.xPos = 1
        PlayerLocation.yPos = 0



########## STORY TIME!!!

class Story():

    @staticmethod
    def Tutorial():
        PlayerMsg.write (f'''
    Welcome, Player - to Project RPG. Shortly, you will be free to explore the city of Piston, meet its inhabitants, and find your way to the fighting tournament to earn your fortune. 
    But first, a little about how the game works.

    In the game world, you will be presented with menus that looks like this:
        ''')
        time.sleep(0.5)
        GameWorld.TutorialLocation()
        time.sleep(1)
        PlayerMsg.write ('''
    Whenever you see a list like the one above, just enter the number of the option you wish to select. It's that easy!

    Further hints like will appear like this as the game continues. 
    There will be another tutorial section when you enter a battle for the first time. Until then, enjoy the game!
        ''')
        time.sleep(2)
   
    @staticmethod
    def StoryBegins():
        GameWorld.TrainCarriage()
        Narration.write ('''
You're riding the skytrain to Piston, a city on the Southern Alliance's edge. You served the Alliance during it's last war against the Northern Commonwealth. 
The Empire won, but you were cast aside afterwards, just like the rest of the conscriptions.
Now you're barely getting by - but an underground fight tournament in Piston may give you just enough fortune to start the new life you deserve...
While looking out the brass port hole you notice the stranger opposite peering at you through his goggles. After meeting your eyes, he introduces himself with a familiar Pistonian drawl:
        ''')
        npctalk.write ('''
    'Well hey there friend, Armish Cornwall's the name - Who do I got the pleasure of acquantancin' today?'
        ''')
        Player.Naming()
        npctalk.write (f'''
    'Howdy, {Player.name} - a pleasure. You go' dat stern look about yer feller, one only an Alliance vet could git. 
    I were a low rank soldier in the war, how'd they git you to serve?'
        ''')
        Player.ClassChoice()
        if Player.job == "Soldier":
            npctalk.write ('''
    Well I'll be, I had feelings yer might be a brother in arms
        ''')
        elif Player.job == "Scientist":
            npctalk.write ('''
    Shoot, you one o' dem fancy science types huh?
    Well I'm grateful fer the tech you nerds done worked up fer us!
        ''')
        elif Player.job == "Medic":
            npctalk.write ('''
    Hell, you boys were all whut kept us going some days... thank you, brother.
        ''')
        elif Player.job == "Officer":
            npctalk.write ('''
    Officer, huh... higher ups always lookin' down on us rank and file...
    I suppose yer orders kept us alive.
        ''')
        Narration.write ("Armish leans back in his chair and studies you")
        npctalk.write ('''
    ... Yer never been ter Piston, have yer? Rough place, no Alliance peacekeepers around this far out. I gotta spare knife. Not much, but it's better than yer fists. A healing salve too, in case someone manages to get too close.
    ''')
        Narration.write ('''
Armish hands you a knife. The blade is serrated, but rusted. Handle seems sturdy enough.
He also hands you a healing salve. Looks like a standard spray applicator.
        ''')
        Player.phyweapons.append("Knife")
        Player.items.append ("Healing Salve")
        PlayerMsg.write ('''
    A Knife has been added to your weapons list.
    A Healing Salve has been added to your items list.
        ''')
        Narration.write ('''
Armish looks out the window. You are nearing Piston now, the gleaming metal superstructures piercing the clouds you are now descending towards.
He stands to leave and turns to you:
        ''')
        npctalk.write (f'''
    It were good makin' yer acquaintanceship the day, friend - maybe we'll see each other round the way.
    Stay safe, now, {Player.name}.
        ''')
        Narration.write (f'''
After watching Armish leave, you look around the skytrain cabin. 
The battered leather seats haven't been fixed in years, and the once polished brass has started to rust in places.
You glance out of the port hole one last time at the incoming city - the skytrain is on it's landing approach. 
You turn and walk through the rusted cabin door into the skytrain's passenger corridor...
        ''')
    
