class Diva:
        version = "v3"
        def __init__(self, name = "Diva"):
                self.name = name
        
        def song(self, title = "Song"):
                print(self.name + " sing the " + title)
        def medley(self):
                self.song()
                self.song("second song")
                self.song("third song")

class Child(Diva):
        def __init__(self, module = "class uniform"):
                self.module = module
                # Must set the superclass.
                # if not, can't use parameter "name"
                super().__init__("child")
        def dance(self):
                print("Dancing")

child = Child()
child.dance()
print(child.module)3
print(child.version)
child.medley()
