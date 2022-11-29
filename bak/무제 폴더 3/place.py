import time
import button
import pygame

# 장소(칸) index 리스트
placeList = range(28)
# 장소 이름
placeName = ("출발점", "로스쿨관", "테니스장", "정석학술정보관", "미니게임", "대운동장", "비룡주차장", "인경호", "나빌레관", "5호관", "미니게임"
             , "농구장", "60주년관", "2호관", "황금열쇠", "4호관", "본관", "하이테크센터", "인하드림센터", "6호관", "미니게임", "우남호"
             , "학생회관", "비룡탑", "9호관", "체육관", "미래융합대학", "미니게임")

placeFee = (0, 25, 35, 35, 0, 25, 50, 0, 15, 25, 0, 35, 75, 25, 0, 50, 50, 75, 25, 15, 0, 0, 15, 75, 50, 35, 25, 0)

# 장소 좌표
placeLocation = ((320, 440), (265, 420), (225, 390), (190, 365), (150, 340), (110, 305), (65, 275),
                 (20, 240), (70, 220), (120, 185), (160, 160), (200, 130), (235, 100), (275, 75),
                 (320, 50), (359, 79), (401, 107), (442, 136), (485, 164), (525, 193), (565, 221),
                 (615, 250), (570, 276), (530, 301), (490, 327), (447, 353), (406, 379), (364, 404))


class Place:
    def __init__(self, name, fee):
        self.name = name
        self.fee = fee
        self.owner = None

    def checkEvent(self, game, display, playerInfo, placeInfo, index):
        if self.name == "황금열쇠":
            self.goldenKey()
        elif self.name == "우남호":
            self.airplane(game, display, playerInfo, placeInfo, index)
        elif self.name == "인경호":
            self.inhaLake(display, playerInfo, index)
        elif self.name == "미니게임":
            self.miniGame()
        else:
            self.normalPlace(game, display, playerInfo, placeInfo, index)

    def goldenKey(self):
        pass

    def airplane(self, game, display, playerInfo, placeInfo, index):
        if playerInfo[index].airplane:
            selectedLocation = self.selectAirplaneLocation(game, display)
            image = pygame.image.load('image/textBox/blank.png')
            while playerInfo[index].location != selectedLocation:
                playerInfo[index].move(game, display, playerInfo, None, None, 1, image)
            placeInfo[selectedLocation].checkEvent(game, display, playerInfo, placeInfo, index)
        else:
            playerInfo[index].airplane = True
            display.textBox(pygame.image.load('image/textBox/우남호 탑승.png'))
            display.update()
            time.sleep(1)

    @staticmethod
    def inhaLake(display, playerInfo, index):
        playerInfo[index].penalty = 4
        display.textBox(pygame.image.load('image/textBox/인경호 입수.png'))
        display.update()
        time.sleep(1)

    def miniGame(self):
        pass

    def normalPlace(self, game, display, playerInfo, placeInfo, index):
        if self.owner is None:
            if playerInfo[index].money >= self.fee * 2:
                self.askBuyBuilding(game, display, playerInfo, index)
        else:
            if playerInfo[index].money >= self.fee * 4:
                self.askBuyBuilding(game, display, playerInfo, index)
            elif playerInfo[index].money >= self.fee:
                playerInfo[index].payMoney(self.fee)
                playerInfo[self.owner].getMoney(self.fee)
                display.playerInfo(game, playerInfo)
                display.building(game, playerInfo)
                display.player(game, playerInfo)
                display.textBox(pygame.image.load('image/textBox/통행료 지불.png'))
                display.update()
                time.sleep(1)
            else:
                if playerInfo[index].totalMoney < self.fee:
                    playerInfo[index].파산 = True
                    display.playerInfo(game, playerInfo)
                    display.building(game, playerInfo)
                    display.player(game, playerInfo)
                    display.textBox(pygame.image.load('image/textBox/파산.png'))
                    display.update()
                    time.sleep(3)

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
                            time.sleep(1)
                            break

    def askBuyBuilding(self, game, display, playerInfo, index):
        display.textBox(pygame.image.load('image/textBox/건물 매입?.png'))
        display.update()

        yesButton = button.Button()
        noButton = button.Button()

        done = False
        while not done:
            yesButton.imageButton(display, display.yesImage, display.yesImage2, display.buttonLocation[0], True)
            noButton.imageButton(display, display.noImage, display.noImage2, display.buttonLocation[1], True)
            game.exitCheck()

            if yesButton.result:
                if self.owner is not None:
                    playerInfo[self.owner].sellBuilding(self)
                    playerInfo[index].buyBuilding(self, True)
                else:
                    playerInfo[index].buyBuilding(self, False)
                done = True
            elif noButton.result:
                done = True

            display.update()
            time.sleep(0.05)

        display.board()
        display.playerInfo(game, playerInfo)
        display.building(game, playerInfo)
        display.player(game, playerInfo)
        display.textBox(pygame.image.load('image/textBox/건물 매입 성공.png'))
        display.update()
        time.sleep(1)

    @staticmethod
    def selectAirplaneLocation(game, display):
        display.textBox(pygame.image.load('image/textBox/우남호 이동.png'))
        display.update()

        done = False
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
        time.sleep(1)

    @staticmethod
    def initPlace():
        place = []
        for i in placeList:
            place.append(Place(placeName[i], placeFee[i]))

        return place
