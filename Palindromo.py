
#Palindromo


#como hacer el codigo para hallar las palabras que sean paindromas?

def is_palindrome(word):
    # remueve los espacios en blanco, convierte a minusculas y chequea si la palabra es igual a su inversa
    if word.replace(' ', '').lower() == word.replace(' ', '').lower()[::-1]:
        return True
    else:
        return False


word = input("Insert a word: ")
if is_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")
