# CALCULAR EL AÑO QUE VA A CUMPLIR 100 AÑOS

# 1. Pedir la edad y su edad 
nombre = str(input("Ingrese su nombre "))
edad = int(input("Ingrese su edad "))
año = int(input("Ingrese el año vigente "))
# 2. Calcular en que año va a cumplir 100 años
calculo = (100 - edad) + año
# 3. Dar el resultado
print("El usuario " + nombre + " Tendra 100 años en el año: " + str(calculo) )
