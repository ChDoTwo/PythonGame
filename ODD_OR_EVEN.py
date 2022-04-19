import random

done = False

while not done:
  rungame = True
  # 1~9 랜덤 숫자 하나 생성
  print(" 랜덤으로 숫자 하나가 생성 되었습니다.")
  result = random.randrange(1,9)

  # 사용자 답 입력
  while rungame:
    answer = int(input("그 값이 <1> 홀 <2> 짝 : "))

    # 정답 확인
    if (answer == 1 and result % 2 == 1) or (answer == 2 and result % 2 == 0):
      print("\n맞췄습니다. 정답입니다!")

    elif (answer == 1 and result % 2 == 0) or (answer == 2 and result % 2 == 1):
      print("\n틀렸습니다. 아쉽습니다.")
    
    else:
      print("잘못입력하셨습니다..")
      continue
     
    # 답 공개
    print("답은 {} 였습니다!\n".format(result))
    rungame = False

  # 재시작 여부
  restart = int(input("게임 종료를 원하시면 1번, 다시 시작하실려면 아무키나 입력해주세요."))
  if restart == 1:
    done = True
    