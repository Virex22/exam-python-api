from fastapi.responses import JSONResponse

from classes.Car import Car
from classes.Plane import Plane
from classes.Boat import Boat
from classes.Motorbike import Motorbike

def addVehicle(store,type,datas):
    try:
        if type == "car":
            store.append(Car(datas["name"],datas["mark"],datas["maxSpeed"],datas["kms"],datas["motor"]))
        elif type == "plane":
            store.append(Plane(datas["name"],datas["mark"],datas["maxSpeed"],datas["kms"],datas["airResistance"],datas["nbOfPassengers"]))
        elif type == "boat":
            store.append(Boat(datas["name"],datas["mark"],datas["maxSpeed"],datas["kms"],datas["nodePower"]))
        elif type == "motorbike":
            store.append(Motorbike(datas["name"],datas["mark"],datas["maxSpeed"],datas["kms"],datas["motor"],datas["nbWheel"]))
    except Exception as e:
        return JSONResponse({'error': f'given datas for type {type} is not compliant'})
    else:
        return JSONResponse({'success': 'the data sent are well saved'})

def getTypeCount(type):
    if type == "car":
       return JSONResponse({'count' : Car.nbCar})
    elif type == "plane":
       return JSONResponse({'count' : Plane.nbPlane})
    elif type == "boat":
       return JSONResponse({'count' : Boat.nbBoat})
    elif type == "motorbike":
       return JSONResponse({'count' : Motorbike.nbMotorbike})

def searchVehicle(store,key,value):
    try:
        data = []
        assert key in ["name","mark","maxSpeed","kms"]
        for vehicle in store:
            if key == "name":
                if vehicle.name == value:
                    data.append(vars(vehicle))
            elif key == "mark":
                if vehicle.mark == value:
                    data.append(vars(vehicle))
            elif key == "maxSpeed":
                if vehicle.maxSpeed == value:
                    data.append(vars(vehicle))
            elif key == "kms" :
                if vehicle.kms == value:
                    data.append(vars(vehicle))
        return JSONResponse({'result' : data})
    except:
        return JSONResponse({'error' : "key not available or internal error"})
    