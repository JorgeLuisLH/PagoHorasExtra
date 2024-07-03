import tkinter as tk
from tkinter import messagebox

# Se crea la ventana
ventana = tk.Tk()
ventana.title("Pago de Horas extra")
ventana.iconbitmap("D:\Diplomado de Ciencia de datos\Python\PagoHorasExtra\pago.ico")
ventana.geometry("340x180")

# Etiqueta y entrada del nombre
label_nombre = tk.Label(ventana,text="Nombre:",fg="blue")
label_nombre.grid(row=0, column=0,padx=10,pady=5,sticky=tk.W)

input_nombre = tk.Entry(ventana)
input_nombre.grid(row=0, column=1,padx=10,pady=5)

# Etiqueta y entrada del salario por dia
label_salario = tk.Label(ventana,text="Salario:")
label_salario.grid(row=1,column=0,padx=10,pady=5, sticky=tk.W)

input_salario =tk.Entry(ventana)
input_salario.grid(row=1,column=1,padx=10,pady=5)

label_horas_extras = tk.Label(ventana,text="Horas extras:")
label_horas_extras.grid(row=2,column=0,padx=10,pady=5,sticky=tk.W)

input_horas_extras = tk.Entry(ventana)
input_horas_extras.grid(row=2,column=1,padx=10,pady=5)

def calcular_pago_horas_extras():
    try:
        # Tomar los datos ingresados
        nombre = input_nombre.get()
        salario = float(input_salario.get())
        horas_extra = float(input_horas_extras.get())
        # Hacer el calculo
        salario_x_hora = salario / 8
        pago =(2*(9 * salario_x_hora)) + ( 3* ((horas_extra-9)*salario_x_hora))
        label_resultado.config(text=f"Hola {nombre}, tu pago por horas extras es de {pago}")
    except ValueError:
        messagebox.showerror("Error","Por favor ingresa datos validos")

calculo_button = tk.Button(ventana,text="Calcular Pago", command=calcular_pago_horas_extras)
calculo_button.grid(row=3, column=1,padx=10,pady=5,columnspan=2,sticky=tk.W)

label_resultado = tk.Label(ventana,text="", font=("Arial", 8, "bold"),fg="blue")
label_resultado.grid(row=4,column=0,columnspan=11,rowspan=2,padx=10,pady=5,sticky=tk.W)
        
label_by = tk.Label(ventana,text="By: jorgeluislh.com",font=("Arial", 7))
label_by.grid(row=6,column=7,columnspan=3,rowspan=2,padx=10,pady=5,sticky=tk.W)
  
# Ejecutar la ventana
ventana.mainloop()
