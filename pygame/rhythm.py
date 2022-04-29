# github.com/Do-Two
# pygame 선언 
import pygame 

pygame.init()

# 전역변수 선언
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)
BLUE  = (  0,   0, 255)

# 폼 설정
screen_height = 900
screen_width = 600
size = (screen_width, screen_height) 
screen = pygame.display.set_mode(size)

done = False  # 게임 종료 여부
clock = pygame.time.Clock()  # 프레임 설정

# 폰트 설정
small_font = pygame.font.SysFont(None, 50)


# 포인트 클래스 선언
class Point:
    def __init__(self):
        self.position_x = 50, 180, 310, 440  # 포인트 x축 리스트
        self.point_list = []

        for i in range(4):
            rect = pygame.Rect(self.position_x[i], screen_height - 150, 100, 50)
            self.point_list.append(rect)
    
    # 이미지 생성
    def draw(self):
        for i in range(4):
            pygame.draw.rect(screen, WHITE, self.point_list[i], width=1)



# 비트 클래스 선언
class Beat:
    def __init__(self, speed = 20):
        self.position_x = 50, 180, 310, 440  # 비트 x축 리스트
        self.speed = speed  # 떨어지는 속도 인수로 받기, 초기값 20 (난이도 설정)
        self.beats = []  # 각각 떨어지는 비트 구분
        self.ponts = small_font.render("HOLD", True, GREEN)  # 폰트 초기 값

        y = - 100
        # 초기 4개의 비트 생성
        for i in range(4):
            rect = pygame.Rect(self.position_x[i], y, 100, 50)
            self.beats.append({'rect':rect})
            y -= 100


    # 이미지 생성
    def draw(self):
        for beat_draw in self.beats:
            pygame.draw.rect(screen, RED, beat_draw['rect'])


    # 비트 움직임 설정
    def move(self):
        for beat_down in self.beats:
            beat_down['rect'].top += self.speed  # 자동 추락

            if beat_down['rect'].top > (screen_height + 100):  # 바닥에 떨어 질시 다시 위로
                beat_down['rect'].top = -100

                self.ponts = small_font.render("FAIL", True, RED)  # 폰트 메시지 FAIL 으로 변환
                screen.blit(self.ponts, (screen_width // 2 - 50 , screen_height // 2 - 50))  


    # 비트랑 포인트가 닿았는지 체크
    def match(self, i, point_list):
        for beat_match in self.beats:
            if beat_match['rect'].colliderect(point_list):
                beat_match['rect'] = pygame.Rect(self.position_x[i], -100, 100, 50)

                self.ponts = small_font.render("GOOD", True, GREEN)  # 폰트 메시지 GOOD 으로 변환
                screen.blit(self.ponts, (screen_width // 2 - 50 , screen_height // 2 - 50))  

    # 폰트 비추기
    def pont_view(self):
        screen.blit(self.ponts, (screen_width // 2 - 50 , screen_height // 2 - 50))    



# 메인
def runGame():
    global done
    beat = Beat()
    point = Point()

    while not done:
        clock.tick(30) # 10fps
        screen.fill(BLACK) # 흰색 폼 생성 

        # 키 입력
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # 종료
                done = True
            elif event.type == pygame.KEYDOWN:  # 키 눌렀을 때
                if event.key == pygame.K_a:  # 스페이스바
                    beat.match(0, point.point_list[0])
                elif event.key == pygame.K_s:
                    beat.match(1, point.point_list[1])
                elif event.key == pygame.K_d:
                    beat.match(2, point.point_list[2])
                elif event.key == pygame.K_f:
                    beat.match(3, point.point_list[3])
                 

        # 비트 좌우 이동
        beat.move()

        # 이미지 생성
        beat.draw()
        beat.pont_view()
        point.draw()

        pygame.display.update()
    
runGame()
pygame.quit()