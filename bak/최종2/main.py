import pygame
import game
import player
import place
import display
# pygame 모듈 초기화
pygame.init()
# 게임 객체 생성 및 초기화
game = game.Game()
# 플레이어 수만큼 객체 생성
player = player.initPlayer(game.playerNum)
# 보드 칸 수만큼 객체 생성
place = place.Place.initPlace()
# 게임 디스플레이 초기화
display = display.Display(game, player)
# 정해진 턴수만큼 반복
for game.turn in range(game.endTurn):
    # 플레이어 수만큼 반복
    for game.nowTurnPlayer in range(game.playerNum):
        display.turn(game, player, game.nowTurnPlayer)
        player[game.nowTurnPlayer].throwDice(game, display, player, place)

display.result(game, player)
display.update()
while True:
    game.exitCheck()
