import tkinter as tk
from PIL import Image, ImageTk
import analyzers.lexical_analyzer as lexical
import analyzers.syntax_analyzer as syntax
import sys
import ply.yacc as yacc
import os
import datetime

class TextComponent:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, string):
        self.text_widget.config(state=tk.NORMAL)  # Habilitar escritura
        self.text_widget.insert(tk.END, string)
        self.text_widget.see(tk.END)
        self.text_widget.config(state=tk.DISABLED)  # Deshabilitar escritura

log_username = "default_user"

def edit_username():
    """Ventana emergente para editar el nombre de usuario."""
    def save_username():
        global log_username
        log_username = username_entry.get()
        username_window.destroy()

    username_window = tk.Toplevel(root)
    username_window.title("Editar Nombre de Usuario")
    username_window.geometry("300x150")
    username_window.configure(bg="#2C3E50")

    label = tk.Label(username_window, text="Ingrese su nombre de usuario:", bg="#2C3E50", fg="white", font=("Arial", 12))
    label.pack(pady=10)

    username_entry = tk.Entry(username_window, font=("Arial", 12))
    username_entry.pack(pady=5)

    save_button = tk.Button(username_window, text="Guardar", command=save_username, bg="green", fg="white", font=("Arial", 10))
    save_button.pack(pady=10)

def run_TypeScript(text_input):
    console_text.config(state=tk.NORMAL)
    console_text.delete(1.0, tk.END)
    sys.stdout = TextComponent(console_text)

    lexical.lexer.input(text_input)
    try:
        for token in lexical.lexer:
            print(token)
        lexical.lexer.lineno = 1
        syntax.parser.parse(text_input)
        lexical.lexer.lineno = 1
    except Exception as e:
        print(f"Error: {e}")

    log_directory = "logs/semantic/"
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    log_filename = f"semantic-({log_username})-{datetime.datetime.now().strftime('%Y%m%d-%Hh%M')}.txt"
    log_filepath = os.path.join(log_directory, log_filename)

    with open(log_filepath, "w") as f:
        sys.stdout = f
        lines = text_input.strip().split('\n')
        for line_num, line in enumerate(lines, start=1):
            try:
                syntax.parser.parse(line)
            except Exception as e:
                print(f"Error en línea {line_num}: {e}")
        sys.stdout = sys.__stdout__

    print("Análisis completado. Los errores semánticos se han guardado en el archivo de registro:", log_filename)


def validate_input(text_input):
    if not text_input.strip():
        print("No se ha ingresado texto para analizar.")
        return False
    return True

def on_run():
    input_text_content = code_text.get(1.0, tk.END)
    if validate_input(input_text_content):
        run_TypeScript(input_text_content)

# Crear la ventana principal
root = tk.Tk()
root.title("TypeScript Analyzer")
root.configure(bg="#2C3E50")
    
# Configurar el tamaño inicial y permitir redimensionamiento
root.geometry("800x600")
root.grid_columnconfigure(0, weight=1)  # Permitir que la columna 0 se ajuste
root.grid_columnconfigure(1, weight=1)  # Permitir que la columna 1 se ajuste
root.grid_rowconfigure(0, weight=1)     # Permitir que la fila se ajuste

# Crear un marco principal para contener todo
main_frame = tk.Frame(root, bg="#2C3E50")
main_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")

# Configurar encabezado
header = tk.Frame(main_frame, bg="#3498DB")
header.grid(row=0, column=0, columnspan=2, sticky="ew")
header.grid_columnconfigure(0, weight=1)

# Agregar botón para editar el nombre de usuario
edit_user_button = tk.Button(header, text="Editar Usuario", bg="orange", fg="white", font=("Arial", 12), relief="flat", command=edit_username)
edit_user_button.grid(row=0, column=3, padx=10, pady=5, sticky="e")

# Añadir el logo y el título al encabezado
try:
    logo_image = Image.open("typescript_logo.png")
    logo_image = logo_image.resize((30, 30), Image.LANCZOS)
    logo = ImageTk.PhotoImage(logo_image)
    logo_label = tk.Label(header, image=logo, bg="#3498DB")
    logo_label.image = logo
    logo_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
except FileNotFoundError:
    print("Error: No se encontró el archivo 'typescript_logo.png'")

title_label = tk.Label(header, text="TypeScript Code Analyzer", font=("Arial", 16, "bold"), fg="white", bg="#3498DB")
title_label.grid(row=0, column=1, sticky="w")

# Añadir botón "Run"
run_button = tk.Button(header, text="RUN ▶", bg="green", fg="white", font=("Arial", 12, "bold"), relief="flat", command=on_run)
run_button.grid(row=0, column=2, padx=10, pady=5, sticky="e")

# Configurar área de código y consola
code_frame = tk.Frame(main_frame, bg="#ECF0F1")
code_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
console_frame = tk.Frame(main_frame, bg="#ECF0F1")
console_frame.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

main_frame.grid_rowconfigure(1, weight=1)  # Permitir que el área de código/consola se ajuste
main_frame.grid_columnconfigure(0, weight=1)  # Ajustar ancho del área de código
main_frame.grid_columnconfigure(1, weight=1)  # Ajustar ancho del área de consola

# Añadir widget de texto para código
code_text = tk.Text(code_frame, wrap=tk.WORD, bg="white", fg="black")
code_text.pack(expand=True, fill="both", padx=5, pady=5)

# Añadir etiqueta y consola
console_label = tk.Label(console_frame, text="Console", bg="#ECF0F1", fg="#2C3E50", font=("Arial", 12, "bold"))
console_label.pack(anchor="nw", padx=5, pady=5)

console_text = tk.Text(console_frame, wrap=tk.WORD, bg="white", fg="black", state=tk.DISABLED)
console_text.pack(expand=True, fill="both", padx=5, pady=5)

# Añadir footer
footer = tk.Label(main_frame, text="Version Alpha 1.0", bg="#2C3E50", fg="white", anchor="w", font=("Arial", 10))
footer.grid(row=2, column=0, columnspan=2, sticky="ew")

# Ejecutar la ventana
root.mainloop()


