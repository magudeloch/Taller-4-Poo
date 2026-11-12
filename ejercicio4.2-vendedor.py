import tkinter as tk
from tkinter import ttk, messagebox

class Vendedor:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = 0

    def verificar_edad(self, edad):
        if edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 años.")
        if edad >= 0 and edad < 120:
            self.edad = edad
        else:
            raise ValueError("La edad no puede ser negativa ni mayor a 120.")

    def imprimir(self):
        return f"Vendedor registrado:\nNombre: {self.nombre}\nApellidos: {self.apellidos}\nEdad: {self.edad}"

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ejercicio 6.5 - Vendedor")
        self.geometry("400x300")
        
        marco = ttk.LabelFrame(self, text="Datos del Vendedor", padding=15)
        marco.pack(fill="both", expand=True, padx=10, pady=10)
        
        ttk.Label(marco, text="Nombre:").grid(row=0, column=0, sticky="e", pady=5)
        self.ent_nombre = ttk.Entry(marco)
        self.ent_nombre.grid(row=0, column=1, pady=5)
        
        ttk.Label(marco, text="Apellidos:").grid(row=1, column=0, sticky="e", pady=5)
        self.ent_apellidos = ttk.Entry(marco)
        self.ent_apellidos.grid(row=1, column=1, pady=5)
        
        ttk.Label(marco, text="Edad:").grid(row=2, column=0, sticky="e", pady=5)
        self.ent_edad = ttk.Entry(marco)
        self.ent_edad.grid(row=2, column=1, pady=5)
        
        ttk.Button(marco, text="Verificar edad e imprimir", command=self.registrar_vendedor).grid(row=3, column=0, columnspan=2, pady=15)
        
        self.lbl_res = ttk.Label(marco, text="", foreground="blue", justify="left")
        self.lbl_res.grid(row=4, column=0, columnspan=2)

    def registrar_vendedor(self):
        try:
            nombre = self.ent_nombre.get()
            apellidos = self.ent_apellidos.get()
            edad_str = self.ent_edad.get()
            
            if not edad_str.isdigit():
                raise ValueError("La edad debe ser un número entero.")
                
            vendedor = Vendedor(nombre, apellidos)
            vendedor.verificar_edad(int(edad_str))
            
            self.lbl_res.config(text=vendedor.imprimir(), foreground="green")
        except ValueError as e:
            self.lbl_res.config(text=f"Excepción de argumento ilegal:\n{str(e)}", foreground="red")

if __name__ == "__main__":
    App().mainloop()