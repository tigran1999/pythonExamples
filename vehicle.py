class Vehicle:
    def __init__(self,engine,hp):
        self.engine = engine
        self.hp = hp
    
    def getHp(self):
        return self.hp
        
    def getEngine(self):
        return self.engine

class Passenger(Vehicle):
    
    def __init__(self,engine,hp,passengerCount):
        super().__init__(engine,hp)
        self.passengerCount = passengerCount
        
    def getPassengetCount(self):
        return self.passengerCount
        
        
class Truck(Vehicle):
    
    def __init__(self,engine,hp,maxWeight):
        super().__init__(engine,hp)
        self.maxWeight = maxWeight
        
    def getMaxWeight(self):
        return self.maxWeight        
        
        
        
mercedes = Passenger("2.0 L",240,5)

print(mercedes.getHp())
print(mercedes.getEngine())
print(mercedes.getPassengetCount())


print("====================")

man = Truck("6.0 L",500,"50 t")

print(man.getHp())
print(man.getEngine())
print(man.getMaxWeight())

print("====================")

print(isinstance(mercedes, Vehicle))
print(isinstance(man, Truck))
print(isinstance(man, Passenger))
print(isinstance(mercedes, Passenger))






