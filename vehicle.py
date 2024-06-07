class Vehicle:
    def __init__(self,make,color):
        self.make = make
        self.color = color
    
    def accelerate(self):
        print("Acceleration start")

    def hoot(self):
        print("honk honk")

class Bus(Vehicle):
    def __init__(self,make,color,passenger):
        super().__init__(make,color)
        self.passenger = passenger

    def start_boarding(self):
       print("The bus is boarding")

class Lorry(Vehicle):
    def __init__(self, make, color,max_load):
        super().__init__(make, color)
        self.max_load = max_load

    def unload(self):
        print("unloading")

class Food :
    def __init__(self, ingredients, types) :
        self.methods = ingredients
        self.types = types

    def displayfood(self):
        print("This food is called biryani")
    
class Zimbabwe(Food):
    def __init__(self, ingredients, types,time) :
        super().__init__(ingredients,types)
        self.time = time

    def cooking(self):
        print("This food takes,self.types,self.ingredients,self.time")
       
y = Zimbabwe(["Tomato","Onion","Cassava"],"Traditional","8:00pm")
y.cooking()




        
