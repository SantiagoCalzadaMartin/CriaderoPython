class Terminal:

# Array de arrays que contiene las razas de perros, sus nombres y sus precios
    perros = [
        ["Pastor Aleman", "Max", 50],
        ["Bulldog Frances", "Princesa", 30],
        ["Chihuahua", "Deborador de mundos", 10],
        ["Dálmata", "Pancho", 20],
        ["Husky", "Epi", 25]
    ]

# El método ver_base_datos se encarga de leer el array y mostrar por terminal la "base de datos" de perros
    def ver_base_datos(self):
        print("\n" * 10)
        print("Base de datos:")
        R = "Raza"
        N = "Nombre"
        P = "Precio"
        print(R.ljust(25), N.ljust(25), P)
        print("-" * 60)
        for perro in self.perros:
            raza = perro[0]
            nombre = perro[1]
            precio = perro[2]
            print(raza.ljust(25), nombre.ljust(25), str(precio).ljust(10))
        print("\n" * 2)
        input("Pulsa Enter para continuar")

# El método añadir_datos se encarga de añadir un nuevo perro a la base de datos, pidiendole al usuario raza, nombre y precio
    def añadir_datos(self):
        self.ver_base_datos()
        raza = input("Ingresa la raza del perro: ")
        nombre = input("Ingresa el nuevo nombre del perro: ")
        precio = int(input("Ingresa el precio: "))
        if precio < 0:
            print("Precio introducido no aceptado")
        else:
            self.perros.append([raza, nombre, precio])
            print("Base de datos actualizada.")
            self.ver_base_datos()

# El método buscar_raza se encarga de encontrar todos los perros que son de la misma raza que ha dicho el usuario
    def buscar_raza(self):
        print("\n" * 10)
        raza = input("Dime la raza del perro: ")
        encontrado = False
        for perro in self.perros:
            if raza == perro[0]:
                raza = perro[0]
                nombre = perro[1]
                precio = perro[2]
                print("\n" * 10)
                print(raza.ljust(25), nombre.ljust(25), str(precio).ljust(10))
                encontrado = True
                print("\n" * 2)
                input("Pulsa Enter para continuar")
                print("\n" * 10)
        if not encontrado:
            print("No disponemos de esa raza")
            print("\n" * 2)
            input("Pulsa Enter para continuar")
            print("\n" * 10)

# El método actualizar_precio se encarga de buscar a un perro en específico por nombre y raza y actualizarle a este su precio al que diga el usuario
    def actualizar_precio(self):
        encontrado = False
        self.ver_base_datos()
        razaP = input("Dime la raza del perro: ")
        nombreP = input("Dime el nombre del perro: ")
        for perro in self.perros:
            if razaP == perro[0] and nombreP == perro[1]:
                precio = perro[2]
                print(razaP.ljust(25), nombreP.ljust(25), str(precio).ljust(10))
                nuevo_precio = int(input("Introduce el nuevo precio: "))
                if nuevo_precio < 0:
                    print("Precio introducido no aceptado")
                else:
                    perro[2] = nuevo_precio
                    print("Precio actualizado")
                    self.ver_base_datos()
                encontrado = True
        if not encontrado:
            print("No disponemos de esa raza")
            print("\n" * 2)
            input("Pulsa Enter para continuar")
            print("\n" * 10)

# El método buscar_por_precio se encarga de buscar un perro que este por debajo del umbral del precio introducido por el usuario
    def buscar_por_precio(self):
        self.ver_base_datos()
        encontrado = False
        precio_maximo = int(input("Introduce el precio máximo: "))
        print("\n" * 2)
        for perro in self.perros:
            if precio_maximo >= perro[2]:
                print(perro[0].ljust(25), perro[1].ljust(25), str(perro[2]).ljust(10))
                encontrado = True
        if not encontrado:
            print("No se encontró ningún perro con un precio igual o más bajo a", precio_maximo)
        print("\n")
        input("Pulsa Enter para continuar")
        print("\n" * 10)

# El método eliminar_producto se encarga de eliminar un perro que diga el usuario buscandolo por raza y nombre
    def eliminar_producto(self):
        razaElim = input("Dime la raza del perro que deseas eliminar: ")
        nombreElim = input("Dime el nombre del perro que deseas eliminar: ")
        encontrado = False
        for perro in self.perros:
            if nombreElim in perro and razaElim in perro:
                self.perros.remove(perro)
                self.ver_base_datos()
                encontrado = True
        if not encontrado:
            print("Perro no encontrado")
            print("\n")
            input("Pulsa Enter para continuar")
            print("\n" * 10)

# El método buscar_mas_caro se encarga de mostrar el perro más caro y el más barato de la base de datos
    def buscar_mas_caro(self):
        perro_mas_caro = self.perros[0]
        perro_mas_barato = self.perros[0]

        for perro in self.perros:
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

# El método valor_total se encarga de devolver cuanto vale en total el conjunto de todos los perros de la base de datos
    def valor_total(self):
        print("\n" * 10)
        total = 0
        for perro in self.perros:
            total += perro[2]
        print("El valor de la suma de todos los perros es " + str(total))
        print("\n" * 2)
        input("Pulsa Enter para continuar")
        print("\n" * 10)

# El método buscar_datos se encarga de englobar todos los metodos de busqueda de datos en un menú para que elija el usuario cual quiere utilizar
    def buscar_datos(self):
        print("\n" * 10)
        opcion = int(input("Elige la opción\n1- Mostrar todos\n2- Buscar por raza\n3- Buscar por precio\n4- Buscar mas caro y barato\n5- Mostrar valor total\n"))
        match opcion:
            case 1:
                self.ver_base_datos()
            case 2:
                self.buscar_raza()
            case 3:
                self.buscar_por_precio()
            case 4:
                self.buscar_mas_caro()
            case 5:
                self.valor_total()
            case _:
                print("Opción no válida")

# El método terminal engloba las opciones para que elija el usuario entre ver bases de datos, añadir un perro, actualizar precios o eliminar un perro.
    def terminal(self):
        fin = True
        while fin == True:
            print("\n" * 10)
            opcion = int(input("Elige la opción\n1- Mostrar datos\n2- Añadir perro\n3- Actualizar precio\n4- Eliminar productos del inventario\n5- Salir del programa\n"))
            match opcion:
                case 1:
                    self.buscar_datos()
                case 2:
                    self.añadir_datos()
                case 3:
                    self.actualizar_precio()
                case 4:
                    self.eliminar_producto()
                case 5:
                    print("Saliendo...")
                    fin == False
                    break
                case _:
                    print("Opción no válida, por favor intenta de nuevo.")