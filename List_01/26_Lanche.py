precos = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50
}

linha = input().split()

codigo = int(linha[0])
quantidade = int(linha[1])

preco_total = precos[codigo] * quantidade

print(f"Total: R$ {preco_total:.2f}") 