import math
import tkinter as tk
from tkinter import ttk

class CalculosNumericos:
    @staticmethod
    def logaritmo_neperiano(valor):
        if valor < 0:
            raise ArithmeticError("El valor debe ser un número positivo.")
        return math.log(valor)

    @staticmethod
    def raiz_cuadrada(valor):
        if valor < 0:
            raise ArithmeticError("El valor debe ser un número positivo.")
        return math.sqrt(valor)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ejercicio 6.6 - Catchs Múltiples")
        self.geometry("400x250")
        
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.crear_pestana("Logaritmo Neperiano", CalculosNumericos.logaritmo_neperiano, "calcular el logaritmo")
        self.crear_pestana("Raíz Cuadrada", CalculosNumericos.raiz_cuadrada, "calcular la raíz cuadrada")

    def crear_pestana(self, titulo, funcion, operacion_texto):
        marco = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(marco, text=titulo)
        
        ttk.Label(marco, text="Valor numérico:").grid(row=0, column=0, pady=10)
        entrada = ttk.Entry(marco)
        entrada.grid(row=0, column=1, pady=10)
        
        lbl_res = ttk.Label(marco, text="", wraplength=350)
        
        def calcular():
            try:
                valor_texto = entrada.get()
                valor = float(valor_texto)
                res = funcion(valor)
                lbl_res.config(text=f"Resultado = {res:.4f}", foreground="green")
            except ValueError:
                lbl_res.config(text=f"El valor debe ser numérico para {operacion_texto}", foreground="red")
            except ArithmeticError as e:
                lbl_res.config(text=f"{str(e)} para {operacion_texto}", foreground="red")

        ttk.Button(marco, text="Calcular", command=calcular).grid(row=1, column=0, columnspan=2, pady=10)
        lbl_res.grid(row=2, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    App().mainloop()