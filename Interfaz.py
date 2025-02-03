import tkinter as tk

class Interfaz:

    def interfaz(self):
        ventana = tk.Tk()
        ventana.title("PerriClub")
        ventana.geometry("270x300")

        resultado = tk.Label(ventana, text="PerriClub", font=("Arial", 25))
        resultado.grid(row=0, column=0, columnspan=2, pady=20)

        botonMostrar = tk.Button(ventana, text="Mostrar Datos", width=15)
        botonMostrar.grid(row=1, column=0, padx=10, pady=10)

        botonAñadir = tk.Button(ventana, text="Añadir perros", width=15)
        botonAñadir.grid(row=2, column=0, padx=10, pady=10)

        botonActualizarPrecio = tk.Button(ventana, text="Modificar precio", width=15)
        botonActualizarPrecio.grid(row=1, column=1, padx=10, pady=10)

        botonEliminar = tk.Button(ventana, text="Eliminar perro", width=15,)
        botonEliminar.grid(row=2, column=1, padx=10, pady=10)

        ventana.mainloop()