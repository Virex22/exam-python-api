from classes.Vehicle import Vehicle

class Plane(Vehicle):
    nbPlane = 0
    def __init__(self,name,mark,maxSpeed,kms,airResistance,nbOfPassengers):
        Vehicle.__init__(self,name,mark,maxSpeed,kms)
        self.airResistance = airResistance
        self.nbOfPassengers = nbOfPassengers
        Plane.nbPlane += 1