import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from operaciones.conversor import (
    binario_a_decimal,
    decimal_a_binario,
    decimal_a_octal,
    decimal_a_hexadecimal,
)


def convertir():
    num = entrada.get()
    sistema_origen = opcion_origen.get()
    sistema_destino = opcion_destino.get()

    try:
        if sistema_origen == "Binario":
            decimal = binario_a_decimal(num)
        elif sistema_origen == "Octal":
            decimal = int(num, 8)
        elif sistema_origen == "Decimal":
            decimal = int(num)
        elif sistema_origen == "Hexadecimal":
            decimal = int(num, 16)
        else:
            raise ValueError("Sistema de origen no reconocido")

        if sistema_destino == "Binario":
            resultado = decimal_a_binario(decimal)
        elif sistema_destino == "Octal":
            resultado = decimal_a_octal(decimal)
        elif sistema_destino == "Decimal":
            resultado = str(decimal)
        elif sistema_destino == "Hexadecimal":
            resultado = decimal_a_hexadecimal(decimal)
        else:
            raise ValueError("Sistema de destino no reconocido")

        resultado_var.set(f"Resultado {resultado}")

    except ValueError:
        messagebox.showerror("Error", "Número no válido para el sistema seleccionado")


def crear_ventana():
    ventana = ctk.CTk()  # Cambiamos a customtkinter
    ventana.title("Calculadora de Conversión de Sistema Numérico")

    # Crear ventana CTk
    ventana.geometry("400x400")
    ctk.set_appearance_mode("System")

    # Etiqueta y entrada para el número
    ctk.CTkLabel(ventana, text="Ingresa el número:").pack(pady=10)
    global entrada
    entrada = ctk.CTkEntry(ventana)
    entrada.pack(pady=10)

    # Sistema de origen
    ctk.CTkLabel(ventana, text="Sistema de origen:").pack(pady=5)
    global opcion_origen
    opcion_origen = ctk.StringVar(value="Binario")
    ctk.CTkOptionMenu(
        ventana,
        variable=opcion_origen,
        values=["Binario", "Octal", "Decimal", "Hexadecimal"],
    ).pack(pady=5)

    # Sistema de destino
    ctk.CTkLabel(ventana, text="Sistema de destino:").pack(pady=5)
    global opcion_destino
    opcion_destino = ctk.StringVar(value="Decimal")
    ctk.CTkOptionMenu(
        ventana,
        variable=opcion_destino,
        values=["Binario", "Octal", "Decimal", "Hexadecimal"],
    ).pack(pady=5)

    # Resultado y botón de conversión
    global resultado_var
    resultado_var = ctk.StringVar()
    ctk.CTkButton(ventana, text="Convertir", command=convertir).pack(pady=10)
    ctk.CTkLabel(ventana, textvariable=resultado_var, font=("Arial", 14)).pack(pady=20)

    ventana.mainloop()
