from Characters import *

class Tutorial (Location, PlayerSelection):
    firstvisit = True
    def __init__():
        if Tutorial.firstvisit:
            Location.firstvisit = True
            Tutorial.firstvisit = False
        Location.describe1 = "A description of your location and the world around you"
        Location.describe2 = "Another description of your location and the world around you"
        Location.name = "The name of your location"
        Location.option1 = "Talk to NPC"
        Location.option2 = "Look at item of interest"
        Location.travel1 = "Go in one direction"
        Location.travel2 = "Go in another direction"
        PlayerSelection.option0 = Train.__init__
        PlayerSelection.option1 = ""
        PlayerSelection.option2 = ""
        PlayerSelection.option3 = ""
        PlayerSelection.option4 = ""
        PlayerSelection.option5 = ""
        PlayerSelection.option6 = ""
        PlayerSelection.option7 = ""
        PlayerSelection.option8 = ""
        PlayerSelection.option9 = ""
        Tutorial.Screen()

class Train (Location, PlayerSelection):
    firstvisit = True
    selection = ""
    def __init__():
        if Train.firstvisit:
            Location.firstvisit = True
            Train.firstvisit = False
        Location.describe1 = "You are in a Skytrain cabin. The battered leather seats haven't been fixed in years, and the once polished brass has started to rust in places."
        Location.describe2 = "Once again you enter the Skytrain and find a cabin."
        Location.name = "Skytrain"
        Location.option1 = "-"
        Location.option2 = "-"
        Location.option3 = "-"
        Location.travel1 = "Leave the Skytrain"
        Location.travel2 = "-"
        Location.travel3 = "-"
        PlayerSelection.option0 = Tutorial.__init__
        PlayerSelection.option1 = Station.__init__
        PlayerSelection.option2 = ""
        PlayerSelection.option3 = ""
        PlayerSelection.option4 = ""
        PlayerSelection.option5 = ""
        PlayerSelection.option6 = ""
        PlayerSelection.option7 = ""
        PlayerSelection.option8 = ""
        PlayerSelection.option9 = ""
        Train.Screen()

class Station (Location, PlayerSelection):
    firstvisit = True
    selection = ""
    def __init__():
        if Station.firstvisit:
            Location.firstvisit = True
            Station.firstvisit = False
        Location.describe1 = "You step off the Skytrain onto the Station dock. It stinks of smoke and diesel, and you can barely see in the smog."
        Location.describe2 = "Back at the station, you see the magnificent Skytrain docked - they always amazed you, as a boy you had never imagined they would one day take off from the rails."
        Location.name = "Skytrain"
        Location.option1 = "-"
        Location.option2 = "-"
        Location.option3 = "-"
        Location.travel1 = "Leave the Skytrain"
        Location.travel2 = "-"
        Location.travel3 = "-"
        PlayerSelection.option0 = Tutorial.__init__
        PlayerSelection.option1 = ""
        PlayerSelection.option2 = ""
        PlayerSelection.option3 = ""
        PlayerSelection.option4 = ""
        PlayerSelection.option5 = ""
        PlayerSelection.option6 = ""
        PlayerSelection.option7 = ""
        PlayerSelection.option8 = ""
        PlayerSelection.option9 = ""
        Train.Screen()
    


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