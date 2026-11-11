import tkinter as tk
from tkinter import ttk, messagebox

class Vendedor:
    def __init__(self, nombre, apellidos, edad):
        if not nombre or not apellidos:
            raise ValueError("El nombre y apellidos no pueden estar vacíos (Excepción de constructor).")
        if edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 años.")
        if edad > 120:
            raise ValueError("La edad no puede ser mayor a 120 años.")
        
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def imprimir(self):
        return f"Vendedor registrado:\nNombre: {self.nombre}\nApellidos: {self.apellidos}\nEdad: {self.edad}"

class TablaASCII:
    def __init__(self):
        self.tabla = {}

    def set_simbolo(self, simbolo, numero):
        if not simbolo:
            raise ValueError("El símbolo no puede ser nulo o vacío.")
        self.tabla[simbolo] = numero

    def get_simbolo(self, simbolo):
        if not simbolo:
            raise ValueError("El símbolo no puede ser nulo.")
        if simbolo not in self.tabla:
            raise KeyError(f"El símbolo '{simbolo}' no existe en la tabla ASCII.")
        return self.tabla[simbolo]

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ejercicio 6.5 - Vendedor y Tabla ASCII")
        self.geometry("450x350")
        
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.tabla_ascii = TablaASCII()
        self._crear_pestana_vendedor()
        self._crear_pestana_ascii()

    def _crear_pestana_vendedor(self):
        marco = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(marco, text="Vendedor")
        
        ttk.Label(marco, text="Nombre:").grid(row=0, column=0, sticky="e", pady=5)
        self.ent_nombre = ttk.Entry(marco)
        self.ent_nombre.grid(row=0, column=1, pady=5)
        
        ttk.Label(marco, text="Apellidos:").grid(row=1, column=0, sticky="e", pady=5)
        self.ent_apellidos = ttk.Entry(marco)
        self.ent_apellidos.grid(row=1, column=1, pady=5)
        
        ttk.Label(marco, text="Edad:").grid(row=2, column=0, sticky="e", pady=5)
        self.ent_edad = ttk.Entry(marco)
        self.ent_edad.grid(row=2, column=1, pady=5)
        
        ttk.Button(marco, text="Registrar Vendedor", command=self._registrar_vendedor).grid(row=3, column=0, columnspan=2, pady=15)
        
        self.lbl_res_vendedor = ttk.Label(marco, text="", foreground="blue")
        self.lbl_res_vendedor.grid(row=4, column=0, columnspan=2)

    def _registrar_vendedor(self):
        try:
            edad_str = self.ent_edad.get()
            if not edad_str.isdigit():
                raise ValueError("La edad debe ser un número entero.")
            vendedor = Vendedor(self.ent_nombre.get(), self.ent_apellidos.get(), int(edad_str))
            self.lbl_res_vendedor.config(text=vendedor.imprimir(), foreground="green")
        except ValueError as e:
            self.lbl_res_vendedor.config(text=f"Error: {str(e)}", foreground="red")

    def _crear_pestana_ascii(self):
        marco = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(marco, text="Tabla ASCII")
        
        ttk.Label(marco, text="Símbolo:").grid(row=0, column=0, sticky="e", pady=5)
        self.ent_simbolo = ttk.Entry(marco, width=10)
        self.ent_simbolo.grid(row=0, column=1, pady=5, sticky="w")
        
        ttk.Label(marco, text="Número asociado:").grid(row=1, column=0, sticky="e", pady=5)
        self.ent_numero = ttk.Entry(marco, width=10)
        self.ent_numero.grid(row=1, column=1, pady=5, sticky="w")
        
        ttk.Button(marco, text="Guardar Símbolo (SET)", command=self._set_ascii).grid(row=2, column=0, pady=15)
        ttk.Button(marco, text="Buscar Símbolo (GET)", command=self._get_ascii).grid(row=2, column=1, pady=15)
        
        self.lbl_res_ascii = ttk.Label(marco, text="", foreground="blue")
        self.lbl_res_ascii.grid(row=3, column=0, columnspan=2)

    def _set_ascii(self):
        try:
            num = int(self.ent_numero.get())
            self.tabla_ascii.set_simbolo(self.ent_simbolo.get(), num)
            self.lbl_res_ascii.config(text="Símbolo guardado correctamente.", foreground="green")
        except ValueError as e:
            self.lbl_res_ascii.config(text="Error: Ingrese un símbolo y un número válido.", foreground="red")

    def _get_ascii(self):
        try:
            simbolo = self.ent_simbolo.get()
            num = self.tabla_ascii.get_simbolo(simbolo)
            self.lbl_res_ascii.config(text=f"El valor ASCII de '{simbolo}' es {num}.", foreground="green")
        except (ValueError, KeyError) as e:
            self.lbl_res_ascii.config(text=f"Error: {str(e)}", foreground="red")

if __name__ == "__main__":
    App().mainloop()