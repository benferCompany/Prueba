class Fecha:
    def __init__(self, dia, mes, anio):
        self.dia = dia
        self.mes = mes
        self.anio = anio

    def __str__(self):
        return "{}/{}/{}".format(self.dia, self.mes, self.anio)

    def getDia(self):
        return self.dia
    
    def getMes(self):
        return self.mes

    def getAnio(self):
        return self.anio

    def setDia(self, dia):
        self.dia = dia

    def setMes(self, mes):
        self.mes = mes

    def setAnio(self, anio):
        self.anio = anio

    def esBisiesto(self):
        if self.anio % 4 == 0:
            if self.anio % 400 == 0: # 400, 800, 1200, 1600, 2000, 2400
                return True
        else:
            if self.anio % 100 == 0: # 100, 200, 300, 500, 600, 700, 900
                return False
            else:
                if self.anio % 4 == 0:
                    return True
                else:
                    return False
    
    def esFechaValida(self):
        if self.dia < 1 or self.dia > 31:
            return False
        if self.mes < 1 or self.mes > 12:
            return False
        if self.anio < 1:
            return False

    def diasMes(self):
        if self.mes == 2:
            if self.esBisiesto():
                return 29
            else:
                return 28
        elif self.mes == 4 or self.mes == 6 or self.mes == 9 or self.mes == 11:
                return 30
        else:
                return 31

    def primerDiaMes(self):
        return Fecha(1, self.mes, self.anio)
    
    def ultimoDiaMes(self):
        return Fecha(self.diasMes(), self.mes, self.anio)
    
    def diaSiguiente(self):
        if self.dia < self.diasMes():
            return Fecha(self.dia + 1, self.mes, self.anio)
        else:
            if self.mes < 12:
                return Fecha(1, self.mes + 1, self.anio)
            else:
                return Fecha(1, 1, self.anio + 1)

    def diaAnterior(self):
        if self.dia > 1:
            return Fecha(self.dia - 1, self.mes, self.anio)
        else:
            if self.mes > 1:
                return Fecha(self.diasMes() if self.mes != 3 else 28, self.mes - 1, self.anio)
            else:
                return Fecha(self.diasMes(), 12, self.anio - 1)

    def diasMesAnterior(self, fecha):
        if fecha.mes == 3:
            if fecha.esBisiesto():
                return 29
            else:
                return 28
        elif fecha.mes == 5 or fecha.mes == 7 or fecha.mes == 10 or fecha.mes == 12:
                return 30
        else:
                return 31


    def diasMesSiguiente(self):
        if self.mes == 1:
            if self.esBisiesto():
                return 29
            else:
                return 28
        elif self.mes == 3 or self.mes == 5 or self.mes == 8 or self.mes == 10:
                return 30
        else:
                return 31

    def mesSiguiente(self):
        if self.mes < 12:
            return Fecha(self.dia, self.mes + 1, self.anio)
        else:
            return Fecha(self.dia, 1, self.anio + 1)

    def mesAnterior(self):
        if self.mes > 1:
            return Fecha(self.dia, self.mes - 1, self.anio)
        else:
            return Fecha(self.dia, 12, self.anio - 1)

    def anioSiguiente(self):
        return Fecha(self.dia, self.mes, self.anio + 1)

    def anioAnterior(self):
        return Fecha(self.dia, self.mes, self.anio - 1)

    def diasTranscurridos(self, fecha):
        dias = 0
        fechaActual = self
        string_fechaActual = fechaActual.__str__()
        string_fecha = fecha.__str__()
        

mi_cumple = Fecha(8, 8, 1995)
# - Diferencia en días: 9813
# - Diferencia en semanas completas: 1401
# - Diferencia en meses: 321
print(mi_cumple.diasTranscurridos(Fecha(20, 6, 2022)))