import pygame

pygame.mixer.init()
pygame.mixer.music.load("audio1.wav")
pygame.mixer.music.play()
print("now playing")

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

print("finished playing")
