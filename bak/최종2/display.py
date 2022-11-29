import pygame
import time
import random
import place
import button

diceDegree = (0, 120, 240)
diceResult = {diceDegree[0]: 1, diceDegree[1]: 2, diceDegree[2]: 3}
# 플레이어 위치 겹칠 때 좌표 보정 값
sameLocationAddValue = ((0, 0), (0, 0), (-10, 10), (-20, 0, 20), (-30, -10, 10, 30))
# 주사위 표시 좌표
dice1Location = (300, 200)
dice2Location = (350, 200)
# 캐릭터 창 표시 좌표
playerInfoLocation = ((5, 35), (442, 35), (5, 485), (442, 485))
# 캐릭터 자산 표시 좌표
playerInfoTextLocation = (((118, 67), (118, 88), (134, 108)), ((530, 67), (530, 88), (547, 108)),
                          ((118, 495), (118, 516), (134, 536)), ((530, 495), (530, 516), (547, 536)))
# playerInfoTextLocation = (((118, 65), (118, 86), (134, 106)), ((530, 65), (530, 86), (547, 106)),
# ((118, 492), (118, 513), (134, 533)), ((530, 492), (530, 513), (547, 533)))
# 플레이어 랭크 표시 좌표
playerRankLocation = ((197, 42), (449, 42), (197, 525), (449, 525))
# 건물 가격 표 표시 좌표
buildingFeeInfoLocation = (10, 5)
# 현재 턴 수 표시 좌표
turnInfoLocation = (540, 7)
# 게임 결과 창 표시 좌표
resultBackgroundLocation = (100, 100)
# 게임 결과 창에서 플레이어 이름 표시 좌표
resultPlayerLocation = ((276, 215), (276, 265), (276, 305), (276, 347))
# 1등 플레이어 이름 표시 좌표
resultWinnerLocation = (164, 443)


# 게임 관련 변수, 객체, 메소드 등
class Display:
    def __init__(self, game, playerInfo):
        # 이미지 출력을 위한 객체 선언
        self.display = None
        self.boardImage = None
        self.turnTextBox = []
        self.playerIcon = []
        self.playerInfoImage = []
        self.playerInfoYellowImage = []
        self.buildingImage = []
        self.rankImage = []
        self.resultPlayerImage = []
        self.diceImage = None
        self.yesImage = None
        self.noImage = None
        self.yesImage2 = None
        self.noImage2 = None
        self.textLocation = (50, 590)
        self.buttonLocation = ((200, 250), (400, 250))

        self.showLoading()
        self.init(game, playerInfo)

    # 게임 디스플레이 초기화
    def init(self, game, playerInfo):
        # 게임 창 크기 설정
        windowSize = (700, 700)

        self.display = pygame.display.set_mode(windowSize)

        # 보드 이미지
        self.boardImage = pygame.image.load('image/board.png')

        # 플레이어 관련 객체 리스트
        self.turnTextBox.append(pygame.image.load('image/player0Turn.png'))
        self.turnTextBox.append(pygame.image.load('image/player1Turn.png'))
        self.playerIcon.append(pygame.image.load('image/player0.png'))
        self.playerIcon.append(pygame.image.load('image/player1.png'))
        self.playerInfoImage.append(pygame.image.load('image/playerInfo0.png'))
        self.playerInfoImage.append(pygame.image.load('image/playerInfo1.png'))
        self.playerInfoYellowImage.append(pygame.image.load('image/playerInfo0Yellow.png'))
        self.playerInfoYellowImage.append(pygame.image.load('image/playerInfo1Yellow.png'))
        self.buildingImage.append(pygame.image.load('image/building0.png'))
        self.buildingImage.append(pygame.image.load('image/building1.png'))
        self.rankImage.append(pygame.image.load('image/1등.png'))
        self.rankImage.append(pygame.image.load('image/2등.png'))
        self.resultPlayerImage.append(pygame.image.load('image/result/player0.png'))
        self.resultPlayerImage.append(pygame.image.load('image/result/player1.png'))

        # 플레이어 수가 3 ~ 4 명일 경우 객체 추가
        if game.playerNum >= 3:
            self.turnTextBox.append(pygame.image.load('image/player2Turn.png'))
            self.playerIcon.append(pygame.image.load('image/player2.png'))
            self.playerInfoImage.append(pygame.image.load('image/playerInfo2.png'))
            self.playerInfoYellowImage.append(pygame.image.load('image/playerInfo2Yellow.png'))
            self.buildingImage.append(pygame.image.load('image/building2.png'))
            self.rankImage.append(pygame.image.load('image/3등.png'))
            self.resultPlayerImage.append(pygame.image.load('image/result/player2.png'))
            if game.playerNum == 4:
                self.turnTextBox.append(pygame.image.load('image/player3Turn.png'))
                self.playerIcon.append(pygame.image.load('image/player3.png'))
                self.playerInfoImage.append(pygame.image.load('image/playerInfo3.png'))
                self.playerInfoYellowImage.append(pygame.image.load('image/playerInfo3Yellow.png'))
                self.buildingImage.append(pygame.image.load('image/building3.png'))
                self.rankImage.append(pygame.image.load('image/4등.png'))
                self.resultPlayerImage.append(pygame.image.load('image/result/player3.png'))
        # 주사위 이미지
        self.diceImage = pygame.image.load('image/dice.png')
        # yes, no 버튼 이미지
        self.yesImage = pygame.image.load('image/yes1.png')
        self.yesImage2 = pygame.image.load('image/yes2.png')
        self.noImage = pygame.image.load('image/no1.png')
        self.noImage2 = pygame.image.load('image/no2.png')

        # 창 제목 표시
        pygame.display.set_caption("인하마블")

        self.board()
        self.player(game, playerInfo)
        self.playerInfo(game, playerInfo)
        self.textBox(pygame.image.load('image/textBox/시작 멘트.png'))
        self.update()
        # Enter 버튼 입력 대기
        button.Button.waitForKeyboardEnter()

    # 보드 표시
    def board(self):
        self.display.blit(self.boardImage, (0, 0))
        self.display.blit(pygame.image.load('image/buildingFee.png'), buildingFeeInfoLocation)

    # 플레이어 아이콘 표시
    def player(self, game, playerInfo):
        sameLocation = []

        # 같은 칸에 겹쳐 있는 플레이어 확인
        for i in range(game.playerNum):
            for j in range(game.playerNum):
                if not (i == j):
                    if playerInfo[i].location == playerInfo[j].location:
                        sameLocation.append(playerInfo[i].location)

        # 집합으로 변환하여 중복 제거
        sameLocation = set(sameLocation)

        for location in sameLocation:
            sameCount = 0
            sameLocationPlayers = []

            for person in range(game.playerNum):
                if place.placeLocation[playerInfo[person].location] == place.placeLocation[location]:
                    sameCount += 1
                    sameLocationPlayers.append(playerInfo[person].index)
            # 한 칸에 2명 이상 서 있을 때
            if sameCount > 1:
                for i in range(sameCount):
                    # 겹친 플레이어 수에 따라 x 좌표 보정하여 표시
                    displayLocation = (place.placeLocation[location][0] + sameLocationAddValue[sameCount][i],
                                       place.placeLocation[location][1])
                    self.display.blit(self.playerIcon[sameLocationPlayers[i]], displayLocation)

        # 겹치치 않은 플레이어 표시
        for person in range(game.playerNum):
            if playerInfo[person].location not in sameLocation:
                self.display.blit(self.playerIcon[person], place.placeLocation[playerInfo[person].location])

    # 플레이어 창 표시
    def playerInfo(self, game, playerInfo):
        blank = pygame.image.load('image/textBox/blank.png')
        blank = pygame.transform.scale(blank, (250, 100))

        playerTotalMoney = []

        # 플레이어 총 자산 크기대로 정렬하여 랭킹 정하기
        for i in range(game.playerNum):
            playerTotalMoney.append(playerInfo[i].totalMoney)
        # 집합으로 변경하여 중복 제거
        playerTotalMoney = set(playerTotalMoney)
        playerTotalMoney = list(playerTotalMoney)
        playerTotalMoney.sort(reverse=True)

        # 플레이어 창에 랭킹 표시
        for i in playerTotalMoney:
            for j in range(game.playerNum):
                if playerInfo[j].totalMoney == i:
                    playerInfo[j].rank = playerTotalMoney.index(i)

        for i in range(game.playerNum):
            self.display.blit(blank, playerInfoLocation[i])

            # 현재 플레이중인 플레이어는 강조 표시된 이미지 표시
            if game.nowTurnPlayer == i:
                self.display.blit(self.playerInfoYellowImage[i], (playerInfoLocation[i][0] - 3,
                                                                  playerInfoLocation[i][1] - 5))
            else:
                self.display.blit(self.playerInfoImage[i], playerInfoLocation[i])

            self.display.blit(self.rankImage[playerInfo[i].rank], playerRankLocation[i])
            # 돈, 건물 자산, 총 자산 표시
            self.text(str(playerInfo[i].money) + "만원", playerInfoTextLocation[i][0])
            self.text(str(playerInfo[i].buildingMoney) + "만원", playerInfoTextLocation[i][1])
            self.text(str(playerInfo[i].totalMoney) + "만원", playerInfoTextLocation[i][2])
        # 남은 턴 수 표시
        blank = pygame.transform.scale(blank, (250, 25))
        self.display.blit(blank, turnInfoLocation)
        self.text("남은 턴 수 : " + str(game.endTurn - game.turn - 1) + "턴", turnInfoLocation, 18)

    def text(self, text, location, size=12):
        font = pygame.font.SysFont('applegothic', size)
        # font = pygame.font.SysFont('malgungothic', size)
        text_image = font.render(text, True, (0, 0, 0))
        self.display.blit(text_image, (location[0], location[1]))

    # 건물 표시 함수
    def building(self, game, playerInfo):
        for i in range(game.playerNum):
            for j in range(len(playerInfo[i].building)):
                placeIndex = place.placeName.index(playerInfo[i].building[j])
                if 0 < placeIndex < 7:
                    image = pygame.transform.flip(self.buildingImage[i], True, False)
                    self.display.blit(image, (place.placeLocation[placeIndex][0] + 23,
                                              place.placeLocation[placeIndex][1] - 23))

                elif 7 < placeIndex < 14:
                    self.display.blit(self.buildingImage[i], (place.placeLocation[placeIndex][0] - 25,
                                                              place.placeLocation[placeIndex][1] - 18))

                elif 14 < placeIndex < 21:
                    image = pygame.transform.flip(self.buildingImage[i], True, False)
                    self.display.blit(image, (place.placeLocation[placeIndex][0] + 25,
                                              place.placeLocation[placeIndex][1] - 12))

                else:
                    self.display.blit(self.buildingImage[i], (place.placeLocation[placeIndex][0] - 30,
                                                              place.placeLocation[placeIndex][1] - 18))

    def textBox(self, text):
        self.display.blit(pygame.image.load('image/textBox/blank.png'), self.textLocation)
        self.display.blit(text, self.textLocation)

    def turn(self, game, playerInfo, index):
        self.playerInfo(game, playerInfo)
        self.building(game, playerInfo)
        self.player(game, playerInfo)
        self.textBox(self.turnTextBox[index])
        self.update()
        time.sleep(1)

    # 주사위 표시
    def dice(self, diceRotatedImage1, diceRotatedImage2):
        self.display.blit(diceRotatedImage1,
                          (dice1Location[0] + self.diceImage.get_width() / 2 - diceRotatedImage1.get_width() / 2,
                           dice1Location[1] + self.diceImage.get_height() / 2 - diceRotatedImage1.get_height() / 2))
        self.display.blit(diceRotatedImage2,
                          (dice2Location[0] + self.diceImage.get_width() / 2 - diceRotatedImage2.get_width() / 2,
                           dice2Location[1] + self.diceImage.get_height() / 2 - diceRotatedImage2.get_height() / 2))

    # 주사위 회전 표시
    def diceRotate(self):
        # 주사위 회전 속도 (50 ~ 150 사이 값)
        speed1 = random.randrange(50, 150, 3)
        speed2 = random.randrange(50, 150, 3)
        # 주사위 결과 값
        result1 = random.choice(diceDegree)
        result2 = random.choice(diceDegree)
        # 주사위 표시 각도
        degree1 = 0
        degree2 = 0

        while True:
            # 주사위 회전 속도만큼 각도 변경
            degree1 += speed1
            degree2 += speed2

            if degree1 >= 360:
                degree1 -= 360
            if degree2 >= 360:
                degree2 -= 360

            # 주사위 회전 속도 빠르면 speed 2씩 감소, 회전 속도 느리면 speed 1씩 감소
            if speed1 >= 60:
                speed1 -= 2
            elif 3 < speed1 < 60:
                speed1 -= 1
            if speed2 >= 60:
                speed2 -= 2
            elif 3 < speed2 < 60:
                speed2 -= 1

            diceImage1 = pygame.transform.rotate(self.diceImage, degree1)
            diceImage2 = pygame.transform.rotate(self.diceImage, degree2)

            self.dice(diceImage1, diceImage2)
            self.update()

            # 주사위 회전 속도가 최소일 때
            if speed1 <= 3 and speed2 <= 3:
                if degree1 == result1:
                    speed1 = 0
                    result1 = diceResult[degree1]

                if degree2 == result2:
                    speed2 = 0
                    result2 = diceResult[degree2]

                if speed1 == 0 and speed2 == 0:
                    return result1, result2, diceImage1, diceImage2

            if speed1 <= 3 or speed2 <= 3:
                time.sleep(0.003)
            else:
                time.sleep(0.01)

    # 게임 결과 창 표시
    def result(self, game, playerInfo):
        self.display.blit(pygame.image.load('image/result/result.png'), resultBackgroundLocation)

        for i in range(game.playerNum):
            for j in range(game.playerNum):
                if playerInfo[j].rank == i:
                    self.display.blit(self.resultPlayerImage[j], resultPlayerLocation[i])
                    if i == 0:
                        self.display.blit(self.resultPlayerImage[j], resultWinnerLocation)
                    break

    # 디스플레이 업데이트
    @staticmethod
    def update():
        pygame.display.update()

    # 로딩 화면 출력 함수
    @staticmethod
    def showLoading():
        comment = "인하마블 now loading.. "
        randomList = [1, 1, 1, 1, 1, 1, 3, 5, 10, 20]

        i = 0
        while i < 100:
            # 로딩 속도를 일정하지 않게 하기 위해 랜덤으로 i 증가
            i += random.choice(randomList)
            if i > 100:
                i = 100

            # @를 50개만 출력
            gauge = "@" * int(i / 2)
            percent = str(i) + "%"

            # 커서를 맨 앞으로 이동
            print("\r", end='', flush=True)
            # 총 출력되는 칸수는 70칸, 왼쪽으로 정렬하여 문자열 출력
            print("%-70s" % (comment + gauge) + percent, end='', flush=True)

            time.sleep(0.1)

        print("\ndone.")
        time.sleep(0.75)

        print("openning 소융마블..")
        time.sleep(1.5)
