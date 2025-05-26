class reserva:
    __numero_reserva: int
    __nombre_persona: str
    __numero_cabaña: int
    __fecha_inicio: str
    __cantidad_huespedes: int
    __cantidad_dias: int
    __importe_seña: float

    def __init__(self, numero_reserva: int, nombre_persona: str, numero_cabaña: int, fecha_inicio: str, cantidad_huespedes: int, cantidad_dias: int, importe_seña: float):
        self.__numero_reserva = numero_reserva
        self.__nombre_persona = nombre_persona
        self.__numero_cabaña = numero_cabaña
        self.__fecha_inicio = fecha_inicio
        self.__cantidad_huespedes = cantidad_huespedes
        self.__cantidad_dias = cantidad_dias
        self.__importe_seña = importe_seña
    
    def get_numero_reserva(self):
        return self.__numero_reserva
    
    def get_nombre_persona(self):
        return self.__nombre_persona
    
    def get_numero_cabaña(self):
        return self.__numero_cabaña
    
    def get_fecha_inicio(self):
        return self.__fecha_inicio
    
    def get_cantidad_huespedes(self):
        return self.__cantidad_huespedes
    
    def get_cantidad_dias(self):
        return self.__cantidad_dias
    
    def get_importe_seña(self):
        return self.__importe_seña
    
    def set_numero_reserva(self, numero_reserva):
        self.__numero_reserva = numero_reserva
    
    def set_nombre_persona(self, nombre_persona):
        self.__nombre_persona = nombre_persona
    
    def set_numero_cabaña(self, numero_cabaña):
        self.__numero_cabaña = numero_cabaña
    
    def set_fecha_inicio(self, fecha_inicio):
        self.__fecha_inicio = fecha_inicio
    
    def set_cantidad_huespedes(self, cantidad_huespedes):
        self.__cantidad_huespedes = cantidad_huespedes
    
    def set_cantidad_dias(self, cantidad_dias):
        self.__cantidad_dias = cantidad_dias
    
    def set_importe_seña(self, importe_seña):
        self.__importe_seña = importe_seña
    
    def __str__(self):
        return "Numero de reserva: " + str(self.__numero_reserva) + "\n" + "Nombre de persona: " + str(self.__nombre_persona) + "\n" + "Numero de cabaña: " + str(self.__numero_cabaña) + "\n" + "Fecha de inicio: " + str(self.__fecha_inicio) + "\n" + "Cantidad de huespedes: " + str(self.__cantidad_huespedes) + "\n" + "Cantidad de dias: " + str(self.__cantidad_dias) + "\n" + "Importe de la seña: " + str(self.__importe_seña) + "\n"
    
    def __lt__(self, otro):
        return self.__numero_cabaña < otro.__numero_cabaña