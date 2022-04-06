from classes.Vehicle import Vehicle

class Motorbike(Vehicle):
    nbMotorbike = 0
    def __init__(self,name,mark,maxSpeed,kms,motor,nbWheel):
        Vehicle.__init__(self,name,mark,maxSpeed,kms)
        self.motor = motor
        self.nbWheel = nbWheel
        Motorbike.nbMotorbike += 1