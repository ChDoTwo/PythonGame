import pygame
import random
from datetime import datetime
from datetime import timedelta

pygame.init()

## 색상
RED   = (255,   0,   0)   # 먹이
GREEN = (  0, 255,   0)   # 뱀 몸통
BLACK = (  0,   0,   0)   # 뱀 머리
WHITE = (255, 255, 255)   # 폼

# 폼 크기 및 생성
size = (800,400)
screen = pygame.display.set_mode(size)

# 게임 종료 여부 및 프레임
form_crash = 0
done = False
clock = pygame.time.Clock()

# 속도 설정
apple_eat = 0    # 먹은 갯수
speed_move = 0.3 # 속도 s

# 자동 무빙
last_moved_time = datetime.now()

# 키 딕셔너리
KEY_DIRECTION = {
    pygame.K_w: "UP",
    pygame.K_s: "DOWN",
    pygame.K_a: "LEFT",
    pygame.K_d: "RIGHT",
}

# 이미지 생성
def draw_Head(position):    # 뱀 머리
    pygame.draw.rect(screen, BLACK, (position[0]*15, position[1]*15, 15, 15))

def draw_Snake(position):   # 뱀 생성
    pygame.draw.rect(screen, GREEN, (position[0]*15, position[1]*15, 15, 15))

def draw_Apple(position):   # 먹이 생성
    pygame.draw.rect(screen, RED, (position[0]*15, position[1]*15, 15, 15))

# 뱀 무빙 클래스
class Snake:
    def __init__(self):
        # 2, 0 이 뱀 머리, 뱀 처음 포지션
        self.positions = [(2, 0),(1, 0),(0, 0)]
        self.direction = ""

    # 뱀 이미지 생성
    def draw(self):
        for position in self.positions:
            if position == self.positions[0]:
                draw_Head(position)
            else:
                draw_Snake(position)

    # 뱀 무빙
    def move(self):
        head_position = self.positions[0]
        x, y = head_position
        if self.direction == "UP":
            self.positions = [(x , y - 1)] + self.positions[:-1]
        elif self.direction == "DOWN":
            self.positions = [(x , y + 1)] + self.positions[:-1]
        elif self.direction == "LEFT":
            self.positions = [(x - 1 , y)] + self.positions[:-1]
        elif self.direction == "RIGHT":
            self.positions = [(x + 1 , y)] + self.positions[:-1]
        # 벽 충돌 확인
        if x < 0 or x > 53 or y < 0 or y > 26:
            self.form_crash += 1
        
    
    # 뱀 꼬리 추가
    def grow(self):
        tail_position = self.positions[-1]
        x, y = tail_position
        if self.direction == "UP":
            self.positions.append((x, y - 1))
        elif self.direction == "DOWN":
            self.positions.append((x, y + 1))
        elif self.direction == "LEFT":
            self.positions.append((x - 1, y))
        elif self.direction == "RIGHT":
            self.positions.append((x + 1, y))

# 사과 클래스
class Apple:
    def __init__(self,position=(5, 5)):
        self.position = position

    # 사과 이미지 생성
    def draw(self):
            draw_Apple(self.position)

    
# 메인
def GamePlay():
    global done, last_moved_time
    global speed_move, apple_eat # 난이도 조절
    snake = Snake()
    apple = Apple()

    while not done:
        clock.tick(10)
        screen.fill(WHITE)

        # 키 입력 받기
        for event in pygame.event.get():
            # 오른쪽 상단 종료
            if event.type == pygame.QUIT:
                done = True
            # 키보드 입력
            if event.type == pygame.KEYDOWN:
                if event.key in KEY_DIRECTION:
                    snake.direction = KEY_DIRECTION[event.key]
                    snake.move()
                    last_moved_time = datetime.now()

        # 0.3초 마다 자동 무빙
        if timedelta(seconds = speed_move) <= datetime.now() - last_moved_time:
            snake.move()
            last_moved_time = datetime.now()
        

        # 먹이 섭취 확인
        if snake.positions[0] == apple.position:
            snake.grow()
            apple.position = (random.randint(0, 50), random.randint(0, 25))
            # 먹은 갯수 +1
            apple_eat += 1
            # 3개 먹을때마다 0.05초 감소
            if apple_eat % 3 == 0:
                speed_move -= 0.05

        # 뱀 충돌 확인
        if snake.positions[0] in snake.positions[1:]:
            done = True

        # 벽 충돌 확인
        if form_crash > 0:
            done = True

        snake.draw()
        apple.draw()
        pygame.display.update()

GamePlay()
pygame.quit()

