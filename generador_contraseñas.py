import random
import string
import pyperclip  # Para copiar al portapapeles
import re

class Contraseña:
    def __init__(self, contraseña, longitud, seguridad):
        self.contraseña = contraseña
        self.longitud = longitud
        self.seguridad = seguridad


class GeneradorDeContraseñas:
    def __init__(self, mayúsculas, minúsculas, números, símbolos, longitud_min, longitud_max):
        self.mayúsculas = mayúsculas
        self.minúsculas = minúsculas
        self.números = números
        self.símbolos = símbolos
        self.longitug_min = longitud_min
        self.longitud_max = longitud_max

    def generar_contraseña(self):
        caracteres_disponibles = ""

        if self.mayúsculas:
            caracteres_disponibles += string.ascii_uppercase  # A-Z
        if self.minúsculas:
            caracteres_disponibles += string.ascii_lowercase  # a-z
        if self.números:
            caracteres_disponibles += string.digits  # 0-9
        if self.símbolos:
            caracteres_disponibles += string.punctuation  # ! " # $ % & ...

        if not caracteres_disponibles:
            raise ValueError("Debe seleccionar al menos un tipo de carácter (mayúsculas, minúsculas, números o símbolos)")

        longitud = random.randint(self.longitug_min, self.longitud_max)
        contraseña = ''.join(random.choice(caracteres_disponibles) for _ in range(longitud))

        seguridad = "Alta" if longitud >= 12 and (self.mayúsculas and self.minúsculas and self.números and self.símbolos) else "Media"

        return Contraseña(contraseña, longitud, seguridad)

    def verificar_seguridad(self, contraseña):
        """
        Verifica la seguridad de la contraseña. Los criterios son:
        - Longitud mínima de 8 caracteres.
        - Debe contener al menos una letra mayúscula, una minúscula, un número y un símbolo.
        """
        if len(contraseña) < 8:
            return "Contraseña débil (menos de 8 caracteres)"
        
        if not re.search(r"[A-Z]", contraseña):  # Al menos una mayúscula
            return "Contraseña débil (falta una mayúscula)"
        if not re.search(r"[a-z]", contraseña):  # Al menos una minúscula
            return "Contraseña débil (falta una minúscula)"
        if not re.search(r"[0-9]", contraseña):  # Al menos un número
            return "Contraseña débil (falta un número)"
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", contraseña):  # Al menos un símbolo
            return "Contraseña débil (falta un símbolo)"

        return "Contraseña segura"


def menu_principal():
    while True:
        print("\n****************** Menú Principal ******************")
        print("1. Generar una nueva contraseña")
        print("2. Verificar la seguridad de una contraseña")
        print("3. Salir")
        print("*****************************************************")
        
        opción = input("Seleccione una opción (1, 2, o 3): ")

        if opción == "1":
            generar_contraseña()
        elif opción == "2":
            verificar_contraseña()
        elif opción == "3":
            print("¡Hasta luego! Gracias por usar el generador de contraseñas.")
            break
        else:
            print("Opción no válida. Por favor, elija una opción entre 1, 2 o 3.")


def generar_contraseña():
    print("\nGenerador de Contraseñas:")
    mayúsculas = input("¿Quieres incluir mayúsculas? (s/n): ").lower() == "s"
    minúsculas = input("¿Quieres incluir minúsculas? (s/n): ").lower() == "s"
    números = input("¿Quieres incluir números? (s/n): ").lower() == "s"
    símbolos = input("¿Quieres incluir símbolos? (s/n): ").lower() == "s"
    longitud_min = int(input("¿Cuál es la longitud mínima de la contraseña? (por ejemplo, 8): "))
    longitud_max = int(input("¿Cuál es la longitud máxima de la contraseña? (por ejemplo, 16): "))

    generador = GeneradorDeContraseñas(
        mayúsculas=mayúsculas,
        minúsculas=minúsculas,
        números=números,
        símbolos=símbolos,
        longitud_min=longitud_min,
        longitud_max=longitud_max
    )

    contraseña = generador.generar_contraseña()

    print(f"\nContraseña generada: {contraseña.contraseña}")
    print(f"Longitud: {contraseña.longitud}")
    print(f"Seguridad: {contraseña.seguridad}")

    copiar = input("\n¿Quieres copiar la contraseña al portapapeles? (s/n): ").lower()
    if copiar == "s":
        pyperclip.copy(contraseña.contraseña)
        print("La contraseña ha sido copiada al portapapeles.")


def verificar_contraseña():
    print("\nVerificador de Contraseñas:")
    contraseña = input("Introduce la contraseña para verificar su seguridad: ")
    
    generador = GeneradorDeContraseñas(
        mayúsculas=False,  
        minúsculas=False,
        números=False,
        símbolos=False,
        longitud_min=0,
        longitud_max=0
    )

    seguridad = generador.verificar_seguridad(contraseña)
    print(f"Resultado de la verificación: {seguridad}")


if __name__ == "__main__":
    menu_principal()
