import tkinter as tk
from tkinter import ttk

class PruebaExcepcionesGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ejercicio 6.4 - Prueba de Excepciones")
        self.geometry("500x350")
        self.resizable(False, False)

        ttk.Label(self, text="Simulador de Excepciones", font=("Arial", 12, "bold")).pack(pady=10)

        frame_botones = ttk.Frame(self)
        frame_botones.pack(pady=10)

        ttk.Button(frame_botones, text="1. División por Cero", command=self.excepcion_aritmetica).grid(row=0, column=0, padx=5)
        ttk.Button(frame_botones, text="2. Objeto Nulo", command=self.excepcion_general).grid(row=0, column=1, padx=5)

        ttk.Button(self, text="Limpiar Consola", command=self.limpiar).pack(pady=5)

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

    def excepcion_aritmetica(self):
        try:
            self.log("Ingresando al primer try...")
            cociente = 10000 / 0
        except ZeroDivisionError:
            self.log(">> Error capturado: División por cero.")
        finally:
            self.log("Ingresando al primer finally.\n")

    def excepcion_general(self):
        try:
            self.log("Ingresando al segundo try...")
            objeto = None
            objeto.toString()
        except AttributeError:
            self.log(">> Error capturado: Ocurrió una excepción general.")
        finally:
            self.log("Ingresando al segundo finally.\n")

if __name__ == "__main__":
    app = PruebaExcepcionesGUI()
    app.mainloop()