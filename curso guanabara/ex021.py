import pygame
pygame.init()
pygame.mixer.music.load('musicas/1.mp3')
pygame.mixer.music.play()
print('tocando...')
pygame.event.wait()
print('terminou')