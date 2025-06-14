import tkinter as tk
from tkinter import ttk

class PantRegResRevManual:

    def __init__(self, gestor):
        self.gestor = gestor

    def habilitarVentana(self):
        ventana = tk.Tk()
        ventana.title("Registrar resultado de revisión manual")
        ventana.geometry("1024x768")

        lista_eventos = self.gestor.buscarEventoSismicoAD()
        valores_combo = [f"Evento #{i+1}" for i in range(len(lista_eventos))]

        combo_opciones = ttk.Combobox(ventana, values=valores_combo, width=20, state="readonly")
        combo_opciones.place(x=40, y=31)
        combo_opciones.current(0)

        # Contenedor principal
        frame_principal = tk.Frame(ventana)
        frame_principal.place(x=40, y=80)

        # Frame de detalles generales (columna izquierda)
        frame_izquierda = tk.Frame(frame_principal)
        frame_izquierda.grid(row=0, column=0, sticky="nw", padx=10, pady=10)

        etiqueta_estado = tk.Label(frame_izquierda, text="")
        etiqueta_estado.pack(anchor="w")
        etiqueta_fecha_fin = tk.Label(frame_izquierda, text="")
        etiqueta_fecha_fin.pack(anchor="w")
        etiqueta_fecha_ocurrencia = tk.Label(frame_izquierda, text="")
        etiqueta_fecha_ocurrencia.pack(anchor="w")
        etiqueta_epicentro = tk.Label(frame_izquierda, text="")
        etiqueta_epicentro.pack(anchor="w")
        etiqueta_hipocentro = tk.Label(frame_izquierda, text="")
        etiqueta_hipocentro.pack(anchor="w")
        etiqueta_magnitud = tk.Label(frame_izquierda, text="")
        etiqueta_magnitud.pack(anchor="w")
        etiqueta_alcance = tk.Label(frame_izquierda, text="")
        etiqueta_alcance.pack(anchor="w")
        etiqueta_origen = tk.Label(frame_izquierda, text="")
        etiqueta_origen.pack(anchor="w")

        # Frame de datos adicionales (columna derecha)
        frame_derecha = tk.Frame(frame_principal)
        frame_derecha.grid(row=0, column=1, sticky="ne", padx=60, pady=10)

        etiqueta_titulo_adicionales = tk.Label(frame_derecha, text="Datos Adicionales (Serie Temporal y Muestra)", font=("Arial", 10, "bold"))
        etiqueta_titulo_adicionales.pack(anchor="w")

        etiqueta_serie_info = tk.Label(frame_derecha, text="")
        etiqueta_serie_info.pack(anchor="w", pady=10)
        etiqueta_muestra_valor = tk.Label(frame_derecha, text="")
        etiqueta_muestra_valor.pack(anchor="w", pady=10)

        def actualizar_detalles(event=None):
            idx = combo_opciones.current()
            if idx >= 0:
                e = lista_eventos[idx]
                etiqueta_estado.config(text=f"Estado: {e.estado.nombre}")
                etiqueta_fecha_fin.config(text=f"Fecha Fin: {e.fechaHoraFin}")
                etiqueta_fecha_ocurrencia.config(text=f"Fecha Ocurrencia: {e.fechaHoraOcurrencia}")
                etiqueta_epicentro.config(text=f"Epicentro (lat,long): ({e.latitudEpicentro}, {e.longitudEpicentro})")
                etiqueta_hipocentro.config(text=f"Hipocentro (lat,long): ({e.latitudHipocentro}, {e.longitudHipocentro})")
                etiqueta_magnitud.config(text=f"Magnitud: {e.valorMagnitud}")
                etiqueta_alcance.config(text=f"Alcance: {e.alcanceSismo.nombre}")
                etiqueta_origen.config(text=f"Origen: {e.origenGeneracion.descripcion}")

                # Ocultar info avanzada hasta bloquear
                etiqueta_serie_info.config(text="")
                etiqueta_muestra_valor.config(text="")

        def bloquear_evento():
            idx = combo_opciones.current()
            if idx >= 0:
                evento = lista_eventos[idx]
                self.gestor.cambiarEstadoEvento(evento, "bloqueado en revisión")
                actualizar_detalles()

                # Mostrar info de SerieTemporal
                if evento.serieTemporal:
                    serie = evento.serieTemporal[0]
                    etiqueta_serie_info.config(
                        text=f"SerieTemporal:\n  - Alarma: {serie.condicionAlarma}\n  - Registro: {serie.fechaHoraRegistro}\n  - Frecuencia: {serie.frecuenciaMuestreo} Hz"
                    )

                if hasattr(evento, "listaMuestrasSismicas") and evento.listaMuestrasSismicas:
                    muestra = evento.listaMuestrasSismicas[0]
                    etiqueta_muestra_valor.config(
                        text=f"Muestra Sismica:\n  - Valor: {muestra.detalleMuestraSismica.valor}"
                    )

        combo_opciones.bind("<<ComboboxSelected>>", actualizar_detalles)
        actualizar_detalles()

        boton_mostrar = tk.Button(ventana, text="Bloquear Evento Seleccionado", command=bloquear_evento)
        boton_mostrar.place(x=40, y=330)

        cancelar_boton = tk.Button(ventana, text="Cancelar", command=ventana.destroy)
        cancelar_boton.place(x=40, y=700)

        ventana.mainloop()
