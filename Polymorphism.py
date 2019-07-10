class Animal:
    def makeNoise(self):
        raise NotImplementedError
    
class Cat(Animal):
    def makeNoise(self):
        print("Meoooowwwww")
        
class Dog(Animal):
    def makeNoise(self):
        print("Woooooof")
        
class Cow(Animal):
    def makeNoise(self):
        print("Mmmaaaaaaaaaa")
        
a = Cat();
a.makeNoise() 

a = Dog();
a.makeNoise()   

a = Cow();
a.makeNoise()    