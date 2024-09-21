class Vehicle:
    def __init__(self, brand, model, price):
        #Encapsulación
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"El vehiculo {self.brand}. Ha sido vendido")
        else:
            print(f"El vehiculo {self.brand}. No está disponible")
    
    #Abstracción
    def check_available(self):
        return self.is_available
    
    #Abstracción
    def get_price(self):
        return self.price
    
    def start_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")
    
    def stop_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")


class Car(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"El motor del carro {self.brand} esta en marcha"
        else:
            return f"El carro {self.brand} no esta disponible"
        
    def stop_engine(self):
        if self.is_available:
            return f"El motor del carro {self.brand} se ha detenido"
        else:
            return f"El carro {self.brand} NO esta disponible"
        
class Bike(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"La bicleta {self.brand} esta en marcha"
        else:
            return f"La bicleta {self.brand} no esta disponible"
        
    def stop_engine(self):
        if self.is_available:
            return f"La bicleta {self.brand} se ha detenido"
        else:
            return f"La bicleta {self.brand} NO esta disponible"
        
class Truck(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"El motor del camión {self.brand} esta en marcha"
        else:
            return f"El camión {self.brand} no esta disponible"
        
    def stop_engine(self):
        if self.is_available:
            return f"El motor del camión {self.brand} se ha detenido"
        else:
            return f"El camión {self.brand} NO esta disponible"
        
class Customer:
    def __init__(self, name):
        self.name = name
        self.purchase_vehicles = []

    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            vehicle.sell()
            self.purchase_vehicles.append(vehicle)
        else:
            print(f"Lo siento, {vehicle.brand} no esta disponible")

    def inquire_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            availability = "Disponible"
        else:
            availability = "NO Disponible"
        print(f"{vehicle.brand} esta {availability} y cuesta {vehicle.get_price()}")

class Dealership:
    def __init__(self):
        self.inventory = []
        self.customer = []

    def add_vehicles(self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f"El {vehicle.brand} ha sido añadido al inventario")

    def register_customers(self, customer: Customer):
        self.customers.append(customer)
        print(f"El cliente {customer.name} ha sido añadido")

    def show_available_vehicle(self):
        print("Vehiculos disponibles a la tienda")
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f"- {vehicle.brand} por {vehicle.get_price()}")


car1 = Car("Toyota", "Corolla", 20000)
bike1 = Bike("Yamaha", "MT-07", 7000)
truck1 = Truck("Volvo", "FH16", 80000)

customer1 = Customer("Carlos")

dealearship = Dealership()
dealearship.add_vehicles(car1)
dealearship.add_vehicles(bike1)
dealearship.add_vehicles(truck1)

#Mostrar vehiculos disponibles
dealearship.show_available_vehicle()

#cliente consultar un vehiculo
customer1.inquire_vehicle(car1)

#Cliente comprar un vehiculo
customer1.buy_vehicle(car1)

#Mostrar vehiculos disponibles
dealearship.show_available_vehicle()
