import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from instancias import eventosSismicos as EventoSismico
from control import GestorRegResRevManual as g


class PantRegResRevManual:

    def __init__(self):
        self.gestor = g.GestorRegResRevManual()

    def procesarAccion(self, opcion_var, evento):
        seleccion = opcion_var.get()

        if seleccion == "1":
            self.gestor.actualizarCambioEstado(evento, seleccion)
            messagebox.showinfo("Confirmado", "El evento fue confirmado.")
        elif seleccion == "2":
            self.gestor.actualizarCambioEstado(evento, seleccion)
            messagebox.showinfo("Rechazado", "El evento fue rechazado.")
        elif seleccion == "3":
            self.gestor.actualizarCambioEstado(evento, seleccion)
            messagebox.showinfo("Solicitado", "Se solicitó revisión a un experto.")
        else:
            messagebox.showwarning("Error", "Por favor selecciona una acción.")

    def habilitarVentana(self):

        def bloquearEvento():
            seleccion = eventos_lista.curselection()
            if not seleccion:
                messagebox.showwarning("Advertencia", "Por favor, seleccioná un evento.")
                return

            index = seleccion[0]
            evento = self.eventos_cargados[index]
            self.gestor.bloquearEventoSismicoYRevisar(evento)
            messagebox.showinfo("Éxito", "Evento bloqueado con éxito.")

            info = self.gestor.buscarDatosSismicos(evento)

            ventana_muestras = tk.Toplevel(ventana)
            ventana_muestras.title("Información del Evento Sísmico")
            ventana_muestras.geometry("700x500")

            def formatear_info(info):
                def procesar_objeto(obj, nivel=0):
                    texto = ""
                    sangria = "  " * nivel
                    if hasattr(obj, '__dict__'):
                        for k, v in vars(obj).items():
                            if hasattr(v, '__dict__'):
                                texto += f"{sangria}{k}:\n"
                                texto += procesar_objeto(v, nivel + 1)
                            else:
                                texto += f"{sangria}{k}: {v}\n"
                    else:
                        texto += f"{sangria}{obj}\n"
                    return texto

                texto = ""
                if not info:
                    return "No se encontraron datos."

                if isinstance(info, list):
                    for i, item in enumerate(info, start=1):
                        texto += f"[{i}]\n"
                        if isinstance(item, list):
                            for j, subitem in enumerate(item, start=1):
                                texto += f"  ({j})\n"
                                texto += procesar_objeto(subitem, nivel=2)
                        else:
                            texto += procesar_objeto(item, nivel=1)
                        texto += "\n"
                else:
                    texto += procesar_objeto(info)

                return texto

            texto_formateado = formatear_info(info)

            frame_scroll = tk.Frame(ventana_muestras)
            frame_scroll.pack(fill=tk.BOTH, expand=True)

            canvas = tk.Canvas(frame_scroll)
            scrollbar = tk.Scrollbar(frame_scroll, orient="vertical", command=canvas.yview)
            scroll_frame = tk.Frame(canvas)

            scroll_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
            )

            canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)

            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")

            label_info = tk.Label(
                scroll_frame,
                text=texto_formateado,
                font=("Courier New", 10),
                justify="left",
                anchor="nw"
            )
            label_info.pack(fill="both", expand=True, padx=10, pady=10)

            boton_mapa = tk.Button(ventana_muestras, text="Ver Mapa")
            boton_mapa.place(x=300, y=450)

            ventana_muestras.update_idletasks()

            x = ventana_muestras.winfo_x()
            y = ventana_muestras.winfo_y()
            ancho = ventana_muestras.winfo_width()

            ancho_sismo = 500
            alto_sismo = 400

            nueva_x = x + ancho + 10
            nueva_y = y

            sismograma_ventana = tk.Toplevel(ventana_muestras)
            sismograma_ventana.title("Sismograma y Modificación")
            sismograma_ventana.geometry(f"{ancho_sismo}x{alto_sismo}+{nueva_x}+{nueva_y}")

            mod_label = tk.Label(sismograma_ventana, text="Modificación de Datos del Evento (opcional):", font=("Arial", 12, "bold"))
            mod_label.place(x=20, y=20)

            magnitud_label = tk.Label(sismograma_ventana, text="Magnitud:", font=("Arial", 10, "bold"))
            magnitud_label.place(x=20, y=60)
            magnitud_input = tk.Entry(sismograma_ventana)
            magnitud_input.place(x=20, y=80)

            alcance_label = tk.Label(sismograma_ventana, text="Alcance:", font=("Arial", 10, "bold"))
            alcance_label.place(x=20, y=120)
            alcance_input = tk.Entry(sismograma_ventana)
            alcance_input.place(x=20, y=140)

            origen_label = tk.Label(sismograma_ventana, text="Origen:", font=("Arial", 10, "bold"))
            origen_label.place(x=20, y=180)
            origen_input = tk.Entry(sismograma_ventana)
            origen_input.place(x=20, y=200)

            modificar_button = tk.Button(sismograma_ventana, text="Modificar Datos")
            modificar_button.place(x=20, y=240)

            sismograma_text = tk.Label(ventana, text="Sismograma", font=("Arial", 12, "bold"))
            sismograma_text.place(x=800, y=20)

            sismograma = Image.open("sismograma.jpg")
            sismograma_pic = ImageTk.PhotoImage(sismograma)

            sismograma_label = tk.Label(ventana, image=sismograma_pic)
            sismograma_label.image = sismograma_pic
            sismograma_label.place(x=800, y=60)

            opcion = tk.StringVar(value="1")
            confirmar = tk.Radiobutton(ventana, text="Confirmar Evento", variable=opcion, value="1")
            rechazar = tk.Radiobutton(ventana, text="Rechazar Evento", variable=opcion, value="2")
            solicitarRAE = tk.Radiobutton(ventana, text="Solicitar Revisión a Experto", variable=opcion, value="3")

            confirmar.place(x=800, y=350)
            rechazar.place(x=800, y=380)
            solicitarRAE.place(x=800, y=410)

            confirmacion_boton = tk.Button(
                ventana,
                text="Confirmar Selección de Acción",
                command=lambda: self.procesarAccion(opcion, evento)
            )
            confirmacion_boton.place(x=800, y=450)

        ventana = tk.Tk()
        ventana.title("Registrar resultado de revisión manual")
        ventana.geometry("1410x510")

        eventos_label = tk.Label(ventana, text="Eventos Sísmicos:", font=("Arial", 12, "bold"))
        eventos_label.place(x=25, y=20)

        eventos_lista = tk.Listbox(ventana)
        eventos_lista.config(width=30, height=10)
        eventos_lista.place(x=25, y=60)

        eventos = self.gestor.buscarEventoSismicoAD()
        self.eventos_cargados = eventos

        for i, evento in enumerate(eventos, start=1):
            eventos_lista.insert(tk.END, f"Evento {i}")

        datos_evento_label = tk.Label(ventana, text="Datos del Evento Seleccionado:", font=("Arial", 12, "bold"))
        datos_evento_label.place(x=300, y=20)

        etiquetas_datos = {}
        valores_datos = {}
        campos = [
            "fechaHoraOcurrencia",
            "latitudEpicentro",
            "longitudEpicentro",
            "latitudHipocentro",
            "longitudHipocentro",
            "valorMagnitud"
        ]

        for i, campo in enumerate(campos):
            etiquetas_datos[campo] = tk.Label(ventana, text=f"{campo}:", font=("Arial", 10, "bold"))
            etiquetas_datos[campo].place(x=300, y=60 + i * 30)

            valores_datos[campo] = tk.Label(ventana, text="", font=("Arial", 10))
            valores_datos[campo].place(x=500, y=60 + i * 30)

        def actualizar_datos(event):
            seleccion = eventos_lista.curselection()
            if seleccion:
                index = seleccion[0]
                evento = self.eventos_cargados[index]
                datos = evento.getDatosPrincipales()

                for campo in campos:
                    valor = datos.get(campo, "N/A")
                    valores_datos[campo].config(text=str(valor))

        eventos_lista.bind("<<ListboxSelect>>", actualizar_datos)

        boton_bloquear = tk.Button(ventana, text="Seleccionar Evento", command=bloquearEvento)
        boton_bloquear.place(x=25, y=300)

        ventana.mainloop()
