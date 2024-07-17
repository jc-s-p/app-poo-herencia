from model.Vehiculo import Vehiculo

class Furgoneta(Vehiculo):
    def __init__(self, marca, modelo, anio, volumenCarga):
        super().__init__(marca, modelo, anio)
        self.volumenCarga = volumenCarga
    
    def descripcion(self):
        return f"{super().descripcion()}, Nro de pasajeros {self.volumenCarga}"