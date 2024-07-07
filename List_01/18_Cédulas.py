"""
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.
"""

#   Código:

valor = int(input())

notas_100 = valor // 100
valor %= 100

notas_50 = valor // 50
valor %= 50

notas_20 = valor // 20
valor %= 20

notas_10 = valor // 10
valor %= 10

notas_5 = valor // 5
valor %= 5

notas_2 = valor // 2
valor %= 2

notas_1 = valor

print(f"{notas_100}")
print(f"{notas_50}")
print(f"{notas_20}")
print(f"{notas_10}")
print(f"{notas_5}")
print(f"{notas_2}")
print(f"{notas_1}")