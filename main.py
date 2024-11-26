import tkinter as tk
from PIL import Image, ImageTk

def create_gui():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Code Analyzer")
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

    # Añadir el logo y el título al encabezado
    logo_image = Image.open("typescript_logo.png")
    logo_image = logo_image.resize((30, 30), Image.LANCZOS)
    logo = ImageTk.PhotoImage(logo_image)

    logo_label = tk.Label(header, image=logo, bg="#3498DB")
    logo_label.image = logo  # Mantener una referencia de la imagen
    logo_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    title_label = tk.Label(header, text="TypeScript Code Analyzer", font=("Arial", 16, "bold"), fg="white", bg="#3498DB")
    title_label.grid(row=0, column=1, sticky="w")

    # Añadir botón "Run"
    run_button = tk.Button(header, text="RUN ▶", bg="green", fg="white", font=("Arial", 12, "bold"), relief="flat", command=lambda: print("Run clicked"))
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

create_gui()