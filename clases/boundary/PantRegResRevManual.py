class PantRegResRevManual:

    def habilitarVentana(self):
        import tkinter as tk
        from tkinter import ttk

        ventana = tk.Tk()

        ventana.title("")

        ventana.geometry("")


        etiqueta = tk.Label(ventana, text="Nombre:")

        entrada_nombre = tk.Entry(ventana)
        entrada_nombre.pack(pady=5)

        opciones = ["Opción 1", "Opción 2", "Opción 3"]
        combo_opciones = ttk.Combobox(ventana, values=opciones)
        combo_opciones.pack(pady=5)
        combo_opciones.current(0) 

        boton_mostrar = tk.Button(ventana, text="Mostrar datos"""", command=""")
        boton_mostrar.pack(pady=10)

        # Etiqueta para mostrar el resultado
        etiqueta_resultado = tk.Label(ventana, text="")
        etiqueta_resultado.pack(pady=10)


        ventana.mainloop()