from ScreenSystem import *
class Medic(Chat):
    def init():
        Chat.name = "Medic"
        Chat.greeting1 = "Hey there, nice to meet you"
        Chat.greeting2 = "Nice to see you again!"
        Chat.option1 = "-"
        Chat.option2 = "-"
        Chat.option3 = "-"
        ChatScreenSelect.option1 = ""
        Medic.Screen()
