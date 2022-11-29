import time
import random

count = 4
typingTime = 5

typingList = ("ㅁㅁㅁㅁㅁㅁ", "ㄴㄴㄴㄴㄴㄴㄴ", "ㅇㅇㅇㅇㅇㅇㅇ", "ㄹㄹㄹㄹㄹ", "ㅎㅎㅎㅎㅎㅎㅎ")
quizList = (("1111111", "1 : a, 2 : b, 3 : c, 4 : d"), ("2222222", "1 : a, 2 : b, 3 : c, 4 : d"),
            ("3333333", "1 : a, 2 : b, 3 : c, 4 : d"), \
            ("4444444", "1 : a, 2 : b, 3 : c, 4 : d"), ("555555", "1 : a, 2 : b, 3 : c, 4 : d"))

answerList = ("1", "2", "3", "4", "4")


def memoryGame():
    print("박승보 교수님과 마주쳤습니다! 행운의 과제를 받았습니다.")
    time.sleep(1)
    print("기억력 게임을 시작합니다.")
    time.sleep(1)
    print("빠르게 나타나는 숫자 %d개를 기억하여 입력하세요." % count)
    time.sleep(1)
    input("Enter 버튼을 눌러 게임을 시작하세요.")

    numbers = []

    for i in range(count):
        numbers.append(random.randrange(1, 100))
        print("%d번째 숫자 : %d" % (i + 1, numbers[i]), end='')
        time.sleep(1.5)
        print("\r", end='')

    for i in range(count):
        print("%d번째 숫자를 입력하세요 : " % (i + 1), end='')
        if int(input()) != numbers[i]:
            print("틀렸습니다! 박승보 교수님의 과제를 실패했습니다..")
            return False

        if i == count - 1:
            print("축하합니다! 모두 맞췄습니다.")
            return True


def timingGame():
    pass


def typingGame():
    print("간호윤 교수님과 마주쳤습니다! 행운의 과제를 받았습니다.")
    time.sleep(1)
    print("타자 게임을 시작합니다.")
    time.sleep(1)
    print("제시된 문장을 %d초 안에 똑같이 입력하세요." % typingTime)
    time.sleep(1)
    input("Enter 버튼을 눌러 게임을 시작하세요.")

    typingString = random.choice(typingList)
    print("입력할 문장 : %s" % typingString)

    startTime = time.time()

    inputString = input("")

    endTime = time.time()

    if inputString == typingString:
        if endTime <= startTime + 5:
            print("축하합니다! 정확히 입력했습니다.")
        else:
            print("실패했습니다! 정답을 입력하는데 %.1f초가 걸렸습니다." % float(endTime - startTime))
    else:
        print("틀렸습니다! 간호윤 교수님의 과제를 실패했습니다..")


def pythonQuizGame():
    print("남춘성 교수님과 마주쳤습니다! 행운의 과제를 받았습니다.")
    time.sleep(1)
    print("파이썬 퀴즈 게임을 시작합니다.")
    time.sleep(1)
    print("제시된 퀴즈의 정답을 입력하세요.")
    time.sleep(1)
    input("Enter 버튼을 눌러 게임을 시작하세요.")

    randomIndex = random.randrange(0, 4)

    print(quizList[randomIndex][0])
    print(quizList[randomIndex][1])

    while True:
        answer = input("정답 : ")

        if "1" > answer or answer > "5":
            print("잘못 입력하셨습니다. 다시 입력하세요.")
        else:
            if answer == answerList[randomIndex]:
                print("축하합니다! 정답입니다.")
            else:
                print("틀렸습니다! 남춘성 교수님의 과제를 실패했습니다..")
            break
