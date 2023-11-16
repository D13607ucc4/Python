
def contar_palabras(frase):
    palabras = frase.split()        # Separa la oracion en palabras y las pone en un array.
    return len(palabras)            # Len() devuelve la cantidad de espacios ocupados

# Ejemplo de uso
frase = "Esto es una frase de ejemplo para contar palabras en Python."
frase2 = "Es esto una frase de ejemplo para contar palabras en Python? si; o no."

cantidad_palabras = contar_palabras(frase)
cantidad_palabras2 = contar_palabras(frase2)


print(f"La frase tiene {cantidad_palabras} palabrasen el primer ejemplo.")
print(f"La frase tiene {cantidad_palabras2} palabras en el segundo ejemplo.")

