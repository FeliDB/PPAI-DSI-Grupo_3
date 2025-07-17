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
            messagebox.showinfo("Confirmado", "El evento fue confirmado.")
        elif seleccion == "2":
            self.gestor.rechazarEventoSismico(evento)
            messagebox.showinfo("Rechazado", "El evento fue rechazado.")
        elif seleccion == "3":
            messagebox.showinfo("Solicitado", "Se solicitó revisión a un experto.")
        else:
            messagebox.showwarning("Error", "Por favor selecciona una acción.")

    def habilitarVentana(self):
        ventana = tk.Tk()
        ventana.title("Registrar resultado de revisión manual")
        ventana.geometry("1650x750")

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

        boton_bloquear = tk.Button(ventana, text="Seleccionar Evento", command=lambda: bloquearEvento())
        boton_bloquear.place(x=25, y=300)

        # Elementos ocultos al inicio
        mod_label = tk.Label(ventana, text="Modificación de Datos del Evento (opcional):", font=("Arial", 12, "bold"))
        magnitud_label = tk.Label(ventana, text="Magnitud:", font=("Arial", 10, "bold"))
        magnitud_input = tk.Entry(ventana)
        alcance_label = tk.Label(ventana, text="Alcance:", font=("Arial", 10, "bold"))
        alcance_input = tk.Entry(ventana)
        origen_label = tk.Label(ventana, text="Origen:", font=("Arial", 10, "bold"))
        origen_input = tk.Entry(ventana)
        modificar_button = tk.Button(ventana, text="Modificar Datos")

        sismograma_text = tk.Label(ventana, text="Sismograma", font=("Arial", 12, "bold"))
        sismograma = Image.open("sismograma.jpg")
        sismograma_pic = ImageTk.PhotoImage(sismograma)
        sismograma_label = tk.Label(ventana, image=sismograma_pic)
        sismograma_label.image = sismograma_pic

        opcion = tk.StringVar(value="1")
        confirmar = tk.Radiobutton(ventana, text="Confirmar Evento", variable=opcion, value="1")
        rechazar = tk.Radiobutton(ventana, text="Rechazar Evento", variable=opcion, value="2")
        solicitarRAE = tk.Radiobutton(ventana, text="Solicitar Revisión a Experto", variable=opcion, value="3")

        confirmacion_boton = tk.Button(
            ventana,
            text="Confirmar Selección de Acción",
            command=lambda: self.procesarAccion(opcion, self.evento_seleccionado)
        )

        for widget in [
            mod_label, magnitud_label, magnitud_input,
            alcance_label, alcance_input, origen_label, origen_input,
            modificar_button, sismograma_text, sismograma_label,
            confirmar, rechazar, solicitarRAE, confirmacion_boton
        ]:
            widget.place_forget()

        def bloquearEvento():
            seleccion = eventos_lista.curselection()
            if not seleccion:
                messagebox.showwarning("Advertencia", "Por favor, seleccioná un evento.")
                return

            index = seleccion[0]
            evento = self.eventos_cargados[index]
            self.evento_seleccionado = evento
            print("POST")
            self.gestor.bloquearEventoSismico(evento)
            print("PRE")
            messagebox.showinfo("Éxito", "Evento bloqueado con éxito.")

            # ❗ Eliminar el evento de la lista visual y del backend
            eventos_lista.delete(index)
            del self.eventos_cargados[index]

            # ❌ NO limpiamos los campos de datos → se mantienen visibles

            info = self.gestor.buscarDatosSismicos(evento)

            base_y = 380
            mod_label.place(x=25, y=base_y)
            magnitud_label.place(x=25, y=base_y + 40)
            magnitud_input.place(x=120, y=base_y + 40)
            alcance_label.place(x=25, y=base_y + 80)
            alcance_input.place(x=120, y=base_y + 80)
            origen_label.place(x=25, y=base_y + 120)
            origen_input.place(x=120, y=base_y + 120)
            modificar_button.place(x=25, y=base_y + 160)

            sismograma_text.place(x=1000, y=20)
            sismograma_label.place(x=1000, y=60)
            confirmar.place(x=1000, y=350)
            rechazar.place(x=1000, y=380)
            solicitarRAE.place(x=1000, y=410)
            confirmacion_boton.place(x=1000, y=450)

        ventana.mainloop()
