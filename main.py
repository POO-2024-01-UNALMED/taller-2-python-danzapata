class Asiento:
    def _init_(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self, colorsito):
        self.color = colorsito

class Motor:
    def _init_(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registroN):
        if (registroN=="gasolina") or (registroN=="electrico"):
            self.registro = registroN
    
    def asignarTipo(self, tipoN):
        self.tipo = tipoN

class Auto:
    def _init_(self, modelo, precio, asientos, marca, motor, registro, cantidadCreados):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        self.cantidadCreados = cantidadCreados

    def cantidadAsientos(self, asientos):
        oky = 0
        for i in asientos:
            oky = oky+1 
        return oky

    def verificarIntegridad(self, registro):
        if (Asiento.self.registro==Motor.self.registro) and (Motor.self.registro==Auto.self.registro):
            return "Auto original"
        else:
            return "Las piezas no son originales"





