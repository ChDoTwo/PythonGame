import random

done = False

result = {'win':0,'lose':0,'draw':0}  # 전적
cnt = 1  # 게임 횟수

while not done:
    print("****** [{}번째]가위바위보 게임 ******".format(cnt))
    print("1.가위\t 2.바위\t 3.보\t 4.전적보기\t 5.종료\n")
    answer = int(input("\n무엇을 낼건가요? : "))

    # 게임 진행
    if answer > 0 and answer < 4:
        cnt += 1
        # 컴퓨터
        com = random.randrange(3)
        if com == 0:
            print("컴퓨터는 가위를 냈습니다.")
        elif com == 1:
            print("컴퓨터는 바위를 냈습니다.")
        else:
            print("컴퓨터는 보자기를 냈습니다.")
        
        # 승패 확인
        if com == answer:
            print("\n======= 서로 비겼습니다 !! =======\n")
            result["draw"] += 1  # draw +1
        elif ((com==1) and (answer==3)) or ((com==2) and (answer==1)) or ((com==3) and (answer==2)):
            print("\n======= 당신이 졌습니다 !! =======\n")
            result["lose"] += 1  # lose +1
        else:
            print("\n======= 당신이 이기셨습니다 !! =======\n")
            result["win"] += 1  # win +1
    # 전적 출력
    elif answer == 4:
        print("\n★☆★☆★☆★☆★☆★☆★☆")
        print(result)
        print("★☆★☆★☆★☆★☆★☆★☆\n")
    # 종료 여부
    elif answer == 5:
        done = True
    else:
        print("잘못 입력하셨습니다.\n\n")    
