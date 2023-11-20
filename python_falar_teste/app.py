from playsound import playsound 
import gtts

with open('frase.txt', 'r') as arquivo:
    for linha in arquivo:
        frase = gtts.gTTS(linha, lang='pt-br') #Precisa guardar em uma variavel para ser usada na próxima linha
        frase.save('frase.mp3') #Salvar com a extensão mp3
        print('Preparando...')
        print('Falando...')
        playsound('frase.mp3')
