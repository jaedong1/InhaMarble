import time
import button
import pygame
import minigame
import random

# 장소(칸) index 리스트
placeList = range(28)
# 장소 이름
placeName = ("출발점", "로스쿨관", "테니스장", "정석학술정보관", "업다운게임", "대운동장", "비룡주차장", "인경호", "나빌레관", "5호관", "타이핑게임"
             , "농구장", "60주년관", "2호관", "황금열쇠", "4호관", "본관", "하이테크센터", "인하드림센터", "6호관", "파이썬퀴즈게임", "우남호"
             , "학생회관", "비룡탑", "9호관", "체육관", "미래융합대학", "기억력게임")
# 건물 통행료
placeFee = (0, 25, 35, 35, 0, 25, 50, 0, 15, 25, 0, 35, 65, 25, 0, 50, 50, 65, 25, 15, 0, 0, 15, 65, 50, 35, 25, 0)
# 장소 좌표
placeLocation = ((320, 440), (270, 405), (230, 380), (193, 354), (150, 327), (110, 302), (70, 277),
                 (25, 240), (73, 214), (120, 185), (160, 160), (200, 132), (240, 107), (280, 82),
                 (320, 50), (359, 79), (401, 107), (442, 136), (485, 164), (525, 193), (565, 221),
                 (615, 250), (570, 276), (530, 301), (490, 327), (447, 353), (406, 379), (364, 404))


class Place:
    def __init__(self, name, fee):
        self.name = name
        self.fee = fee
        self.owner = None

    # 장소별 이벤트 체크 함수
    def checkEvent(self, game, display, playerInfo, placeInfo, index):
        if self.name == "황금열쇠":
            self.goldenKey(game, display, playerInfo, index)
        elif self.name == "우남호":
            self.airplane(game, display, playerInfo, placeInfo, index)
        elif self.name == "인경호":
            self.inhaLake(display, playerInfo, index)
        elif self.name == "업다운게임" or self.name == "타이핑게임" or self.name == "파이썬퀴즈게임" or self.name == "기억력게임":
            self.miniGame(game, display, playerInfo, index)
        elif self.name == "출발점":
            pass
        else:
            self.normalPlace(game, display, playerInfo, placeInfo, index)

    @staticmethod
    def goldenKey(game, display, playerInfo, index):
        result = random.randrange(0, 6)

        if result == 0:
            playerInfo[index].item = 100
            display.textBox(pygame.image.load('image/textBox/황금열쇠_통행료면제.png'))
            display.update()
            time.sleep(3)

        elif result == 1:
            playerInfo[index].getMoney(100)

            display.board()
            display.playerInfo(game, playerInfo)
            display.building(game, playerInfo)
            display.player(game, playerInfo)
            display.textBox(pygame.image.load('image/textBox/황금열쇠_성적우수장학금.png'))
            display.update()
            time.sleep(3)

        elif result == 2:
            playerInfo[index].item = 3
            display.textBox(pygame.image.load('image/textBox/황금열쇠_플러스 3칸.png'))
            display.update()
            time.sleep(3)

        elif result == 3:
            playerInfo[index].penalty = 4
            image = pygame.image.load('image/textBox/황금열쇠_인경호.png')
            while playerInfo[index].location != placeName.index("인경호"):
                playerInfo[index].move(game, display, playerInfo, None, None, 1, image)
            display.update()
            time.sleep(0.5)

        elif result == 4:
            playerInfo[index].payMoney(50)

            display.board()
            display.playerInfo(game, playerInfo)
            display.building(game, playerInfo)
            display.player(game, playerInfo)
            display.textBox(pygame.image.load('image/textBox/황금열쇠_장학금환수.png'))
            display.update()
            time.sleep(3)

        else:
            playerInfo[index].item = -3
            display.textBox(pygame.image.load('image/textBox/황금열쇠_마이너스 3칸.png'))
            display.update()
            time.sleep(3)

    def airplane(self, game, display, playerInfo, placeInfo, index):
        if playerInfo[index].airplane:
            playerInfo[index].airplane = False
            # 우남호 타고 이동할 장소 선택
            selectedLocation = self.selectAirplaneLocation(game, display)

            image = pygame.image.load('image/textBox/blank.png')
            # 선택한 장소까지 이동
            while playerInfo[index].location != selectedLocation:
                playerInfo[index].move(game, display, playerInfo, None, None, 1, image)

            placeInfo[selectedLocation].checkEvent(game, display, playerInfo, placeInfo, index)
        else:
            playerInfo[index].airplane = True
            display.textBox(pygame.image.load('image/textBox/우남호 탑승.png'))
            display.update()
            time.sleep(1.5)

    @staticmethod
    def inhaLake(display, playerInfo, index):
        playerInfo[index].penalty = 4
        display.textBox(pygame.image.load('image/textBox/인경호 입수.png'))
        display.update()
        time.sleep(1.5)

    def miniGame(self, game, display, playerInfo, index):
        pygame.event.clear()
        if self.name == "업다운게임":
            display.textBox(pygame.image.load('image/textBox/업다운게임 시작.png'))
            display.update()
            time.sleep(2)

            display.textBox(pygame.image.load('image/textBox/미니게임 콘솔창 안내.png'))
            display.update()

            if minigame.updownGame():
                button.Button.waitForMouseMotion()
                playerInfo[index].getMoney(50)
                display.playerInfo(game, playerInfo)
                display.building(game, playerInfo)
                display.player(game, playerInfo)
                display.textBox(pygame.image.load('image/textBox/미니게임 성공.png'))
                display.update()
                time.sleep(2)
            else:
                button.Button.waitForMouseMotion()
                display.textBox(pygame.image.load('image/textBox/업다운게임 실패.png'))
                display.update()
                time.sleep(3)

        elif self.name == "타이핑게임":
            display.textBox(pygame.image.load('image/textBox/타이핑게임 시작.png'))
            display.update()
            time.sleep(2)

            display.textBox(pygame.image.load('image/textBox/미니게임 콘솔창 안내.png'))
            display.update()

            if minigame.typingGame():
                button.Button.waitForMouseMotion()
                playerInfo[index].getMoney(50)
                display.playerInfo(game, playerInfo)
                display.building(game, playerInfo)
                display.player(game, playerInfo)
                display.textBox(pygame.image.load('image/textBox/미니게임 성공.png'))
                display.update()
                time.sleep(2)
            else:
                button.Button.waitForMouseMotion()
                display.textBox(pygame.image.load('image/textBox/타이핑게임 실패.png'))
                display.update()
                time.sleep(3)

        elif self.name == "파이썬퀴즈게임":
            display.textBox(pygame.image.load('image/textBox/파이썬 퀴즈게임 시작.png'))
            display.update()
            time.sleep(2)

            display.textBox(pygame.image.load('image/textBox/미니게임 콘솔창 안내.png'))
            display.update()

            if minigame.python_quizGame():
                button.Button.waitForMouseMotion()
                playerInfo[index].getMoney(50)
                display.playerInfo(game, playerInfo)
                display.building(game, playerInfo)
                display.player(game, playerInfo)
                display.textBox(pygame.image.load('image/textBox/미니게임 성공.png'))
                display.update()
                time.sleep(2)
            else:
                button.Button.waitForMouseMotion()
                display.textBox(pygame.image.load('image/textBox/파이썬 퀴즈게임 실패.png'))
                display.update()
                time.sleep(3)

        else:
            display.textBox(pygame.image.load('image/textBox/기억력게임 시작.png'))
            display.update()
            time.sleep(2)

            display.textBox(pygame.image.load('image/textBox/미니게임 콘솔창 안내.png'))
            display.update()

            if minigame.memoryGame():
                button.Button.waitForMouseMotion()
                playerInfo[index].getMoney(50)
                display.playerInfo(game, playerInfo)
                display.building(game, playerInfo)
                display.player(game, playerInfo)
                display.textBox(pygame.image.load('image/textBox/미니게임 성공.png'))
                display.update()
                time.sleep(2)
            else:
                button.Button.waitForMouseMotion()
                display.textBox(pygame.image.load('image/textBox/기억력게임 실패.png'))
                display.update()
                time.sleep(3)

    # 일반 칸 이벤트 처리 함수
    def normalPlace(self, game, display, playerInfo, placeInfo, index):
        # 해당 위치에 건물이 없는 경우
        if self.owner is None:
            # 건물 매입할 돈이 있는 경우
            if playerInfo[index].money >= self.fee * 2:
                self.askBuyBuilding(game, display, playerInfo, index)
            else:
                display.textBox(pygame.image.load('image/textBox/건물 매입 돈 부족.png'))
                display.update()
                time.sleep(1.5)
        else:
            # 건물 주인이 현재 플레이어인 경우 return
            if self.owner == index:
                return
            # 다른 플레이어 건물을 매입(건물가격 * 2)할 돈이 있는 경우
            if playerInfo[index].money >= self.fee * 4:
                self.askBuyBuilding(game, display, playerInfo, index)
            # 통행료를 낼 돈이 있는 경우
            elif playerInfo[index].money >= self.fee:
                # 통행료 면제 아이템이 있는 경우
                if playerInfo[index].item == 100:
                    playerInfo[index].item = 0

                    display.textBox(pygame.image.load('image/textBox/통행료 면제.png'))
                    display.update()
                    time.sleep(1.5)
                else:
                    playerInfo[index].payMoney(self.fee)
                    playerInfo[self.owner].getMoney(self.fee)
                    display.playerInfo(game, playerInfo)
                    display.building(game, playerInfo)
                    display.player(game, playerInfo)
                    display.textBox(pygame.image.load('image/textBox/통행료 지불.png'))
                    display.update()
                    time.sleep(1.5)
            # 통행료를 낼 돈이 없는 경우
            else:
                # 통행료 면제 아이템이 있는 경우
                if playerInfo[index].item == 100:
                    playerInfo[index].item = 0

                    display.textBox(pygame.image.load('image/textBox/통행료 면제.png'))
                    display.update()
                    time.sleep(1.5)
                else:
                    # 돈도 없고 건물도 없는 경우
                    if playerInfo[index].totalMoney < self.fee:
                        playerInfo[index].파산 = True
                        display.playerInfo(game, playerInfo)
                        display.building(game, playerInfo)
                        display.player(game, playerInfo)
                        display.textBox(pygame.image.load('image/textBox/파산.png'))
                        display.update()
                        time.sleep(3)
                    # 매각할 건물이 있는 경우
                    else:
                        while True:
                            self.selectSellBuilding(game, display, playerInfo, placeInfo, index)
                            if playerInfo[index].money >= self.fee:
                                playerInfo[index].payMoney(self.fee)
                                playerInfo[self.owner].getMoney(self.fee)
                                display.playerInfo(game, playerInfo)
                                display.building(game, playerInfo)
                                display.player(game, playerInfo)
                                display.textBox(pygame.image.load('image/textBox/통행료 지불.png'))
                                display.update()
                                time.sleep(1.5)
                                break

    # 건물 매입 여부 선택 함수
    def askBuyBuilding(self, game, display, playerInfo, index):
        # 건물 주인 있는 경우
        if self.owner is not None:
            display.textBox(pygame.image.load('image/textBox/건물 매입 여부_주인있음.png'))
        else:
            display.textBox(pygame.image.load('image/textBox/건물 매입 여부.png'))

        display.update()

        yesButton = button.Button()
        noButton = button.Button()

        done = False
        pygame.event.clear()
        while not done:
            yesButton.imageButton(display, display.yesImage, display.yesImage2, display.buttonLocation[0])
            noButton.imageButton(display, display.noImage, display.noImage2, display.buttonLocation[1])
            game.exitCheck()

            # 건물 매입 선택 시
            if yesButton.result:
                # 건물 주인 있는 경우
                if self.owner is not None:
                    playerInfo[self.owner].sellBuilding(self)
                    playerInfo[index].buyBuilding(self, True)
                else:
                    playerInfo[index].buyBuilding(self, False)

                display.board()
                display.playerInfo(game, playerInfo)
                display.building(game, playerInfo)
                display.player(game, playerInfo)
                display.textBox(pygame.image.load('image/textBox/건물 매입 성공.png'))

                done = True
            # 건물 매입 선택하지 않을 시
            elif noButton.result:
                # 건물 주인 있는 경우
                if self.owner is not None:
                    # 통행료 면제 아이템이 있는 경우
                    if playerInfo[index].item == 100:
                        playerInfo[index].item = 0

                        display.board()
                        display.playerInfo(game, playerInfo)
                        display.building(game, playerInfo)
                        display.player(game, playerInfo)
                        display.textBox(pygame.image.load('image/textBox/통행료 면제.png'))
                        display.update()
                        time.sleep(1.5)
                    else:
                        playerInfo[index].payMoney(self.fee)
                        playerInfo[self.owner].getMoney(self.fee)

                        display.board()
                        display.playerInfo(game, playerInfo)
                        display.building(game, playerInfo)
                        display.player(game, playerInfo)
                        display.textBox(pygame.image.load('image/textBox/통행료 지불.png'))
                        display.update()
                        time.sleep(1.5)
                # 건물 주인 없는 경우
                else:
                    display.board()
                    display.playerInfo(game, playerInfo)
                    display.building(game, playerInfo)
                    display.player(game, playerInfo)
                    display.update()

                done = True

            display.update()
            time.sleep(0.05)

        time.sleep(1.5)

    @staticmethod
    def selectAirplaneLocation(game, display):
        display.textBox(pygame.image.load('image/textBox/우남호 이동.png'))
        display.update()

        done = False
        pygame.event.clear()
        while not done:
            for i in placeList:
                if button.Button.placeButton(placeLocation[i]):
                    return i

            game.exitCheck()
            display.update()
            time.sleep(0.05)

    @staticmethod
    def selectSellBuilding(game, display, playerInfo, placeInfo, index):
        display.textBox(pygame.image.load('image/textBox/매각 건물 선택.png'))
        display.update()

        list_placeName = list(placeName)

        done = False
        pygame.event.clear()
        while not done:
            for i in playerInfo[index].building:
                placeIndex = list_placeName.index(i)
                if button.Button.placeButton(placeLocation[placeIndex]):
                    playerInfo[index].sellBuilding(placeInfo[placeIndex])
                    playerInfo[index].getMoney(placeFee[placeIndex] * 2)
                    done = True
                    break

            game.exitCheck()
            display.update()
            time.sleep(0.05)

        display.board()

        display.playerInfo(game, playerInfo)
        display.building(game, playerInfo)
        display.player(game, playerInfo)
        display.textBox(pygame.image.load('image/textBox/매각 성공.png'))
        display.update()
        time.sleep(1.5)

    @staticmethod
    def initPlace():
        place = []
        for i in placeList:
            place.append(Place(placeName[i], placeFee[i]))

        return place
