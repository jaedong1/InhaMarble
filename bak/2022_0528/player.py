import pygame
import sys
import time
import place

diceDegree = (0, 0, 120, 240)


class Player:
    def __init__(self, index):
        self.index = index
        self.money = 300
        self.buildingMoney = 0
        self.totalMoney = self.money + self.buildingMoney
        self.rank = 0
        self.location = 0
        self.building = []
        self.penalty = 0

    # 주사위 던지는 함수
    def throwDice(self, game, display, playerInfo, placeInfo):
        # 인경호에 빠졌으면 안내 문구 출력
        if self.penalty > 0:
            # print("당신은 인경호에 빠져 있습니다. 더블이 나오면 탈출합니다!")
            # time.sleep(0.5)
            pass

        display.textBox(pygame.image.load('image/textBox/주사위 안내.png'))
        display.update()

        done = False
        dice1, dice2, = 0, 0
        diceImage1, diceImage2 = None, None
        double = 0

        while not done:
            done = True
            pygame.event.clear()

            while True:
                try:
                    for event in pygame.event.get():
                        # 엔터 키 감지 시
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                            dice1, dice2, diceImage1, diceImage2 = display.diceRotate()
                            raise NotImplementedError
                        # 게임 창 닫기 버튼을 눌렀을 경우
                        elif event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                except NotImplementedError:
                    break

            if dice1 + dice2 == 2:
                image = pygame.image.load('image/textBox/2칸 이동.png')
            elif dice1 + dice2 == 3:
                image = pygame.image.load('image/textBox/3칸 이동.png')
            elif dice1 + dice2 == 4:
                image = pygame.image.load('image/textBox/4칸 이동.png')
            elif dice1 + dice2 == 5:
                image = pygame.image.load('image/textBox/5칸 이동.png')
            else:
                image = pygame.image.load('image/textBox/6칸 이동.png')

            display.textBox(image)
            display.update()

            if self.penalty <= 0:
                self.move(game, display, playerInfo, diceImage1, diceImage2, dice1 + dice2, image)
                placeInfo[self.location].checkEvent(game, display, playerInfo, self.index)

            # 더블일 경우
            if dice1 == dice2:
                # 인경호에 빠져있는 경우
                if self.penalty > 0:
                    self.penalty = 0
                    display.textBox(pygame.image.load('image/textBox/인경호 탈출 성공.png'))
                    display.update()
                    time.sleep(1)

                    display.textBox(pygame.image.load('image/textBox/더블_주사위한번더.png'))
                    display.update()
                    done = False
                else:
                    # 더블이 연속 3번인 경우
                    double += 1
                    if double >= 3:
                        self.penalty = 3
                        image = pygame.image.load('image/textBox/트리플 더블.png')
                        while self.location != place.placeName.index("인경호"):
                            self.move(game, display, playerInfo, None, None, 1, image)
                        time.sleep(0.5)
                    else:
                        display.textBox(pygame.image.load('image/textBox/더블_주사위한번더.png'))
                        display.update()
                        done = False
            # 더블이 아닌 경우
            else:
                if self.penalty > 0:
                    # 인경호에 빠져있었으면 탈출 실패 문구 출력
                    if self.penalty == 3:
                        display.textBox(pygame.image.load('image/textBox/인경호 탈출 실패1.png'))
                        display.update()
                        time.sleep(2)
                    elif self.penalty == 2:
                        display.textBox(pygame.image.load('image/textBox/인경호 탈출 실패2.png'))
                        display.update()
                        time.sleep(2)
                    elif self.penalty == 1:
                        display.textBox(pygame.image.load('image/textBox/인경호 탈출 실패3.png'))
                        display.update()
                        time.sleep(2)

                    self.penalty -= 1

    def move(self, game, display, playerInfo, diceImage1, diceImage2, move, image):
        # 이동할 칸 수만큼 반복하여 game.moveDisplay 함수 호출
        for i in range(move):
            # 1칸씩 이동
            self.location += 1

            # 출발점을 지나면 위치 index 클리어
            if self.location >= len(place.placeList):
                self.getMoney(20)
                self.location = 0

                display.board()
                display.playerInfo(game, playerInfo)
                display.building(game, playerInfo)
                display.player(game, playerInfo)
                display.textBox(pygame.image.load('image/textBox/출발지 통과.png'))

                if diceImage1 is not None and diceImage2 is not None:
                    display.dice(diceImage1, diceImage2)

                display.update()
                time.sleep(1)
            else:
                display.board()
                display.playerInfo(game, playerInfo)
                display.building(game, playerInfo)
                display.player(game, playerInfo)
                display.textBox(image)

                if diceImage1 is not None and diceImage2 is not None:
                    display.dice(diceImage1, diceImage2)

                display.update()
                time.sleep(0.25)

    def getMoney(self, money):
        self.money += money
        self.totalMoney = self.money + self.buildingMoney

    def payMoney(self, money):
        self.money -= money
        self.totalMoney = self.money + self.buildingMoney

    def buyBuilding(self, buildingInfo):
        if buildingInfo.owner is None:
            money = buildingInfo.fee * 2
        else:
            money = buildingInfo.fee * 4
        self.payMoney(money)
        self.buildingMoney += money
        self.building.append(buildingInfo.name)
        self.totalMoney = self.money + self.buildingMoney
        buildingInfo.owner = self.index

    def sellBuilding(self, building):
        self.buildingMoney -= building.fee * 2
        self.totalMoney = self.money + self.buildingMoney
        self.building.remove(building.name)


def initPlayer(num):
    # player 객체 배열 초기화
    player = []
    # 플레이어 수만큼 객체 배열 생성
    for i in range(num):
        player.append(Player(i))

    return player
