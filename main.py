from Terminal import Terminal
from Interfaz import Interfaz

# La función main se encarga de englobar el menú de elección entre terminal e interfaz para elegir cual utilizar
def main():
    terminal = Terminal()
    interfaz = Interfaz()
    
    opcion = 0
    while opcion != 3:
        opcion = int(input("-----------------\n1- Terminal\n-----------------\n2- Interfaz\n-----------------\n3- Salir\n"))
        match opcion:
            case 1:
                terminal.terminal()
            case 2:
                interfaz.interfaz()
            case 3:
                print("Saliendo...")
            case _:
                print("Número no válido")

main()  