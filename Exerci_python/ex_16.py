#Crie uma função retira_espaço(texto) que retorne uma string sem espaço em branco.

def retira_espaço(texto):
    texto_sem_espaco= texto.replace(" " ,"")
    return texto_sem_espaco

texto_original="O desafio é ser eu mesma num mundo que tenta,me fazer igual a todos. (Rita Lee)"
texto_modificado=retira_espaço(texto_original)

print("Texto original:", texto_original)
print("Texto sem espaço:",texto_modificado)