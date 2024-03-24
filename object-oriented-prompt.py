# Watto needs a new system for organizing his inventory of podracers.
# Help him do this by implementing an Object Oriented solution according to the following criteria.
# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes.
# Define a repair() method that will update the condition of the podracer to "repaired".
# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
# Define another class that inherits Podracer and call this one SebulbasPod.
# This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".

class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "repaired"

class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def boost(self):
        self.max_speed * 2

class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def flame_jet(self, other):
        other.condition = "trashed"

pod1 = Podracer(50, "perfect", 100)
pod2 = AnakinsPod(50, "perfect", 100)
pod3 = SebulbasPod(50, "perfect", 100)

print(pod1.condition)
pod1.repair()
print(pod1.condition)

print(pod2.max_speed)
pod2.boost()
print(pod2.max_speed)

print(pod3.condition)
pod3.flame_jet(pod1)
print(pod1.condition)