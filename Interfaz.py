import tkinter as tk
from tkinter import messagebox
from tabulate import tabulate

class Interfaz:

    perros = [
    ["Pastor Aleman", "Max", 1200],
    ["Bulldog Frances", "Princesa", 2500],
    ["Chihuahua", "Deborador de mundos", 800],
    ["Dalmata", "Pancho", 1000],
    ["Husky Siberiano", "Epi", 1500],
    ["Golden Retriever", "Luna", 1800],
    ["Labrador Retriever", "Thor", 1600],
    ["Poodle", "Bella", 1200],
    ["Rottweiler", "Rocky", 2000],
    ["Beagle", "Toby", 900],
    ["Boxer", "Bruno", 1300],
    ["Husky", "Mimi", 1000],
    ["Bulldog Ingles", "Winston", 3000],
    ["Pug", "Lola", 1500],
    ["Doberman", "Rex", 1800],
    ["Corgi", "Leo", 2000],
    ["Schnauzer", "Max", 1200],
    ["Border Collie", "Luna", 1400],
    ["Bichon Frise", "Coco", 1100],
    ["San Bernardo", "Bear", 2500],
    ["Pastor Aleman", "Rex", 1300],
    ["Husky", "Lola", 2600],
    ["Chihuahua", "Peque", 850],
    ["Dalmata", "Luna", 1100],
    ["Husky Siberiano", "Nieve", 1600],
    ["Golden Retriever", "Max", 1900],
    ["Labrador Retriever", "Bella", 1700],
    ["Poodle", "Coco", 1250],
    ["Rottweiler", "Thor", 2100],
    ["Beagle", "Luna", 950],
]

    def MostrarPerro(self):
        ventana_perros = tk.Toplevel()
        ventana_perros.title("Lista de Perros")
        ventana_perros.geometry("470x450")

        tabla = tabulate(self.perros, headers=["Raza", "Nombre", "Precio (€)"])

        text = tk.Text(ventana_perros, font=("Courier", 10))
        text.insert(tk.END, tabla)
        text.config(state="disabled")
        text.pack(pady=10, padx=10, expand=True, fill="both")

        btn_cerrar = tk.Button(ventana_perros, text="Cerrar", command=ventana_perros.destroy)
        btn_cerrar.pack(pady=0)

    def Precio_Perro(self):
        self.ventana_filtrar = tk.Toplevel()
        self.ventana_filtrar.title("Mostrar por precio")
        self.ventana_filtrar.geometry("170x300")

        tk.Label(self.ventana_filtrar, text="Precio maximo").grid(row=0, column=0, pady=10)
        self.precio_maximo = tk.Entry(self.ventana_filtrar)
        self.precio_maximo.grid(row=1, column=0, padx=10, pady=10)

        btn_filtrar = tk.Button(self.ventana_filtrar, text="Filtrar", command=self.filtrar_perros)
        btn_filtrar.grid(row=2, column=0, pady=10)

        btn_cerrar = tk.Button(self.ventana_filtrar, text="Cerrar", command=self.ventana_filtrar.destroy)
        btn_cerrar.grid(row=3, column=0, pady=10)


    
    def filtrar_perros(self):
        try:
            precio_max = float(self.precio_maximo.get())
            perros_filtrados = [] 


            for perro in self.perros:
                if perro[2] <= precio_max:
                    perros_filtrados.append(perro)

            ventana_filtrada = tk.Toplevel()
            ventana_filtrada.title("Perros Filtrados por Precio")
            ventana_filtrada.geometry("470x450")
    
            if perros_filtrados:
                tabla = tabulate(perros_filtrados, headers=["Raza", "Nombre", "Precio (€)"])
            else:
                tabla = "No hay perros con un precio menor o igual al introducido."

            text = tk.Text(ventana_filtrada, font=("Courier", 10))
            text.insert(tk.END, tabla)
            text.config(state="disabled")
            text.pack(pady=10, padx=10, expand=True, fill="both")

            btn_cerrar = tk.Button(ventana_filtrada, text="Cerrar", command=ventana_filtrada.destroy)
            btn_cerrar.pack(pady=10)

        except ValueError:
            tk.messagebox.showerror("Error", "Por favor, introduce un valor numerico valido.")
    
    def Buscar_raza(self):
        self.ventana_buscar_raza = tk.Toplevel()
        self.ventana_buscar_raza.title("Buscar por raza")
        self.ventana_buscar_raza.geometry("170x300")

        tk.Label(self.ventana_buscar_raza, text="raza").grid(row=0, column=0, pady=10)
        self.precio_raza = tk.Entry(self.ventana_buscar_raza)
        self.precio_raza.grid(row=1, column=0, padx=10, pady=10)

        btn_raza = tk.Button(self.ventana_buscar_raza, text="Filtrar", command=self.filtrar_raza)
        btn_raza.grid(row=2, column=0, pady=10)

        btn_cerrar = tk.Button(self.ventana_buscar_raza, text="Cerrar", command=self.ventana_buscar_raza.destroy)
        btn_cerrar.grid(row=3, column=0, pady=10)

    def filtrar_raza(self):
        raza = self.precio_raza.get()
        perros_filtrados = [] 

        for perro in self.perros:
                if perro[0] == raza:
                    perros_filtrados.append(perro)

        ventana_filtrada = tk.Toplevel()
        ventana_filtrada.title("Perros Filtrados por Precio")
        ventana_filtrada.geometry("470x450")

        if perros_filtrados:
            tabla = tabulate(perros_filtrados, headers=["Raza", "Nombre", "Precio (€)"])
        else:
            tabla = "No hay perros de la raza introducida."

        text = tk.Text(ventana_filtrada, font=("Courier", 10))
        text.insert(tk.END, tabla)
        text.config(state="disabled")
        text.pack(pady=10, padx=10, expand=True, fill="both")

        btn_cerrar = tk.Button(ventana_filtrada, text="Cerrar", command=ventana_filtrada.destroy)
        btn_cerrar.pack(pady=10)


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
        self.ventana_añadir = tk.Toplevel()
        self.ventana_añadir.title("Añadir Perro Ventana")
        self.ventana_añadir.geometry("480x300")

        tk.Label(self.ventana_añadir, text="Raza").grid(row=0, column=0, pady=10)
        self.Raza = tk.Entry(self.ventana_añadir)
        self.Raza.grid(row=1, column=0, padx=10, pady=10)

        tk.Label(self.ventana_añadir, text="Nombre").grid(row=0, column=1, pady=10)
        self.Nombre = tk.Entry(self.ventana_añadir)
        self.Nombre.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.ventana_añadir, text="Precio").grid(row=0, column=2, pady=10)
        self.Precio = tk.Entry(self.ventana_añadir)
        self.Precio.grid(row=1, column=2, padx=10, pady=10)

        tk.Button(self.ventana_añadir, text="Añadir", command=self.Añadir_Perro).grid(row=2, column=1, pady=10)

        btn_cerrar = tk.Button(self.ventana_añadir, text="Cerrar", command=self.ventana_añadir.destroy)
        btn_cerrar.grid(row=5, column=1, pady=10)

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

        btn_cerrar = tk.Button(self.ventana_actualizar, text="Cerrar", command=self.ventana_actualizar.destroy)
        btn_cerrar.grid(row=5, column=1, pady=10)

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

        btn_cerrar = tk.Button(self.ventana_eliminar, text="Cerrar", command=self.ventana_eliminar.destroy)
        btn_cerrar.grid(row=3, column=1, pady=10)

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

        btn_cerrar = tk.Button(self.ventana_mostrar, text="Cerrar", command=self.ventana_mostrar.destroy)
        btn_cerrar.grid(row=5, column=1, pady=10)

    def Salir(self):
        self.ventana.destroy()


    def interfaz(self):
        self.ventana = tk.Tk()
        self.ventana.title("PerriClub")
        self.ventana.geometry("270x300")

        resultado = tk.Label(self.ventana, text="PerriClub", font=("Arial", 25))
        resultado.grid(row=0, column=0, columnspan=2, pady=20)

        botonMostrar = tk.Button(self.ventana, text="Mostrar Datos", width=15, command=self.MostrarPerro)
        botonMostrar.grid(row=1, column=0, padx=10, pady=10)

        botonAñadir = tk.Button(self.ventana, text="Añadir perros", width=15, command=self.Ventana_Añadir_Perro)
        botonAñadir.grid(row=2, column=0, padx=10, pady=10)

        botonActualizarPrecio = tk.Button(self.ventana, text="Modificar precio", width=15, command=self.Ventana_Actualizar_Perro)
        botonActualizarPrecio.grid(row=1, column=1, padx=10, pady=10)

        botonEliminar = tk.Button(self.ventana, text="Eliminar perro", width=15, command=self.Ventana_Eliminar_Perro)
        botonEliminar.grid(row=2, column=1, padx=10, pady=10)

        BuscarPrecio = tk.Button(self.ventana, text="Buscar por precio", width=15, command=self.Precio_Perro )
        BuscarPrecio.grid(row=3,column=0,padx=10,pady=10)

        buscarRaza = tk.Button(self.ventana,text="Buscar por raza", width=15, command=self.Buscar_raza)
        buscarRaza.grid(row=4,column=0,padx=10,pady=10)

        estadisticas = tk.Button(self.ventana,text="Estadisticas", width=15, command=self.Ventana_Mostrar_Perro_Caro_Barato)
        estadisticas.grid(row=3,column=1,padx=10,pady=10)

        Salir = tk.Button(self.ventana,text=" Salir ", width=15, command=self.Salir)
        Salir.grid(row=4,column=1,padx=10,pady=10)

        self.ventana.mainloop()