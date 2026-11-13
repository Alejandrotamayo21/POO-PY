# Ejercicio 4: Herencia


class Mascota:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(self.nombre + " está comiendo")


class Perro(Mascota):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def ladrar(self):
        print(self.nombre + " dice: ¡Guau!")


class Gato(Mascota):
    def __init__(self, nombre, color):
        super().__init__(nombre)
        self.color = color

    def maullar(self):
        print(self.nombre + " dice: ¡Miau!")


# RETO FINAL
class Cachorro(Perro):
    def jugar(self):
        print(self.nombre + " está jugando")


perro = Perro("Firulais", "labrador")
gato = Gato("Michi", "blanco")

perro.comer()
perro.ladrar()
gato.comer()
gato.maullar()

# RETO FINAL
cachorro = Cachorro("Toby", "criollo")
cachorro.comer()
cachorro.ladrar()
cachorro.jugar()

# Respuesta: un Cachorro hereda de Perro y de Mascota
# (Cachorro -> Perro -> Mascota).
