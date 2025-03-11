# Desenvolva um algoritmo com os sálarios minimos 
#de 2000 á 2005, e plot um gráfico com essa representação.

#Pode ser plont, scatter ou bar

import matplotlib.pyplot as plt

anos = list(range(2000, 2026))
salarios_minimos = [
    151, 180, 200, 240, 260, 300, 350, 380, 415, 465, 510, 545, 622, 678, 724,
    788, 880, 937, 998, 1045, 1100, 1212, 1320, 1400, 1450, 1500]

bars = plt.bar(anos, salarios_minimos)

plt.plot(anos, salarios_minimos, color="Red")
plt.title("Salário Mínimo de 2000-2025")
plt.xlabel("Ano")
plt.ylabel("Salário Mínimo (R$)")

plt.xticks(anos, rotation=45)
plt.bar_label(bars, labels=[f'R$ {v}' for v in salarios_minimos], padding=5)

plt.show()
