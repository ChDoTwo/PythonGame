import random

done = False

while not done:
  # 모드 선택
  num = 0
  ending = False
  mode = int(input("모드 선택 <1> 1인 <2> 2인 : "))


  # 1인모드
  if mode == 1:
    while not ending:
      # 인간 턴 
      print()
      cnt = int(input("\n몇 회 연속된 숫자를 부르시겠습니까? : "))
      print(">>",end=" ")

      if cnt > 0 and cnt < 4:  # 1~3 숫자만 받을 수 있게
        for i in range(cnt):
          num += 1
          print(num, end=" ")
          if num == 31:  # 31 체크
            print("\n★★★ 당신이 지셨습니다.★★★")
            ending = True
            break
      else:
        print("잘못 입력하셨습니다. (1~3)")
        continue
      
      if ending == True:  # 인간 턴에서 종료 여부 확인
        continue

      # 컴퓨터 턴
      print()
      print("\n컴퓨터 차례입니다.")
      print(">>",end=" ")
      compu = random.randrange(1, 4)
      for i in range(compu):
        num += 1
        print(num,end=" ")
        if num == 31:
          print("\n★★★ 당신이 이기셨습니다. ★★★")
          ending = True
          break
      

  # 2인모드
  elif mode == 2:
    while not ending:
      print()
      cnt = int(input("몇 회 연속된 숫자를 부르시겠습니까? : "))
      print(">> ", end=" ")
      if cnt > 0 and cnt < 4:
        for i in range(cnt):
          num += 1
          print(num, end=" ")
          if num == 31:
            print("31을 외치셨습니다. 당신이 지셨습니다.")
            ending = True
            break
      else:
        print("잘못 입력하셨습니다. (1~3)")
        continue

  # 모드 선택 실수
  else:
    print("잘못 입력하셨습니다. ")
    continue

  # 재시작 여부
  restart = int(input("게임 종료를 원하시면 1번, 다시 시작하실려면 아무키나 입력해주세요."))
  if restart == 1:
    done = True
  else:
    pass



