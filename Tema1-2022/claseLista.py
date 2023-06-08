from claseNodo import Nodo
from clasePasajeros import pasajeros
from claseCarga import carga
class Lista:
    __comienzo: Nodo
    __actual: Nodo
    __indice: int
    __tope: int
    
    
    def __init__(self):
        self.__comienzo= None
        self.__actual= None
        self.__indice=0
        self.__tope=0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice=0
            raise StopIteration
        
        else:
            self.__indice +=1
            dato= self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato
    
    
    def agregarVehiculo(self, vehiculo):
        nodo= Nodo(vehiculo)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo= nodo
        self.__actual= nodo
        self.__tope +=1
    
    
    def mostrarVehiculoPasajero(self):
       aux= self.__comienzo
       i=0
       while aux != None and i <= self.__tope:
           if isinstance(aux.getDato(), pasajeros):
               if aux.getDato().getCantAsientos() > 6:
                   print("Vehiculo con Marca: {}, Modelo: {}, Patente:{}, Importe:{}, CantKm: {}".format(aux.getDato().getMarca(), aux.getDato().getModelo(), aux.getDato().getPatente(), aux.getDato().getImporteBasico(), aux.getDato().getCantKm()))
                  # print(aux.getDato())
           aux  = aux.getSiguiente()
           i +=1
    
    
    def contar(self, marca):
        aux= self.__comienzo
        c=0
        i=0
        while aux != None and i <= self.__tope:
            if isinstance(aux.getDato(), carga):
                if aux.getDato().getMarca() == marca:
                    c += 1
            
            aux= aux.getSiguiente()
            i +=1
        print("La cantidad de autos con la marca ingresada es: {}".format(c))
    
    
    def mostrar(self):
        aux= self.__comienzo
        i=0
        #print("Marca:   \t Modelo:  \t\tPatente:  \t\t\tTipoVehiculo:  \t\t\t\tTotalAlquiler: \t\t\t\t\t")
        while aux != None and i <= self.__tope:
            #print("{} \t{}")
            print("Marca: {}  \t Modelo: {}  t\tTipoVehiculo:{}  t\t\tTotalAlquiler:{} ".format(aux.getDato().getMarca(), aux.getDato().getModelo(), aux.getDato().getTipo(), aux.getDato().getImporteBasico()))
            i+=1
            aux= aux.getSiguiente()
        
            
        
        
            
    
            
        