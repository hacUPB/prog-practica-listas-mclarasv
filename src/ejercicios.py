# Ejercicio 1: Suma de elementos en una lista de listas
def suma_matriz(matriz):
    """
    Recibe una lista de listas y devuelve la suma de todos sus elementos.
    Incluir el código aquí para sumar los elementos de la matriz.
    """
    suma_total = 0
    for fila in matriz:
        for elemento in fila:
            suma_total += elemento
    return suma_total



# Ejercicio 2: Encontrar el valor máximo en una matriz
def maximo_matriz(matriz):
    """
    Recibe una lista de listas y devuelve el valor máximo.
    Incluir el código aquí para encontrar el valor máximo en la matriz.
    """
    maximo = matriz[0][0]
    for fila in matriz:
        for elemento in fila:
            if elemento > maximo:
                maximo = elemento
    return maximo


# Ejercicio 3: Verificar si un número es primo
def es_primo(n):
    """
    Recibe un número y devuelve True si es primo, False en caso contrario.
    Incluir el código aquí para determinar si un número es primo.
    """
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True



# Ejercicio 4: Transponer una matriz
def transponer_matriz(matriz):
    """
    Recibe una lista de listas y devuelve la matriz transpuesta.
    Incluir el código aquí para transponer la matriz.
    """
    filas = len(matriz)
    columnas = len(matriz[0])
    transpuesta = []

    for j in range(columnas):
        nueva_fila = []
        for i in range(filas):
            nueva_fila.append(matriz[i][j])
        transpuesta.append(nueva_fila)

    return transpuesta



# Ejercicio 5: Filtrar números pares
def filtrar_pares(lista):
    """
    Recibe una lista de números y devuelve una nueva lista con solo los números pares.
    Incluir el código aquí para filtrar los números pares.
    """ 
    pares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

# Ejercicio 6: Contar la cantidad de palabras en una frase
def contar_palabras(frase):
   """
    Recibe una frase y devuelve el número de palabras.
    Incluir el código aquí para contar las palabras en la frase.
    """
    palabras = frase.split()
    return len(palabras)


# Ejercicio 7: Crear una tabla de multiplicar
def tabla_multiplicar(n):
    """
    Recibe un número y devuelve una lista con su tabla de multiplicar del 1 al 10.
    Incluir el código aquí para generar la tabla de multiplicar.
    """
    tabla = []
    for i in range(1, 11):
        tabla.append(n * i)
    return tabla



# Ejercicio 8: Contar números negativos en una lista
def contar_negativos(lista):
    """
    Recibe una lista de números y devuelve la cantidad de números negativos.
    Incluir el código aquí para contar los números negativos en la lista.
    """
    negativos = 0
    for numero in lista:
        if numero < 0:
            negativos += 1
    return negativos

# Ejercicio 9: Determinar si una lista está ordenada
def lista_ordenada(lista):
    """
    Recibe una lista de números y devuelve True si está ordenada de menor a mayor.
    Incluir el código aquí para verificar si la lista está ordenada.
    """
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True


# Ejercicio 10: Cifrar un texto con el cifrado César
def cifrado_cesar(texto, desplazamiento):
    """
    Recibe un texto y un desplazamiento, y devuelve el texto cifrado usando el cifrado César.
    Incluir el código aquí para cifrar el texto con el cifrado César.
    """
    resultado = ""

    for caracter in texto:
        if caracter.isalpha():
            if caracter.isupper():
                codigo_original = ord(caracter)
                base = ord('A')
                posicion = codigo_original - base
                nueva_posicion = (posicion + desplazamiento) % 26
                nuevo_codigo = base + nueva_posicion
                nuevo_caracter = chr(nuevo_codigo)
                resultado += nuevo_caracter
            else:
                codigo_original = ord(caracter)
                base = ord('a')
                posicion = codigo_original - base
                nueva_posicion = (posicion + desplazamiento) % 26
                nuevo_codigo = base + nueva_posicion
                nuevo_caracter = chr(nuevo_codigo)
                resultado += nuevo_caracter
        else:
            resultado += caracter

    return resultado




#Aquí comienza el progrma principal. No modifiques el código debajo de esta línea.
def main():
    pass


if __name__ == "__main__":
    main()