import matplotlib.pyplot as plt

anos = list(range(2000, 2026))
Candidatos = [
 'Adriane Lopes (PP) 140.913 votos,'
 'Rose Modesto (UNIÃO) 131.525 votos,'
 'Beto Pereira (PSDB) 115.516 votos,'
 'Camila Jara (PT) 41.966 votos,'
 'Beto Figueiró (NOVO) 10.885 votos,'
 'Luso Queiroz (PSOL), 3.108 votos'
 'Ubirajara Martins (DC),1.067 votos'
 ]

 
plt.plot(anos, Candidatos, color="Red")
plt.title("Últimos candidatos a Prefeito")
plt.xlabel("Ano")
plt.ylabel("Número de votos")
plt.show()

