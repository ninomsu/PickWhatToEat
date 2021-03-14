import xml.etree.ElementTree as ET

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
    def __init__(self):
        self.root = None
        self.tree =  None
    
    def OpenXml(self, f):
        self.tree = ET.parse(f)
        self.root = self.tree.getroot()
        
    
    def ParseForEatingIn(self):
        for recipe in self.root.findall('Recipes'):
            name = recipe.attrib
            cost = recipe.find('Cost').text
            cleanUpTime = recipe.get('CleanUpTime').text
            link = recipe.get('Link').text
            cookTime = recipe.get('CookTime').text

            print(name, cost, cleanUpTime, link, cookTime)


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
    print('pick')

def PickWhatToEatRandom():
    print("Print something to eat")
    return "bullshit"

parser = XmlParser()    
parser.OpenXml("recipes.xml")
parser.ParseForEatingIn()
SelectOptions(parser.GetMealOptions())
option = PickWhatToEatRandom()
print(option)