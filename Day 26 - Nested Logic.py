class Solucion():
    valorMultaDia = 15
    valorMultaMes = 500
    valorMultaAnio = 10000
    def __init__(self, dev_real, dev_estimada):
        self.fecha_devuelto = dev_real
        self.fecha_agendada = dev_estimada
    def calculaMulta(self):
        multa = 0
        if(self.fecha_devuelto[2] > self.fecha_agendada[2]):#Comparando el año
            multa = self.__multaXanio()
        elif(self.fecha_devuelto[2] == self.fecha_agendada[2]):
            if(self.fecha_devuelto[1] > self.fecha_agendada[1]):#Comparando el mes
                multa = self.__multaXmes()
            elif(self.fecha_devuelto[1] == self.fecha_agendada[1]):
                if(self.fecha_devuelto[0] > self.fecha_agendada[0]):#Comparando el dia
                    multa = self.__multaXdia()
        return(multa)


    def __multaXanio(self):
        return(self.valorMultaAnio)

    def __multaXmes(self):
        diferencia = self.fecha_devuelto[1] - self.fecha_agendada[1]
        return(self.valorMultaMes * diferencia)

    def __multaXdia(self):
        diferencia = self.fecha_devuelto[0] - self.fecha_agendada[0]
        return(self.valorMultaDia * diferencia)

fecha_devolucion_real = list(map(int, input().split()))
fecha_devolucion_estimada = list(map(int, input().split()))
ejercicio = Solucion(fecha_devolucion_real, fecha_devolucion_estimada)
print(ejercicio.calculaMulta())
