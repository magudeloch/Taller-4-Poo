import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class LectorArchivo:
    @staticmethod
    def leer_en_mayusculas(ruta):
        if not ruta:
            raise ValueError("No se ha seleccionado ninguna ruta de archivo.")
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
                return contenido.upper()
        except FileNotFoundError:
            raise IOError("No se encontró el archivo especificado en la ruta.")
        except (OSError, UnicodeDecodeError):
            raise IOError("No se pudo leer el formato del archivo.")

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ejercicio 6.8 - Lectura y Mayúsculas")
        self.geometry("600x450")
        
        marco_sup = ttk.Frame(self, padding=10)
        marco_sup.pack(fill="x")
        
        ttk.Label(marco_sup, text="Ruta del archivo:").pack(side="left")
        self.ent_ruta = ttk.Entry(marco_sup, width=40)
        self.ent_ruta.pack(side="left", padx=10)
        
        ttk.Button(marco_sup, text="Examinar...", command=self._examinar).pack(side="left", padx=5)
        ttk.Button(marco_sup, text="Leer y Convertir", command=self._leer).pack(side="left")
        
        marco_txt = ttk.Frame(self, padding=10)
        marco_txt.pack(fill="both", expand=True)
        
        self.txt_salida = tk.Text(marco_txt, wrap="word", state="disabled", font=("Consolas", 10))
        scroll = ttk.Scrollbar(marco_txt, command=self.txt_salida.yview)
        self.txt_salida.config(yscrollcommand=scroll.set)
        
        scroll.pack(side="right", fill="y")
        self.txt_salida.pack(side="left", fill="both", expand=True)

    def _examinar(self):
        ruta = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
        if ruta:
            self.ent_ruta.delete(0, tk.END)
            self.ent_ruta.insert(0, ruta)

    def _leer(self):
        try:
            ruta = self.ent_ruta.get().strip()
            texto_mayusculas = LectorArchivo.leer_en_mayusculas(ruta)
            
            self.txt_salida.config(state="normal")
            self.txt_salida.delete("1.0", tk.END)
            self.txt_salida.insert(tk.END, texto_mayusculas)
            self.txt_salida.config(state="disabled")
            
        except ValueError as e:
            messagebox.showwarning("Atención", str(e))
        except IOError as e:
            messagebox.showerror("Error de Lectura", str(e))

if __name__ == "__main__":
    App().mainloop()