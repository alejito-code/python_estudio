import random

class Personaje:
    def __init__(self, nombre, ataque, defensa):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.vida = 100

    def atacar(self, otro_personaje):
        otro_personaje.defensa -= self.ataque
        if otro_personaje.defensa < 0:
            otro_personaje.vida += otro_personaje.defensa
            otro_personaje.defensa = 0
        print(f"{self.nombre} ataca a {otro_personaje.nombre} con un daño de {self.ataque}!")

    def esta_derrotado(self):
        return self.vida <= 0

def combate(personaje_a, personaje_b):
    turno = random.choice([personaje_a, personaje_b])
    while True:
        print(f"\nTurno de {turno.nombre}:")
        input("Presiona Enter para atacar...")
        if turno == personaje_a:
            personaje_a.atacar(personaje_b)
            print(f"Vida de {personaje_b.nombre}: {personaje_b.vida}")
            if personaje_b.esta_derrotado():
                print(f"{personaje_b.nombre} ha sido derrotado! {personaje_a.nombre} gana!")
                break
            turno = personaje_b
        else:
            personaje_b.atacar(personaje_a)
            print(f"Vida de {personaje_a.nombre}: {personaje_a.vida}")
            if personaje_a.esta_derrotado():
                print(f"{personaje_a.nombre} ha sido derrotado! {personaje_b.nombre} gana!")
                break
            turno = personaje_a

# Pedir nombres de los jugadores
nombre_a = input("Nombre del jugador A: ")
nombre_b = input("Nombre del jugador B: ")

# Crear personajes
personaje_a = Personaje(nombre_a, 20, 10)
personaje_b = Personaje(nombre_b, 25, 12)

# Iniciar combate
print("¡Comienza el combate!")
combate(personaje_a, personaje_b)