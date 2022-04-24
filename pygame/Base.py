# github.com/Do-Two
# pygame 선언 
import pygame 

pygame.init()

# 전역변수 선언
WHITE = (255,255,255)
size = (600,450) 
screen = pygame.display.set_mode(size)

done = False # 게임 종료 여부
clock = pygame.time.Clock() # 프레임 설정

# 비행기 이미지 호출과 이미지 크기 조절
airplane = pygame.image.load('images/plane.png')
airplane = pygame.transform.scale(airplane,(60, 45))

def runGame():
    global done, airplane
    x = 20
    y = 24

    while not done:
        clock.tick(10) # 10fps
        screen.fill(WHITE) # 흰색 폼 생성 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN: # 키 이동 설정
                if event.key == pygame.K_w:
                    if y > 10:
                        y -= 10
                elif event.key == pygame.K_s:
                    if y < 400:
                        y += 10
                elif event.key == pygame.K_d:
                    if x < 540:
                        x += 10
                elif event.key == pygame.K_a:
                    if x > 0:
                        x -= 10
        screen.blit(airplane, (x, y))    
        pygame.display.update()
    
runGame()
pygame.quit()
        

