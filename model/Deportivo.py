from model.Vehiculo import Vehiculo

class Deportivo(Vehiculo):    
    def __init__(self, marca, modelo, anio, velocidad_max):
        super().__init__(marca, modelo, anio)
        self.velocidad_max = velocidad_max
    
    def descripcion(self):
        return f"{super().descripcion()}, Velocidad: {self.velocidad_max}"
