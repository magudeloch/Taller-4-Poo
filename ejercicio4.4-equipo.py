import tkinter as tk
from tkinter import ttk, messagebox

class Programador:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
        
    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

class EquipoMaratonProgramacion:
    def __init__(self, nombre_equipo, universidad, lenguaje):
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje_programacion = lenguaje
        self.programadores = []
        self.tamano_equipo = 0
        
    def esta_lleno(self):
        return self.tamano_equipo == 3

    def anadir(self, programador):
        if self.esta_lleno():
            raise Exception("El equipo está completo. No se pudo agregar programador.")
        self.programadores.append(programador)
        self.tamano_equipo += 1

    @staticmethod
    def validar_campo(campo):
        if len(campo) > 20:
            raise Exception("La longitud no debe ser superior a 20 caracteres.")
        for c in campo:
            if c.isdigit():
                raise Exception("El nombre no puede tener dígitos.")

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ejercicio 6.7 - Maratón")
        self.geometry("450x450")
        self.equipo = None
        
        f_equipo = ttk.LabelFrame(self, text="Datos del Equipo", padding=10)
        f_equipo.pack(fill="x", padx=10, pady=5)
        
        ttk.Label(f_equipo, text="Nombre del equipo:").grid(row=0, column=0, sticky="e")
        self.e_equipo = ttk.Entry(f_equipo)
        self.e_equipo.grid(row=0, column=1)
        
        ttk.Label(f_equipo, text="Universidad:").grid(row=1, column=0, sticky="e")
        self.e_univ = ttk.Entry(f_equipo)
        self.e_univ.grid(row=1, column=1)
        
        ttk.Label(f_equipo, text="Lenguaje de programación:").grid(row=2, column=0, sticky="e")
        self.e_leng = ttk.Entry(f_equipo)
        self.e_leng.grid(row=2, column=1)
        
        ttk.Button(f_equipo, text="Crear equipo", command=self.crear_equipo).grid(row=3, column=0, columnspan=2, pady=10)
        
        self.f_int = ttk.LabelFrame(self, text="Datos de los integrantes", padding=10)
        self.f_int.pack(fill="both", expand=True, padx=10, pady=5)
        
        ttk.Label(self.f_int, text="Nombre del integrante:").grid(row=0, column=0, sticky="e")
        self.e_nom = ttk.Entry(self.f_int)
        self.e_nom.grid(row=0, column=1)
        
        ttk.Label(self.f_int, text="Apellidos del integrante:").grid(row=1, column=0, sticky="e")
        self.e_ape = ttk.Entry(self.f_int)
        self.e_ape.grid(row=1, column=1)
        
        ttk.Button(self.f_int, text="Añadir integrante", command=self.anadir).grid(row=2, column=0, columnspan=2, pady=10)
        
        self.lbl_equipo = ttk.Label(self.f_int, text="", foreground="blue")
        self.lbl_equipo.grid(row=3, column=0, columnspan=2)
        
        self.lista = tk.Listbox(self.f_int, height=4)
        self.lista.grid(row=4, column=0, columnspan=2, sticky="we")

    def crear_equipo(self):
        self.equipo = EquipoMaratonProgramacion(self.e_equipo.get(), self.e_univ.get(), self.e_leng.get())
        self.lbl_equipo.config(text=f"Equipo creado: {self.equipo.nombre_equipo}")
        self.lista.delete(0, tk.END)

    def anadir(self):
        if not self.equipo:
            messagebox.showwarning("Atención", "Primero cree el equipo.")
            return
        try:
            nombre = self.e_nom.get()
            apellidos = self.e_ape.get()
            
            EquipoMaratonProgramacion.validar_campo(nombre)
            EquipoMaratonProgramacion.validar_campo(apellidos)
            
            prog = Programador(nombre, apellidos)
            self.equipo.anadir(prog)
            self.lista.insert(tk.END, str(prog))
            self.e_nom.delete(0, tk.END)
            self.e_ape.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    App().mainloop()