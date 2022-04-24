import random

buylist = [] # 로또 구입 목록
matchnum = [] # 매칭 확인

class Lotto:
    def __init__(self):
        self.weeknum = set() # 이번주 로또번호
        self.addnum = set()  # 보너스 번호
        self.mynum = set()   # 자신 번호

    # 이번주 로또 번호 생성
    def week(self):
        self.weeknum.clear()
        self.addnum.clear()

        while len(self.weeknum) < 6:  # 로또 번호 생성 6개
            self.weeknum.add(random.randrange(1,46))

        while True:  # 보너스 번호 1개 생성
            n = random.randrange(1,46)

            if not (n in self.weeknum):  # 기존 로또 번호와 다른 번호로 생성
                self.addnum.add(n)
                break

    # 로또번호 확인 (출력)
    def Check(self):
        tmp = list(self.weeknum)
        tmp.sort()
        print("로또 번호 : " , tmp , "+" , list(self.addnum))
    
    # 내 로또번호 확인 (출력)
    def MyCheck(self):
        if buylist == []:  # 구입 여부 확인
            print("구입 내역이 없습니다.")
            return
        
        for i in range(len(buylist)):
            print(str(i+1)+"번째 구입한 번호 : " , buylist[i])
    
    # 자신의 로또번호 입력
    def insert(self):
        self.mynum.clear()

        while True:  # 로또번호 자동입력, 수동입력 설정
            n = int(input("[1] 자동 [2] 수동 : "))

            if n == 1:   # 자동으로 값 설정
                much = int(input("얼마나 구입하시겠습니까? (최대 10개) : "))

                if much > 0 and much <= 10:  # 10개 구매 제한                
                    for i in range(much):
                        if len(self.mynum) == 6:
                            self.mynum.clear()
                        while len(self.mynum) < 6:
                            self.mynum.add(random.randrange(1,46))

                        tmp = list(self.mynum)  # 구매 내역에 삽입
                        tmp.sort()
                        buylist.append(tmp)

                elif much > 10:
                    print("최대 10개까지만 구입하실수 있습니다.")
                    continue
                else:
                    print("잘못 입력하셨습니다.. 다시 입력해주세요!")
                    continue
                break

            elif n == 2:  # 수동으로 값 설정
                while len(self.mynum) < 6:
                    n = int(input(str(len(self.mynum)+1)+"번째 숫자 (1~45) : "))

                    if (n <= 0) or (n >= 46) or (n in self.mynum):  # 0보다 작거나, 45보다 크거나 중복 체크
                        print("중복된 번호 혹은 잘못된 번호가 입력되었습니다.")
                        continue
                    self.mynum.add(n)
                    tmp = list(self.mynum)
                    print("현재까지 입력된 번호 : "+str(tmp))

                tmp.sort()  # 구매 내역에 삽입
                buylist.append(tmp)
                break

            else:
                print("잘못 입력하셨습니다. 다시 입력해주세요.")
                continue

    # 로또 번호 매칭 
    def match(self):
        if buylist == []:  # 구입 여부 확인
            print("구입 내역이 없습니다.")
            return
            
        self.Check()  # 로또 번호 출력
        self.MyCheck()  # 구입 로또 번호 출력

        for i in range(len(buylist)):  # 각각 번호 매칭 확인
            n = buylist[i]
            matchnum.append(len(self.weeknum.intersection(n)))
        
            if matchnum[i] == 6:
                print(i+1,"번째꺼 [1등] 축하합니다 !! 총 20억 입니다.")
            elif matchnum[i] == 5 and self.mynum(self.addnum):
                print(i+1,"번째꺼 [2등] 축하합니다 ~~ 총 7000만원 입니다.")
            else:
                print(i+1,"번째꺼 꽝입니다 ! 다음기회에 !!")


# 메인
def Starting():
    lotto = Lotto()
    lotto.week()

    while True:
        print("1. 로또번호 보기 , 2. 로또번호 구입 , 3. 구입 로또 보기  4. 매칭 5. 종료 ")
        
        choice = int(input())
        if choice == 1:
            lotto.Check()
        elif choice == 2:
            lotto.insert()
        elif choice == 3:
            lotto.MyCheck()
        elif choice == 4:
            lotto.match()
        elif choice == 5:
            break
        print()

Starting()