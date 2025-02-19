import pygame

print('Começo po')
pygame.init()
window = pygame.display.set_mode(size = (600,480))
print('Parô')


while True:
    #Ve os evento po
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit() #fechar a janela
            quit() #terminar o pygame