import random

done = False

while not done:
  cnt = 5  # 기회

  # 랜덤 1 ~ 50 숫자 생성
  print("랜덤으로 숫자 하나를 생성중입니다.")
  result = random.randrange(1,50)
  print("★☆★☆★ 숫자가 생성 되었습니다 .!! ★☆★☆★")

  # 답 입력
  for i in range(5,0,-1):
    answer = int(input("1 ~ 50까지의 숫자 중 하나를 말해주세요 : "))
    # 마지막 기회에서
    if i == 1:
      if answer == result:
        print("\n\n축하합니다. 정답입니다!\n\n")
      else:
        print("\n모든 기회를 소멸하셨습니다.")
        print("정답은 {} 였습니다.\n".format(result))
    # 평상시 기회
    else:
      if answer > result:
        print("\n[DOWN] 더 아래의 숫자입니다!")
        print("기회 {} 번 남았습니다.\n".format(i-1))

      elif answer < result:
        print("\n[UP] 더 위의 숫자입니다!")
        print("기회 {} 번 남았습니다!\n".format(i-1))

      else:
        print("\n\n축하합니다. 정답입니다!\n\n")
        break

  # 재시작 여부
  restart = int(input("게임 종료를 원하시면 1번, 다시 시작하실려면 아무키나 입력해주세요. : "))
  if restart == 1:
    done = True