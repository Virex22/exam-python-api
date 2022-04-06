# rendu REMY Vincent

## route n°1

> get /status

## route n°2

> post /vehicles

avec le body suivant :
```
{
    "type" : "boat",
    "data" : {
        "name" : "name",
        "mark" : "mark",
        "maxSpeed" : "maxSpeed",
        "kms" : "kms",
        "nodePower" : "nodePower"
    }
}
```

## route n°3

> get /vehicles/count

## route n°4

> get /vehicles/count/{type}

## route n°5

> get /vehicles/search/{key}/{value}

avec les clés suivante :
- "name"
- "mark"
- "maxSpeed"
- "kms"