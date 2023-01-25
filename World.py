from Characters import *

class Tutorial (Location):
    Location.describe1 = "A description of your location and the world around you"
    Location.describe2 = "A description of your location and the world around you"
    Location.name = "The name of your location"
    Location.option1 = "Talk to NPC"
    Location.option2 = "Look at item of interest"
    Location.travel1 = "Go in one direction"
    Location.travel2 = "Go in another direction"

class Train(Location):
    Location.describe1 = "You are in the Skytrain cabin. The battered leather seats haven't been fixed in years, and the once polished brass has started to rust in places."
    Location.describe2 = "Once again you enter the Skytrain and find a cabin."
    Location.name = "Skytrain"
    Location.option1 = "-"
    Location.option2 = "-"
    Location.option3 = "-"
    Location.travel1 = "Leave the Skytrain"
    Location.travel2 = "-"
    Location.travel3 = "-"


class World():

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