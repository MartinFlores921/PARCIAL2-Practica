class vehiculo:
    __marca: str
    __modelo: str
    __patente: str
    __importeBasico: int
    __cantKm: int
    
    def __init__(self, mar, mod, pat, imp, cantkilometros):
        self.__marca= mar
        self.__modelo= mod
        self.__patente= pat
        self.__importeBasico= imp
        self.__cantKm= cantkilometros
    
    
    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__modelo
    
    def getPatente(self):
        return self.__patente
    
    def getImporteBasico(self):
        return self.__importeBasico
    
    def getCantKm(self):
        return self.__cantKm
    
    def ImporteTotal():
        pass
    
    def getTipo():
        pass
    
    