
print("\n"*10)
print("Bienvenido a PerriClub")

opcion = 1
perros = [
    ["Pastor Aleman", "Max",50],
    ["Bulldog Frances", "Princesa",30],
    ["Chihuahua", "Deborador de mundos",10],
    ["Dálmata", "Pancho",20],
    ["Husky", "Epi",25]
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
def BuscarRaza():
    print("\n"*10)
    raza = input("Dime la raza del perro: ")
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



#Metodo para buscar por un precio maximo
def BuscarPorPrecio():
    print("\n"*10)
    encontrado = False
    precioMaximo = int(input("Introduce en precio maximo: "))
    print("\n"*2)
    for perro in perros:
        if(precioMaximo >= perro[2]):
            print(perro[0].ljust(25), perro[1].ljust(25), str(perro[2]).ljust(10))
            encontrado = True
    
    if(encontrado == False):
        print("No se encontro ningun perro con un precio igual o mas bajo a ", precioMaximo)
    print("\n")
    input("Pulsa Enter para continuar")
    print("\n"*10)


#Metodo para eliminar un perro del array de perros
def EliminarProducto():
    print("\n"*10)
    razaElim = input("Dime la raza del perro que deseas eliminar: ")
    nombreElim = input("Dime el nombre del perro que deseas eliminar: ")
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


#Metodo para mostrar el perro mas caro y el mas barato
def BuscarMasCaro():
    perro_mas_caro = perros[0]
    perro_mas_barato = perros[0]

    for perro in perros:
        if perro[2] > perro_mas_caro[2]:
            perro_mas_caro = perro
        if perro[2] < perro_mas_barato[2]:
            perro_mas_barato = perro

    print("\n" * 10)
    print("Perro más caro:")
    print(perro_mas_caro[0].ljust(25), perro_mas_caro[1].ljust(25), str(perro_mas_caro[2]).ljust(10))

    print("\nPerro más barato:")
    print(perro_mas_barato[0].ljust(25), perro_mas_barato[1].ljust(25), str(perro_mas_barato[2]).ljust(10))

    print("\n" * 2)
    input("Pulsa Enter para continuar")
    print("\n" * 10)

#Metodo para ver el valor de todo el inventario
def ValorTotal():
    print("\n" * 10)
    total = 0
    for perro in perros:
        total += perro[2]
    
    print("El valor de la suma de todos los perros es " + str(total))
    print("\n" * 2)
    input("Pulsa Enter para continuar")
    print("\n" * 10)

        

#Metodo para dar opcion al usuario el que quiere mostrar
def BuscarDatos():
    print("\n"*10)
    opcion = int(input("Elige la opción\n1- Mostrar todos\n2- Buscar por raza\n3- Buscar por precio\n4- Buscar mas caro y barato\n5- Mostrar valor total\n"))
    match opcion:
        case 1:
            VerBaseDatos()
        case 2:
            BuscarRaza()
        case 3:
            BuscarPorPrecio()
        case 4:
            BuscarMasCaro()
        case 5:
            ValorTotal()
        case _:
            print("no se")
 
while opcion !=6:
    opcion = int(input("Elige la opción\n1- Mostrar datos\n2- Añadir perro\n3- Actualizar precio\n4- Eliminar productos del inventario\n5- Salir del programa\n"))
    match opcion:
        
        case 1:
            BuscarDatos()
        case 2:
            AñadirDatos()
        case 3:
            ActualizarPrecio()
        case 4:
            EliminarProducto()
        case 5:
            print("Saliendo...")
        case _:
            print("Opción no válida, por favor intenta de nuevo.")
