import random
import string
import pyperclip  # Para copiar al portapapeles
import re
import tkinter as tk
from tkinter import messagebox


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


def generar_contraseña_gui():
    try:
        mayúsculas = var_mayúsculas.get()
        minúsculas = var_minúsculas.get()
        números = var_números.get()
        símbolos = var_símbolos.get()
        longitud_min = int(entry_longitud_min.get())
        longitud_max = int(entry_longitud_max.get())

        # Validación de longitud mínima y máxima
        if longitud_min < 8 or longitud_min > 32:
            raise ValueError("La longitud mínima debe ser entre 8 y 32")
        if longitud_max < 8 or longitud_max > 32:
            raise ValueError("La longitud máxima debe ser entre 8 y 32")
        if longitud_min > longitud_max:
            raise ValueError("La longitud mínima no puede ser mayor que la máxima")

        generador = GeneradorDeContraseñas(
            mayúsculas=mayúsculas,
            minúsculas=minúsculas,
            números=números,
            símbolos=símbolos,
            longitud_min=longitud_min,
            longitud_max=longitud_max
        )

        contraseña = generador.generar_contraseña()
        label_resultado.config(text=f"Contraseña: {contraseña.contraseña}\nLongitud: {contraseña.longitud}\nSeguridad: {contraseña.seguridad}")

        # Habilitar botón de copiar
        btn_copiar.config(state="normal", command=lambda: copiar_contraseña(contraseña.contraseña))

    except ValueError as e:
        messagebox.showerror("Error", str(e))


def copiar_contraseña(contraseña):
    pyperclip.copy(contraseña)  # Copia la contraseña al portapapeles
    messagebox.showinfo("Copiado", "La contraseña ha sido copiada al portapapeles")


def verificar_contraseña_gui():
    contraseña = entry_verificar.get()
    generador = GeneradorDeContraseñas(
        mayúsculas=False,
        minúsculas=False,
        números=False,
        símbolos=False,
        longitud_min=0,
        longitud_max=0
    )
    seguridad = generador.verificar_seguridad(contraseña)
    messagebox.showinfo("Resultado de la verificación", seguridad)


# Configuración de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Generador y Verificador de Contraseñas")

# Agregar título dentro de la interfaz
label_titulo = tk.Label(ventana, text="Generador y Verificador de Contraseñas", font=("Arial", 16, "bold"))
label_titulo.pack(pady=10)

# Generación de contraseña
frame_generar = tk.Frame(ventana)
frame_generar.pack(padx=10, pady=10)

label_mayúsculas = tk.Label(frame_generar, text="¿Incluir mayúsculas?")
label_mayúsculas.grid(row=0, column=0, sticky="w")
var_mayúsculas = tk.BooleanVar()
check_mayúsculas = tk.Checkbutton(frame_generar, variable=var_mayúsculas)
check_mayúsculas.grid(row=0, column=1)

label_minúsculas = tk.Label(frame_generar, text="¿Incluir minúsculas?")
label_minúsculas.grid(row=1, column=0, sticky="w")
var_minúsculas = tk.BooleanVar()
check_minúsculas = tk.Checkbutton(frame_generar, variable=var_minúsculas)
check_minúsculas.grid(row=1, column=1)

label_números = tk.Label(frame_generar, text="¿Incluir números?")
label_números.grid(row=2, column=0, sticky="w")
var_números = tk.BooleanVar()
check_números = tk.Checkbutton(frame_generar, variable=var_números)
check_números.grid(row=2, column=1)

label_símbolos = tk.Label(frame_generar, text="¿Incluir símbolos?")
label_símbolos.grid(row=3, column=0, sticky="w")
var_símbolos = tk.BooleanVar()
check_símbolos = tk.Checkbutton(frame_generar, variable=var_símbolos)
check_símbolos.grid(row=3, column=1)

label_longitud_min = tk.Label(frame_generar, text="Longitud mínima:")
label_longitud_min.grid(row=4, column=0, sticky="w")
entry_longitud_min = tk.Entry(frame_generar)
entry_longitud_min.grid(row=4, column=1)

label_longitud_max = tk.Label(frame_generar, text="Longitud máxima:")
label_longitud_max.grid(row=5, column=0, sticky="w")
entry_longitud_max = tk.Entry(frame_generar)
entry_longitud_max.grid(row=5, column=1)

btn_generar = tk.Button(frame_generar, text="Generar Contraseña", command=generar_contraseña_gui)
btn_generar.grid(row=6, column=0, columnspan=2, pady=10)

label_resultado = tk.Label(frame_generar, text="Contraseña: ")
label_resultado.grid(row=7, column=0, columnspan=2)

btn_copiar = tk.Button(frame_generar, text="Copiar al portapapeles", state="disabled")
btn_copiar.grid(row=8, column=0, columnspan=2, pady=10)

# Verificación de contraseña
frame_verificar = tk.Frame(ventana)
frame_verificar.pack(padx=10, pady=10)

label_verificar = tk.Label(frame_verificar, text="Introduce la contraseña a verificar:")
label_verificar.grid(row=0, column=0, sticky="w")
entry_verificar = tk.Entry(frame_verificar, show="*")
entry_verificar.grid(row=0, column=1)

btn_verificar = tk.Button(frame_verificar, text="Verificar Contraseña", command=verificar_contraseña_gui)
btn_verificar.grid(row=1, column=0, columnspan=2, pady=10)

ventana.mainloop()


