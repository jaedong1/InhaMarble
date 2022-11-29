import pygame
import sys


class Game:
    def __init__(self):
        # 플레이어 수, 턴 수
        self.playerNum = None
        self.endTurn = None
        self.turn = 0

        # 초기화 함수 호출
        self.initPlayerNum()
        self.initEndTurn()

    # 플레이어 수 설정
    def initPlayerNum(self):
        while True:
            self.playerNum = int(input("플레이어 수(2 ~ 4)를 입력하세요 : "))
            if 2 <= self.playerNum <= 4:
                break
            else:
                print("잘못 입력하셨습니다.")

    # 턴 수 설정
    def initEndTurn(self):
        while True:
            self.endTurn = int(input("게임을 진행할 턴 수(10 ~ 20)를 입력하세요 : "))
            if 10 <= self.endTurn <= 20:
                break
            else:
                print("잘못 입력하셨습니다.")

    # 게임 창 닫기 버튼 감지
    @staticmethod
    def exitCheck():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
