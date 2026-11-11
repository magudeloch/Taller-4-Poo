import tkinter as tk
from tkinter import ttk, messagebox
import re

class Programador:
    def __init__(self, nombre, apellidos):
        self.nombre = EquipoMaraton.validar_texto(nombre, "Nombre")
        self.apellidos = EquipoMaraton.validar_texto(apellidos, "Apellidos")
        
    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

class EquipoMaraton:
    def __init__(self, nombre_equipo, universidad, lenguaje, pass1, pass2):
        self.nombre_equipo = nombre_equipo.strip()
        self.universidad = universidad.strip()
        self.lenguaje = lenguaje.strip()
        
        if not self.nombre_equipo or not self.universidad or not self.lenguaje:
            raise ValueError("Los datos del equipo no pueden estar vacíos.")
            
        self.password = self.validar_password(pass1, pass2)
        self.programadores = []
        
    @staticmethod
    def validar_texto(texto, campo):
        texto = texto.strip()
        if not texto:
            raise ValueError(f"El campo '{campo}' no puede estar vacío.")
        if any(c.isdigit() for c in texto):
            raise ValueError(f"El campo '{campo}' no puede contener números.")
        return texto

    @staticmethod
    def validar_password(p1, p2):
        if p1 != p2:
            raise ValueError("Las contraseñas no coinciden.")
        if len(p1) < 8:
            raise ValueError("La contraseña debe tener mínimo 8 caracteres.")
        if " " in p1:
            raise ValueError("La contraseña no debe tener espacios en blanco.")
        if not re.search(r'[A-Z]', p1):
            raise ValueError("La contraseña debe tener al menos una letra mayúscula.")
        if not re.search(r'\d', p1):
            raise ValueError("La contraseña debe tener al menos un número.")
        if not re.search(r'[^A-Za-z0-9]', p1):
            raise ValueError("La contraseña debe tener al menos un carácter especial.")
        return p1

    def anadir_programador(self, programador):
        if len(self.programadores) >= 3:
            raise OverflowError("El equipo ya está completo (Máximo 3 integrantes).")
        self.programadores.append(programador)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ejercicio 6.7 - Maratón y Contraseñas")
        self.geometry("500x550")
        self.equipo = None
        
        # --- Frame Equipo ---
        f_equipo = ttk.LabelFrame(self, text="Datos del Equipo y Seguridad", padding=10)
        f_equipo.pack(fill="x", padx=10, pady=5)
        
        ttk.Label(f_equipo, text="Equipo:").grid(row=0, column=0, sticky="e")
        self.e_equipo = ttk.Entry(f_equipo)
        self.e_equipo.grid(row=0, column=1, pady=2)
        
        ttk.Label(f_equipo, text="Universidad:").grid(row=1, column=0, sticky="e")
        self.e_univ = ttk.Entry(f_equipo)
        self.e_univ.grid(row=1, column=1, pady=2)
        
        ttk.Label(f_equipo, text="Lenguaje:").grid(row=2, column=0, sticky="e")
        self.e_leng = ttk.Entry(f_equipo)
        self.e_leng.grid(row=2, column=1, pady=2)
        
        ttk.Label(f_equipo, text="Contraseña:").grid(row=0, column=2, sticky="e")
        self.e_pass1 = ttk.Entry(f_equipo, show="*")
        self.e_pass1.grid(row=0, column=3, pady=2, padx=5)
        
        ttk.Label(f_equipo, text="Confirmar:").grid(row=1, column=2, sticky="e")
        self.e_pass2 = ttk.Entry(f_equipo, show="*")
        self.e_pass2.grid(row=1, column=3, pady=2, padx=5)
        
        ttk.Button(f_equipo, text="Registrar Equipo", command=self._crear_equipo).grid(row=3, column=0, columnspan=4, pady=10)
        
        # --- Frame Integrantes ---
        self.f_int = ttk.LabelFrame(self, text="Integrantes", padding=10)
        self.f_int.pack(fill="both", expand=True, padx=10, pady=5)
        
        ttk.Label(self.f_int, text="Nombre:").grid(row=0, column=0, sticky="e")
        self.e_nom = ttk.Entry(self.f_int)
        self.e_nom.grid(row=0, column=1, pady=2)
        
        ttk.Label(self.f_int, text="Apellidos:").grid(row=0, column=2, sticky="e")
        self.e_ape = ttk.Entry(self.f_int)
        self.e_ape.grid(row=0, column=3, pady=2, padx=5)
        
        ttk.Button(self.f_int, text="Añadir Integrante", command=self._anadir).grid(row=1, column=0, columnspan=4, pady=10)
        
        self.lista = tk.Listbox(self.f_int, height=5)
        self.lista.grid(row=2, column=0, columnspan=4, sticky="we")

    def _crear_equipo(self):
        try:
            self.equipo = EquipoMaraton(self.e_equipo.get(), self.e_univ.get(), self.e_leng.get(), self.e_pass1.get(), self.e_pass2.get())
            messagebox.showinfo("Éxito", "Equipo creado y contraseña validada correctamente.")
            self.lista.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Error de Validación", str(e))

    def _anadir(self):
        if not self.equipo:
            messagebox.showwarning("Atención", "Primero debe registrar el equipo.")
            return
        try:
            prog = Programador(self.e_nom.get(), self.e_ape.get())
            self.equipo.anadir_programador(prog)
            self.lista.insert(tk.END, str(prog))
            self.e_nom.delete(0, tk.END)
            self.e_ape.delete(0, tk.END)
        except (ValueError, OverflowError) as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    App().mainloop()