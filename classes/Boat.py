from classes.Vehicle import Vehicle

class Boat(Vehicle):
    nbBoat = 0
    def __init__(self,name,mark,maxSpeed,kms,nodePower):
        Vehicle.__init__(self,name,mark,maxSpeed,kms)
        self.nodePower = nodePower
        Boat.nbBoat += 1