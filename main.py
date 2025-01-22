print("Bienvenido a PerriClub")


opcion = 1
perros = [
    ["Pastor Aleman", "Max",20],
    ["Bulldog Frances", "Princesa",20],
    ["Chihuahua", "Deborador de mundos",20],
    ["Dálmata", "Pancho",20],
    ["Husky", "Epi",20]
]

# Metodos para ver la tabla de la base de datos, la tabla de perros
def VerBaseDatos():
    print("\n"*10)
    print("Base de datos:")
    R = "Raza"
    N = "Nombre"
    P = "Precio"
    print(R.ljust(25),N.ljust(25),P)
    print("-" * 60)
    for perro in perros:
        raza = perro[0]
        nombre = perro[1]
        precio = perro[2]
        print(raza.ljust(25), nombre.ljust(25), str(precio).ljust(10))
    print("\n"*2)
    input("Pulsa Enter para continuar") 
    print("\n"*10)


#Metodo para añadir datos al array de perros
def AñadirDatos():
    raza = input("Ingresa la raza del perro: ")
    nombre = input("Ingresa el nuevo nombre del perro: ")
    precio = input("Ingresa el precio: ")
    perros.append([raza,nombre,precio])
    print("Base de datos actualizada.")
    VerBaseDatos()



while opcion !=3:
    opcion = int(input("Elige la opción\n1- Ver base de datos\n2- Modificar base de datos\n3- Salir del programa\n"))
    match opcion:
        
        case 1:
            VerBaseDatos()
        case 2:
            AñadirDatos()
        case 3:
            print("Saliendo...")
        case _:
            print("Opción no válida, por favor intenta de nuevo.")
