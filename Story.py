from GameEngine import *

class Story:
    
    #runs at the start of the game to kick everything off
    def StartTheGame():
        MenuTitle.write("Project RPG        \n\n")
        GMtalk.write("Welcome, player.")
        PressEnterToContinue()

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
            Story.StartTheGame()
        elif selection == "2":
            GMtalk.write ("Thank you for playing. The game will close itself in \n")
            CountDown()
            quit()
        else:
            InvalidInput()
            Story.EndTheGame()

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
