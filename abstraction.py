from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def get_sound(self):
        pass
    @abstractmethod
    def get_legs(self):
        pass
class lion(Animal):
    def get_sound(self):
        print("Roar")  
    def get_legs(self):
        print("4")      
class cow(Animal):
    def get_sound(self):
        print("Moo") 
    def get_legs(self):
       print("4")          
lion=lion()
cow=cow()
lion.get_sound()
cow.get_sound()
lion.get_legs()
cow.get_legs()


