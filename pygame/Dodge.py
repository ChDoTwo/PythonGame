# github.com/Do-Two
# pygame 선언 
import pygame 
import random
import os

pygame.init()

# 전역변수 선언
WHITE = (255,255,255)
BLACK = (  0,  0,  0)
size = (600,900)
screen = pygame.display.set_mode(size)

# 게임 설정
done = False # 게임 종료 여부
clock = pygame.time.Clock() # 프레임 설정
pygame.display.set_caption("Dodge game") #게임 이름

# 비행기 이미지 호출과 이미지 크기 조절
airplane_image = pygame.image.load('images/Airplane.png') # 이미지 호출
airplane_image = pygame.transform.scale(airplane_image,(70, 50)) # 사이즈 설정
airplane = pygame.Rect(airplane_image.get_rect())

# 비행기 시작 위치 설정 및 좌표 값 
airplane.left = (size[0] // 2) - (airplane.width // 2)
airplane.top = size[1] - airplane.height

# 총알 이미지 호출과 이미지 크기 조절
bullet_image = pygame.image.load('images/bullet.png') # 이미지 호출
bullet_image = pygame.transform.scale(bullet_image,(20, 20)) # 사이즈 설정
bullets = [] # 총알 갯수 담기

# 총알 생성 함수
for i in range(5):
    rect = pygame.Rect(bullet_image.get_rect())
    rect.left = random.randint(0, size[0])
    rect.top = -100
    dy = 10
    bullets.append({'rect':rect, 'dy':dy})

# 메인
def runGame():
    global done
    plane_x = 0
    plane_y = 0
    while not done:
        clock.tick(30) 
        screen.fill(BLACK)

        # 종료 확인
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            # 키 입력 설정
            if event.type == pygame.KEYDOWN:    # 키 눌렀을 때
                if event.key == pygame.K_RIGHT:
                    plane_x = 10
                elif event.key == pygame.K_LEFT:
                    plane_x = -10
            if event.type == pygame.KEYUP:      # 키 눌럿다 땟을 때
                if event.key == pygame.K_RIGHT:
                    plane_x = 0
                elif event.key == pygame.K_LEFT:
                    plane_x = 0
        
        # 총알 이동
        for bullet_down in bullets:
            bullet_down['rect'].top += bullet_down['dy']
            # 밑에 닿으면 삭제
            if bullet_down['rect'].top >= size[1]:
                bullets.remove(bullet_down)
            # 중간 지점 지나면 생성
            elif bullet_down['rect'].top == size[1]//3:
                rect = pygame.Rect(bullet_image.get_rect())
                rect.left = random.randint(0, size[0])
                rect.top = 10
                dy = 10
                bullets.append({'rect':rect, 'dy':dy})

        # 총알에 닿았는지 확인
        for touch in bullets:
            if touch['rect'].colliderect(airplane):
                done = True
            screen.blit(bullet_image, touch['rect'])

        # 비행기 이동
        airplane.left += plane_x
        # 비행기 화면 탈출 방지
        if airplane.left < 0:
            airplane.left = 0
        elif airplane.left > size[0] - airplane.width:
            airplane.left = size[0] - airplane.width
        screen.blit(airplane_image, airplane)

        pygame.display.update()
    
runGame()
pygame.quit()