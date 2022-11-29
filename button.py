import pygame
import sys


class Button:
    def __init__(self):
        self.result = None

    # 버튼 표시 및 클릭 이벤트 처리 함수
    # firstImg : 기본 버튼 이미지, secondImg : 커서 갖다댈 시 표시할 버튼 이미지
    def imageButton(self, display, firstImg, secondImg, location):
        self.result = None

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        x, y = location[0], location[1]

        if x <= mouse[0] <= x + firstImg.get_width() and y <= mouse[1] <= y + firstImg.get_height():
            display.display.blit(secondImg, location)
            if click[0]:
                self.result = True

        else:
            display.display.blit(firstImg, location)

    # 보드 칸(장소) 클릭 감지 함수
    @staticmethod
    def placeButton(location):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        x, y = location[0], location[1]

        # 보드 칸 크기 만큼 좌표 보정
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
