class character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

goodguy = character ("goodguy", 200)
badguy = character ("badguy", 200)

class Item:
    def __init__(self, name, effect, action, actionlevel, damage, hits, value):
        self.name = name
        self.effect = effect
        self.action = action
        self.actionlevel = actionlevel
        self.damage = damage
        self.hits = hits
        self.value = value

#stick all the available item functions in here 
class ItemEffects(Item):    
    def HPBuff():
        itemsystem.target.hp += itemsystem.selecteditem.actionlevel * itemsystem.selecteditem.damage
    def HPDeBuff():
        itemsystem.target.hp -= itemsystem.selecteditem.actionlevel * itemsystem.selecteditem.damage

# containing all of the available item functions within one object that can be called on by the items negates the need for SELF and also negates each item storing all the available functions which is better for app performance 

ItemEffectsList = ItemEffects


#so now we create instances of items where the item's action is determined as one of the itemeffectslist object's functions. 

potion = Item ("Potion","HP Buff", ItemEffectsList.HPBuff, 2, 15, 1, 20)
badpotion = Item ("Potion","HP Damage", ItemEffectsList.HPDeBuff, 2, 15, 1, 20)

#item system facsimile. using this instead of battle system function allows it to be called from inside or outside of combat making it agnostic to player location. this pretends that all of the 'list items, let player select items' stuff has been done already. also includes an if statement which will be used to determine whether the item selects friendly or enemy characters.
class itemsystem:
    selecteditem = ""
    target = ""
    def function():    
        if "Damage" in itemsystem.selecteditem.effect:
            itemsystem.target = badguy
            itemsystem.selecteditem.action()
        elif "Buff" in itemsystem.selecteditem.effect:
            itemsystem.target = goodguy
            itemsystem.selecteditem.action()
        else:
            print("you messed up your code here. ")

itemsystem.selecteditem = potion
itemsystem.function()

print  (itemsystem.target.name)
print (itemsystem.target.hp)