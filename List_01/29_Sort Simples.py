a, b, c = map(int, input().split())

numeros = [a, b, c]

numeros_ordenados = sorted(numeros)

for numero in numeros_ordenados:
    print(numero)

print()

for numero in numeros:
    print(numero)