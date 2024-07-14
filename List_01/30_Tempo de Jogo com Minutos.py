hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())

minutos_inicial = hora_inicial * 60 + minuto_inicial
minutos_final = hora_final * 60 + minuto_final

diferenca_minutos = minutos_final - minutos_inicial

if diferenca_minutos <= 0:
    diferenca_minutos += 24 * 60

duracao_horas = diferenca_minutos // 60
duracao_minutos = diferenca_minutos % 60

print(f"O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)")