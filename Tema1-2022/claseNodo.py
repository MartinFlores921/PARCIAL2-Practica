from claseVehiculo import vehiculo
from clasePasajeros import pasajeros
from claseCarga import carga
class Nodo:
    __Vehiculo: vehiculo
    __siguiente: object
    
    
    def __init__(self,vehiculo):
        self.__Vehiculo= vehiculo
        self.__siguiente= None
    
    
    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente
    
    
    def getSiguiente(self):
        return self.__siguiente
    
    def getDato(self):
        return self.__Vehiculo
    
    

    