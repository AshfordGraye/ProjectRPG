from World import *
import random
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