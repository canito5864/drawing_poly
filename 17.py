import pygame
import sys
from math import atan2,sin,cos,pi
from time import sleep

pygame.init()

# 화면 설정
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("17")

# 색깔
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0,255,0)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #시간 조절
    def T():
        pygame.display.flip()
        sleep(0.3)

    #기준선&원 그리기
    pygame.draw.line(screen,red,(160,240),(480,240),1)
    T()
    pygame.draw.circle(screen, white, (320,240), 80, 2)
    T()

    #수직이등분선 그리기
    def pm(x1,y1,x2,y2,r):
        xd=(x2-x1)/2
        yd=(y2-y1)/2
        xm=(x1+x2)/2
        ym=(y1+y2)/2
        pygame.draw.circle(screen, blue, (x1, y1), r, 1)
        T()
        pygame.draw.circle(screen, blue, (x2, y2), r, 1)
        T()
        pygame.draw.line(screen, red, (xm+yd,ym-xd),(xm-yd,ym+xd) ,1)
        T()
        return xm+yd,ym-xd,xm-yd,ym+xd

    #각이등분선 그리기
    def ab(ax,ay,bx1,by1,bx2,by2,d):
        s = atan2((ay-by1),(bx1-ax))
        f = atan2((ay-by2),(bx2-ax))
        pygame.draw.arc(screen,blue,(ax-d,ay-d,2*d,2*d),f,s)
        T()
        pygame.draw.circle(screen,blue,(bx1,by1), d,1)
        T()
        pygame.draw.circle(screen,blue,(bx2,by2), d,1)
        T()
        pygame.draw.line(screen,red,(ax,ay),(ax+d*cos(-(s+f)/2),ay+d*sin(-(s+f)/2)),1)
        T()
        return ax+d*cos(-(s+f)/2), ay+d*sin(-(s+f)/2)

    #두 점 사이 거리 구하기
    def pd(x1,y1,x2,y2):
        return ((x1-x2)**2+(y1-y2)**2)**(1/2)


    #작도 시작, 전부 작도 과정임

    pm(240, 240,400, 240, 160)
    sleep(0.5)
    pm(320,160,320,240,80)
    sleep(0.5)
    pm(320,200,320,240,40)
    sleep(0.5)

    pygame.draw.line(screen, red, (320, 220), (400, 240), 1)
    T()

    #화면 정리
    screen.fill(black)
    pygame.draw.line(screen, red, (120, 240), (480, 240), 1)
    pygame.draw.line(screen, red, (320, 80), (320,400), 1)
    pygame.draw.circle(screen, white, (320, 240), 80, 2)
    pygame.draw.line(screen, red, (320, 220), (400, 240), 1)
    T()
    sleep(0.3)

    d=pd(320,220,400,240)
    abx1,aby1 = ab(320, 220, 400, 240, 320, 220+d,d)
    T()
    abx2,aby2 = ab(320,220,abx1,aby1,320, 220+d,d)
    T()

    pygame.draw.line(screen,red,(abx2,aby2),(640-abx2,440-aby2),1)
    T()
    sleep(0.3)

    abx3,aby3,n,m = pm(abx2,aby2,640-abx2,440-aby2,d)
    T()
    abx4,aby4 = ab(320,220,abx2,aby2,abx3,aby3,d)
    T()

    #화면 정리
    screen.fill(black)
    pygame.draw.line(screen, red, (120, 240), (480, 240), 1)
    pygame.draw.line(screen, red, (320, 80), (320, 400), 1)
    pygame.draw.circle(screen, white, (320, 240), 80, 2)
    pygame.draw.line(screen,red,(abx2,aby2),(640-abx2,440-aby2),1)
    pygame.draw.line(screen, red,(320,220),(abx4,aby4),1)
    T()
    sleep(0.3)

    px0 = 320 - (20 * ((320 - abx4) / (aby4 - 220)))
    pm(px0, 240, 400, 240, (400 - px0))
    sleep(0.3)

    pygame.draw.circle(screen, blue, ((px0 + 400) / 2, 240), (400 - px0) / 2, 1)
    T()
    sleep(0.5)

    #화면 정리
    screen.fill(black)
    pygame.draw.line(screen, red, (120, 240), (480, 240), 1)
    pygame.draw.line(screen, red, (320, 80), (320, 400), 1)
    pygame.draw.circle(screen, white, (320, 240), 80, 2)
    pygame.draw.line(screen, red, (abx2, aby2), (640 - abx2, 440 - aby2), 1)
    pygame.draw.line(screen, red, (320, 220), (abx4, aby4), 1)
    pygame.draw.circle(screen, blue, ((px0 + 400) / 2, 240), (400 - px0) / 2, 1)
    T()
    sleep(0.3)

    px1=(abx2-320)*20/(aby2-220)+320
    py2=240-(20*((400-px0)/2)/pd(320,220,(px0+400)/2,240))
    px2=((px0+400)/2)-(((px0+400)/2-320)*((400-px0)/2)/pd(320,220,(px0+400)/2,240))
    pygame.draw.circle(screen,blue,(px1,240),pd(px1,240,px2,py2),1)
    T()
    sleep(0.5)

    #화면 정리
    screen.fill(black)
    pygame.draw.line(screen, red, (120, 240), (480, 240), 1)
    pygame.draw.line(screen, red, (320, 80), (320, 400), 1)
    pygame.draw.circle(screen, white, (320, 240), 80, 2)
    pygame.draw.line(screen, red, (abx2, aby2), (640 - abx2, 440 - aby2), 1)
    pygame.draw.line(screen, red, (320, 220), (abx4, aby4), 1)
    pygame.draw.circle(screen,blue,(px1,240),pd(px1,240,px2,py2),1)
    T()
    sleep(0.3)

    pygame.draw.circle(screen, blue, (px1+ pd(px1, 240, px2, py2),240),20, 1)
    T()
    sleep(0.5)
    pm(px1+ pd(px1, 240, px2, py2)-20,240,px1+ pd(px1, 240, px2, py2)+20,240,20)
    pygame.draw.line(screen, red, (px1+ pd(px1, 240, px2, py2),240), (px1+ pd(px1, 240, px2, py2),168),1)
    T()
    sleep(0.3)

    #화면 정리
    screen.fill(black)
    pygame.draw.line(screen, red, (120, 240), (480, 240), 1)
    pygame.draw.line(screen, red, (320, 80), (320, 400), 1)
    pygame.draw.circle(screen, white, (320, 240), 80, 2)
    pygame.draw.line(screen, red, (px1 + pd(px1, 240, px2, py2), 240), (px1 + pd(px1, 240, px2, py2), 168), 1)
    T()
    sleep(0.5)

    pygame.draw.line(screen,green,(px1 + pd(px1, 240, px2, py2),168),(400,240),2)
    T()
    l=pd(px1 + pd(px1, 240, px2, py2),168,400,240)
    pygame.draw.circle(screen,blue,(400,240),l,1)
    T()
    sleep(0.5)

    #작도로 구한 각과 반지름을 이용해 원 반복해서 그리기
    for i in range(17):
        a=((2*pi)*3/17)*i
        pygame.draw.circle(screen,blue,(320+80*cos(a),240+80*sin(a)),l,1)
        T()
    sleep(0.5)

    #교점 이어 그리기 -> 17각형 작도 끝
    for i in range(17):
        a=((2*pi)/17)*i
        na=((2*pi)/17)*(i+1)
        pygame.draw.aaline(screen, green, (320 + 80 * cos(a), 240 + 80 * sin(a)),
                         (320 + 80 * cos(na), 240 + 80 * sin(na)), 2)
        T()
    sleep(0.5)

    #화면정리, 17각형만 보여주기
    screen.fill(black)
    for i in range(17):
        a=((2*pi)/17)*i
        na=((2*pi)/17)*(i+1)
        pygame.draw.aaline(screen, green, (320 + 80 * cos(a), 240 + 80 * sin(a)),
                         (320 + 80 * cos(na), 240 + 80 * sin(na)), 2)
    T()
    sleep(5.0)

    running=False

# 종료
pygame.quit()
sys.exit()
