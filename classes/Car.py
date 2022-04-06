from classes.Vehicle import Vehicle

class Car(Vehicle):
    nbCar = 0
    def __init__(self,name,mark,maxSpeed,kms,motor):
        Vehicle.__init__(self,name,mark,maxSpeed,kms)
        self.motor = motor
        Car.nbCar += 1
        
    