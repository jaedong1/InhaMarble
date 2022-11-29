import pygame


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

        if x <= mouse[0] <= x + 30 and y <= mouse[1] <= y + 30:
            if click[0]:
                return True
