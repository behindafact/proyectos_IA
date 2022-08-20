import string
import random

class InformacionVehiculo:
    
    def __init__(self, marca, electrico, precio_catalogo):
        self.marca = marca
        self.electrico = electrico
        self.precio_catalogo = precio_catalogo

    def calcular_impuesto(self):
        porcentaje_impuesto = 0.05
        if self.electrico:
            porcentaje_impuesto = 0.02
        return porcentaje_impuesto * self.precio_catalogo

    def print(self):
        print(f"Marca: {self.marca}")
        print(f"Impuesto a pagar: {self.calcular_impuesto()}")

class Vehiculo:

    def __init__(self, id, license_plate, info):
        self.id = id
        self.license_plate = license_plate
        self.info = info

    def print(self):
        print(f"Id: {self.id}")
        print(f"Placa vehiculo: {self.license_plate}")
        self.info.print()


class RegistroVehicular:

    def __init__(self):
        self.vehicle_info = { }
        self.agregar_inf_vehiculo("Tesla Model 3", True, 60000)
        self.agregar_inf_vehiculo("Volkswagen ID3", True, 35000)
        self.agregar_inf_vehiculo("BMW 5", False, 45000)
        self.agregar_inf_vehiculo("Tesla Model Y", True, 75000)

    def agregar_inf_vehiculo(self, marca, electrico, precio_catalogo):
        self.vehicle_info[marca] = InformacionVehiculo(marca, electrico, precio_catalogo)

    def generar_id_vehiculo(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generar_licencia_vehiculo(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

    def crear_vehiculo(self, marca):
        id = self.generar_id_vehiculo(12)
        license_plate = self.generar_licencia_vehiculo(id)
        return Vehiculo(id, license_plate, self.vehicle_info[marca])


class Aplicacion:

    def registrar_vehiculo(self, marca: string):
        # create a registry instance
        registry = RegistroVehicular()

        vehicle = registry.crear_vehiculo(marca)

        # print out the vehicle information
        vehicle.print()

app = Aplicacion()
app.registrar_vehiculo("Volkswagen ID3")
