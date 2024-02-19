class Asiento:
    def _init_(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self, color):
        if (color=="rojo" or color=="verde" or color=="negro" or color=="blanco" or color=="negro" or color=="amarillo"):
            self.color = color

class Motor:
    def _init_(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
            self.registro = registro
    
    def asignarTipo(self, tipo):
        if (tipo=="gasolina") or (tipo=="electrico"):
           self.tipo = tipo

class Auto:

    cantidadCreados=0
    
    def _init_(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        oky = 0
        for i in self.asientos:
            oky = oky+1 
        return oky

    def verificarIntegridad(self):
        if self.registro!=self.motor.registro:
            return "Las piezas no son originales"
        
        for i in self.asientos:
            if i != None:
                if self.registro!=i.registro:
                    return "Las piezas no son originales"
                
        return "Auto original"





