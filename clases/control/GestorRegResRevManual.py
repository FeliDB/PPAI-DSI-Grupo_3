class GestorRegResRevManual:
    def __init__(self):
        # Lista que almacena los eventos sísmicos
        self.eventos = []

    def cargarEventos(self, lista_eventos):
        """
        Carga una lista de objetos EventoSismico al gestor.

        :param lista_eventos: list de EventoSismico
        """
        if not isinstance(lista_eventos, list):
            raise TypeError("Se esperaba una lista de eventos sísmicos.")

        for evento in lista_eventos:
            # Se puede validar tipo aquí si se desea
            self.eventos.append(evento)

    def buscarEventoSismicoAD(self):
        """
        Retorna la lista de eventos sísmicos disponibles para ser mostrados en la pantalla.

        :return: list de EventoSismico
        """
        return self.eventos

    def cambiarEstadoEvento(self, evento, nombre_estado):
        for estado in self.lista_estados:
            if estado.nombre == nombre_estado:
                evento.estado = estado
                return
        raise ValueError(f"No se encontró el estado con nombre '{nombre_estado}'")

