numbers = {1: "uno", 2: "dos", 3: "tres"}
print(numbers)
print(numbers[2])
information = {"nombre": "Jairo",
               "apellido": "Chacon",
               "altura": 1.70,
               "edad": 36}
print(information)
del information ["edad"]
print(information)
llaves = information.keys()
print(llaves)
print(type(llaves))
values = information.values()
print(values)
pairs = information.items()
print(pairs)
contacts = {"Jairo": {"apellido": "Chacon",
               "altura": 1.70,
               "edad": 36},
            "Angel": {"apellido": "Cordova",
               "altura": 1.60,
               "edad": 20}} 
print(contacts)
print(contacts["Angel"])