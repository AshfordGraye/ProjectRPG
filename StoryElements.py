from MenuSystem import *

class Story():

    @staticmethod
    def Tutorial():
        GMtalk.write (f'''
    Welcome, Player - to Project RPG. Shortly, you will be free to explore the city of Piston, meet its inhabitants, and find your way to the fighting tournament to earn your fortune. 
    But first, a little about how the game works.

    In the game world, you will be presented with menus that looks like this:
        ''')
        time.sleep(0.5)
        World.TutorialLocation()
        time.sleep(1)
        GMtalk.write ('''
    Whenever you see a list like the one above, just enter the number of the option you wish to select. It's that easy!

    Further hints like will appear like this as the game continues. 
    There will be another tutorial section when you enter a battle for the first time. Until then, enjoy the game!
        ''')
        time.sleep(2)
   
    @staticmethod
    def StoryBegins():
        GMnarrate.write ('''
You're riding the skytrain to Piston, a city on the Southern Alliance's edge. You served the Alliance during it's last war against the Northern Commonwealth. 
The Empire won, but you were cast aside afterwards, just like the rest of the conscriptions.
Now you're barely getting by - but an underground fight tournament in Piston may give you just enough fortune to start the new life you deserve...
While looking out the brass port hole you notice the stranger opposite peering at you through his goggles. After meeting your eyes, he introduces himself with a familiar Pistonian drawl:
        ''')
        NPCtalk.write ('''
    'Well hey there friend, Armish Cornwall's the name - Who do I got the pleasure of acquantancin' today?'
        ''')
        Player.Naming()
        NPCtalk.write (f'''
    'Howdy, {Player.name} - a pleasure. You go' dat stern look about yer feller, one only an Alliance vet could git. 
    I were a low rank soldier in the war, how'd they git you to serve?'
        ''')
        Player.ClassChoice()
        if Player.job == "Soldier":
            NPCtalk.write ('''
    Well I'll be, I had feelings yer might be a brother in arms
        ''')
        elif Player.job == "Scientist":
            NPCtalk.write ('''
    Shoot, you one o' dem fancy science types huh?
    Well I'm grateful fer the tech you nerds done worked up fer us!
        ''')
        elif Player.job == "Medic":
            NPCtalk.write ('''
    Hell, you boys were all whut kept us going some days... thank you, brother.
        ''')
        elif Player.job == "Officer":
            NPCtalk.write ('''
    Officer, huh... higher ups always lookin' down on us rank and file...
    I suppose yer orders kept us alive.
        ''')
        GMnarrate.write ("Armish leans back in his chair and studies you")
        NPCtalk.write ('''
    ... Yer never been ter Piston, have yer? Rough place, no Alliance peacekeepers around this far out. I gotta spare knife. Not much, but it's better than yer fists. A healing salve too, in case someone manages to get too close.
    ''')
        GMnarrate.write ('''
Armish hands you a knife. The blade is serrated, but rusted. Handle seems sturdy enough.
He also hands you a healing salve. Looks like a standard spray applicator.
        ''')
        Player.phyweapons.append("Knife")
        Player.items.append ("Healing Salve")
        GMtalk.write ('''
    A Knife has been added to your weapons list.
    A Healing Salve has been added to your items list.
        ''')
        GMnarrate.write ('''
Armish looks out the window. You are nearing Piston now, the gleaming metal superstructures piercing the clouds you are now descending towards.
He stands to leave and turns to you:
        ''')
        NPCtalk.write (f'''
    It were good makin' yer acquaintanceship the day, friend - maybe we'll see each other round the way.
    Stay safe, now, {Player.name}.
        ''')
        GMnarrate.write (f'''
After watching Armish leave, you look around the skytrain cabin. 
The battered leather seats haven't been fixed in years, and the once polished brass has started to rust in places.
You glance out of the port hole one last time at the incoming city - the skytrain is on it's landing approach. 
You turn and walk through the rusted cabin door into the skytrain's passenger corridor...
        ''')