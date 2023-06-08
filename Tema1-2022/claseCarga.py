from claseVehiculo import vehiculo

class carga(vehiculo):
    __peso: int
    
    def __init__(self, marca, modelo, patente, importeBasico, cantKm, pes):
        super().__init__(marca, modelo, patente, importeBasico, cantKm)
        self.__peso= pes
    
    def getPeso(self):
        return self.__peso
    def getTipo(self):
        return "Vehiculo de Carga"
    
    def ImporteTotal(self):
        importe=0
        
        if self.getCantKm() > 100:
            importe += (self.getImporteBasico() * 0.05) * (self.getCantKm()/10)
        if self.getPeso()> 500:
            importe += (self.getImporteBasico() * 0.10) * (self.getCantKm()/100)
        
        return importe
    
            