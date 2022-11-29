import pygame
import sys


class Button:
    def __init__(self):
        self.result = None

    def imageButton(self, display, firstImg, secondImg, location, result):
        self.result = None

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        x, y = location[0], location[1]

        if x <= mouse[0] <= x + firstImg.get_width() and y <= mouse[1] <= y + firstImg.get_height():
            display.display.blit(secondImg, location)
            if click[0]:
                self.result = result

        else:
            display.display.blit(firstImg, location)

    @staticmethod
    def placeButton(location):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        x, y = location[0], location[1]

        if x + 15 <= mouse[0] <= x + 55 and y + 30 <= mouse[1] <= y + 70:
            if click[0]:
                return True

    @staticmethod
    def waitForMouseMotion():
        pygame.event.clear()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    mouse = pygame.mouse.get_pos()
                    if 0 <= mouse[0] <= 700 and 0 <= mouse[1] <= 700:
                        done = True
                        break

                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    @staticmethod
    def waitForKeyboardEnter():
        pygame.event.clear()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    done = True
                    break

                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
