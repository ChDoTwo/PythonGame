# github.com/Do-Two
import pygame
import random

pygame.init()

# 전역변수 선언
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
GREEN = (  0, 255,   0)

# 폼 설정
screen_width = 600 # 가로
screen_height = 600 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("BricksBreak") #제목
done = False # 게임 종료 여부
clock = pygame.time.Clock() # 프레임 설정

# 스틱 바 설정
stick = pygame.Rect(screen_width // 2 - 100 // 2, screen_height - 16, 100, 16)

# 블록 설정
blocks = []
COLUMN_COUNT = 6
ROW_COUNT = 6
for column_index in range(COLUMN_COUNT):
    for row_index in range(ROW_COUNT):
        block = pygame.Rect(column_index*(80+10)+35, row_index*(16+5)+35, 80, 16)
        blocks.append(block) 

# 볼 설정
ball = pygame.Rect(screen_width // 2 - 16 // 2, screen_height // 2 - 16 // 2, 16, 16)

# 스틱 바 이미지 생성
def draw_stick():
    pygame.draw.rect(screen, WHITE, stick)

# 블록 이미지 생성
def draw_block(block_color):
    for block in blocks:
            pygame.draw.rect(screen, block_color, block)
            
# 볼 이미지 생성
def draw_ball():
    pygame.draw.circle(screen, WHITE, (ball.centerx, ball.centery), ball.width // 2)

# 메인
def runGame():

    global done

    # 스피드 설정
    stick_x = 0 
    ball_x = -3
    ball_y = -5

    while not done:
        clock.tick(30)
        screen.fill(BLACK)

        # 키 입력
        for event in pygame.event.get():
            # 오른쪽 상단 x
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    stick_x = -5
                elif event.key == pygame.K_RIGHT:
                    stick_x = 5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    stick_x = 0
                elif event.key == pygame.K_RIGHT:
                    stick_x = 0

        # 이동
        stick.left += stick_x
        ball.left += ball_x
        ball.top += ball_y

        # 볼 벽 부딪힘 처리
        if ball.left <= 0:  # 왼쪽벽
            ball.left = 0
            ball_x = -ball_x
        elif ball.left >= screen_width - ball.width: # 오른쪽 벽
            ball.left = screen_width - ball.width
            ball_x = -ball_x
        if ball.top < 0:    # 위쪽 벽
            ball.top = 0
            ball_y = -ball_y
        elif ball.top >= screen_height: # 아래쪽 벽
            ball.left = screen_width // 2 - ball.width // 2
            ball.top = screen_height // 2 - ball.width // 2
            ball_y = -ball_y 

        # 볼 블록 부딪힘 처리
        for block in blocks:
            if ball.colliderect(block):
                blocks.remove(block)
                ball_y = -ball_y
                break

        # 스틱 바에 볼 부딪힘
        if ball.colliderect(stick):
            ball_y = -ball_y

        # 스틱 바 폼 이탈 방지
        if stick.left < 0:
            stick.left = 0
        elif stick.left > screen_width - stick.width:
            stick.left = screen_width - stick.width

        draw_block(GREEN)
        draw_stick()
        draw_ball()

        pygame.display.update()
    
runGame()
pygame.quit()