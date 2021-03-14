import xml.etree.ElementTree as ET


class XmlTags:
    def __init__(self):
        self.eatingOut = "EatingOut"
        self.eatingIn = "EatingIn"
        self.restaurant = "Restaurant"
        self.recipe = "Recipe"
        self.name = "name"
        self.cost = "cost"
        self.cookTime = "CookTime"
        self.ingredients = "Ingredients"
        self.ingredient = "Ingredients"
        self.link = "Link"
        self.units = "Units"
        self.quantity = "Quantity"
        self.cleanUpTime = "cleanUpTime"

class Meal:
    def __init__(self):
        self.cost = 0
        self.cleanUpTime = 0

class Ingredient:
    def __init__(self):
        self.name = "n/a"
        self.quantity = 0
        self.units = "n/a"

class EatingIn(Meal):
    def __init__(self):
        self.ingredients = []
        self.recipe = "no link"
        self.mealName = "n/a"   
        self.cookTime = 0

class EatingOut(Meal):
    def __init__(self):
        self.companyName = "n/a"

class XmlParser():
    def __init__(self, tags):
        self.root = None
        self.tree =  None
        self.tags = tags
    
    def OpenXml(self, f):
        self.tree = ET.parse(f)
        self.root = self.tree.getroot()
        
    def ParseForEatingOut(self, printData = False):
        for EatingOut in self.root.findall(self.tags.eatingOut):
            for restaurant in EatingOut.findall(self.tags.restaurant):
                name = restaurant.attrib.get(self.tags.name)
                cost = restaurant.attrib.get(self.tags.cost)
                cleanUpTime = restaurant.attrib.get(self.tags.cleanUpTime)
                
                if printData:
                    print("Restaurant: {0} \n\t Cost: {1} \n\t Clean Up Time: {2} \n".format(name, cost, cleanUpTime))
    
    def ParseForEatingIn(self, printData = False):
        for EatingIn in self.root.findall(self.tags.eatingIn):
            for recipe in EatingIn.findall(self.tags.recipe):
                name = recipe.attrib.get(self.tags.name)
                cost = recipe.attrib.get(self.tags.cost)
                cleanUpTime = recipe.attrib.get(self.tags.cleanUpTime)
                
                if printData:
                    print("Recipe: {0} \n\t Cost: {1} \n\t Clean Up Time: {2} \n".format(name, cost, cleanUpTime))


    def printAllRestaurants(self):
        self.ParseForEatingOut(True)
        
    def printAllRecipes(self):
            self.ParseForEatingIn(True)

    def Parse(self):
        for neighbor in self.root.iter('CleanUpTime'):
            print(neighbor.text)

    def GetMealOptions(self):
        options = []
        return options

class XmlGenerator:
    def __init__(self):
        pass

    def CreateRecipe(self):
        print("We are creating recipes")

def SelectOptions(options):
    #spawn a gui that allows the user to pick a certain number of food options
    pass

def PickWhatToEatRandom():
    print("Print something to eat")
    return "bullshit"

xmlTags = XmlTags()
parser = XmlParser(xmlTags)    
parser.OpenXml("recipes.xml")
#parser.OpenXml("countries.xml")
parser.ParseForEatingOut(True)
parser.ParseForEatingIn(True)
SelectOptions(parser.GetMealOptions())
option = PickWhatToEatRandom()
print(option)