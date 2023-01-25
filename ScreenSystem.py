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




# Location Menus. The menu items will be adjusted dynamically based on location
class Location:

    firstvisit = True
    currentlocation = ""
    holdlocation = ""
    lastlocation = ""
    describe1 = ""
    describe2 = ""
    name = ""
    option1 = ""
    option2 = ""
    option3 = ""
    travel1 = ""
    travel2 = ""
    travel3 = ""    
    
    def Screen():
        if Location.firstvisit:
            GMnarrate.write (f"{Location.describe1}\n")
            Location.firstvisit = False
        else:
            GMnarrate.write (f"{Location.describe2}\n")
        Location.lastlocation = Location.holdlocation
        MenuTitle.write (f"{Location.name}\n")
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
        PlayerInput.write (f"0: Go back where I just came from")
        print ()
        PlayerSelection.__init__()

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
class PlayerSelection:
    option1 = ""
    option2 = ""
    option3 = ""
    option4 = ""
    option5 = ""
    option6 = ""
    option7 = PlayerScreens.ItemScreen
    option8 = PlayerScreens.WeaponScreen
    option9 = PlayerScreens.StatScreen

    def __init__():

        selection = input("What would you like to do?   \n")
        print()
        if selection == "0":
            if Location.lastlocation == "":
                PlayerSelection.InvalidChoice()
            else:
                Location.holdlocation = Location.currentlocation  
                Location.lastlocation()   
        elif selection == "1":
            if PlayerSelection.option1 == "-":
                PlayerSelection.InvalidChoice()
            else:
                Location.firstvisit = False
                Location.holdlocation = Location.currentlocation
                PlayerSelection.option1()
        elif selection == "2":
            if PlayerSelection.option2 == "-":
                PlayerSelection.InvalidChoice()
            else:
                Location.firstvisit = False
                Location.holdlocation = Location.currentlocation
                PlayerSelection.option2()
        elif selection == "3":
            if PlayerSelection.option3 == "-":
                PlayerSelection.InvalidChoice()
            else:
                Location.firstvisit = False
                Location.holdlocation = Location.currentlocation
                PlayerSelection.option3()
        elif selection == "4":
            PlayerSelection.option4()
        elif selection == "5":
            PlayerSelection.option5()
        elif selection == "6":
            PlayerSelection.option6()
        elif selection == "7":
            PlayerSelection.option7()
            input ("Press Enter to go back")
            ClearScreen()
            Location.Screen()
        elif selection == "8":
            PlayerSelection.option8()
            input ("Press Enter to go back")
            ClearScreen()
            Location.Screen()
        elif selection == "9":
            PlayerSelection.option9()
            input ("Press Enter to go back")
            ClearScreen()
            Location.Screen()
        else:
            PlayerSelection.InvalidChoice()
    
    def InvalidChoice():
        GMtalk.write ("That won't work here... Try something else.")
        input("Press Enter to go back")
        ClearScreen()
        Location.Screen()