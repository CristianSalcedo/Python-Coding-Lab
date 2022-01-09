import math
# CALCULAR EL AREA DE UN CIRCULO
# 1.PEDIR AL ESTUDIANTE EL RADIO
while True :
    try:
        radio = int(input("Ingrese un radio: "))
        if radio >=0:
            break
        else:
            print("Ingrese un radio valido")
    except:
        print("Ingrese un radio valido")

# 2. UTILIZAR EL RADIO QUE NOS DIERON PARA CALCULAR EL AREA
area =  math.pi * radio * radio
# 3. DAR EL RESULTADO DEL AREA
print("El area del circulo es : " + str(area))