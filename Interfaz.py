import tkinter as tk
from tkinter import messagebox

class Interfaz:

    perros = [
        ["Pastor Aleman", "Max", 50],
        ["Bulldog Frances", "Princesa", 30],
        ["Chihuahua", "Deborador de mundos", 10],
        ["Dálmata", "Pancho", 20],
        ["Husky", "Epi", 25]
    ]

    def Añadir_Perro(self):
        raza = self.Raza.get()
        nombre = self.Nombre.get()
        try:
            precio = int(self.Precio.get())
        except ValueError:
            error = tk.Label(self.ventana, text="Error: Precio debe ser un número", fg="red")
            error.grid(row=3, column=1, padx=10, pady=10)
            return

        if precio < 0:
            error = tk.Label(self.ventana, text="Error: Precio no aceptable", fg="red")
            error.grid(row=3, column=1, padx=10, pady=10)
        else:
            self.perros.append([raza, nombre, precio])
            exito = tk.Label(self.ventana, text="Perro añadido con éxito", fg="green")
            exito.grid(row=3, column=1, padx=10, pady=10)


    def Ventana_Añadir_Perro(self):
        self.ventana = tk.Toplevel()
        self.ventana.title("Añadir Perro Ventana")
        self.ventana.geometry("480x300")

        tk.Label(self.ventana, text="Raza").grid(row=0, column=0, pady=10)
        self.Raza = tk.Entry(self.ventana)
        self.Raza.grid(row=1, column=0, padx=10, pady=10)

        tk.Label(self.ventana, text="Nombre").grid(row=0, column=1, pady=10)
        self.Nombre = tk.Entry(self.ventana)
        self.Nombre.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.ventana, text="Precio").grid(row=0, column=2, pady=10)
        self.Precio = tk.Entry(self.ventana)
        self.Precio.grid(row=1, column=2, padx=10, pady=10)

        tk.Button(self.ventana, text="Añadir", command=self.Añadir_Perro).grid(row=2, column=1, pady=10)

    def Ventana_Actualizar_Perro(self):
        self.ventana_actualizar = tk.Toplevel()
        self.ventana_actualizar.title("Actualizar Precio")
        self.ventana_actualizar.geometry("400x250")

        tk.Label(self.ventana_actualizar, text="Raza").grid(row=0, column=0, pady=10)
        self.raza_update = tk.Entry(self.ventana_actualizar)
        self.raza_update.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.ventana_actualizar, text="Nombre").grid(row=1, column=0, pady=10)
        self.nombre_update = tk.Entry(self.ventana_actualizar)
        self.nombre_update.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.ventana_actualizar, text="Nuevo Precio").grid(row=2, column=0, pady=10)
        self.precio_update = tk.Entry(self.ventana_actualizar)
        self.precio_update.grid(row=2, column=1, padx=10, pady=10)

        self.mensaje_actualizar = tk.Label(self.ventana_actualizar, text="", fg="red")
        self.mensaje_actualizar.grid(row=4, column=0, columnspan=2, pady=10)

        tk.Button(self.ventana_actualizar, text="Actualizar", command=self.Actualizar_Precio).grid(row=3, column=1, pady=10)

    def Actualizar_Precio(self):
        raza = self.raza_update.get()
        nombre = self.nombre_update.get()
        try:
            nuevo_precio = int(self.precio_update.get())
        except ValueError:
            self.mensaje_actualizar.config(text="Error: El precio debe ser un número", fg="red")
            return

        for perro in self.perros:
            if perro[0] == raza and perro[1] == nombre:
                perro[2] = nuevo_precio
                self.mensaje_actualizar.config(text="Precio actualizado correctamente", fg="green")
                return

        self.mensaje_actualizar.config(text="Error: Perro no encontrado", fg="red")

    def Ventana_Eliminar_Perro(self):
        self.ventana_eliminar = tk.Toplevel()
        self.ventana_eliminar.title("Eliminar Perro")
        self.ventana_eliminar.geometry("400x200")

        tk.Label(self.ventana_eliminar, text="Raza").grid(row=0, column=0, pady=10)
        self.raza_eliminar = tk.Entry(self.ventana_eliminar)
        self.raza_eliminar.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.ventana_eliminar, text="Nombre").grid(row=1, column=0, pady=10)
        self.nombre_eliminar = tk.Entry(self.ventana_eliminar)
        self.nombre_eliminar.grid(row=1, column=1, padx=10, pady=10)

        self.mensaje_eliminar = tk.Label(self.ventana_eliminar, text="", fg="red")
        self.mensaje_eliminar.grid(row=3, column=0, columnspan=2, pady=10)

        tk.Button(self.ventana_eliminar, text="Eliminar", command=self.Eliminar_Perro).grid(row=2, column=1, pady=10)

    def Eliminar_Perro(self):
        raza = self.raza_eliminar.get()
        nombre = self.nombre_eliminar.get()
        for perro in self.perros:
            if perro[0] == raza and perro[1] == nombre:
                self.perros.remove(perro)
                self.mensaje_eliminar.config(text="Perro eliminado correctamente", fg="green")
                return

        self.mensaje_eliminar.config(text="Error: Perro no encontrado", fg="red")

    def Ventana_Mostrar_Perro_Caro_Barato(self):
        self.ventana_mostrar = tk.Toplevel()
        self.ventana_mostrar.title("Perro más caro y más barato")
        self.ventana_mostrar.geometry("400x200")

        if not self.perros:
            tk.Label(self.ventana_mostrar, text="No hay perros registrados", fg="red").pack(pady=10)
            return

        perro_mas_caro = max(self.perros, key=lambda p: p[2])
        perro_mas_barato = min(self.perros, key=lambda p: p[2])

        info = f"Perro más caro: {perro_mas_caro[1]} ({perro_mas_caro[0]}) - ${perro_mas_caro[2]}\n"
        info += f"Perro más barato: {perro_mas_barato[1]} ({perro_mas_barato[0]}) - ${perro_mas_barato[2]}"

        tk.Label(self.ventana_mostrar, text=info, fg="blue").pack(pady=10)

    def Salir(self):
        self.ventana.destroy()


    def interfaz(self):
        self.ventana = tk.Tk()
        self.ventana.title("PerriClub")
        self.ventana.geometry("270x300")

        resultado = tk.Label(self.ventana, text="PerriClub", font=("Arial", 25))
        resultado.grid(row=0, column=0, columnspan=2, pady=20)

        botonMostrar = tk.Button(self.ventana, text="Mostrar Datos", width=15, )
        botonMostrar.grid(row=1, column=0, padx=10, pady=10)

        botonAñadir = tk.Button(self.ventana, text="Añadir perros", width=15, command=self.Ventana_Añadir_Perro)
        botonAñadir.grid(row=2, column=0, padx=10, pady=10)

        botonActualizarPrecio = tk.Button(self.ventana, text="Modificar precio", width=15, command=self.Ventana_Actualizar_Perro)
        botonActualizarPrecio.grid(row=1, column=1, padx=10, pady=10)

        botonEliminar = tk.Button(self.ventana, text="Eliminar perro", width=15, command=self.Ventana_Eliminar_Perro)
        botonEliminar.grid(row=2, column=1, padx=10, pady=10)

        BuscarPrecio = tk.Button(self.ventana, text="Buscar por precio", width=15, )
        BuscarPrecio.grid(row=3,column=0,padx=10,pady=10)

        buscarRaza = tk.Button(self.ventana,text="Buscar por raza", width=15, )
        buscarRaza.grid(row=4,column=0,padx=10,pady=10)

        estadisticas = tk.Button(self.ventana,text="Estadisticas", width=15, command=self.Ventana_Mostrar_Perro_Caro_Barato)
        estadisticas.grid(row=3,column=1,padx=10,pady=10)

        Salir = tk.Button(self.ventana,text=" Salir ", width=15, command=self.Salir)
        Salir.grid(row=4,column=1,padx=10,pady=10)

        self.ventana.mainloop()