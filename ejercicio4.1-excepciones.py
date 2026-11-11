import tkinter as tk
from tkinter import ttk

class PruebaExcepcionesGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ejercicio 6.4 - Prueba de Excepciones")
        self.geometry("500x350")
        self.resizable(False, False)

        ttk.Label(self, text="Simulador de Excepciones (Base y Propuestos)", font=("Arial", 12, "bold")).pack(pady=10)

        # Marco de botones
        frame_botones = ttk.Frame(self)
        frame_botones.pack(pady=10)

        ttk.Button(frame_botones, text="1. División por Cero (Base)", command=self.excepcion_aritmetica).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(frame_botones, text="2. Objeto Nulo (Base)", command=self.excepcion_general).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(frame_botones, text="3. Fuera de Límite (Propuesto)", command=self.excepcion_fuera_limite).grid(row=1, column=0, padx=5, pady=5)
        ttk.Button(frame_botones, text="4. Formato Número (Propuesto)", command=self.excepcion_formato).grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(self, text="Limpiar Consola", command=self.limpiar).pack(pady=5)

        # Consola de salida
        self.consola = tk.Text(self, height=10, width=55, state="disabled", bg="#1e1e1e", fg="#00ff00")
        self.consola.pack(pady=10)

    def log(self, mensaje):
        self.consola.config(state="normal")
        self.consola.insert(tk.END, mensaje + "\n")
        self.consola.see(tk.END)
        self.consola.config(state="disabled")

    def limpiar(self):
        self.consola.config(state="normal")
        self.consola.delete(1.0, tk.END)
        self.consola.config(state="disabled")

    # 1. Simula el bloque try/catch de división por cero
    def excepcion_aritmetica(self):
        try:
            self.log("Ingresando al primer try (Aritmética)...")
            cociente = 10000 / 0
        except ZeroDivisionError:
            self.log(">> Error capturado: División por cero.")
        finally:
            self.log("Ingresando al finally de Aritmética.\n")

    # 2. Simula el bloque try/catch de un objeto nulo llamando un método
    def excepcion_general(self):
        try:
            self.log("Ingresando al try (Objeto Nulo)...")
            objeto = None
            objeto.toString()
        except AttributeError:
            self.log(">> Error capturado: Ocurrió una excepción general (Objeto es None).")
        finally:
            self.log("Ingresando al finally de Objeto Nulo.\n")

    # 3. Simula la excepción StringIndexOutOfBoundsException (Propuesto)
    def excepcion_fuera_limite(self):
        try:
            self.log("Ingresando al try (Fuera de límite)...")
            texto = "Programación"
            caracter = texto[14] # El índice máximo es 11
        except IndexError:
            self.log(">> Error capturado: Índice de string por fuera del límite.")
        finally:
            self.log("Ingresando al finally de Fuera de límite.\n")

    # 4. Simula la excepción NumberFormatException (Propuesto)
    def excepcion_formato(self):
        try:
            self.log("Ingresando al try (Formato de Número)...")
            numero = int("Número")
        except ValueError:
            self.log(">> Error capturado: Excepción de formato de número.")
        finally:
            self.log("Ingresando al finally de Formato de Número.\n")

if __name__ == "__main__":
    app = PruebaExcepcionesGUI()
    app.mainloop()