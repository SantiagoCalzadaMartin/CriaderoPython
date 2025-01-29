
print("\n"*10)
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
    print("\n"*2)
    raza = input("Ingresa la raza del perro: ")
    nombre = input("Ingresa el nuevo nombre del perro: ")
    precio = int(input("Ingresa el precio: "))
    if(precio < 0):
        print("Precio introducido no aceptado")
    else:
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
            print("\n"*10)
            print(raza.ljust(25), nombre.ljust(25), str(precio).ljust(10))
            encotrado = True
            print("\n"*2)
            input("Pulsa Enter para continuar") 
            print("\n"*10)
    if encotrado == False:
        print("No disponemos de esa raza")
        print("\n"*2)
        input("Pulsa Enter para continuar") 
        print("\n"*10)

#Metodo para actualizar precios de perros que estan en la base de datos
def ActualizarPrecio():
    encotrado = False
    print("\n"*2)
    razaP = input("Dime la raza del perro: ")
    nombreP = input("Dime el nombre del perro: ")
    for perro in perros:
        if razaP == perro[0] and nombreP == perro[1]:
            precio = perro[2]
            print(razaP.ljust(25), nombreP.ljust(25), str(precio).ljust(10))
            NuevoPrecio = int(input("introduce el nuevo precio: "))
            if(NuevoPrecio < 0):
                 print("Precio introducido no aceptado")
            else:
                perro[2] = NuevoPrecio
                print("Precio actualizado")
            encotrado = True
    if encotrado == False:
        print("No disponemos de esa raza")
        print("\n"*2)
        input("Pulsa Enter para continuar") 
        print("\n"*10)

def BuscarPorPrecio():
    encontrado = False
    precioMaximo = int(input("Introduce en precio maximo: "))
    for perro in perros:
        if(precioMaximo >= perro[2]):
            print(perro[0].ljust(25), perro[1].ljust(25), str(perro[2]).ljust(10))
            encontrado = True
    
    if(encontrado == False):
        print("No se encontro ningun perro con un precio igual o mas bajo a ", precioMaximo)

def EliminarProducto(razaElim, nombreElim):
    print("\n")
    encontrado = False
    for perro in perros:
        if nombreElim in perro and razaElim in perro:
            perros.remove(perro)
            encontrado = True
    if encontrado == False:
        print("Perro no encontrado")
        print("\n")
        input("Pulsa Enter para continuar")
        print("\n"*10)

while opcion !=6:
    opcion = int(input("Elige la opción\n1- Ver base de datos\n2- Añadir perro\n3- Buscar un perro por raza\n4- Actualizar precio\n5- Buscar por precio\n6- Eliminar productos del inventario\n7- Salir del programa\n"))
    match opcion:
        
        case 1:
            VerBaseDatos()
        case 2:
            AñadirDatos()
        case 3:
            print("\n"*10)
            razaP = input("Dime la raza del perro: ")
            BuscarDatos(razaP)
        case 4:
            ActualizarPrecio()
        case 5:
            BuscarPorPrecio()
        case 6:
            print("\n"*10)
            razaElim = input("Dime la raza del perro que deseas eliminar: ")
            nombreElim = input("Dime el nombre del perro que deseas eliminar: ")
            EliminarProducto(razaElim, nombreElim)
        case 7:
            print("Saliendo...")
        case _:
            print("Opción no válida, por favor intenta de nuevo.")
