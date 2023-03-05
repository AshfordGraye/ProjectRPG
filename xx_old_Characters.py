class Porter (NPC):
    firstvisit = True
    localinventory = []
    def init():
        NPC.name = "Skytrain Dock porter"
        if Porter.firstvisit:
            NPC.firstvisit = True
            NPC.gmintro1 = Story.GMIntroTest1
            Porter.firstvisit = False
        else:
            NPC.gmintro2 = Story.GMIntroTest2
        NPC.option1 = "-"
        NPC.option2 = "-"
        NPC.option3 = "-"
        NPC.select1 = ""
        NPC.select2 = ""
        NPC.select3 = ""
        NPC.Display()

class HomelessGuy(NPC):
    firstvisit = True
    localinventory = []
    def init():
        NPC.name = "Homeless Guy"
        if HomelessGuy.firstvisit:
            NPC.firstvisit = True
            NPC.gmintro1 = Story.GMIntroTest1
            HomelessGuy.firstvisit = False
        else:
            NPC.gmintro2 = Story.GMIntroTest2
        NPC.option1 = "-"
        NPC.option2 = "-"
        NPC.option3 = "-"
        NPC.select1 = ""
        NPC.select2 = ""
        NPC.select3 = ""
        NPC.Display()

class BossMan(NPC):
    firstvisit = True
    def init():
        NPC.name = "BossMan"
        if BossMan.firstvisit:
            NPC.firstvisit = True
            NPC.gmintro1 = Story.GMIntroTest1

            BossMan.firstvisit = False
        else:
            NPC.gmintro2 = Story.GMIntroTest2

        NPC.option1 = "Need to get into the fights"
        NPC.option2 = "-"
        NPC.option3 = "-"
        NPC.select1 = Interactions.BossManConfirmFight
        NPC.select2 = ""
        NPC.select3 = ""
        NPC.Display()

class Medic(NPC):
    firstvisit = True
    localinventory = []
    def init():
        NPC.name = "Medic"
        if Medic.firstvisit:
            NPC.firstvisit = True
            NPC.gmintro1 = Story.GMIntroTest1
            Medic.firstvisit = False
        else:
            NPC.gmintro2 = Story.GMIntroTest2
        NPC.option1 = "I'm hurt, can you help?"
        NPC.option2 = "What's that droid for?"
        NPC.option3 = "-"
        NPC.select1 = ""
        NPC.select2 = ""
        NPC.select3 = ""
        NPC.Display()

class FieldDroid(NPC):
    firstvisit = True
    localinventory = []
    def init():
        NPC.name = "Field Droid"
        if FieldDroid.firstvisit:
            NPC.firstvisit = True
            NPC.gmintro1 = Story.GMIntroTest1
            FieldDroid.firstvisit = False
        else:
            NPC.gmintro2 = Story.GMIntroTest2
        NPC.option1 = "Instruct Droid to fix you up"
        NPC.option2 = "-"
        NPC.option3 = "-"
        NPC.select1 = ""
        NPC.select2 = ""
        NPC.select3 = ""
        NPC.Display()

class VendorPhys (NPC):
    firstvisit = True
    localinventory = []
    def init():
        NPC.name = "Store - Iron Will"
        if VendorPhys.firstvisit:
            NPC.firstvisit = True
            NPC.gmintro1 = Interactions.VendorGreeting
            VendorPhys.firstvisit = False
        else:
            NPC.gmintro2 = Interactions.VendorGreeting
        NPC.option1 = "-"
        NPC.option2 = "-"
        NPC.option3 = "-"
        NPC.select1 = ""
        NPC.select2 = ""
        NPC.select3 = ""
        NPC.Display()

class VendorMag (NPC):
    firstvisit = True
    localinventory = []
    def init():
        NPC.name = "Store - Technomancy"
        if VendorMag.firstvisit:
            NPC.firstvisit = True
            NPC.gmintro1 = Interactions.VendorGreeting
            VendorMag.firstvisit = False
        else:
            NPC.gmintro2 = Interactions.VendorGreeting
        NPC.option1 = "-"
        NPC.option2 = "-"
        NPC.option3 = "-"
        NPC.select1 = ""
        NPC.select2 = ""
        NPC.select3 = ""
        NPC.Display()

class VendorItem (NPC):
    firstvisit = True
    localinventory = [Potion, HiPotion]
    def init():
        NPC.name = "Store - Going Alone"
        if VendorItem.firstvisit:
            NPC.firstvisit = True
            NPC.gmintro1 = Interactions.VendorGreeting
            VendorItem.firstvisit = False
        else:
            NPC.gmintro2 = Interactions.VendorGreeting
        NPC.inventory = VendorItem.localinventory
        NPC.option1 = "View wares"
        NPC.option2 = "-"
        NPC.option3 = "-"
        NPC.select1 = NPC.SaleDisplay
        NPC.select2 = ""
        NPC.select3 = ""
        NPC.Display()
