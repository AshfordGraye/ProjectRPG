from Characters import *

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
        MenuTitle.write ("Action Menu")
        PlayerInput.write (f"1: {Location.option1}")
        PlayerInput.write (f"2: {Location.option2}")
        PlayerInput.write (f"3: {Location.option3}")
        MenuTitle.write ("Travel Menu")
        PlayerInput.write (f"4: {Location.travel1}")
        PlayerInput.write (f"5: {Location.travel2}")
        PlayerInput.write (f"6: {Location.travel3}")
        MenuTitle.write ("Player Menu")
        PlayerInput.write (f"7: Check Items")
        PlayerInput.write (f"8: Check Weapons")
        PlayerInput.write (f"9: Check Stats")
        print ()