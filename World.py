from ScreenSystem import *
from NPCs import *

# FRAMEWORK FOR CLASS

# class X (Location):
#     firstvisit = True
#     def init():
#         Location.currentlocation = XXXXX.init
#         if XXXXX.firstvisit:
#             Location.firstvisit = True
#             Station.firstvisit = False
#         Location.describe1 = "XXXXX"
#         Location.describe2 = "XXXXX"
#         Location.name = "XXXXX"
#         Location.option1 = "-"
#         Location.option2 = "-"
#         Location.option3 = "-"
#         Location.travel1 = "-"
#         Location.travel2 = "-"
#         Location.travel3 = "-"
#         LocationScreenSelect.option1 = ""
#         LocationScreenSelect.option2 = ""
#         LocationScreenSelect.option3 = ""
#         LocationScreenSelect.option4 = ""
#         LocationScreenSelect.option5 = ""
#         LocationScreenSelect.option6 = ""
#         XXXXX.Screen()


class Tutorial (Location):
    def init():
        Location.currentlocation = Tutorial.init
        if Tutorial.firstvisit:
            Location.firstvisit = True
            Tutorial.firstvisit = False
        Location.describe1 = "A description of your location and the world around you"
        Location.describe2 = "Another description of your location and the world around you"
        Location.name = "The name of your location"
        Location.option1 = "Talk to NPC"
        Location.option2 = "Look at item of interest"
        Location.option3 = "-"
        Location.travel1 = "Go in that direction"
        Location.travel2 = "Go in the other direction"
        Location.travel3 = "-"
        Tutorial.Screen()

# EDIT THIS SUBCLASS TO ADD A HIDDEN ITEM AFTER LEAVING FOR THE FIRST TIME
class Train (Location): 
    firstvisit = True
    def init():
        Location.currentlocation = Train.init
        if Train.firstvisit:
            Location.firstvisit = True
            Train.firstvisit = False
        Location.describe1 = "You are in a Skytrain cabin. The battered leather seats haven't been fixed in years, and the once polished brass has started to rust in places."
        Location.describe2 = "Once again you enter the Skytrain and find a cabin."
        Location.name = "Skytrain"
        Location.travel1 = "Leave the Skytrain"
        Location.travel2 = "-"
        Location.travel3 = "-"
        Location.option1 = "-"
        Location.option2 = "-"
        Location.option3 = "-"
        LocationScreenSelect.option1 = Station.init
        Train.Screen()

class Station (Location):
    firstvisit = True
    def init():
        Location.currentlocation = Station.init
        if Station.firstvisit:
            Location.firstvisit = True
            Station.firstvisit = False
        Location.describe1 = "You step off the Skytrain onto the Station dock. It stinks of smoke and diesel, and you can barely see in the smog."
        Location.describe2 = "Back at the station, you see the magnificent Skytrain docked - they always amazed you, as a boy you had never imagined they would one day take off from the rails."
        Location.name = "Skytrain Dock Station"
        Location.travel1 = "Proceed to the Power Station"
        Location.travel2 = "-"
        Location.travel3 = "-"
        Location.option1 = "-"
        Location.option2 = "-"
        Location.option3 = "-"
        LocationScreenSelect.option1 = PowerStation.init
        LocationScreenSelect.option2 = ""
        LocationScreenSelect.option3 = ""
        LocationScreenSelect.option4 = ""
        LocationScreenSelect.option5 = ""
        LocationScreenSelect.option6 = ""
        Train.Screen()

class PowerStation (Location):
    firstvisit = True
    def init():
        Location.currentlocation = PowerStation.init
        if PowerStation.firstvisit:
            Location.firstvisit = True
            PowerStation.firstvisit = False
        Location.describe1 = "The hulking mass of concrete, steel and towering chimneys stands before you"
        Location.describe2 = "You stand in the grounds of the old Power Station"
        Location.name = "Old Power Station - Grounds"
        Location.travel1 = "Visit the MedicStation"
        Location.travel2 = "Visit the makeshift Bazaar in the Station lobby"
        Location.travel3 = "Head up to the Power Station workfloor"
        Location.option1 = "-"
        Location.option2 = "-"
        Location.option3 = "-"
        LocationScreenSelect.option1 = MedicStation.init
        LocationScreenSelect.option2 = Bazaar.init
        LocationScreenSelect.option3 = StationFloor.init
        LocationScreenSelect.option4 = ""
        LocationScreenSelect.option5 = ""
        LocationScreenSelect.option6 = ""
        PowerStation.Screen()

class MedicStation (Location):
    firstvisit = True
    def init():
        Location.currentlocation = MedicStation.init
        if MedicStation.firstvisit:
            Location.firstvisit = True
            MedicStation.firstvisit = False
        Location.describe1 = "The Medic's Station area seems to be staffed only by an old man and a beaten up droid."
        Location.describe2 = "The MedicStation sits in the corner. You hear the beeps and whirs of the Field Droid busying itself around the area."
        Location.name = "Old Power Station - Medic's Area"
        Location.travel1 = "-"
        Location.travel2 = "-"
        Location.travel3 = "-"
        Location.option1 = "Talk to the MedicStation"
        Location.option2 = "Approach the Field Droid"
        Location.option3 = "-"
        LocationScreenSelect.option1 = ""
        LocationScreenSelect.option2 = ""
        LocationScreenSelect.option3 = ""
        LocationScreenSelect.option4 = Medic.init
        LocationScreenSelect.option5 = ""
        LocationScreenSelect.option6 = ""
        MedicStation.Screen()

class Bazaar (Location):
    firstvisit = True
    def init():
        Location.currentlocation = Bazaar.init
        if Bazaar.firstvisit:
            Location.firstvisit = True
            Bazaar.firstvisit = False
        Location.describe1 = "You enter the Bazaar"
        Location.describe2 = "The bazaar are is full of people"
        Location.name = "Old Power Station - Makeshift Bazaar"
        Location.travel1 = "-"
        Location.travel2 = "-"
        Location.travel3 = "-"
        Location.option1 = "Talk to the Magetek Vendor"
        Location.option2 = "Talk to the Physical Vendor"
        Location.option3 = "Talk to the Item Vendor"
        LocationScreenSelect.option1 = ""
        LocationScreenSelect.option2 = ""
        LocationScreenSelect.option3 = ""
        LocationScreenSelect.option4 = ""
        LocationScreenSelect.option5 = ""
        LocationScreenSelect.option6 = ""
        Bazaar.Screen()

class StationFloor (Location):
    firstvisit = True
    def init():
        Location.currentlocation = StationFloor.init
        if StationFloor.firstvisit:
            Location.firstvisit = True
            StationFloor.firstvisit = False
        Location.describe1 = "You enter the Power Station Floor"
        Location.describe2 = "Once again into the Arena area... here goes. "
        Location.name = "Old Power Station - Work Floor"
        Location.travel1 = "-"
        Location.travel2 = "-"
        Location.travel3 = "-"
        Location.option1 = "Approach the Arena Cage"
        Location.option2 = "-"
        Location.option3 = "-"
        LocationScreenSelect.option1 = ""
        LocationScreenSelect.option2 = ""
        LocationScreenSelect.option3 = ""
        LocationScreenSelect.option4 = ""
        LocationScreenSelect.option5 = ""
        LocationScreenSelect.option6 = ""
        StationFloor.Screen()