from fastapi import FastAPI, Request
from json import JSONDecodeError

from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from utils.dataUtils import addVehicle, getTypeCount, searchVehicle

app = FastAPI()
store = []

@app.get('/status')
def getStatus():
    return JSONResponse({'status' : 'online'})

@app.get('/vehicles/count')
def getStatus():
    return store[0].nbVehicles if len(store) > 0 else 0
    # dans ce cas on peut faire aussi 
    # return len(store)
    # mais j'imagine qu'il était attendu d'utiliser la variable globale de la classe mère

@app.get('/vehicles/count/{type}')
def getStatus(type : str):
    if type not in ["boat","plane","car","motorbike"]:
        return JSONResponse({'error' : f'the type {type} is not available'})
    return getTypeCount(type)
    
@app.get('/vehicles/search/{key}/{value}')
def getStatus(key : str,value : str):
    return searchVehicle(store,key,value)

@app.post('/vehicles')
async def postVehicle(request: Request):
    try:
        body = await request.json()
        type = body["type"].lower()
        if type not in ["boat","plane","car","motorbike"]:
            return JSONResponse({'error' : f'the type {type} is not available'})
        return addVehicle(store,type,body["data"])
    except JSONDecodeError:
        return JSONResponse({'error': 'il n y a pas de body pour executer le / les scripts'})
    except:
        return JSONResponse({'error': 'internal problem'})
    
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse({"error": "this page is not available"})