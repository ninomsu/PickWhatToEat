import xml.etree.ElementTree as ET
#TODO
#Critera to ask user
#how quick do you want to eat
#how much do you want to spend per person, how many people?
#do you feel like cooking?

#have option for random food picker

#maybe add support for getting recipes from some api

#separte classes into separate files

#create gui
#supports the questions above
#lets you select the xml file
#lets you add recipes/restaruants
#lets you edit recipes/resaruants 


class XmlTags:
    def __init__(self):
        self.restaurant = "Restaurant"
        self.recipe = "Recipe"
        self.name = "name"
        self.cost = "cost"
        self.cookTime = "CookTime"
        self.ingredient = "Ingredient"
        self.link = "Link"
        self.units = "Units"
        self.quantity = "Quantity"
        self.cleanUpTime = "cleanUpTime"

class Meal:
    def __init__(self):
        self.name ="n/a"
        self.cost = 0
        self.cleanUpTime = 0

class Ingredient:
    def __init__(self):
        self.name = "n/a"
        self.quantity = 0
        self.units = "n/a"
    
    def Print(self):
        print("\n\t Ingredient: {0}  \
        \n\t Quantity: {1}  \
        \n\t Units: {2} \n".format(self.name, self.quantity, self.units))

class Recipe(Meal):
    def __init__(self):
        self.ingredients = []
        self.recipe = "no link"
        self.cookTime = 0
    
    def Print(self):
        print("Recipe: {0}  \
        \n\t Cost: {1}  \
        \n\t Clean Up Time: {2} \
        \n\t Link: {3} \
        \n\t Cook Time: {4} ".format(self.name, self.cost, self.cleanUpTime, self.link, self.cookTime))
        for ing in self.ingredients:
            ing.Print()

class Restaurant(Meal):
    def __init__(self):
        pass
    
    def Print(self):
        print("Restaurant: {0}  \
        \n\t Cost: {1}  \
        \n\t Clean Up Time: {2}".format(self.name, self.cost, self.cleanUpTime))

class XmlParser():
    def __init__(self, tags):
        self.root = None
        self.tree =  None
        self.tags = tags
    
    def OpenXml(self, f):
        self.tree = ET.parse(f)
        self.root = self.tree.getroot()
        
    def ParseForEatingOut(self, printData = False):
        restaurants = []
        for restaurantXml in self.root.findall(self.tags.restaurant):
            restaurant = Restaurant()
            restaurant.name = restaurantXml.attrib.get(self.tags.name)
            restaurant.cost = restaurantXml.attrib.get(self.tags.cost)
            restaurant.cleanUpTime = restaurantXml.attrib.get(self.tags.cleanUpTime)
            restaurants.append(restaurant)
        
        return restaurants
            
    def ParseForEatingIn(self, printData = False):
        recipes = []
        for recipeXml in self.root.findall(self.tags.recipe):
            recipe = Recipe()
            recipe.name = recipeXml.attrib.get(self.tags.name)
            recipe.cost = recipeXml.attrib.get(self.tags.cost)
            recipe.cleanUpTime = recipeXml.attrib.get(self.tags.cleanUpTime)
            recipe.link = recipeXml.find(self.tags.link).text
            recipe.cookTime = recipeXml.find(self.tags.cookTime).text
            for ingredientXml in recipeXml.findall(self.tags.ingredient):
                ingredient = Ingredient()
                ingredient.name = ingredientXml.attrib.get(self.tags.name)
                ingredient.quantity = ingredientXml.find(self.tags.quantity).text
                ingredient.units = ingredientXml.find(self.tags.units).text
                recipe.ingredients.append(ingredient)
            
            recipes.append(recipe)
        
        return recipes

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
restaurants = parser.ParseForEatingOut(True)
for x in restaurants:
    x.Print()

recipes = parser.ParseForEatingIn(True)
for x in recipes:
    x.Print()

SelectOptions(parser.GetMealOptions())
option = PickWhatToEatRandom()
print(option)