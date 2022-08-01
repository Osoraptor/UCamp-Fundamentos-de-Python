
nombre = input("Introduce tu nombre: ")
apellido_paterno = input("Introduce tu apellido paterno: ")
apellido_materno = input("Introduce tu apellido materno: ")
edad = int(input("Introduce tu edad: "))
peso = float(input("Introduce tu peso: "))
estatura = float(input(f'Introduce tu estatura (en metros): '))

print("Nombre: " + nombre)
print("Apellido Paterno: " + apellido_paterno)
print("Apellido Materno: " + apellido_materno)
print("Edad: " + str(edad) + " años.")
print("Peso: " + str(peso) + " kilos.")
print("Estatura: " + str(estatura) + " metros.")


imc = round(peso / (estatura ** 2), 2)

if imc < 18.5:
  print(f"Tu índice de masa corporal (IMC) es de {imc}, tu peso es bajo.")
elif imc <= 24.99:
  print(f"Tu índice de masa corporal (IMC) es de {imc}, tu peso es normal.")
elif imc <= 29.99:
  print(f"Tu índice de masa corporal (IMC) es de {imc}, tienes sobrepeso.")
elif imc <= 34.99:
  print(f"Tu índice de masa corporal (IMC) es de {imc}, tienes obesidad leve.")
elif imc <= 39.99:
  print(f"Tu índice de masa corporal (IMC) es de {imc}, tienes obesidad media.")
else:
  print(f"Tu índice de masa corporal (IMC) es de {imc}, tienes obesidad mórbida.")

