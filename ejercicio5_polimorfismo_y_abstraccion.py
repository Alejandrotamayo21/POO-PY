# Ejercicio 5: Polimorfismo y abstracción

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def hacer_sonido(self):
        pass

    # RETO FINAL: segundo método abstracto
    @abstractmethod
    def moverse(self):
        pass


class Perro(Animal):
    def hacer_sonido(self):
        print(self.nombre + ": ¡Guau!")

    def moverse(self):
        print(self.nombre + " corre")


class Gato(Animal):
    def hacer_sonido(self):
        print(self.nombre + ": ¡Miau!")

    def moverse(self):
        print(self.nombre + " camina sigilosamente")


class Vaca(Animal):
    def hacer_sonido(self):
        print(self.nombre + ": ¡Muuu!")

    def moverse(self):
        print(self.nombre + " camina despacio")


# RETO FINAL
class Pajaro(Animal):
    def hacer_sonido(self):
        print(self.nombre + ": ¡Pío!")

    def moverse(self):
        print(self.nombre + " vuela")


animales = [Perro("Firulais"), Gato("Michi"), Vaca("Lola")]

# RETO FINAL: se agrega el pájaro sin tocar el ciclo for
animales.append(Pajaro("Piolín"))

for animal in animales:
    animal.hacer_sonido()
    animal.moverse()

# Intentar crear un Animal directamente da error:
# a = Animal("Rex")   # TypeError: no se puede instanciar una clase abstracta
