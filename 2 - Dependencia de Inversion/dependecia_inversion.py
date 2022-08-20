from abc import ABC, abstractmethod


class Cambiable(ABC):
    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass


class bombillo(Cambiable):
    def encender(self):
        print("bombillo: encendido ...")

    def apagar(self):
        print("bombillo: apagado...")


class Ventilador(Cambiable):
    def encender(self):
        print("Ventilador: encendido ...")

    def apagar(self):
        print("Ventilador: apagado...")


class InterruptorElectrico:

    def __init__(self, c: Cambiable):
        self.cliente = c
        self.on = False

    def press(self):
        if self.on:
            self.cliente.apagar()
            self.on = False
        else:
            self.cliente.encender()
            self.on = True


b = bombillo()
v = Ventilador()
switch = InterruptorElectrico(v)
switch.press()
switch.press()
