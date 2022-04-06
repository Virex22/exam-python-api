# je fait les properties juste dans cette classe
class Vehicle:
    nbVehicles = 0
    def __init__(self,name,mark,maxSpeed,kms):
        self._name = name
        self._mark = mark
        self._maxSpeed = maxSpeed
        self._kms = kms
        Vehicle.nbVehicles += 1
        
    def _setName(self,name):
        self._name = name
    def _getName(self):
        return self._name
        
    def _setMark(self,mark):
        self._mark = mark
    def _getMark(self):
        return self._mark
        
    def _setMaxSpeed(self,maxSpeed):
        self._maxSpeed = maxSpeed
    def _getMaxSpeed(self):
        return self._maxSpeed
        
    def _setKms(self,kms):
        self._kms = kms
    def _getKms(self):
        return self._kms

    kms = property(_getKms,_setKms)
    maxSpeed = property(_getMaxSpeed,_setMaxSpeed)
    mark = property(_getMark,_setMark)
    name = property(_getName,_setName)

    