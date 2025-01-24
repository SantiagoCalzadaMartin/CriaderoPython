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


#Metodo para buscar perros por raza
def BuscarDatos(raza):
    encotrado = False
    for perro in perros:
        if raza == perro[0]:
            raza = perro[0]
            nombre = perro[1]
            precio = perro[2]
            print(raza.ljust(25), nombre.ljust(25), str(precio).ljust(10))
            encotrado = True
    if encotrado == False:
        print("No disponemos de esa raza")

#Metodo para actualizar precios de perros que estan en la base de datos
def ActualizarPrecio():
    encotrado = False
    razaP = input("Dime la raza del perro: ")
    nombreP = input("Dime el nombre del perro: ")
    for perro in perros:
        if razaP == perro[0] and nombreP == perro[1]:
            precio = perro[2]
            print(razaP.ljust(25), nombreP.ljust(25), str(precio).ljust(10))
            NuevoPrecio = input("introduce el nuevo precio: ")
            perro[2] = NuevoPrecio
            print("Precio actualizado")
            encotrado = True
    if encotrado == False:
        print("No disponemos de esa raza")


while opcion !=5:
    opcion = int(input("Elige la opción\n1- Ver base de datos\n2- Añadir perro\n3- Buscar un perro por raza\n4- Actualizar precio\n5- Salir del programa\n"))
    match opcion:
        
        case 1:
            VerBaseDatos()
        case 2:
            AñadirDatos()
        case 3:
            razaP = input("Dime la raza del perro: ")
            BuscarDatos(razaP)
        case 4:
            ActualizarPrecio()
        case 5:
            print("Saliendo...")
        case _:
            print("Opción no válida, por favor intenta de nuevo.")
