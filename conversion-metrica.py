# Paso 1: Solicitar al usuario las medidas de la pieza del mueble en cms

medida_en_cms = float(input("Por favor, ingresar las medidas de la pieza del mueble (en cms): "))

# Paso 2: Convertir las medidas de centímetros a pulgadas

medida_en_pulgadas = medida_en_cms / 2.54

# Paso 3: Mostrar las medidas convertidas en pulgadas al usuario 

print("Las medidas en pulgadas de la pieza ingresada son:", medida_en_pulgadas)