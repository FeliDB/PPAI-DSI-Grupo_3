import tkinter as tk
from tkinter import ttk

class PantRegResRevManual:

    def __init__(self, gestor):
        self.gestor = gestor

    def habilitarVentana(self):

        ventana = tk.Tk()
        ventana.title("Registrar resultado de revisión manual")
        ventana.geometry("1024x768")

        estados_posibles = [
            "pendiente de revisión",
            "pendiente de cierre",
            "bloqueado en revisión",
            "derivado a experto",
            "confirmado",
            "rechazado"
        ]

        lista_eventos = self.gestor.buscarEventoSismicoAD()

        valores_combo = [f"Evento #{i+1}" for i in range(len(lista_eventos))]

        combo_opciones = ttk.Combobox(ventana, values=valores_combo, width=20, state="readonly")
        combo_opciones.place(x=40,y=31)
        combo_opciones.current(0)

        frame_detalles = tk.Frame(ventana)
        frame_detalles.place(x=40, y=80)

        etiqueta_estado = tk.Label(frame_detalles, text="")
        etiqueta_estado.pack(anchor="w")
        etiqueta_fecha_fin = tk.Label(frame_detalles, text="")
        etiqueta_fecha_fin.pack(anchor="w")
        etiqueta_fecha_ocurrencia = tk.Label(frame_detalles, text="")
        etiqueta_fecha_ocurrencia.pack(anchor="w")
        etiqueta_epicentro = tk.Label(frame_detalles, text="")
        etiqueta_epicentro.pack(anchor="w")
        etiqueta_hipocentro = tk.Label(frame_detalles, text="")
        etiqueta_hipocentro.pack(anchor="w")
        etiqueta_magnitud = tk.Label(frame_detalles, text="")
        etiqueta_magnitud.pack(anchor="w")

        etiqueta_estado_actual = tk.Label(ventana, text="Estado actual del evento:")
        etiqueta_estado_actual.pack(pady=10)

        combo_estado = ttk.Combobox(ventana, values=estados_posibles, state="readonly")
        combo_estado.pack(pady=5)

        def actualizar_detalles(event):
            idx = combo_opciones.current()
            if idx >= 0:
                e = lista_eventos[idx]
                etiqueta_estado.config(text=f"Estado: {e.estado}")
                etiqueta_fecha_fin.config(text=f"Fecha Fin: {e.fechaHoraFin}")
                etiqueta_fecha_ocurrencia.config(text=f"Fecha Ocurrencia: {e.fechaHoraOcurrencia}")
                etiqueta_epicentro.config(text=f"Epicentro (lat,long): ({e.latitudEpicentro}, {e.longitudEpicentro})")
                etiqueta_hipocentro.config(text=f"Hipocentro (lat,long): ({e.latitudHipocentro}, {e.longitudHipocentro})")
                etiqueta_magnitud.config(text=f"Magnitud: {e.valorMagnitud}")

                combo_estado.set(e.estado)

        combo_opciones.bind("<<ComboboxSelected>>", actualizar_detalles)
        actualizar_detalles(None)

        boton_mostrar = tk.Button(ventana, text="Mostrar datos", state=tk.DISABLED)
        boton_mostrar.pack(pady=10)

        ventana.mainloop()