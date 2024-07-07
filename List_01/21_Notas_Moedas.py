"""
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.
"""

#   Código:

valor = float(input())

notas_100 = int(valor // 100)
valor = valor - notas_100 * 100

notas_50 = int(valor // 50)
valor = valor - notas_50 * 50

notas_20 = int(valor // 20)
valor = valor - notas_20 * 20

notas_10 = int(valor // 10)
valor = valor - notas_10 * 10

notas_5 = int(valor // 5)
valor = valor - notas_5 * 5

notas_2 = int(valor // 2)
valor = valor - notas_2 * 2

moedas_1 = int(valor // 1) 
valor = valor - moedas_1 * 1

moedas_50 = int((valor / 0.50)) 
valor =  round(valor - moedas_50 * 0.50, 2)  

moedas_25 = int((valor / 0.25))
valor = round(valor - moedas_25 * 0.25, 2)

moedas_10 = int((valor / 0.10))
valor = round(valor - moedas_10 * 0.10, 2)

moedas_05 = int((valor / 0.05)) 
valor = round(valor - moedas_05 * 0.05, 2)

moedas_01 = int((valor / 0.01)) 

print("NOTAS:")
print(f"{notas_100} nota(s) de R$ 100.00")
print(f"{notas_50} nota(s) de R$ 50.00")
print(f"{notas_20} nota(s) de R$ 20.00")
print(f"{notas_10} nota(s) de R$ 10.00")
print(f"{notas_5} nota(s) de R$ 5.00")
print(f"{notas_2} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{moedas_1} moeda(s) de R$ 1.00")
print(f"{moedas_50} moeda(s) de R$ 0.50")
print(f"{moedas_25} moeda(s) de R$ 0.25")
print(f"{moedas_10} moeda(s) de R$ 0.10")
print(f"{moedas_05} moeda(s) de R$ 0.05")
print(f"{moedas_01} moeda(s) de R$ 0.01")