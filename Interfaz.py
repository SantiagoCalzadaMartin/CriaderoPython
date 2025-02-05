import tkinter as tk

class Interfaz:

    perros = [
        ["Pastor Aleman", "Max", 50],
        ["Bulldog Frances", "Princesa", 30],
        ["Chihuahua", "Deborador de mundos", 10],
        ["Dálmata", "Pancho", 20],
        ["Husky", "Epi", 25]
    ]

    def Añadir_Perro(self):
        raza = str(self.Raza.get())
        nombre = str(self.Nombre.get())
        precio = int(self.Precio.get())

        if precio < 0:
            print("Precio introducido no aceptado")
        else:
            self.perros.append([raza, nombre, precio])
            print("Base de datos actualizada.")
            self.ver_base_datos()


    def VentanaAñadirPerro(self):
        ventana = tk.Tk()
        ventana.title("Añadir Perro")
        ventana.geometry("480x300")

        RazaT = tk.Label(ventana, text="Raza")
        RazaT.grid(row=0, column=0, pady=10)

        Raza = tk.Entry(ventana)
        Raza.grid(row=1, column=0, padx=10, pady=10)

        NombreT = tk.Label(ventana, text="Nombre")
        NombreT.grid(row=0, column=1, pady=10)

        Nombre = tk.Entry(ventana)
        Nombre.grid(row=1, column=1, padx=10, pady=10)

        PrecioT = tk.Label(ventana, text="Precio")
        PrecioT.grid(row=0, column=2, pady=10)

        Precio = tk.Entry(ventana)
        Precio.grid(row=1, column=2, padx=10, pady=10)

        boton_calc = tk.Button(ventana, text="Añadir", command=self.Añadir_Perro)
        boton_calc.grid(row=2, column=1, pady=10)

    def Ventana_Actualizar_Perro(self):
        print()

    def Ventana_Eliminar_Perro(self):
        print()

    def Ventana_Mostrar_Perro_Caro_Barato(self):
        print()

    def Salir(self):
        print()

    def interfaz(self):
        ventana = tk.Tk()
        ventana.title("PerriClub")
        ventana.geometry("270x300")

        resultado = tk.Label(ventana, text="PerriClub", font=("Arial", 25))
        resultado.grid(row=0, column=0, columnspan=2, pady=20)

        botonMostrar = tk.Button(ventana, text="Mostrar Datos", width=15)
        botonMostrar.grid(row=1, column=0, padx=10, pady=10)

        botonAñadir = tk.Button(ventana, text="Añadir perros", width=15, command=self.VentanaAñadirPerro)
        botonAñadir.grid(row=2, column=0, padx=10, pady=10)

        botonActualizarPrecio = tk.Button(ventana, text="Modificar precio", width=15)
        botonActualizarPrecio.grid(row=1, column=1, padx=10, pady=10)

        botonEliminar = tk.Button(ventana, text="Eliminar perro", width=15,)
        botonEliminar.grid(row=2, column=1, padx=10, pady=10)

        BuscarPrecio = tk.Button(ventana, text="Buscar por precio", width=15)
        BuscarPrecio.grid(row=3,column=0,padx=10,pady=10)

        buscarRaza = tk.Button(ventana,text="Buscar por raza", width=15)
        buscarRaza.grid(row=4,column=0,padx=10,pady=10)

        estadisticas = tk.Button(ventana,text="Estadisticas", width=15)
        estadisticas.grid(row=3,column=1,padx=10,pady=10)

        Salir = tk.Button(ventana,text=" Salir ", width=15)
        Salir.grid(row=4,column=1,padx=10,pady=10)

        ventana.mainloop()