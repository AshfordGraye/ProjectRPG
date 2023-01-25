from TypewriterText import *

# Location Menus. The menu items will be adjusted dynamically based on location
class Location:

    firstvisit = True
    describe1 = ("")
    describe2 = ("")
    name = ("")
    option1 = ("")
    option2 = ("")
    option3 = ("")
    travel1 = ("")
    travel2 = ("")
    travel3 = ("")    
    
    def Screen():
        if Location.firstvisit:
            GMnarrate.write (f"{Location.describe1}\n")
            Location.firstvisit = False
        else:
            GMnarrate.write (f"{Location.describe2}\n")
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
        PlayerSelection.PlayerAction()

# Basic setup for player selections in the world 
class PlayerSelection:
    option0 = ""
    option1 = ""
    option2 = ""
    option3 = ""
    option4 = ""
    option5 = ""
    option6 = ""
    option7 = ""
    option8 = ""
    option9 = ""
    def __init__():
        PlayerSelection.option0 = ""
        PlayerSelection.option1 = ""
        PlayerSelection.option2 = ""
        PlayerSelection.option3 = ""
        PlayerSelection.option4 = ""
        PlayerSelection.option5 = ""
        PlayerSelection.option6 = ""
        PlayerSelection.option7 = ""
        PlayerSelection.option8 = ""
        PlayerSelection.option9 = ""

    def PlayerAction():
        selection = input("What would you like to do?   \n")
        if selection == "0":
            PlayerSelection.option0()
        elif selection == "1":
            PlayerSelection.option1()
        elif selection == "2":
            PlayerSelection.option2()
        elif selection == "3":
            PlayerSelection.option3()
        elif selection == "4":
            PlayerSelection.option4()
        elif selection == "5":
            PlayerSelection.option5()
        elif selection == "6":
            PlayerSelection.option6()
        elif selection == "7":
            PlayerSelection.option7()
        elif selection == "8":
            PlayerSelection.option8()
        elif selection == "9":
            PlayerSelection.option9()
