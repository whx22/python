class Mammal:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self.num_eyes = 2

    def breathe(self):
        print(f"{self.name} is breathing...")

    def poop(self):
        print(f"{self.name} is pooping...")

class Human(Mammal):
    def __init__(self, name, sex):
        super().__init__(name, sex)
        self.has_tail = False

    def read(self):
        print(f"{self.name} is reading...")

class Cat(Mammal):
    def __init__(self, name, sex):
        super().__init__(name, sex)
        self.has_tail = True

    def scratch_sofa(self):
        print(f"{self.name} is scratching sofa...")

    def poop(self):
        print(f"{self.name} is poop on washroom...")

human_1 = Human("Wang", "man")
human_1.breathe()
human_1.poop()
human_1.read()

cat_1 = Cat("huxin", "woman")
cat_1.breathe()
cat_1.scratch_sofa()
cat_1.poop()