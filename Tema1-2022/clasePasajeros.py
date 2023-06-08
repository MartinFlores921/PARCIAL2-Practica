from claseVehiculo import vehiculo

class pasajeros(vehiculo):
    __cantAsientos: int
    
    def __init__(self, marca, modelo, patente, importeBasico, cantKm, cantA):
        super().__init__(marca, modelo, patente, importeBasico, cantKm)
        self.__cantAsientos= cantA
        
    def getCantAsientos(self):
        return self.__cantAsientos
    def getTipo(self):
        return "Vehiculo de Transporte"
    
    def ImporteTotal(self):
        imp=0
        if self.getCantKm() > 100:
            imp += (self.getImporteBasico() * 0.01) * (self.getCantKm()/10)
        
        if self.getCantAsientos() < 4:
            imp += (self.getImporteBasico()*0.01)
        
        return imp
    
    
        