# Doble de los números
# Dada una lista de números [1,2,3,4,5], crea una nueva lista que contenga el doble de cada número usando una List Comprehesion.
numbers = [number for number in range(1,6)]
double_numbers = [number * 2 for number in numbers]
#print(numbers)
#print(double_numbers)


# Filtrar y Transformar en un solo paso
# Tienes una lista de palabras ["sol","mar","montaña","rio","estrella"] y quieres obtener una nueva lista
# Con las palabras que tengan más de 3 letras y esten en mayúsculas.
words = ["sol","mar","montaña","rio","estrella"]
new_words = [word.upper() for word in words if len(word) > 3]
#print(new_words) 


# Crear un diccionario con List Comprehesion
# Tienes 2 listas, una de claves ["nombre", "edad", "ocupación"]
# Y otra de valores ["Juan",30,"Ingeniero"]. Crea un diccionario
# Combinando ambas listas usando una List Comprehension
keys = ["nombre","edad","ocupación"]
values = ["Juan", 30, "Ingeniero"]
new_dict = {keys[i] : values[i] for i in range(len(keys))}
print(new_dict)