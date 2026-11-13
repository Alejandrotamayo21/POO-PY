# Ejercicio 1: Clases y objetos


class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def presentarse(self):
        print("Hola, soy " + self.nombre + " y soy un " + self.especie)

    # RETO FINAL
    def cumplir_anios(self):
        self.edad = self.edad + 1
        print(self.nombre + " ahora tiene " + str(self.edad) + " años")

#alias
perro = Mascota("Firulais", "perro", 3)
gato = Mascota("Michi", "gato", 2)

#presentarse
perro.presentarse()
gato.presentarse()

# RETO FINAL: cumplir años dos veces
perro.cumplir_anios()
perro.cumplir_anios()
