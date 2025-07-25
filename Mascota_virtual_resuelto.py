# importar el modulo random
# import imagen desde el archivo mascota.py

import random
from mascota import imagen

class MascotaVirtual:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hambre = 0
        self.felicidad = 0
        self.imagen = imagen.inicio
        self.imagen_triste = imagen.triste
        self.imagen_muerto = imagen.muerto
        self.imagen_disgustado = imagen.disgustado
        self.imagen_feliz = imagen.feliz

    def alimentar(self):
        self.felicidad -= random.randint(5, 10)
        if self.felicidad < 0:
            self.felicidad = 0
        if self.hambre == 0:
            print(self.imagen_disgustado)
            print(f"{self.nombre} esta lleno, ya no puede comer mas...")
        else:
            self.hambre -= random.randint(10, 15)
            if self.hambre < 0:
                self.hambre = 0
            print(self.imagen_feliz)
            print(f"{self.nombre} ha sido alimentado.")
 
    def jugar(self):
        if self.hambre < 70:
            self.felicidad += random.randint(10, 25)
            if self.felicidad > 100:
                self.felicidad = 100
            self.hambre += random.randint(10, 15)
            if self.hambre > 100:
                self.hambre = 100
            print(self.imagen_feliz)
            print(f"{self.nombre} se divierte")
        else:
            print(f"{self.nombre} tiene mucha hambre y no puede jugar.")
            print(self.imagen_disgustado)
        
    def estado_animo(self):
        if self.hambre >= 70 and self.felicidad <= 50:
            print(self.imagen_disgustado)
            print(f"{self.nombre} muy hambrienta y muy triste")
        elif self.hambre >= 70:
            print(self.imagen_disgustado)
            print(f"{self.nombre} Esta muy hambrienta")
        elif self.felicidad <= 50:
            print(self.imagen_triste)
            print(f"{self.nombre} Esta muy triste")
        else:
            print(self.imagen_feliz)
            print(f"{self.nombre} esta contenta y satisfecha")

    def presentacion(self):  # opcional
        print(
            f"\n╔════════════════════════════════════╗\n║ Te presento a tu mascota!          ║\n╚════════════════════════════════════╝\n{self.imagen}\tSu nombre es {self.nombre}"
            )

    def despedida(self):  # opcional
        print(
            f"\n╔════════════════════════════════════╗\n║ Nos vemos! ║\n╚════════════════════════════════════╝{self.imagen}╔════════════════════════════════════╗\n║ Jueguemos otro día! ║\n╚════════════════════════════════════╝\n"
        )
    

#Crear una instancia de MascotaVirtual
interfaz_inicio = "\n╔════════════════════════════════════╗\n║       Bienvenido a tu primer       ║\n║          mascota virtual!          ║\n╚════════════════════════════════════╝\n"
interfaz_juego = "\n╔════════════════════════════════════╗\n║       Opciones disponibles:        ║\n║                                    ║\n║ 1 - Alimentar                      ║\n║ 2 - Jugar                          ║\n║ 3 - Mostrar informacion            ║\n║ 4 - Salir                          ║\n║                                    ║\n╚════════════════════════════════════╝\n"

print(interfaz_inicio)

nombre_mascota = input("Elige un nombre para tu mascota: ")
mascota = MascotaVirtual(nombre_mascota) #crea el objeto con el nombre
mascota.presentacion()

#investigar con switch+
while True:
    print(interfaz_juego)
    opcion = int(input("Ingrese una opcion: "))
    match opcion:
        case 1: 
            mascota.alimentar()
        case 2: 
            mascota.jugar()
        case 3: 
            mascota.estado_animo()
        case 4: 
            mascota.despedida()
            break

    


# Interactuar con la mascota virtual
# alimenta, juega y muestra su estado de animo
# repite esta accion al menos 8 veces

# Esto lo vamos a utilizar más adelante 😉