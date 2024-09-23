# Ejercicio manejo archivos con python - scripting
# contar el numero de lineas de un archivo txt

file = open('caperucita.txt', 'r')
lines = file.readlines()
n_lines = 0

for line in lines:
    n_lines += 1

print(f"El archivo caperucita.txt tiene {n_lines} lineas")
file.close()