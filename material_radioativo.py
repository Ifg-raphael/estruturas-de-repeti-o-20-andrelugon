# Sua solução aqui
massa = float(input())
tempo = 0
for i in range (1000):
    if massa < 0.5:
        break
    tempo = tempo + 50
    massa = massa / 2

h = tempo // 3600
resto = tempo % 3600
m = resto // 60
s = resto % 60
print(f"{h}h {m}m {s}s")

