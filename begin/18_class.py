"""
Class: Attributes + Methods

特性： 封装，继承，多态

下划线命名法：适用于变量名
Pascal命名法：适用于类名
"""

class CuteCat:
    def __init__(self, cat_name, cat_age, cat_color):
        self.name = cat_name
        self.age = cat_age
        self.color = cat_color
    def speak(self):
        print("miao" * self.age)
    def think(self, content):
        print(f"The {self.color} cat {self.name} is think about {content}.")

cat_1 = CuteCat("Jojo", 2, "red")
print(f"The cute cat name is {cat_1.name}, age is {cat_1.age}, color is {cat_1.color}.")
cat_1.speak()
cat_1.think("playing with dog")

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(f"The restaurant name is {self.name}, cuisine type is {self.type}.")

    def open_restaurant(self):
        print(f"The restaurant {self.name} is open.")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment_number):
        self.number_served += increment_number

kfc = Restaurant("KFC", "fast food")
print(kfc.name)
print(kfc.type)
print(kfc.number_served)
kfc.describe_restaurant()
kfc.open_restaurant()
kfc.set_number_served(100)
kfc.increment_number_served(20)
print(kfc.number_served)