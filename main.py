# Solicitar dos números al usuario
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Multiplicación
resultado = num1 * num2

# Mostrar el resultado
print(f"El resultado de la multiplicación es: {resultado}")

print ("Hola muchachos, parcial en el que me fue pesimo")

print ("Cuadrado")
lado = 5
for _ in range(lado):
    print("* " * lado)

print("Rectangulo")
for i in range(1, lado + 1):
    print(" " * (lado - i) + "*" * (2 * i - 1))