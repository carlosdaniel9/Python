from pygame import init, mixer, event
init()
mixer.music.load('nirvana.mp3')
mixer.music.play()
input()  # o input evita o código encerrar,  assim a musica irá tocar
event.wait()
