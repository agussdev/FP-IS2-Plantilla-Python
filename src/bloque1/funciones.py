'''
Created on 3 oct 2024

@author: alumno
'''

# Ejercicio 1

print("Ejercicio 1\n")

num_arrays:list = [1,2,3,4,5,6,7,8,9,10]
total = 0

def suma(list):
    total = 0
    if not list:
        raise ValueError("La lista no puede estar vacía")
    for n in list:
        total += n
    return total

def media(list):
    if not list:
        raise ValueError("La lista no puede estar vacía")
    return suma(list) / len(list)

def max(list):
    max = list[0]
    if not list:
        raise ValueError("La lista no puede estar vacía")
    for n in list: 
        if n > max:
            max = n
    return max

def min(list):
    min = list[0]
    if not list:
        raise ValueError("La lista no puede estar vacía")
    for n in list: 
        if n < min:
            min = n
    return min

def varianza(list):
    if not list:
        raise ValueError("La lista no puede estar vacía")
    med = media(list)
    total = 0
    for n in list:
        total += (n - med) ** 2
    return total / len(list)

print(f"Suma: {suma(num_arrays)}")
print(f"Media: {media(num_arrays)}")
print(f"Máximo: {max(num_arrays)}")
print(f"Mínimo: {min(num_arrays)}")
print(f"Varianza: {varianza(num_arrays)}")

print("\n--------------------")

# Ejercicio 2

print("Ejercicio 2\n")

num_arrays_2:list = [50,2,3,4,5,6,7,8,9,10]

def diferencia(list:list):
    dif:list = []
    if not list:
        raise ValueError("La lista no puede estar vacía")
    for n in range(len(list) - 1):
        dif.append(abs(list[n] - list[n+1]))
    return dif

print(f"Diferencia: {diferencia(num_arrays_2)}")

print("\n--------------------")

# Ejercicio 3

print("Ejercicio 3\n")

def truncar(n, x):

    if n <= 0:
        raise ValueError("El número no puede ser negativo")
    if x < 0:
        raise ValueError("El número no puede ser negativo")
    return round(n, x)

print(f"Truncado: {truncar(3.1416, 2)}")

print("\n--------------------")

# Ejercicio 4

print("Ejercicio 4\n")

def producto(n, k):
    total = 1
    if not n>=k:
        raise ValueError("El número n no puede ser menor que k")
    for i in range(k):
        total *= (n - i)
    return total

print(f"Producto: {producto(15, 3)}")

print("\n--------------------")

# Ejercicio 5

print("Ejercicio 5\n")

def primo(n):
    if not n>1:
        raise ValueError("El número no puede ser menor que 1")
    for i in range(2, n):
        if n%i == 0:
            print("No es primo")
            return False
    print(f"El numero {n} es primo")
    return True

print(primo(13))

print("\n--------------------")

# Ejercicio 6

print("Ejercicio 6\n")

def divisores(n):
    lista = []
    if not n>1:
        raise ValueError("El número no puede ser menor que 1")
    for i in range(1, n):
        if n%i == 0:
            lista.append(i)
    return lista

print(divisores(10))

if __name__ == '__main__':
    pass