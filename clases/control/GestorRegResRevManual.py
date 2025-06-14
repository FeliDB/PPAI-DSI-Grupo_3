class GestorRegResRevManual:
    def __init__(self):
        # Lista que almacena los eventos sísmicos
        self.eventos = []
        # Lista que almacena las instancias de Estado posible
        self.lista_estados = []

    def cargarEventos(self, lista_eventos):
        """
        Carga una lista de objetos EventoSismico al gestor.

        :param lista_eventos: list de EventoSismico
        """
        if not isinstance(lista_eventos, list):
            raise TypeError("Se esperaba una lista de eventos sísmicos.")

        for evento in lista_eventos:
            self.eventos.append(evento)

    def setEstados(self, lista_estados):
        """
        Carga una lista de objetos Estado al gestor.

        :param lista_estados: list de Estado
        """
        if not isinstance(lista_estados, list):
            raise TypeError("Se esperaba una lista de estados.")

        self.lista_estados = lista_estados

    def buscarEventoSismicoAD(self):
        """
        Retorna la lista de eventos sísmicos disponibles para ser mostrados en la pantalla.

        :return: list de EventoSismico
        """
        return self.eventos

    def cambiarEstadoEvento(self, evento, nombre_estado):
        """
        Cambia el estado del evento al estado con el nombre especificado.

        :param evento: EventoSismico a modificar
        :param nombre_estado: str con el nombre del nuevo estado
        """
        for estado in self.lista_estados:
            if estado.nombre == nombre_estado:
                evento.estado = estado
                return
        raise ValueError(f"No se encontró el estado con nombre '{nombre_estado}'")
