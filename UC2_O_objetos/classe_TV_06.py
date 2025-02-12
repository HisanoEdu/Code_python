
#Classe tv: Faça um programa que simule um televisor criando-o como como um objeto.
#O usuário deve ser capaz de informar o numero do canal e aumentar ou diminuir o volume.
#certifique-se de que o numero do canal e o nivel do volume permanece dentro de faixas válidas.

class TV:
    def __init__(self):
        self.canal = 1 
        self.volume = 10 
    
    def mudar_canal(self, novo_canal):
        if 1 <= novo_canal <= 999:
            self.canal = novo_canal
            print(f"Canal alterado para {self.canal}")
        else:
            print("Canal inválido. O canal deve estar entre 1 e 999.")

    def aumentar_volume(self):
        if self.volume < 100:
            self.volume += 1
            print(f"Volume aumentado para {self.volume}")
        else:
            print("Volume no máximo! Não é possível aumentar mais.")

    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1
            print(f"Volume diminuído para {self.volume}")
        else:
            print("Volume no mínimo! Não é possível diminuir mais.")
    
    def exibir_status(self):
    
        print(f"Canal: {self.canal}, Volume: {self.volume}")


if __name__ == "__main__":
    tv = TV()
    
    tv.exibir_status()

    tv.mudar_canal(50)
    tv.mudar_canal(999)
    tv.mudar_canal(1000) 

    tv.aumentar_volume()
    tv.aumentar_volume()

    
    tv.exibir_status()

    tv.diminuir_volume()
    tv.diminuir_volume()

    tv.exibir_status()
