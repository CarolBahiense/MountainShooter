from Code.Menu import Menu
import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))

    def run(self,):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass
            # Ve os evento po
            # for events in pygame.event.get():
            #     if events.type == pygame.QUIT:
            #         pygame.quit()  # fechar a janela
            #         quit()  # terminar o pygame