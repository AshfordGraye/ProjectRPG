from StoryElements import *

class Tutorial (Location):
    Location.name = "Tutorial Area"

class World():

    def TutorialLocation():
        GMnarrate.write('''
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

    def Train():
        print("you are on the train")
        playerchoice = int(input("where to go? \n 1)station\n"))
        if playerchoice == 1:
            World.Station()

    def Station():
        print("you have arrived at the station")
        playerchoice = int(input("where to go? \n 2) Plant 2) Train\n"))
        if playerchoice == 1:
            World.PowerPlant()
        elif playerchoice == 2:
            World.Train()

    def PowerPlant():
        print ("you have arrived at the power plant")
        playerchoice = int(input("where to go? \n 1) Arena \n 2) Medic \n 3) Bazaar \n 0) back to the station"))
        if playerchoice == 1:
            World.Arena()
        elif playerchoice == 2:
            World.Medic()
        elif playerchoice == 3:
            World.Bazaar()
        elif playerchoice == 0:
            World.Station()
    
    def Arena():
        print ("you have arrived at the arena. you aren't fighting today, kid!")
        playerchoice = int(input("where to go? \n 1) Back to Plant \n "))
        if playerchoice == 1:
            World.PowerPlant()
    
    def Medic():
        print ("you have arrived at the Medic. No healing just yet!")
        playerchoice = int(input("where to go? \n 1) Back to plant\n "))
        if playerchoice == 1:
            World.PowerPlant()

    def Bazaar():
        print ("You have arrived at the bazaar")
        playerchoice = int(input("where to go? \n 1) Back to plant\n "))
        if playerchoice == 1:
            World.PowerPlant()