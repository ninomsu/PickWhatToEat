import xml.etree.ElementTree as ET
import random
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
    
    def Print(self):
        print("Meal: {0}  \
        \n\t Cost: {1}  \
        \n\t Clean Up Time: {2}".format(self.name, self.cost, self.cleanUpTime))
        print(" ")


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
        print(" ")

class Restaurant(Meal):
    def __init__(self):
        pass
    
    def Print(self):
        print("Restaurant: {0}  \
        \n\t Cost: {1}  \
        \n\t Clean Up Time: {2}".format(self.name, self.cost, self.cleanUpTime))
        print(" ")

class XmlHandler():
    def __init__(self, tags):
        self.root = None
        self.tree =  None
        self.tags = tags
    
    def OpenXml(self, f):
        self.tree = ET.parse(f)
        self.root = self.tree.getroot()
        
    def ParseForEatingOut(self):
        restaurants = []
        for restaurantXml in self.root.findall(self.tags.restaurant):
            restaurant = Restaurant()
            restaurant.name = restaurantXml.attrib.get(self.tags.name)
            restaurant.cost = restaurantXml.attrib.get(self.tags.cost)
            restaurant.cleanUpTime = restaurantXml.attrib.get(self.tags.cleanUpTime)
            restaurants.append(restaurant)
        
        return restaurants
            
    def ParseForEatingIn(self):
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
    
    def CreateDocument(self):
        print("Creating Xml Document for Meals")

    def AddRecipe(self):
        print("We are creating recipes")


    def AddRestaurant(self):
        print("We are adding Restaurant")
    
    def EditRecipe(self, name):

      #  topic=self.root.find(".//*[@topic='Salmon and Green Asparagus']").text
       # print(topic)
#        print(self.root.find(".//*[@name="+ name + "'/1']").text)
        print("We are editing an exisitng recipe")

    def EditRestaurant(self):
        print("We are editing an existing restaurant")   


def SelectOptions(options):
    #spawn a gui that allows the user to pick a certain number of food options
    pass

def PickWhatToEatRandom(meals):
    random.random()
    option = random.randrange(len(meals)-1)
    print("\nYour randomly selected meal for the night is: \
        \n===================================================")
    meals[option].Print()

xmlTags = XmlTags()
handler = XmlHandler(xmlTags)    
handler.OpenXml("recipes.xml")
#handler.OpenXml("countries.xml")
restaurants = handler.ParseForEatingOut()
for x in restaurants:
    x.Print()

recipes = handler.ParseForEatingIn()
for x in recipes:
    x.Print()

meals = []
meals += restaurants
meals += recipes

SelectOptions(meals)
PickWhatToEatRandom(meals)
handler.EditRecipe("Salmon and Green Asparagus")
