
from claseLista import Lista
from claseCarga import carga
from clasePasajeros import pasajeros


if __name__ == "__main__":
    listaV= Lista()
    print("INCISO 1 \n")
    vehiculo1 = carga("Ford", "Fiesta", "ABC123", 20000, 200, 800)
    listaV.agregarVehiculo(vehiculo1)
    vehiculo2 = pasajeros("Chevrolet", "Corsa", "MUP555", 30000, 200, 8)
    listaV.agregarVehiculo(vehiculo2)
    vehiculo3 = carga("Ford", "Focus", "NIB214", 25000, 250, 700)
    listaV.agregarVehiculo(vehiculo3)
    vehiculo4 = pasajeros("Mercedes Benz", "SL-500", "AA253BB", 40000, 500, 8)
    listaV.agregarVehiculo(vehiculo4)
    print("INCISO 2 \n")
    listaV.mostrarVehiculoPasajero()
    print("INCISO 3 \n")
    marca= input("Ingrese una Marca por Teclado: \n")
    listaV.contar(marca)
    print("Inciso 4 \n")
    listaV.mostrar()
    
    

