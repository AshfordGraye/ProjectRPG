from os import system, name
from time import sleep
from TypewriterText import *
from Characters import *

#  Function to clear the screen regardless of the system it runs on. Thanks to GeeksForGeeks!
def ClearScreen():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def InvalidChoice():
    GMtalk.write ("That won't work here... Try something else.")
    input("\n Press Enter to go back")
    ClearScreen()
    Chat.Screen()


# Location Menus. The menu items will be adjusted dynamically based on location
class Location:

    firstvisit = True
    currentlocation = ""
    holdlocation = ""
    lastlocation = ""
    describe1 = ""
    describe2 = ""
    name = ""
    option1 = "-"
    option2 = "-"
    option3 = "-"
    travel1 = "-"
    travel2 = "-"
    travel3 = "-"    
    
    def Screen():
        ScreenTitle.write (f"{Location.name}\n")
        if Location.firstvisit:
            GMnarrate.write (f"{Location.describe1}\n")
        else:
            GMnarrate.write (f"{Location.describe2}\n")
        Location.lastlocation = Location.holdlocation
        MenuTitle.write ("Travel Menu")
        PlayerInput.write (f"0: Go back to where I was")
        PlayerInput.write (f"1: {Location.travel1}")
        PlayerInput.write (f"2: {Location.travel2}")
        PlayerInput.write (f"3: {Location.travel3}")
        MenuTitle.write ("Action Menu")
        PlayerInput.write (f"4: {Location.option1}")
        PlayerInput.write (f"5: {Location.option2}")
        PlayerInput.write (f"6: {Location.option3}")
        MenuTitle.write ("Player Menu")
        PlayerInput.write (f"7: Check Items")
        PlayerInput.write (f"8: Check Weapons")
        PlayerInput.write (f"9: Check Stats")
        print ()
        LocationScreenSelect.init()

#  Screens that load with player information
class PlayerScreens:
    def StatScreen():
        GMnarrate.write(f'''
Your current stats are:
    Health:                 {Player.hp}/{Player.hpmax}

    Physical Strength:      {Player.phystr}
    Physical Defense:       {Player.phydef}
    Magetek Strength:       {Player.magstr}
    Magetek Defense:        {Player.magdef}
    ''')
        

    def WeaponScreen():
        GMnarrate.write (f'''
You currently have the following equipped:
    Physical Weapon:        {Player.physequip}
    Magetek Weapon:         {Player.magequip}
    ''')

    def ItemScreen():
        GMnarrate.write (f'''
You currently have the following in your inventory:
    {Player.items}
    ''')

# Basic setup for player selections in the world 
class LocationScreenSelect:

    option1 = ""
    option2 = ""
    option3 = ""
    option4 = ""
    option5 = ""
    option6 = ""

    def init():

        selection = input("What would you like to do?   \n")
        print()
        if selection == "0":
            if Location.lastlocation == "":
                LocationScreenSelect.InvalidChoice()
            else:
                ClearScreen()
                Location.firstvisit = False
                Location.holdlocation = Location.currentlocation
                Location.lastlocation()   
        elif selection == "1":
            if LocationScreenSelect.option1 == "":
                LocationScreenSelect.InvalidChoice()
            else:
                ClearScreen()
                Location.firstvisit = False
                Location.holdlocation = Location.currentlocation
                LocationScreenSelect.option1()
        elif selection == "2":
            if LocationScreenSelect.option2 == "":
                LocationScreenSelect.InvalidChoice()
            else:
                ClearScreen()
                Location.firstvisit = False
                Location.holdlocation = Location.currentlocation
                LocationScreenSelect.option2()
        elif selection == "3":
            if LocationScreenSelect.option3 == "":
                LocationScreenSelect.InvalidChoice()
            else:
                ClearScreen()
                Location.firstvisit = False
                Location.holdlocation = Location.currentlocation
                LocationScreenSelect.option3()
        elif selection == "4":
            if LocationScreenSelect.option4 == "":
                LocationScreenSelect.InvalidChoice()
            else:
                ClearScreen()
                LocationScreenSelect.option4()
        elif selection == "5":
            if LocationScreenSelect.option5 == "":
                LocationScreenSelect.InvalidChoice()
            else:
                ClearScreen()
                LocationScreenSelect.option5()
        elif selection == "6":
            if LocationScreenSelect.option6 == "":
                LocationScreenSelect.InvalidChoice()
            else:
                ClearScreen()
                LocationScreenSelect.option6()
        elif selection == "7":
            PlayerScreens.ItemScreen()
            input ("Press Enter to go back")
            ClearScreen()
            Location.Screen()
        elif selection == "8":
            PlayerScreens.WeaponScreen()
            input ("Press Enter to go back")
            ClearScreen()
            Location.Screen()
        elif selection == "9":
            PlayerScreens.StatScreen()
            input ("Press Enter to go back")
            ClearScreen()
            Location.Screen()
        else:
            LocationScreenSelect.InvalidChoice()
    
    def InvalidChoice():
        GMtalk.write ("That won't work here... Try something else.")
        input("Press Enter to go back")
        ClearScreen()
        Location.Screen()

class Chat:

    firstvisit = True
    name = ""
    greeting1 = ""
    greeting2 = ""
    items = {}
    option1 = "-"
    option2 = "-"
    option3 = "-"
    
    def Screen():
        ScreenTitle.write (f"{Chat.name}    \n")
        if Chat.firstvisit:
            GMnarrate.write("The Medic says")
            NPCtalk.write (f'{Chat.greeting1}')
            Chat.firstvisit = False
        else:
            GMnarrate.write ("the Medic now says")
            NPCtalk.write (f'{Chat.greeting2}')
        MenuTitle.write ("Chat Menu")
        PlayerInput.write (f"0: Leave this conversation")
        PlayerInput.write (f"1: {Chat.option1}")
        PlayerInput.write (f"2: {Chat.option2}")
        PlayerInput.write (f"3: {Chat.option3}")
        MenuTitle.write ("Player Menu")
        PlayerInput.write (f"7: Check Items")
        PlayerInput.write (f"8: Check Weapons")
        PlayerInput.write (f"9: Check Stats")
        print ()
        ChatScreenSelect.init()

class ChatScreenSelect:

    option1 = "chat1"
    option2 = "chat2"
    option3 = "chat3"

    def init():

        selection = input("What would you like to do?   \n")
        print()
        if selection == "0":
            ClearScreen()
            Location.currentlocation()
        elif selection == "1":
            if ChatScreenSelect.option1 == "":
                InvalidChoice()
            else:
                ClearScreen()
                ChatScreenSelect.option1()
        elif selection == "2":
            if ChatScreenSelect.option2 == "":
                InvalidChoice()
            else:
                ClearScreen()
                ChatScreenSelect.option2()
        elif selection == "3":
            if ChatScreenSelect.option3 == "":
                InvalidChoice()
            else:
                ClearScreen()
                ChatScreenSelect.option3()
        elif selection == "7":
            PlayerScreens.ItemScreen
            input ("Press Enter to go back")
            ClearScreen()
            Chat.Screen()
        elif selection == "8":
            PlayerScreens.WeaponScreen
            input ("Press Enter to go back")
            ClearScreen()
            Chat.Screen()
        elif selection == "9":
            PlayerScreens.StatScreen
            input ("Press Enter to go back")
            ClearScreen()
            Chat.Screen()
        else:
            InvalidChoice()
    
