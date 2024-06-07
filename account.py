

class Account:
    def __init__(self,number,pin ):
        self.number=number
        self.__pin=pin
        self.__balance=0
    def check_balance(self,pin):
        if pin==self.__pin:
            return self.__balance
        else:
            return "Wrong pin"


class Recipe:
    def __init__(self, title, ingredients, preparation_time, cooking_method, nutritional_info):
        self.title = title
        self.ingredients = ingredients
        self.preparation_time = preparation_time
        self.cooking_method = cooking_method
        self.nutritional_info = nutritional_info

    def display_recipe(self):
        print(f"Title: {self.title}")
        print(f"Ingredients: {', '.join(self.ingredients)}")
        print(f"Preparation Time: {self.preparation_time} minutes")
        print(f"Cooking Method: {self.cooking_method}")
        print(f"Nutritional Info: {self.nutritional_info}")

# Subclasses for specific African cuisines
class MoroccanRecipe(Recipe):
    def __init__(self, title, ingredients, preparation_time, cooking_method, nutritional_info, spice_level):
        super().__init__(title, ingredients, preparation_time, cooking_method, nutritional_info)
        self.spice_level = spice_level

    def display_additional_info(self):
        print(f"Spice Level: {self.spice_level}")

class EthiopianRecipe(Recipe):
    def __init__(self, title, ingredients, preparation_time, cooking_method, nutritional_info, type_of_spice):
        super().__init__(title, ingredients, preparation_time, cooking_method, nutritional_info)
        self.type_of_spice = type_of_spice

    def display_additional_info(self):
        print(f"Type of Spice: {self.type_of_spice}")

class NigerianRecipe(Recipe):
    def __init__(self, title, ingredients, preparation_time, cooking_method, nutritional_info, main_protein):
        super().__init__(title, ingredients, preparation_time, cooking_method, nutritional_info)
        self.main_protein = main_protein

    def display_additional_info(self):
        print(f"Main Protein: {self.main_protein}")

