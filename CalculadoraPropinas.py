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
ventana.title("🧮 Calculadora de Propinas")
ventana.geometry("400x500")
ventana.configure(bg="#ffffff")
ventana.resizable(False, False)

# Fuente (Poppins o Arial como backup)
try:
    poppins_font = ("Poppins", 12)
except:
    poppins_font = ("Arial", 12)

# Estilos generales
entrada_estilo = {
    "font": poppins_font,
    "bg": "#f7f7f7",
    "bd": 2,
    "relief": "solid",
    "highlightthickness": 1,
    "highlightbackground": "#cccccc",
}

boton_estilo = {
    "font": poppins_font,
    "fg": "white",
    "width": 12,
    "height": 2,
    "bd": 0,
    "cursor": "hand2",
}

# Título
titulo = tk.Label(ventana, text="Calculadora de Propinas", font=("Poppins", 18, "bold"), bg="#ffffff")
titulo.pack(pady=20)

# Monto
label_monto = tk.Label(ventana, text="Monto de la cuenta ($):", font=poppins_font, bg="#ffffff")
label_monto.pack(pady=5)
entry_monto = tk.Entry(ventana, **entrada_estilo)
entry_monto.pack(pady=5, ipadx=10, ipady=5)

# Porcentaje
label_porcentaje = tk.Label(ventana, text="Porcentaje de propina (%):", font=poppins_font, bg="#ffffff")
label_porcentaje.pack(pady=5)
entry_porcentaje = tk.Entry(ventana, **entrada_estilo)
entry_porcentaje.pack(pady=5, ipadx=10, ipady=5)

# Botones
frame_botones = tk.Frame(ventana, bg="#ffffff")
frame_botones.pack(pady=20)

boton_calcular = tk.Button(
    frame_botones,
    text="Calcular",
    command=calcular_propina,
    bg="#4CAF50",
    activebackground="#45a049",
    **boton_estilo
)
boton_calcular.grid(row=0, column=0, padx=10)

boton_limpiar = tk.Button(
    frame_botones,
    text="Limpiar",
    command=limpiar_campos,
    bg="#2196F3",
    activebackground="#1e88e5",
    **boton_estilo
)
boton_limpiar.grid(row=0, column=1, padx=10)

boton_salir = tk.Button(
    frame_botones,
    text="Salir",
    command=salir_app,
    bg="#f44336",
    activebackground="#e53935",
    **boton_estilo
)
boton_salir.grid(row=0, column=2, padx=10)

# Resultado
label_resultado = tk.Label(ventana, text="", font=("Poppins", 14), bg="#ffffff", fg="#333333")
label_resultado.pack(pady=20)

# Ejecutar
ventana.mainloop()
