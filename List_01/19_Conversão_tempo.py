"""
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.
"""

#   Código:

segundos_totais = int(input())

horas = segundos_totais // 3600
segundos_restantes = segundos_totais % 3600
minutos = segundos_restantes // 60
segundos = segundos_restantes % 60

print(f"{horas}:{minutos}:{segundos}")