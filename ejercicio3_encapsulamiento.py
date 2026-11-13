# Ejercicio 3: Encapsulamiento


class Mascota:
    def __init__(self, nombre, dueno, edad, peso):
        self.nombre = nombre      # público
        self._dueno = dueno       # protegido
        self.__edad = edad        # privado
        self.__peso = peso        # privado (RETO FINAL)

    def get_edad(self):
        return self.__edad

    def set_edad(self, nueva_edad):
        if nueva_edad >= 0:
            self.__edad = nueva_edad
        else:
            print("Error: la edad no puede ser negativa")

    # RETO FINAL
    def get_peso(self):
        return self.__peso

    def set_peso(self, nuevo_peso):
        if nuevo_peso > 0 and nuevo_peso <= 100:
            self.__peso = nuevo_peso
        else:
            print("Error: el peso debe ser mayor que 0 y máximo 100 kg")


m = Mascota("Firulais", "Ana", 3, 10)

print(m.nombre)
print(m._dueno)
m.set_edad(-5)
m.set_edad(4)
print(m.get_edad())

# Intentar leer el atributo privado directamente da error:
# print(m.__edad)   # AttributeError: no existe 'm.__edad'

# RETO FINAL
m.set_peso(150)      # inválido, no cambia
m.set_peso(12)       # válido
print(m.get_peso())
