import tkinter as tk
from tkinter import ttk, filedialog

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ejercicio 6.8 - Lectura de Archivos")
        self.geometry("500x400")
        
        marco_sup = ttk.Frame(self, padding=10)
        marco_sup.pack(fill="x")
        
        ttk.Label(marco_sup, text="Nombre del archivo:").pack(side="left")
        self.ent_ruta = ttk.Entry(marco_sup, width=30)
        self.ent_ruta.insert(0, "C:/prueba.txt")
        self.ent_ruta.pack(side="left", padx=10)
        
        ttk.Button(marco_sup, text="Examinar...", command=self.examinar).pack(side="left")
        
        ttk.Button(self, text="Leer archivo", command=self.leer).pack(pady=5)
        
        marco_txt = ttk.Frame(self, padding=10)
        marco_txt.pack(fill="both", expand=True)
        
        self.txt_salida = tk.Text(marco_txt, wrap="word", state="disabled", font=("Consolas", 10))
        scroll = ttk.Scrollbar(marco_txt, command=self.txt_salida.yview)
        self.txt_salida.config(yscrollcommand=scroll.set)
        
        scroll.pack(side="right", fill="y")
        self.txt_salida.pack(side="left", fill="both", expand=True)

    def examinar(self):
        ruta = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
        if ruta:
            self.ent_ruta.delete(0, tk.END)
            self.ent_ruta.insert(0, ruta)

    def leer(self):
        try:
            ruta = self.ent_ruta.get().strip()
            with open(ruta, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
                
            self.txt_salida.config(state="normal")
            self.txt_salida.delete("1.0", tk.END)
            self.txt_salida.insert(tk.END, contenido)
            self.txt_salida.config(state="disabled")
        except FileNotFoundError:
            self.mostrar_error("No se pudo leer el archivo.")
        except Exception:
            self.mostrar_error("No se pudo leer el archivo.")

    def mostrar_error(self, mensaje):
        self.txt_salida.config(state="normal")
        self.txt_salida.delete("1.0", tk.END)
        self.txt_salida.insert(tk.END, mensaje)
        self.txt_salida.config(state="disabled")

if __name__ == "__main__":
    App().mainloop()