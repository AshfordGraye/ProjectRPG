import collections 

class thing:
    def __init__(self, name):
        self.name = name



item = thing("item")

list = collections.Counter()

list [item] += 1

for count in list:
    print (f"{list[count]} x {count.name}")