from pygame import init, mixer, event
init() # iniciando a pygame
mixer.music.load('nirvana.mp3') # carregando o mp3, que está dentro da pasta do projeto
mixer.music.play()
print('Reproduzindo Smells Like Teen Spirit(nirvana)')
input('Aperte enter para encerrar!')  # o input evita o código encerrar,  assim a musica irá tocar
event.wait()


# carlos daniel  20/09/2023