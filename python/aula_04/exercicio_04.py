class Sensor:
    def __init__(self, temperatura):
        self.__temperatura = temperatura

    def get_temperatura(self):
        return self.__temperatura

    def set_temperatura(self, temperatura):
        if temperatura >= -50 and temperatura <= 150:
            self.__temperatura = temperatura
        else:
            print("Temperatura inválida")

    def status(self):
        if self.__temperatura <= 80:
            return "Normal"
        elif self.__temperatura <= 120:
            return "Alerta"
        else:
            return "Critico"


sensor = Sensor(20)
print(sensor.get_temperatura(), sensor.status())

sensor.set_temperatura(90)
print(sensor.get_temperatura(), sensor.status())

sensor.set_temperatura(130)
print(sensor.get_temperatura(), sensor.status())

sensor.set_temperatura(-10)
print(sensor.get_temperatura(), sensor.status())