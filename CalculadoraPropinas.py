import tkinter as tk
from tkinter import messagebox

def validar_entrada(valor):
    try:
        numero = float(valor)
        if numero < 0:
            raise ValueError
        return numero
    except ValueError:
        return None

def calcular_propina():
    monto = validar_entrada(entry_monto.get())
    porcentaje = validar_entrada(entry_porcentaje.get())

    if monto is None or porcentaje is None:
        messagebox.showerror("Error", "Por favor, ingrese números válidos y positivos.")
        return

    propina = monto * (porcentaje / 100)
    total = monto + propina

    label_resultado.config(
        text=f"💵 Propina: ${propina:.2f}\n💰 Total a pagar: ${total:.2f}"
    )

def limpiar_campos():
    entry_monto.delete(0, tk.END)
    entry_porcentaje.delete(0, tk.END)
    label_resultado.config(text="")

def salir_app():
    if messagebox.askyesno("Salir", "¿Seguro que desea salir?"):
        ventana.destroy()

# Ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Propinas")
ventana.geometry("360x440")
ventana.configure(bg="#f4f4f4")
ventana.resizable(False, False)

# Fuente moderna (Arial como respaldo)
fuente_titulo = ("Segoe UI", 18, "bold")
fuente_normal = ("Segoe UI", 12)

# Entradas
entrada_estilo = {
    "font": fuente_normal,
    "bg": "#ffffff",
    "bd": 1,
    "relief": "flat",
    "highlightthickness": 1,
    "highlightbackground": "#cccccc",
}

# Botones
boton_estilo = {
    "font": fuente_normal,
    "fg": "#ffffff",
    "width": 10,
    "height": 1,
    "bd": 0,
    "cursor": "hand2",
    "relief": "flat",
}

# Título
titulo = tk.Label(ventana, text="💡 Calculadora de Propinas", font=fuente_titulo, bg="#f4f4f4", fg="#333333")
titulo.pack(pady=20)

# Monto
label_monto = tk.Label(ventana, text="Monto de la cuenta ($):", font=fuente_normal, bg="#f4f4f4")
label_monto.pack(anchor="w", padx=40)
entry_monto = tk.Entry(ventana, **entrada_estilo)
entry_monto.pack(padx=40, pady=5, ipady=6, fill="x")


# Porcentaje
label_porcentaje = tk.Label(ventana, text="Porcentaje de propina (%):", font=fuente_normal, bg="#f4f4f4")
label_porcentaje.pack(anchor="w", padx=40, pady=(15, 0))
entry_porcentaje = tk.Entry(ventana, **entrada_estilo)
entry_porcentaje.pack(padx=40, pady=5, ipady=6, fill="x")


entry_monto.bind("<Return>", lambda event: calcular_propina())
entry_porcentaje.bind("<Return>", lambda event: calcular_propina())

# Botones
frame_botones = tk.Frame(ventana, bg="#f4f4f4")
frame_botones.pack(pady=25)

# Botón "Calcular" en la fila 0 (solo)
tk.Button(
    frame_botones,
    text="Calcular",
    command=calcular_propina,
    bg="#6c63ff",
    activebackground="#5a54d6",
    **boton_estilo
).grid(row=0, column=0, columnspan=2, pady=(0, 10))

# Botón "Limpiar" en la fila 1, columna 0
tk.Button(
    frame_botones,
    text="Limpiar",
    command=limpiar_campos,
    bg="#00bcd4",
    activebackground="#00a2b4",
    **boton_estilo
).grid(row=1, column=0, padx=5)

# Botón "Salir" en la fila 1, columna 1
tk.Button(
    frame_botones,
    text="Salir",
    command=salir_app,
    bg="#f44336",
    activebackground="#d32f2f",
    **boton_estilo
).grid(row=1, column=1, padx=5)


# Resultado
label_resultado = tk.Label(ventana, text="", font=("Segoe UI", 13), bg="#f4f4f4", fg="#333333", justify="center")
label_resultado.pack(pady=20)

# Ejecutar
ventana.mainloop()