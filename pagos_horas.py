nombre =input("Ingresa el nombre:")
while True:
    salario =input("Ingresa el salario diario:")
    try:       
        salario =float(salario)
        break
    except ValueError: print("El salario no es un valor valido")
while True:    
    horas_extra =input("Ingresa las horas extras trabajadas en la semana:")
    try:
        horas_extra =float(horas_extra)
        break
    except ValueError: print("El salario no es un valor valido")

salario_x_hora = salario / 8
if horas_extra <= 9:
    pago = 2 * (horas_extra * salario_x_hora)
    print(f"El pago de {nombre} es de {pago}")
else:
    pago = (2*(9 * salario_x_hora)) + ( 3* ((horas_extra-9)*salario_x_hora))
    print(f"El pago de {nombre} es de {pago}")