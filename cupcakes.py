from abc import ABC, abstractmethod
from pprint import pprint
import csv


class Cupcake(ABC):
    size = "regular"
    def __init__(self, name, flavor, frosting, price, filling):
        self.name = name
        self.flavor = flavor
        self.frosting = frosting
        self.price = price
        self.filling = filling
        self.sprinkles = []

    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)

    @abstractmethod 
    def calculate_price(self, quantity):
        return quantity * self.price

    def calculate_price(self, quantity):
        return quantity * self.price


class Regular(Cupcake):
    size = "regular"

class Mini(Cupcake):
    size = "mini"

    def __init__(self, name, flavor, frosting, price, filling):
        self.name = name
        self.flavor = flavor
        self.frosting = frosting
        self.price = price
        self.filling = filling
        self.sprinkles = []

class Large(Cupcake):
    size = "large"

    def __init__(self, name, flavor, frosting, price, filling):
        self.name = name
        self.flavor = flavor
        self.frosting = frosting
        self.price = price
        self.filling = filling
        self.sprinkles = []
favorite_cupcake = Cupcake("Classic", "Vanilla", "buttercream", 1.50, None)

favorite_cupcake.flavor = "Peanut Butter"
favorite_cupcake.name = "Reeses"
favorite_cupcake.add_sprinkles("Reeses chunks")
print(favorite_cupcake.sprinkles)

my_cupcake_mini = Mini("Classic", "Vanilla", "Whipped", 1.25, None)
print(my_cupcake_mini.flavor)
print(my_cupcake_mini.frosting)
print(my_cupcake_mini.size)

def read_csv(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            pprint(row)
        
read_csv("sample.csv")

cupcakes = []

def write_new_csv(file, cupcakes):
    with open(file, "w", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for cupcake in cupcakes:
            if hasattr(Cupcake, "filling"):
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles, "filling": cupcake.filling})
            else:
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})
            
write_new_csv("sample.csv", cupcakes)

def add_cupcake(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if hasattr(Cupcake, "filling"):
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles, "filling": cupcake.filling})
        else:
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})

def get_cupcakes(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        return reader

def find_cupcake(file, name):
    for cupcake in get_cupcakes(file):
        if cupcake["name"] == name:
            return cupcake
    return None

def add_cupcake_dictionary(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(cupcake)