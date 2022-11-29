import random
import time


def updownGame():
    question = random.randint(1, 10)
    count = 0
    print("1부터 10까지 내가 생각한 숫자를 3번의 기회 안에 맞춰보세요^^")

    while True:
        count += 1
        answer = int(input("제가 생각하는 숫자는 : "))
        if answer == question:
            print("정답입니다!")
            return True
        else:
            print("틀렸습니다!")
            if answer < question:
                print("UP")
            else:
                print("DOWN")

        if count == 3:
            print("3번의 기회를 줬는데 맞추지 못했군요 정답은 %d입니다" % question)
            return False


def typingGame():
    list1 = ["주경야독은 바쁜 틈을 타서 어렵게 공부함을 이르는 말입니다", "귀모토각은 있을 수 없는 것이나 불가능한 일 등의 비유입니다",
             "유유상종 같은 사람은 서로 모인다는 말입니다", "적소성대는 티끌모아 태산을 의미합니다"]
    question = random.choice(list1)
    print("사자성어 뜻을 알려줄테니 맞춤법, 띄어쓰기 틀리지 말고 읽어보세요(키보드로 입력 후 엔터)")
    input("Enter키를 누르면 바로 시작합니다")
    print(question)
    start = time.time()
    answer = input()
    end = time.time()
    input_time = int(end - start)
    if input_time < 15:
        if question == answer:
            print("정답입니다!")
            return True
        else:
            print("틀렸습니다!")
            return False
    else:
        print("%d초 걸렸습니다. 시간초과 입니다" % input_time)
        return False


def python_quizGame():
    question_num = 4
    question_list = ["인하대학교 소프트웨어융합공학과 2022년도 1학기 컴퓨터공학 수업을 가르치는 교수님의 성함은 OOO교수님이다. OOO안에 들어갈 단어를 띄어쓰기 없이 3자로 입력하시오.",
                     "파이썬은 16비트의 OO코드 문자열을 지원해서 다양한 언어의 문자 처리가 가능하다. 이때 OO안에 들어갈 단어를 띄어쓰기없이 2자로 입력하시오.",
                     "현실을 디지털 세상으로 확장시키는 것으로, 가상+세계를 의미하는 유니버스의 합성어를 OOOO라고 부른다. 이때 OOOO안에 들어갈 단어를 띄어쓰기 없이 4자로 입력하시오.",
                     "파이썬 연산자 **는 수의 OO을 구하는 연산자이다. 이때 OO안에 들어갈 단어를 띄어쓰기 없이 2자로 입력하시오"]
    true_list = ["남춘성", "유니", "메타버스", "제곱"]
    answer_list = ["학생.. 내 이름도 모르고 수업 듣고 있었나..? 난 학생 이름 반드시 기억하도록 하지.",
                   "학생, 강의 들은 거 맞아? 이런식으로 공부하면 안된다니까그러네. 모르면 질문을 했어야지!",
                   "학생, 강의 들은 거 맞아? 이런식으로 공부하면 안된다니까그러네. 모르면 질문을 했어야지!",
                   "학생, 강의 들은 거 맞아? 이런식으로 공부하면 안된다니까그러네. 모르면 질문을 했어야지!", ]
    index = random.randrange(0, question_num)
    answer = input(question_list[index])
    if answer == true_list[index]:
        print("정답입니다")
        return True
    else:
        print(answer_list[index])
        return False


def memoryGame():
    print("기억력 게임입니다. 일정 시간 동안 보이는 숫자를 외워 그대로 입력하세요.")
    input("Enter키를 누르면 바로 시작합니다")

    question_list = []
    for i in range(4):
        question_list.append(random.randrange(10, 99))
        print("%d" % question_list[i], end='')
        time.sleep(1.5)
        print("\r", end='')

    for z in range(4):
        print("%d번째 숫자를 입력하세요" % (z + 1))
        a = int(input())
        if a != question_list[z]:
            print("틀렸습니다.")
            return False
            break
        if a == question_list[3]:
            print("정답입니다.")
            return True
