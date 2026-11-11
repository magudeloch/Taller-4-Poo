import math
import tkinter as tk
from tkinter import ttk

class CalculosNumericos:
    @staticmethod
    def logaritmo_neperiano(valor):
        if valor <= 0:
            raise ArithmeticError("El valor debe ser positivo para el logaritmo.")
        return math.log(valor)

    @staticmethod
    def raiz_cuadrada(valor):
        if valor < 0:
            raise ArithmeticError("El valor no puede ser negativo para la raíz.")
        return math.sqrt(valor)

    @staticmethod
    def pendiente(x1, y1, x2, y2):
        if x1 == x2:
            raise ZeroDivisionError("La pendiente es indefinida (división por cero).")
        return (y2 - y1) / (x2 - x1)

    @staticmethod
    def raices_cuadraticas(a, b, c):
        if a == 0:
            raise ValueError("El coeficiente 'a' no puede ser cero.")
        discriminante = (b**2) - (4*a*c)
        if discriminante < 0:
            raise ArithmeticError("La ecuación tiene raíces complejas.")
        r1 = (-b + math.sqrt(discriminante)) / (2*a)
        r2 = (-b - math.sqrt(discriminante)) / (2*a)
        return r1, r2

    @staticmethod
    def base_conversion(numero, base):
        if base < 2 or base > 36:
            raise ValueError("La base debe estar entre 2 y 36.")
        if numero < 0:
            raise ValueError("El número debe ser positivo.")
        if numero == 0:
            return "0"
        digitos = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        resultado = ""
        while numero > 0:
            resultado = digitos[numero % base] + resultado
            numero //= base
        return resultado

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ejercicio 6.6 - Múltiples Catch y Propuestos")
        self.geometry("500x350")
        
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        self._crear_pestana_basicas()
        self._crear_pestana_recta()
        self._crear_pestana_cuadratica()

    def _manejar_excepcion(self, label, func, *args):
        try:
            res = func(*args)
            label.config(text=f"Resultado: {res}", foreground="green")
        except ValueError as e:
            label.config(text=f"Error de Valor: {e}", foreground="red")
        except ArithmeticError as e:
            label.config(text=f"Error Matemático: {e}", foreground="red")
        except ZeroDivisionError as e:
            label.config(text=f"Error: {e}", foreground="red")
        except Exception as e:
            label.config(text="Error de formato en los campos.", foreground="red")

    def _crear_pestana_basicas(self):
        marco = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(marco, text="Log / Raíz")
        
        ttk.Label(marco, text="Valor Numérico:").grid(row=0, column=0, pady=10)
        entrada = ttk.Entry(marco)
        entrada.grid(row=0, column=1, pady=10)
        
        lbl_res = ttk.Label(marco, text="", wraplength=400)
        
        def calc_log():
            self._manejar_excepcion(lbl_res, CalculosNumericos.logaritmo_neperiano, float(entrada.get()))
            
        def calc_raiz():
            self._manejar_excepcion(lbl_res, CalculosNumericos.raiz_cuadrada, float(entrada.get()))

        ttk.Button(marco, text="Log Neperiano", command=calc_log).grid(row=1, column=0, pady=10)
        ttk.Button(marco, text="Raíz Cuadrada", command=calc_raiz).grid(row=1, column=1, pady=10)
        lbl_res.grid(row=2, column=0, columnspan=2, pady=10)

    def _crear_pestana_recta(self):
        marco = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(marco, text="Pendiente Recta")
        
        ttk.Label(marco, text="P1 (x1, y1):").grid(row=0, column=0)
        e_x1 = ttk.Entry(marco, width=8)
        e_x1.grid(row=0, column=1)
        e_y1 = ttk.Entry(marco, width=8)
        e_y1.grid(row=0, column=2)
        
        ttk.Label(marco, text="P2 (x2, y2):").grid(row=1, column=0, pady=5)
        e_x2 = ttk.Entry(marco, width=8)
        e_x2.grid(row=1, column=1)
        e_y2 = ttk.Entry(marco, width=8)
        e_y2.grid(row=1, column=2)

        lbl_res = ttk.Label(marco, text="")
        
        def calc_pendiente():
            self._manejar_excepcion(lbl_res, CalculosNumericos.pendiente, float(e_x1.get()), float(e_y1.get()), float(e_x2.get()), float(e_y2.get()))

        ttk.Button(marco, text="Calcular Pendiente", command=calc_pendiente).grid(row=2, column=0, columnspan=3, pady=15)
        lbl_res.grid(row=3, column=0, columnspan=3)

    def _crear_pestana_cuadratica(self):
        marco = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(marco, text="Raíces (ax²+bx+c)")
        
        ttk.Label(marco, text="a:").grid(row=0, column=0)
        e_a = ttk.Entry(marco, width=8)
        e_a.grid(row=0, column=1)
        ttk.Label(marco, text="b:").grid(row=0, column=2)
        e_b = ttk.Entry(marco, width=8)
        e_b.grid(row=0, column=3)
        ttk.Label(marco, text="c:").grid(row=0, column=4)
        e_c = ttk.Entry(marco, width=8)
        e_c.grid(row=0, column=5)

        lbl_res = ttk.Label(marco, text="", wraplength=400)
        
        def calc_raices():
            self._manejar_excepcion(lbl_res, CalculosNumericos.raices_cuadraticas, float(e_a.get()), float(e_b.get()), float(e_c.get()))

        ttk.Button(marco, text="Calcular Raíces", command=calc_raices).grid(row=1, column=0, columnspan=6, pady=15)
        lbl_res.grid(row=2, column=0, columnspan=6)

if __name__ == "__main__":
    App().mainloop()