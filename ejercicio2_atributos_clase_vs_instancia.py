# Ejercicio 2: Atributos de clase vs. de instancia


class Mascota:
    # atributos de clase (iguales para todas)
    reino = "Animal"
    total_mascotas = 0

    def __init__(self, nombre, especie):
        # atributos de instancia (distintos en cada objeto)
        self.nombre = nombre
        self.especie = especie
        Mascota.total_mascotas += 1

    # RETO FINAL
    def mostrar_total(self):
        print("Hay " + str(Mascota.total_mascotas) + " mascotas registradas")


m1 = Mascota("Firulais", "perro")
m2 = Mascota("Michi", "gato")
m3 = Mascota("Piolín", "canario")

print("Total de mascotas:", Mascota.total_mascotas)
print(m1.reino, m2.reino)
print(m1.nombre, m2.nombre, m3.nombre)

# RETO FINAL
m1.mostrar_total()

# Respuesta por escrito:
# Si borro una mascota con "del m1", el total sigue en 3 porque
# del solo borra la variable, no resta 1 al contador.
# Solución: crear un método eliminar() que haga
# Mascota.total_mascotas -= 1 antes de borrar el objeto
# (o usar el método especial __del__ que resta 1).
