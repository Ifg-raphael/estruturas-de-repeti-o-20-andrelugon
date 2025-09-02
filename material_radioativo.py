# Programa lê a massa inicial em gramas, simula a perda de metade a cada 50 segundos
# até que a massa fique menor que 0,5 g, acumula o tempo total e imprime no formato Hh Mm Ss,
# sem mensagens extras na entrada ou na saída.


# Dados de entrada: usuário insere a massa em gramas
massa = float(input())
tempo = 0

#Laço de repetição: em cada passo, soma 50s e divide a massa por 2
while massa >= 0.5:
    tempo = tempo + 50
    massa = massa / 2

# Conversão de segundos para horas, minutos e segundos usando divisões inteiras
h = tempo // 3600               # horas inteiras
resto = tempo % 3600            # resto após remover horas
m = resto // 60                 # minutos inteiros
s = resto % 60                  # segundos restantes

# Saída: Imprime o tempo em horas, minutos e segundos
print(f"{h}h {m}m {s}s")

