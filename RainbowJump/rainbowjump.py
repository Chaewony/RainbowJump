#C077016 서채원
import pygame, sys, time, random
from pygame.locals import*
pygame.init()
pygame.display.set_caption('무지개 점프') #캡션 넣기
"""상수 값 정의, 상수명 대문자 권장"""
SCREEN_WIDTH = 900 #가로 900
SCREEN_HEIGHT = 600 #세로 600
BLACK=(0,0,0)

"""기본설정"""
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
score = 0 #현재점수 0
life = 0 #현재생명 0
start = False #title화면 플래그 변수
x=0
y=0
sf=pygame.font.Font("거승.ttf", 24)#점수,생명 나타내는 폰트 설정
sfclear=pygame.font.Font("거승.ttf", 50)#클리어시 나타나는 폰트 설정
text=sf.render("Points: " + str(score), True, (0,0,0))#점수 나타내는 텍스트 설정
chWidth=90 #캐릭터 가로폭
chHeight=70 #캐릭터 세로폭
rHeight=20 #빗방울 세로폭

"""브금 로드"""
titleBgm=pygame.mixer.Sound('title_bgm.mp3')
inGameBgm=pygame.mixer.Sound('in_game_bgm.mp3')
inGame3Bgm=pygame.mixer.Sound('in_game3_bgm.mp3')
dropSound=pygame.mixer.Sound('drop_sound.wav')
jumpSound=pygame.mixer.Sound('jump_sound.wav')
clearSound=pygame.mixer.Sound('clear_sound.wav')

"""이미지 로드, 변수명 카멜케이스 권장"""
title = pygame.image.load("title.png") #타이틀 글씨
backGround = pygame.image.load("back_ground.png") #기본 배경화면 이미지
tutorial = pygame.image.load("tutorial.png") #튜토리얼 화면
tutorial2 = pygame.image.load("tutorial2.png") #튜토리얼 화면2
mode = pygame.image.load("mode.png") #모드선택 화면
gameClear = pygame.image.load("game_clear.png") #mode1 게임클리어 화면
gameClear2 = pygame.image.load("game_clear2.png") #mode2 게임 클리어 화면 
gameClear3 = pygame.image.load("game_clear3.png") #mode3 게임 클리어 화면

startButton = pygame.image.load("start_button.png") #게임 시작 버튼
startButtonOver = pygame.image.load("start_button_over.png") #게임 시작 버튼 커서
tutorialButton = pygame.image.load("tutorial_button.png") #튜토리얼 버튼
tutorialButtonOver = pygame.image.load("tutorial_button_over.png") #튜토리얼 버튼 커서
modeButton = pygame.image.load("mode_button.png") #모드 버튼
modeButtonOver = pygame.image.load("mode_button_over.png") #모드 버튼 커서
reButton=pygame.image.load("re_button.png") #재시작 버튼
reButtonOver = pygame.image.load("re_button_over.png") #재시작 버튼 커서
backButton = pygame.image.load("back_button.png") #뒤로가기 버튼
backButtonOver = pygame.image.load("back_button_over.png") #뒤로가기 버튼 커서
nextButton = pygame.image.load("next_button.png") #다음으로가기 버튼
nextButtonOver = pygame.image.load("next_button_over.png") #다음으로가기 버튼 커서
mainButton = pygame.image.load("main_button.png") #메인으로가기 버튼
mainButtonOver = pygame.image.load("main_button_over.png") #메인으로가기 버튼 커서
selectButton = pygame.image.load("select_button.png") #선택버튼
selectButtonOver = pygame.image.load("select_button_over.png") #선택버튼 커서

cloudieFront = pygame.image.load("cloudie_front.png") #구름이 하늘색 앞모습
cloudieBlueFront = pygame.image.load("cloudie_blue_front.png") #구름이 파란색 앞모습
cloudieGrayFront = pygame.image.load("cloudie_gray_front.png") #구름이 회색 앞모습

cloudieBack = pygame.image.load("cloudie_back.png") #구름이 하늘색 뒷모습
cloudieBlueBack = pygame.image.load("cloudie_blue_back.png") #구름이 파란색 뒷모습
cloudieGrayBack = pygame.image.load("cloudie_gray_back.png") #구름이 회색 뒷모습

raindrop = pygame.image.load("raindrop.png") #빗방울
rainbowRed = pygame.image.load("rainbow_red.png") #빨간발판
rainbowOrange = pygame.image.load("rainbow_orange.png")#주황발판
rainbowYellow = pygame.image.load("rainbow_yellow.png")#노란발판
rainbowGreen = pygame.image.load("rainbow_green.png") #초록발판
rainbowBlue = pygame.image.load("rainbow_blue.png") #파란발판
rainbowNavy = pygame.image.load("rainbow_navy.png") #남색발판
rainbowPurple = pygame.image.load("rainbow_purple.png") #보라발판
rainbowGray = pygame.image.load("rainbow_gray.png") #회색발판
rainbowBlack = pygame.image.load("rainbow_black.png") #검은발판
rainbowRB=pygame.image.load("rainbow_rb.png") #무지개색 발판

"""이미지 크기조정"""
titleStretched = pygame.transform.scale(title, (450, 250))
startButtonStretched = pygame.transform.scale(startButton,(105,75))
startButtonOverStretched = pygame.transform.scale(startButtonOver,(105,75))
backButtonStretched = pygame.transform.scale(backButton, (105,75))
backButtonOverStretched = pygame.transform.scale(backButtonOver, (105,75))
nextButtonStretched = pygame.transform.scale(nextButton, (105,75))
nextButtonOverStretched = pygame.transform.scale(nextButtonOver, (105,75))

mainButtonStretched = pygame.transform.scale(mainButton, (105,75))
mainButtonOverStretched = pygame.transform.scale(mainButtonOver, (105,75))
modeButtonStretched = pygame.transform.scale(modeButton, (105,75))
modeButtonOverStretched = pygame.transform.scale(modeButtonOver, (105,75))

reButtonStretched= pygame.transform.scale(reButton, (105,75))
reButtonOverStretched = pygame.transform.scale(reButtonOver, (105,75))

selectButtonStretched = pygame.transform.scale(selectButton, (105,75))
selectButtonOverStretched = pygame.transform.scale(selectButtonOver, (105,75))

cloudieBackStretched = pygame.transform.scale(cloudieBack, (90, 70))
cloudieBlueBackStretched = pygame.transform.scale(cloudieBlueBack, (90, 70))
cloudieGrayBackStretched = pygame.transform.scale(cloudieGrayBack, (90, 70))

raindropStretched = pygame.transform.scale(raindrop,(20,40))
rainbowRedStretched = pygame.transform.scale(rainbowRed,(90,30))
rainbowOrangeStretched = pygame.transform.scale(rainbowOrange,(90,30))
rainbowYellowStretched = pygame.transform.scale(rainbowYellow,(90,30))
rainbowGreenStretched = pygame.transform.scale(rainbowGreen,(90,30))
rainbowBlueStretched = pygame.transform.scale(rainbowBlue,(90,30))
rainbowNavyStretched = pygame.transform.scale(rainbowNavy,(90,30))
rainbowPurpleStretched = pygame.transform.scale(rainbowPurple,(90,30))
rainbowGrayStretched = pygame.transform.scale(rainbowGray,(90,30))
rainbowBlackStretched = pygame.transform.scale(rainbowBlack,(90,30))
rainbowRBStretched=pygame.transform.scale(rainbowRB,(90,30))

"""사각형(rect)등 기타 설정"""
character={'rect':pygame.Rect((SCREEN_WIDTH-chWidth)/2,SCREEN_HEIGHT-chHeight, chWidth,chHeight),'color':(0,255,0),'dir':1}

#첫 번째 줄에 나오는 발판 초기 설정, 각 줄당 3개의 발판 있음
rect0={'rect':pygame.Rect(180,SCREEN_HEIGHT-rHeight, 60,rHeight),'color':(255,0,0),'dir':0,'speed':None,'num':'1-1','black':None, 'gray':None, 'red':None, 'orange':None, 'yellow':None, 'green':None, 'blue':None, 'navy':None, 'purple':None, 'RAINDROP':{'raindrop':None,'rect':pygame.Rect(0,0,40,23),'color':(0,200,200)}}
rect1={'rect':pygame.Rect(0,SCREEN_HEIGHT-rHeight, 60,rHeight),'color':(255,0,0),'dir':0,'speed':None,'num':'1-2','black':None,'gray':None,'red':None, 'orange':None, 'yellow':None, 'green':None,'blue':None, 'navy':None, 'purple':None, 'RAINDROP':{'raindrop':None,'rect':pygame.Rect(0,0,40,23),'color':(0,200,200)}}
rect2={'rect':pygame.Rect(0,SCREEN_HEIGHT-rHeight*2, 60,rHeight),'color':(255,0,0),'dir':0,'speed':None,'num':'1-3','black':None,'gray':None,'red':None, 'orange':None, 'yellow':None, 'green':None,'blue':None, 'navy':None, 'purple':None, 'RAINDROP':{'raindrop':None,'rect':pygame.Rect(0,0,40,23),'color':(0,200,200)}}
#두 번째 줄에 나오는 발판 초기 설정, 각 줄당 3개의 발판 있음
rect3={'rect':pygame.Rect(0,SCREEN_HEIGHT-rHeight*2, 60,rHeight),'color':(255,0,0),'dir':1,'speed':None,'num':'2-1','black':None, 'gray':None,'red':None, 'orange':None, 'yellow':None, 'green':None,'blue':None, 'navy':None, 'purple':None, 'RAINDROP':{'raindrop':None,'rect':pygame.Rect(0,0,40,23),'color':(0,200,200)}}
rect4={'rect':pygame.Rect(0,SCREEN_HEIGHT-rHeight*3, 60,rHeight),'color' :(255,0,0),'dir':1,'speed':None,'num':'2-2','black':None, 'gray':None,'red':None, 'orange':None, 'yellow':None, 'green':None,'blue':None, 'navy':None, 'purple':None, 'RAINDROP':{'raindrop':None,'rect':pygame.Rect(0,0,40,23),'color':(0,200,200)}}
rect5={'rect':pygame.Rect(0,SCREEN_HEIGHT-rHeight*3, 60,rHeight),'color':(255,0,0),'dir':1,'speed':None,'num':'2-3','black':None,'gray':None,'red':None, 'orange':None, 'yellow':None, 'green':None,'blue':None, 'navy':None, 'purple':None, 'RAINDROP':{'raindrop':None,'rect':pygame.Rect(0,0,40,23),'color':(0,200,200)}}
#세 번째 줄에 나오는 발판 초기 설정, 각 줄당 3개의 발판 있음
rect6={'rect':pygame.Rect(0,SCREEN_HEIGHT-rHeight*4, 60,rHeight),'color':(255,0,0),'dir':0,'speed':None,'num':'3-1','black':None,'gray':None,'red':None, 'orange':None, 'yellow':None, 'green':None,'blue':None, 'navy':None, 'purple':None, 'RAINDROP':{'raindrop':None,'rect':pygame.Rect(0,0,40,23),'color':(0,200,200)}}
rect7={'rect':pygame.Rect(0,SCREEN_HEIGHT-rHeight*4, 60,rHeight),'color':(255,0,0),'dir':0,'speed':None,'num':'3-2','black':None,'gray':None,'red':None, 'orange':None, 'yellow':None, 'green':None,'blue':None, 'navy':None, 'purple':None, 'RAINDROP':{'raindrop':None,'rect':pygame.Rect(0,0,40,23),'color':(0,200,200)}}
rect8={'rect':pygame.Rect(0,SCREEN_HEIGHT-rHeight*4, 60,rHeight),'color':(255,0,0),'dir':0,'speed':None,'num':'3-3','black':None,'gray':None,'red':None, 'orange':None, 'yellow':None, 'green':None,'blue':None, 'navy':None, 'purple':None, 'RAINDROP':{'raindrop':None,'rect':pygame.Rect(0,0,40,23),'color':(0,200,200)}}
#네 번째 줄에 나오는 발판 초기 설정, 각 줄당 3개의 발판 있음
rect9={'rect':pygame.Rect(0,SCREEN_HEIGHT-rHeight*4, 60,rHeight),'color':(255,0,0),'dir':1,'speed':None,'num':'4-1','black':None,'gray':None,'red':None, 'orange':None, 'yellow':None, 'green':None,'blue':None, 'navy':None, 'purple':None, 'RAINDROP':{'raindrop':None,'rect':pygame.Rect(0,0,40,23),'color':(0,200,200)}}
rect10={'rect':pygame.Rect(0,SCREEN_HEIGHT-rHeight*4, 60,rHeight),'color':(255,0,0),'dir':1,'speed':None,'num':'4-2','black':None,'gray':None,'red':None, 'orange':None, 'yellow':None, 'green':None,'blue':None, 'navy':None, 'purple':None, 'RAINDROP':{'raindrop':None,'rect':pygame.Rect(0,0,40,23),'color':(0,200,200)}}
rect11={'rect':pygame.Rect(0,SCREEN_HEIGHT-rHeight*4, 60,rHeight),'color':(255,0,0),'dir':1,'speed':None,'num':'4-3','black':None,'gray':None,'red':None, 'orange':None, 'yellow':None, 'green':None,'blue':None, 'navy':None, 'purple':None, 'RAINDROP':{'raindrop':None,'rect':pygame.Rect(0,0,40,23),'color':(0,200,200)}}
#다섯 번째 줄에 나오는 발판 초기 설정, 각 줄당 3개의 발판 있음
rect12={'rect':pygame.Rect(0,SCREEN_HEIGHT-rHeight*4, 60,rHeight),'color':(255,0,0),'dir':0,'speed':None,'num':'5-1','black':None,'gray':None,'red':None, 'orange':None, 'yellow':None, 'green':None,'blue':None, 'navy':None, 'purple':None, 'RAINDROP':{'raindrop':None,'rect':pygame.Rect(0,0,40,23),'color':(0,200,200)}}
rect13={'rect':pygame.Rect(0,SCREEN_HEIGHT-rHeight*4, 60,rHeight),'color':(255,0,0),'dir':0,'speed':None,'num':'5-2','black':None,'gray':None,'red':None, 'orange':None, 'yellow':None, 'green':None,'blue':None, 'navy':None, 'purple':None, 'RAINDROP':{'raindrop':None,'rect':pygame.Rect(0,0,40,23),'color':(0,200,200)}}
rect14={'rect':pygame.Rect(0,SCREEN_HEIGHT-rHeight*4, 60,rHeight),'color':(255,0,0),'dir':0,'speed':None,'num':'5-3','black':None,'gray':None,'red':None, 'orange':None, 'yellow':None, 'green':None,'blue':None, 'navy':None, 'purple':None, 'RAINDROP':{'raindrop':None,'rect':pygame.Rect(0,0,40,23),'color':(0,200,200)}}
#여섯 번째 줄에 나오는 발판 초기 설정, 각 줄당 3개의 발판 있음
rect15={'rect':pygame.Rect(0,SCREEN_HEIGHT-rHeight*4, 60,rHeight),'color':(255,0,0),'dir':1,'speed':None,'num':'6-1','black':None,'gray':None,'red':None, 'orange':None, 'yellow':None, 'green':None,'blue':None, 'navy':None, 'purple':None, 'RAINDROP':{'raindrop':None,'rect':pygame.Rect(0,0,40,23),'color':(0,200,200)}}
rect16={'rect':pygame.Rect(0,SCREEN_HEIGHT-rHeight*4, 60,rHeight),'color':(255,0,0),'dir':1,'speed':None,'num':'6-2','black':None,'gray':None,'red':None, 'orange':None, 'yellow':None, 'green':None,'blue':None, 'navy':None, 'purple':None, 'RAINDROP':{'raindrop':None,'rect':pygame.Rect(0,0,40,23),'color':(0,200,200)}}
rect17={'rect':pygame.Rect(0,SCREEN_HEIGHT-rHeight*4, 60,rHeight),'color':(255,0,0),'dir':1,'speed':None,'num':'6-3','black':None,'gray':None,'red':None, 'orange':None, 'yellow':None, 'green':None,'blue':None, 'navy':None, 'purple':None, 'RAINDROP':{'raindrop':None,'rect':pygame.Rect(0,0,40,23),'color':(0,200,200)}}

#줄 기준으로 그룹화, 리스트 생성
l1_rects=[rect0,rect1,rect2]
l2_rects=[rect3,rect4,rect5]
l3_rects=[rect6,rect7,rect8]
l4_rects=[rect9,rect10,rect11]
l5_rects=[rect12,rect13,rect14]
l6_rects=[rect15,rect16,rect17]

#하나의 리스트로 그룹화
rects=[l1_rects,l2_rects,l3_rects,l4_rects,l5_rects,l6_rects]

"""공통 함수 정의"""
#키입력 대기 함수
def wait():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                return

#버튼 만드는 함수
button_down = False
def button(x,y,w,h,picture,pictureOver, action = None, actionArgs = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global buttonDown
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        screen.blit(pictureOver, ( x,y))
        if click[0] == 1 and not buttonDown and action!= None:

            if actionArgs is not None:
                action(*actionArgs)
            else:
                action()

            buttonDown = True

        elif click[0] == 0:
            buttonDown = False
    else:
        screen.blit(picture, (x,y))

#인게임 글씨 나타내기
def draw_text():
    global life, score
    scoreText=sf.render("SCORE: " + str(score), True, (0,0,0)) #미리 설정해둔 sf폰트설정 이용해서 scoreText값 주기
    screen.blit(scoreText,(10,10)) #scoreText 화면에 나타내기, 좌표설정 (10,10)
    lifeText=sf.render("LIFE: " + str(life), True, (0,0,0)) #미리 설정해둔 sf폰트설정 이용해서 lifeText값 주기
    screen.blit(lifeText,(10,30)) #lifeText 화면에 나타내기, 좌표설정 (10,30)
    return

#게임오버 창
def gameover_screen():
    text = sf.render("GAME OVER", True, BLACK)
    text_rect = text.get_rect( )
    text_rect.centerx = screen.get_rect( ).centerx
    text_rect.y = screen.get_rect( ).centery-100
    screen.blit(text, text_rect)

#튜토리얼1쪽 화면 전환 함수
def tutorial_screen():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(tutorial, (0,0))
        button(SCREEN_WIDTH-180, SCREEN_HEIGHT-150,81,50,nextButtonStretched,nextButtonOverStretched,tutorial_screen2)
        button(SCREEN_WIDTH-300, SCREEN_HEIGHT-150,81,50,backButtonStretched,backButtonOverStretched,main)
        pygame.display.update()
        pygame.event.wait()

#튜토리얼2쪽 화면 전환 함수
def tutorial_screen2():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(tutorial2, (0,0))
        button(SCREEN_WIDTH-180, SCREEN_HEIGHT-525,81,50,startButtonStretched,startButtonOverStretched, in_game)
        button(SCREEN_WIDTH-300, SCREEN_HEIGHT-525,81,50,backButtonStretched,backButtonOverStretched,tutorial_screen)
        pygame.display.update()
        pygame.event.wait()

#모드선택화면 전환 함수
def mode_screen():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(mode, (0,0))
        button(SCREEN_WIDTH-180,SCREEN_HEIGHT-525,81,50,startButtonStretched,startButtonOverStretched,in_game)
        button(SCREEN_WIDTH-300,SCREEN_HEIGHT-525,81,50,backButtonStretched,backButtonOverStretched,main)
        button(150,360,81,50,selectButtonStretched,selectButtonOverStretched, in_game)
        button(390,360,81,50,selectButtonStretched,selectButtonOverStretched, in_game2)
        button(630,360,81,50,selectButtonStretched,selectButtonOverStretched, in_game3)
        pygame.display.update()
        pygame.event.wait()
        #button함수 인수1: 이미지x좌표, 인수2: 이미지y좌표, 인수3: 사각형 가로폭, 인수4: 사각형 세로폭, 인수5: 화면전환 함수

"""모드1(하늘색 구름이)에서만 쓰이는 함수 정의"""

#모드1 인게임 발판, 점수판 그리기
def draw_screen():
    global rainbowGray, rainbowRB, rainbowBlack
    #이미지를 전역변수로 사용하니 렉걸려서 지역변수로 고쳤음
    CLOUDIEBACK=cloudieBack
    RAINBOWRB=rainbowRB
    RAINBOWGRAY=rainbowGray
    RAINBOWBLACK=rainbowBlack
    screen.blit(backGround,(0,0))

    for l_rects in rects:
        for r in l_rects:
            #인게임에서 각각의 발판에 key값에 대한 value를 주어줌, 그것을 바탕으로 발판이미지 생성
            if r['gray']==True: #'gray'에 대한 value가 true면
                RAINBOWGRAY=pygame.transform.smoothscale(RAINBOWGRAY,(r['rect'].width,r['rect'].height)) #rainbowGray(즉, RAINBOWGRAY)를 'rect'값에 맞게 사이즈 조정
                screen.blit(RAINBOWGRAY,(r['rect'].x,r['rect'].y)) #화면에 조정된 크기의 회색 발판 이미지 생성

            elif r['black']==True: #'black'에 대한 value가 true면
                RAINBOWBLACK=pygame.transform.smoothscale(RAINBOWBLACK,(r['rect'].width,r['rect'].height)) #rainbowBlack(즉, RAINBOWBLACK)를 'rect'값에 맞게 사이즈 조정
                screen.blit(RAINBOWBLACK,(r['rect'].x,r['rect'].y)) #화면에 조정된 크기의 검은색 발판 이미지 생성

            else: #위의 조건에 해당하지 않으면
                RAINBOWRB=pygame.transform.smoothscale(RAINBOWRB,(r['rect'].width,r['rect'].height)) #rainbowRB(즉, RAINBOWRB)를 'rect'값에 맞게 사이즈 조정
                screen.blit(RAINBOWRB,(r['rect'].x,r['rect'].y)) #화면에 조정된 크기의 무지개색 발판 이미지 생성

            if r['RAINDROP']['raindrop']==True:                
                screen.blit(raindropStretched,(r['RAINDROP']['rect'].x,r['RAINDROP']['rect'].y))
    
    screen.blit(cloudieBackStretched,(character['rect'].x,character['rect'].y)) #rect값에 맞게 하늘색 구름이 뒷모습 이미지 생성
    draw_text()
    return

#모드1 점프
def jump():
    global cloudieBackStretched
    pygame.mixer.Sound.play(jumpSound) #점프 사운드 재생
    for i in range (0,20):
        #밟고 있는 땅과 밟을 땅을 제외한 모든 땅 한칸 아래로 이동
        for l_rects in rects:
            for r in l_rects:
                r['rect'].top += rHeight/20
                r['RAINDROP']['rect'].top += rHeight/20
                r['rect'].right += r['speed']
                r['RAINDROP']['rect'].right += r['speed']                       
        #캐릭터 크기와 위치를 늘렸다 줄여서 점프하는 것처럼 보이게함
        if i<10:
            character['rect'].left-=1
            character['rect'].width+=2
            character['rect'].top-=4
            character['rect'].height+=2
        else:
            character['rect'].left+=1
            character['rect'].width-=2
            character['rect'].top+=4
            character['rect'].height-=2
        draw_screen()
        time.sleep(0.01)
        pygame.display.update()
    return


#모드1 게임클리어 창
def gameclear_screen():

    screen.blit(gameClear, (0,0)) #게임 클리어 이미지 생성
    button(SCREEN_WIDTH/2-70,SCREEN_HEIGHT/2-37,75,75,reButtonStretched,reButtonOverStretched,in_game)
    button(SCREEN_WIDTH/2-70,SCREEN_HEIGHT/2+75,75,75,modeButtonStretched,modeButtonOverStretched,mode_screen)
    scoreText=sfclear.render("SCORE: " + str(score), True, (0,0,0))
    screen.blit(scoreText,(SCREEN_WIDTH/2-125,SCREEN_HEIGHT/2+200))
    pygame.display.update()
    pygame.event.wait()


#모드1 인게임화면 전환 함수
def in_game ():
    pygame.mixer.music.load('in_game_bgm.mp3')
    pygame.mixer.music.play(-1)
    global life,rainbowRB,rainbowGray, score
    while True:
        character['rect']=pygame.Rect((SCREEN_WIDTH-chWidth)/2,SCREEN_HEIGHT-chHeight, chWidth,chHeight)
        #randDir=random.randint(0,1)
        
        yCoord=SCREEN_HEIGHT-rHeight
        on_rect=rects[0][0]
        front_rect=rects[1][0]
        for l_rects in rects:
            randSpeed=random.randint(2,3)/2
            xList=[50,150,250,350,450,550]
            num=5
            for r in l_rects:
                r['rect'].y=yCoord
                xIndex=random.randint(0,num)
                r['rect'].centerx=xList.pop(xIndex)
                num-=1
                r['rect'].width=80
                
                if r['dir']==1:
                    r['speed']=randSpeed
                else:
                    r['speed']=-randSpeed

                if random.randint(0,5)==0:#빗방울 존재확률 :20%
                    r['RAINDROP']['raindrop']=True
                    r['RAINDROP']['rect'].centerx=random.randint(r['rect'].left+(r['RAINDROP']['rect'].width/2),r['rect'].right-(r['RAINDROP']['rect'].width/2))
                    r['RAINDROP']['rect'].centery=r['rect'].centery
                else :
                    r['RAINDROP']['raindrop']=False

                if random.randint(0,20)==0:#회색 발판일 확률 :20%
                    r['gray']=True
                else:
                    r['gray']=False

                if random.randint(0,20)==0:#검은색 발판일 확률 :20%
                    r['black']=True
                else:
                    r['black']=False
                
            yCoord-=rHeight
        rects[0][0]['RAINDROP']['raindrop']=False
        rects[0][0]['gray']=False
        rects[0][0]['black']=False
        rects[0][1]['RAINDROP']['raindrop']=False
        rects[0][2]['RAINDROP']['raindrop']=False
        
        rects[0][0]['rect'].centerx=SCREEN_WIDTH/2
        rects[0][1]['rect'].y=SCREEN_HEIGHT
        rects[0][2]['rect'].y=SCREEN_HEIGHT
        #첫줄만 빗방울,회색이랑 검은색x, 발판 하나만 가운데에 있게 설정
        
        score=0
        life=0
        flag=1#default 가 땅 위에 있을 때
        
        check_over=False
        check_re=False
        while not check_over: #게임오버 플래그 변수 꺼져있을 동안
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    keys=pygame.key.get_pressed()
                    if keys[K_LEFT]:
                        
                        character['rect'].x-=10
                        if character['dir']==1:
                            characterImage = pygame.transform.flip(cloudieBackStretched,True,False)
                            character['dir']=0
                    elif event.key == K_RIGHT:
                        character['rect'].x+=10
                        
                        if character['dir']==0:
                            characterImage = pygame.transform.flip(cloudieBackStretched,True,False)
                            character['dir']=1
                    if event.key == K_SPACE and flag==1:
                        jump()
                        for r in rects[1]:
                            if r['rect'].right>=character['rect'].centerx and r['rect'].left<=character['rect'].centerx and r['rect'].top==SCREEN_HEIGHT-rHeight:
                                on_rect=r
                                break
                            else:
                                continue
                            
                        if on_rect['rect'].right>=character['rect'].centerx and on_rect['rect'].left<=character['rect'].centerx and on_rect['rect'].top==SCREEN_HEIGHT-rHeight and on_rect['gray']==True:
                            #회색 발판을 밟았을 경우
                            life-=1 #생명 하나 감소
                            flag=1 #무사착지 플래그변수 true
                        elif on_rect['rect'].right>=character['rect'].centerx and on_rect['rect'].left<=character['rect'].centerx and on_rect['rect'].top==SCREEN_HEIGHT-rHeight and (on_rect['gray']==False and on_rect['black']==False):
                            #회색발판, 검은색 발판이 아닐 경우, 즉 무지개색 발판일 경우
                            score+=1 #점수1점 증가
                            flag=1 #무사착지 플래그변수 true
                            #점프했을때 땅을 밟아야하고 땅이 부서져있지 않아야함
                        else : #둘다 아닐경우, 즉 검은색 발판일 경우
                            flag=0 #무사착지 플래그변수 false

                        #게임화면 아래로 나가는 발판을 리스트 맨 앞에서 맨 뒤로 보냄   
                        rects.append(rects.pop(0))
                        #발판이 근처에 없을 때 점프하면 미끄러지면서서 게임오버
                        if flag==0 or life<0: #무사착지 플래그 변수가 false이거나 생명이 0보다 작으면
                            pygame.mixer.music.stop() #bgm끄기
                            pygame.mixer.Sound.play(dropSound) #미끄러지는 효과음 재생
                            for i in range (20):
                                character['rect'].width-=chWidth/22

                                character['rect'].left+=chWidth/36
                                character['rect'].height-=chHeight/22
                                character['rect'].top+=chHeight/24
                                time.sleep(0.015)
                                draw_screen()
                                pygame.display.update()
                                
                            check_over=True #게임오버 플래그 변수 켜짐
          
                        
                            
                        #flag가 1일 때 -> 캐릭터가 무사착지 했을 때
                        else:
                            randSpeed=( random.randint(2,3) + (score/50)*random.randint(2,3) )/2
                            #발판들의 위치와 랜덤으로 지정, flag 다시 false로
                            xList=[50,150,250,350,450,550]
                            num=5
                            for r in rects[5]:
                                r['rect'].top=SCREEN_HEIGHT-rHeight*6
                                xIndex=random.randint(0,num)
                                r['rect'].centerx=xList.pop(xIndex)
                                num-=1
                                r['rect'].width=random.randint(70,80)-random.randint(1,2)*score/3
                                
                                if r['dir']==1:
                                    r['speed']=randSpeed
                                else:
                                    r['speed']=-randSpeed
                                if random.randint(0,5)==0:#빗방울 존재확률 :5%
                                    r['RAINDROP']['raindrop']=True
                                    r['RAINDROP']['rect'].centerx=random.randint(r['rect'].left+15,r['rect'].right-15)
                                    r['RAINDROP']['rect'].centery=r['rect'].centery

                                else:
                                    r['raindrop']=False

                                if random.randint(0,20)==0: #회색 발판일 확률 :20%
                                    r['gray']=True
                                else:
                                    r['gray']=False
                                    
                                if random.randint(0,20)==0:#검은색 발판일 확률 :20%
                                    r['black']=True
                                else:
                                    r['black']=False
                                                   
            for l_rects in rects:
                for r in l_rects:
    
                    if r['rect'].left>=SCREEN_WIDTH:
                        r['rect'].right=0
                        r['RAINDROP']['rect'].right=0
                    elif r['rect'].right<=0:
                        r['rect'].left=SCREEN_WIDTH
                        r['RAINDROP']['rect'].left=SCREEN_WIDTH
                
                    r['rect'].centerx += r['speed']
                    r['RAINDROP']['rect'].centerx += r['speed']
            character['rect'].centerx +=on_rect['speed']
            #발판들이 계속 좌우로 움직이고, 구름이가 밟은 발판의 속도에 맞춰서 구름이도 이동됨
            
            if character['rect'].left>=SCREEN_WIDTH or character['rect'].right<=0  :
                check_over=True
            #구름이가 화면 밖으로 나가면 게임 오버(게임오버 플래그변수 켜짐)              
            if (character['rect'].centerx>on_rect['rect'].right or character['rect'].centerx<on_rect['rect'].left ) and flag==1 :
                pygame.mixer.music.stop()
                pygame.mixer.Sound.play(dropSound)
                for i in range (20):
                    character['rect'].width-=chWidth/22
                    character['rect'].left+=chWidth/36
                    character['rect'].height-=chHeight/22
                    character['rect'].top+=chHeight/24
                    time.sleep(0.015)
                    draw_screen()
                    pygame.display.update()    
                check_over=True
                
            if on_rect['RAINDROP']['raindrop']==True and (on_rect['RAINDROP']['rect'].left<=character['rect'].right and on_rect['RAINDROP']['rect'].right>=character['rect'].left and on_rect['RAINDROP']['rect'].bottom>=character['rect'].top):
                on_rect['RAINDROP']['raindrop']=False
                life+=1
                #빗방울 있는 발판에 착지하면 빗방울 그림 지워주고 생명 1증가
            draw_screen()
            draw_text()
            pygame.display.update()
    

            if life>=5:#목숨 5개 이상이면 클리어
                pygame.mixer.music.stop()
                pygame.mixer.Sound.play(clearSound)
                check_clear = True
                while check_clear:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                    gameclear_screen()

                    

            
        while not check_re: #게임 오버시 루프
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            button(SCREEN_WIDTH/2-55,SCREEN_HEIGHT/2-37,75,75,reButtonStretched,reButtonOverStretched,in_game)
            button(SCREEN_WIDTH/2-55,SCREEN_HEIGHT/2+100,75,75,modeButtonStretched,modeButtonOverStretched,mode_screen)
            gameover_screen()  
            pygame.display.update()
            pygame.event.wait()

"""모드2(파란색 구름이)에서만 쓰이는 함수 정의"""

#모드2 인게임 발판, 점수판 그리기
def draw_screen2():
    global rainbowRed,rainbowOrange, rainbowYellow, rainbowGreen, rainbowBlue, rainbowNavy, rainbowPurple, rainbowGray, rainbowRB, rainbowBlack
    #이미지를 전역변수로 사용하니 렉걸려서 지역변수로 고쳤음
    CLOUDIEBLUEBACK=cloudieBlueBack
    RAINBOWRED=rainbowRed
    RAINBOWORANGE=rainbowOrange
    RAINBOWYELLOW=rainbowYellow
    RAINBOWGREEN=rainbowGreen
    RAINBOWBLUE = rainbowBlue
    RAINBOWNAVY=rainbowNavy
    RAINBOWPURPLE=rainbowPurple
    RAINBOWGRAY=rainbowGray
    RAINBOWRB=rainbowRB
    RAINBOWBLACK=rainbowBlack
    screen.blit(backGround,(0,0))

    for l_rects in rects:
        for r in l_rects:
            if r['red']==True:
                RAINBOWRED=pygame.transform.smoothscale(RAINBOWRED,(r['rect'].width,r['rect'].height))
                screen.blit(RAINBOWRED,(r['rect'].x,r['rect'].y))
            elif r['orange']==True:
                RAINBOWORANGE=pygame.transform.smoothscale(RAINBOWORANGE,(r['rect'].width,r['rect'].height))
                screen.blit(RAINBOWORANGE,(r['rect'].x,r['rect'].y))
            elif r['yellow']==True:
                RAINBOWYELLOW=pygame.transform.smoothscale(RAINBOWYELLOW,(r['rect'].width,r['rect'].height))
                screen.blit(RAINBOWYELLOW,(r['rect'].x,r['rect'].y))
            elif r['green']==True:
                RAINBOWGREEN=pygame.transform.smoothscale(RAINBOWGREEN,(r['rect'].width,r['rect'].height))
                screen.blit(RAINBOWGREEN,(r['rect'].x,r['rect'].y))
            elif r['blue']==True:
                RAINBOWBLUE=pygame.transform.smoothscale(RAINBOWBLUE,(r['rect'].width,r['rect'].height))
                screen.blit(RAINBOWBLUE,(r['rect'].x,r['rect'].y))
            elif r['navy']==True:
                RAINBOWNAVY=pygame.transform.smoothscale(RAINBOWNAVY,(r['rect'].width,r['rect'].height))
                screen.blit(RAINBOWNAVY,(r['rect'].x,r['rect'].y))
            elif r['purple']==True:
                RAINBOWPURPLE=pygame.transform.smoothscale(RAINBOWPURPLE,(r['rect'].width,r['rect'].height))
                screen.blit(RAINBOWPURPLE,(r['rect'].x,r['rect'].y))

            elif r['gray']==True:
                RAINBOWGRAY=pygame.transform.smoothscale(RAINBOWGRAY,(r['rect'].width,r['rect'].height))
                screen.blit(RAINBOWGRAY,(r['rect'].x,r['rect'].y))
            elif r['black']==True:
                RAINBOWBLACK=pygame.transform.smoothscale(RAINBOWBLACK,(r['rect'].width,r['rect'].height))
                screen.blit(RAINBOWBLACK,(r['rect'].x,r['rect'].y))
            else:
                RAINBOWRB=pygame.transform.smoothscale(RAINBOWRB,(r['rect'].width,r['rect'].height))
                screen.blit(RAINBOWRB,(r['rect'].x,r['rect'].y))
            
                
            if r['RAINDROP']['raindrop']==True:                
                screen.blit(raindropStretched,(r['RAINDROP']['rect'].x,r['RAINDROP']['rect'].y))
    
    screen.blit(cloudieBlueBackStretched,(character['rect'].x,character['rect'].y))
    draw_text()
    return    

#모드2 점프
def jump2():
    global cloudieBlueBackStretched
    pygame.mixer.Sound.play(jumpSound)
    for i in range (0,20):
        #밟고 있는 발판과 밟을 발판을 제외한 모든 발판 한칸 아래로
        for l_rects in rects:
            for r in l_rects:
                r['rect'].top += rHeight/20
                r['RAINDROP']['rect'].top += rHeight/20
                r['rect'].right += r['speed']
                r['RAINDROP']['rect'].right += r['speed']                       
        #캐릭터의 크기와 위치를 늘렸다 줄여서 점프하는 것처럼 보이게!
        if i<10:
            character['rect'].left-=1
            character['rect'].width+=2
            character['rect'].top-=4
            character['rect'].height+=2
        else:
            character['rect'].left+=1
            character['rect'].width-=2
            character['rect'].top+=4
            character['rect'].height-=2
        draw_screen2()
        time.sleep(0.01)
        pygame.display.update()
    return

#모드2 게임클리어 창
def gameclear_screen2():

    screen.blit(gameClear2, (0,0))
    button(SCREEN_WIDTH/2-70,SCREEN_HEIGHT/2-37,75,75,reButtonStretched,reButtonOverStretched,in_game2)
    button(SCREEN_WIDTH/2-70,SCREEN_HEIGHT/2+75,75,75,modeButtonStretched,modeButtonOverStretched,mode_screen)
    scoreText=sfclear.render("SCORE: " + str(score), True, (0,0,0))
    screen.blit(scoreText,(SCREEN_WIDTH/2-125,SCREEN_HEIGHT/2+200))
    pygame.display.update()
    pygame.event.wait()

#모드2 인게임화면 전환 함수
def in_game2 ():
    pygame.mixer.music.load('in_game_bgm.mp3')
    pygame.mixer.music.play(-1)
    global life,rainboeRed,rainbowGray,score,rainbowOrange, rainbowYellow, rainbowGreen
    while True:
        character['rect']=pygame.Rect((SCREEN_WIDTH-chWidth)/2,SCREEN_HEIGHT-chHeight, chWidth,chHeight)
        
        yCoord=SCREEN_HEIGHT-rHeight
        on_rect=rects[0][0]
        front_rect=rects[1][0]
        for l_rects in rects:
            randSpeed=random.randint(2,3)/2
            xList=[50,150,250,350,450,550]
            num=5
            for r in l_rects:
                r['rect'].y=yCoord
                xIndex=random.randint(0,num)
                r['rect'].centerx=xList.pop(xIndex)
                num-=1
                r['rect'].width=80
                
                if r['dir']==1:
                    r['speed']=randSpeed
                else:
                    r['speed']=-randSpeed
                if random.randint(0,5)==0:#빗방울 존재확률 :5%
                    r['RAINDROP']['raindrop']=True
                    r['RAINDROP']['rect'].centerx=random.randint(r['rect'].left+(r['RAINDROP']['rect'].width/2),r['rect'].right-(r['RAINDROP']['rect'].width/2))
                    r['RAINDROP']['rect'].centery=r['rect'].centery
                else :
                    r['RAINDROP']['raindrop']=False
                if random.randint(0,20)==0:#회색 발판일 확률 :20%
                    r['gray']=True
                else:
                    r['gray']=False
                if random.randint(0,20)==0:#검은 발판일 확률 :20%
                    r['black']=True
                else:
                    r['black']=False
                if random.randint(0,20)==0:#빨간 발판일 확률 :20%
                    r['red']= True
                else:
                    r['red']=False
                if random.randint(0,20)==0:#주황 발판일 확률 :20%
                    r['orange']=True
                else:
                    r['orange']=False
                if random.randint(0,20)==0:#노란 발판일 확률 :20%
                    r['yellow']=True
                else:
                    r['yellow']=False
                if random.randint(0,20)==0:#초록 발판일 확률 :20%
                    r['green']=True
                else:
                    r['green']=False
                if random.randint(0,20)==0:#파란 발판일 확률 :10%
                    r['blue']=True
                else:
                    r['blue']=False
                if random.randint(0,20)==0:#남색 발판일 확률 :10%
                    r['navy']=True
                else:
                    r['navy']=False
                if random.randint(0,20)==0:#보라 발판일 확률 :10%
                    r['purple']=True
                else:
                    r['purple']=False
                #어느 것도 해당되지 않을 경우 무지개색 발판 출력, draw_screen2() 함수 참고
            yCoord-=rHeight
        rects[0][0]['RAINDROP']['raindrop']=False
        rects[0][0]['gray']=False
        rects[0][0]['black']=False
        rects[0][1]['RAINDROP']['raindrop']=False
        rects[0][2]['RAINDROP']['raindrop']=False
        
        rects[0][0]['rect'].centerx=SCREEN_WIDTH/2
        rects[0][1]['rect'].y=SCREEN_HEIGHT
        rects[0][2]['rect'].y=SCREEN_HEIGHT
        #첫줄만 빗방울, 회색이나 검은색 발판 x, 발판 하나만 가운데에 있게 설정
        
        score=0
        life=0
        flag=1#default 가 발판 위에 있을 때
        
        check_over=False
        check_re=False
        while not check_over:
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    keys=pygame.key.get_pressed()
                    if keys[K_LEFT]:
                        
                        character['rect'].x-=10
                        if character['dir']==1:
                            characterImage = pygame.transform.flip(cloudieBackStretched,True,False)
                            character['dir']=0
                    elif event.key == K_RIGHT:
                        character['rect'].x+=10
                        
                        if character['dir']==0:
                            characterImage = pygame.transform.flip(cloudieBackStretched,True,False)
                            character['dir']=1
                    if event.key == K_SPACE and flag==1:
                        jump2()
                        for r in rects[1]:
                            if r['rect'].right>=character['rect'].centerx and r['rect'].left<=character['rect'].centerx and r['rect'].top==SCREEN_HEIGHT-rHeight:
                                on_rect=r
                                break
                            else:
                                continue
                            
                        if on_rect['rect'].right>=character['rect'].centerx and on_rect['rect'].left<=character['rect'].centerx and on_rect['rect'].top==SCREEN_HEIGHT-rHeight and on_rect['gray']==False and on_rect['black']==False and ((on_rect['red']==True) or (on_rect['orange']==True) or (on_rect['yellow']==True) or (on_rect['green']==True)):
                        #단색 발판을 밟았을 경우
                            score+=1 #점수1 획득
                            flag=1
                            
                        elif on_rect['rect'].right>=character['rect'].centerx and on_rect['rect'].left<=character['rect'].centerx and on_rect['rect'].top==SCREEN_HEIGHT-rHeight and on_rect['gray']==False and on_rect['black']==False:
                        #무지개 발판을 밟았을 경우
                            flag=1 
                        elif on_rect['rect'].right>=character['rect'].centerx and on_rect['rect'].left<=character['rect'].centerx and on_rect['rect'].top==SCREEN_HEIGHT-rHeight and on_rect['gray']==True and on_rect['black']==False:
                        #회색 발판을 밟았을 경우
                            life-=1 #생명1 감소
                            flag=1

                        else : #검은색 발판을 밟거나 착지하지 못했을 경우
                            flag=0
                            
                        #게임화면 아래로 나가는 발판을 리스트 맨 앞에서 맨 뒤로 보냄   
                        rects.append(rects.pop(0))
                        #발판이 근처에 없을 때 점프하면 미끄러지며 게임오버
                        if flag==0 or life<0: #무사착지를 못했거나 생명이 0보다 작을 때
                            pygame.mixer.music.stop()
                            pygame.mixer.Sound.play(dropSound)
                            for i in range (20):
                                character['rect'].width-=chWidth/22

                                character['rect'].left+=chWidth/36
                                character['rect'].height-=chHeight/22
                                character['rect'].top+=chHeight/24
                                time.sleep(0.015)
                                draw_screen2()
                                pygame.display.update()    
                            
                            check_over=True
          
                        
                            
                        #flag가 1일 때 -> 캐릭터가 무사착지 했을 때
                        else:
                            randSpeed=( random.randint(2,3) + (score/50)*random.randint(2,3) )/2
                            #발판들의 위치와 랜덤으로 지정, flag 다시 0으로
                            xList=[50,150,250,350,450,550]
                            num=5
                            for r in rects[5]:
                                r['rect'].top=SCREEN_HEIGHT-rHeight*6
                                xIndex=random.randint(0,num)
                                r['rect'].centerx=xList.pop(xIndex)
                                num-=1
                                r['rect'].width=random.randint(70,80)-random.randint(1,2)*score/3
                                
                                if r['dir']==1:
                                    r['speed']=randSpeed
                                else:
                                    r['speed']=-randSpeed
                                if random.randint(0,5)==0:#빗방울 존재확률 :20%
                                    r['RAINDROP']['raindrop']=True
                                    r['RAINDROP']['rect'].centerx=random.randint(r['rect'].left+15,r['rect'].right-15)
                                    r['RAINDROP']['rect'].centery=r['rect'].centery

                                else:
                                    r['raindrop']=False

                                if random.randint(0,20)==0:#회색 발판일 확률 :20%
                                    r['gray']=True
                                else:
                                    r['gray']=False
                                if random.randint(0,20)==0:#빨간 발판일 확률 :20%
                                    r['red']=True
                                else:
                                    r['red']=False
                                if random.randint(0,20)==0:#주황 발판일 확률 :20%
                                    r['orange']=True
                                else:
                                    r['orange']=False
                                if random.randint(0,20)==0:#노란 발판일 확률 :20%
                                    r['yellow']=True
                                else:
                                    r['yellow']=False
                                if random.randint(0,20)==0:#초록 발판일 확률 :20%
                                    r['green']=True
                                else:
                                    r['green']=False
                                if random.randint(0,20)==0:#파란 발판일 확률 :20%
                                    r['blue']=True
                                else:
                                    r['blue']=False
                                if random.randint(0,20)==0:#남색 발판일 확률 :20%
                                    r['navy']=True
                                else:
                                    r['navy']=False
                                if random.randint(0,20)==0:#보라 발판일 확률 :20%
                                    r['purple']=True
                                else:
                                    r['purple']=False
                            #flag=0                     
            for l_rects in rects:
                for r in l_rects:
                   
                    if r['rect'].left>=SCREEN_WIDTH:
                        r['rect'].right=0
                        r['RAINDROP']['rect'].right=0
                    elif r['rect'].right<=0:
                        r['rect'].left=SCREEN_WIDTH
                        r['RAINDROP']['rect'].left=SCREEN_WIDTH
                
                    r['rect'].centerx += r['speed']
                    r['RAINDROP']['rect'].centerx += r['speed']
            character['rect'].centerx +=on_rect['speed']
            #발판들이 계속 좌우로 움직이고, 구름이가 밟은 발판의 속도에 맞춰서 구름이도 이동됨
            
            if character['rect'].left>=SCREEN_WIDTH or character['rect'].right<=0  :
                check_over=True
            #구름이가 화면 밖으로 나가면 게임 오버
            if (character['rect'].centerx>on_rect['rect'].right or character['rect'].centerx<on_rect['rect'].left ) and flag==1 :
                pygame.mixer.music.stop()
                pygame.mixer.Sound.play(dropSound)
                for i in range (20):
                    character['rect'].width-=chWidth/22
                    character['rect'].left+=chWidth/36
                    character['rect'].height-=chHeight/22
                    character['rect'].top+=chHeight/24
                    time.sleep(0.015)
                    draw_screen2()
                    pygame.display.update()    
                check_over=True
            if on_rect['RAINDROP']['raindrop']==True and (on_rect['RAINDROP']['rect'].left<=character['rect'].right and on_rect['RAINDROP']['rect'].right>=character['rect'].left and on_rect['RAINDROP']['rect'].bottom>=character['rect'].top):
                on_rect['RAINDROP']['raindrop']=False
                life+=1
            draw_screen2()
            draw_text()
            pygame.display.update()
            time.sleep(0.01)

            if life>=10:#목숨 10개 이상이면 클리어
                pygame.mixer.music.stop()
                pygame.mixer.Sound.play(clearSound)
                check_clear = True
                while check_clear:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                    gameclear_screen2()
            
        while not check_re:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            button(SCREEN_WIDTH/2-55,SCREEN_HEIGHT/2-37,75,75,reButtonStretched,reButtonOverStretched,in_game2)
            button(SCREEN_WIDTH/2-55,SCREEN_HEIGHT/2+100,75,75,modeButtonStretched,modeButtonOverStretched,mode_screen)
        
            gameover_screen()  
            pygame.display.update()
            pygame.event.wait()

    for l_rects in rects:
        for r in l_rects:
            if r['red']==True:
                RAINBOWRED=pygame.transform.smoothscale(RAINBOWRED,(r['rect'].width,r['rect'].height))
                screen.blit(RAINBOWRED,(r['rect'].x,r['rect'].y))
            if r['orange']==True:
                RAINBOWORANGE=pygame.transform.smoothscale(RAINBOWORANGE,(r['rect'].width,r['rect'].height))
                screen.blit(RAINBOWORANGE,(r['rect'].x,r['rect'].y))
            if r['yellow']==True:
                RAINBOWYELLOW=pygame.transform.smoothscale(RAINBOWYELLOW,(r['rect'].width,r['rect'].height))
                screen.blit(RAINBOWYELLOW,(r['rect'].x,r['rect'].y))
            if r['green']==True:
                RAINBOWGREEN=pygame.transform.smoothscale(RAINBOWGREEN,(r['rect'].width,r['rect'].height))
                screen.blit(RAINBOWGREEN,(r['rect'].x,r['rect'].y))

            elif r['gray']==True:
                RAINBOWGRAY=pygame.transform.smoothscale(RAINBOWGRAY,(r['rect'].width,r['rect'].height))
                screen.blit(RAINBOWGRAY,(r['rect'].x,r['rect'].y))
            if r['RAINDROP']['raindrop']==True:                
                screen.blit(raindropStretched,(r['RAINDROP']['rect'].x,r['RAINDROP']['rect'].y))

    screen.blit(cloudieBackStretched,(character['rect'].x,character['rect'].y))
    draw_text()
    return


"""모드3(회색 구름이)에서만 쓰이는 함수 정의"""

#모드3 인게임 발판, 점수판 그리기
def draw_screen3():
    global rainbowRed,rainbowOrange, rainbowYellow, rainbowGreen, rainbowBlue, rainbowNavy, rainbowPurple, rainbowGray, rainbowRB, rainbowBlack
    #이미지를 전역변수로 사용하니 렉걸려서 지역변수로 고쳤음
    CLOUDIEGRAYBACK=cloudieGrayBack
    RAINBOWRED=rainbowRed
    RAINBOWORANGE=rainbowOrange
    RAINBOWYELLOW=rainbowYellow
    RAINBOWGREEN=rainbowGreen
    RAINBOWBLUE = rainbowBlue
    RAINBOWNAVY=rainbowNavy
    RAINBOWPURPLE=rainbowPurple
    RAINBOWGRAY=rainbowGray
    RAINBOWRB=rainbowRB
    RAINBOWBLACK=rainbowBlack
    screen.blit(backGround,(0,0))

    for l_rects in rects:
        for r in l_rects:
            if r['red']==True:
                RAINBOWRED=pygame.transform.smoothscale(RAINBOWRED,(r['rect'].width,r['rect'].height))
                screen.blit(RAINBOWRED,(r['rect'].x,r['rect'].y))
            elif r['orange']==True:
                RAINBOWORANGE=pygame.transform.smoothscale(RAINBOWORANGE,(r['rect'].width,r['rect'].height))
                screen.blit(RAINBOWORANGE,(r['rect'].x,r['rect'].y))
            elif r['yellow']==True:
                RAINBOWYELLOW=pygame.transform.smoothscale(RAINBOWYELLOW,(r['rect'].width,r['rect'].height))
                screen.blit(RAINBOWYELLOW,(r['rect'].x,r['rect'].y))
            elif r['green']==True:
                RAINBOWGREEN=pygame.transform.smoothscale(RAINBOWGREEN,(r['rect'].width,r['rect'].height))
                screen.blit(RAINBOWGREEN,(r['rect'].x,r['rect'].y))
            elif r['blue']==True:
                RAINBOWBLUE=pygame.transform.smoothscale(RAINBOWBLUE,(r['rect'].width,r['rect'].height))
                screen.blit(RAINBOWBLUE,(r['rect'].x,r['rect'].y))
            elif r['navy']==True:
                RAINBOWNAVY=pygame.transform.smoothscale(RAINBOWNAVY,(r['rect'].width,r['rect'].height))
                screen.blit(RAINBOWNAVY,(r['rect'].x,r['rect'].y))
            elif r['purple']==True:
                RAINBOWPURPLE=pygame.transform.smoothscale(RAINBOWPURPLE,(r['rect'].width,r['rect'].height))
                screen.blit(RAINBOWPURPLE,(r['rect'].x,r['rect'].y))

            elif r['gray']==True:
                RAINBOWGRAY=pygame.transform.smoothscale(RAINBOWGRAY,(r['rect'].width,r['rect'].height))
                screen.blit(RAINBOWGRAY,(r['rect'].x,r['rect'].y))
            elif r['black']==True:
                RAINBOWBLACK=pygame.transform.smoothscale(RAINBOWBLACK,(r['rect'].width,r['rect'].height))
                screen.blit(RAINBOWBLACK,(r['rect'].x,r['rect'].y))
            else:
                RAINBOWRB=pygame.transform.smoothscale(RAINBOWRB,(r['rect'].width,r['rect'].height))
                screen.blit(RAINBOWRB,(r['rect'].x,r['rect'].y))
            
                
            if r['RAINDROP']['raindrop']==True:                
                screen.blit(raindropStretched,(r['RAINDROP']['rect'].x,r['RAINDROP']['rect'].y))
    
    screen.blit(cloudieGrayBackStretched,(character['rect'].x,character['rect'].y))
    draw_text()
    return    

#모드3 점프
def jump3():
    global cloudieGrayBackStretched
    pygame.mixer.Sound.play(jumpSound)
    for i in range (0,20):
        #밟고 있는 발판과 밟을 발판을 제외한 모든 발판 한칸 아래로
        for l_rects in rects:
            for r in l_rects:
                r['rect'].top += rHeight/20
                r['RAINDROP']['rect'].top += rHeight/20
                r['rect'].right += r['speed']
                r['RAINDROP']['rect'].right += r['speed']                       
        #캐릭터의 크기와 위치를 늘렸다 줄여서 점프하는 것처럼 보이게!
        if i<10:
            character['rect'].left-=1
            character['rect'].width+=2
            character['rect'].top-=4
            character['rect'].height+=2
        else:
            character['rect'].left+=1
            character['rect'].width-=2
            character['rect'].top+=4
            character['rect'].height-=2
        draw_screen3()
        time.sleep(0.01)
        pygame.display.update()
    return

#모드3 게임클리어 창
def gameclear_screen3():

    screen.blit(gameClear3, (0,0))
    button(SCREEN_WIDTH/2-70,SCREEN_HEIGHT/2-37,75,75,reButtonStretched,reButtonOverStretched,in_game3)
    button(SCREEN_WIDTH/2-70,SCREEN_HEIGHT/2+75,75,75,modeButtonStretched,modeButtonOverStretched,mode_screen)
    scoreText=sfclear.render("SCORE: " + str(score), True, (0,0,0))
    screen.blit(scoreText,(SCREEN_WIDTH/2-125,SCREEN_HEIGHT/2+200))
    pygame.display.update()
    pygame.event.wait()

#모드3 인게임화면 전환 함수
def in_game3 ():
    pygame.mixer.music.load('in_game3_bgm.mp3')
    pygame.mixer.music.play(-1)
    global life,rainboeRed,rainbowGray,score,rainbowOrange, rainbowYellow, rainbowGreen
    while True:
        character['rect']=pygame.Rect((SCREEN_WIDTH-chWidth)/2,SCREEN_HEIGHT-chHeight, chWidth,chHeight)
        
        yCoord=SCREEN_HEIGHT-rHeight
        on_rect=rects[0][0]
        front_rect=rects[1][0]
        for l_rects in rects:
    
            xList=[50,150,250,350,450,550]
            num=5
            for r in l_rects:
                r['rect'].y=yCoord
                xIndex=random.randint(0,num)
                r['rect'].centerx=xList.pop(xIndex)
                num-=1
                r['rect'].width=80
                
                if r['dir']==1:
                    r['speed']=10 #스피드10으로 지정
                else:
                    r['speed']=-10 #스피드 역방향10으로 지정
                if random.randint(0,5)==0:#빗방울 존재확률 :5%
                    r['RAINDROP']['raindrop']=True
                    r['RAINDROP']['rect'].centerx=random.randint(r['rect'].left+(r['RAINDROP']['rect'].width/2),r['rect'].right-(r['RAINDROP']['rect'].width/2))
                    r['RAINDROP']['rect'].centery=r['rect'].centery
                else :
                    r['RAINDROP']['raindrop']=False
                    
                if random.randint(0,20)==0:#회색 발판일 확률 :20%
                    r['gray']=True
                else:
                    r['gray']=False
                if random.randint(0,20)==0:#검은 발판일 확률 :20%
                    r['black']=True
                else:
                    r['black']=False
                if random.randint(0,20)==0:#빨간 발판일 확률 :20%
                    r['red']= True
                else:
                    r['red']=False
                if random.randint(0,20)==0:#주황 발판일 확률 :20%
                    r['orange']=True
                else:
                    r['orange']=False
                if random.randint(0,20)==0:#노란 발판일 확률 :20%
                    r['yellow']=True
                else:
                    r['yellow']=False
                if random.randint(0,20)==0:#초록 발판일 확률 :20%
                    r['green']=True
                else:
                    r['green']=False
                if random.randint(0,20)==0:#파란 발판일 확률 :10%
                    r['blue']=True
                else:
                    r['blue']=False
                if random.randint(0,20)==0:#남색 발판일 확률 :10%
                    r['navy']=True
                else:
                    r['navy']=False
                if random.randint(0,20)==0:#보라 발판일 확률 :10%
                    r['purple']=True
                else:
                    r['purple']=False
                #어느 것도 해당되지 않을 경우 무지개색 발판 출력, draw_screen3() 함수 참고
            yCoord-=rHeight
        rects[0][0]['RAINDROP']['raindrop']=False
        rects[0][0]['gray']=False
        rects[0][0]['black']=False
        rects[0][0]['speed']=0
        rects[0][1]['RAINDROP']['raindrop']=False
        rects[0][2]['RAINDROP']['raindrop']=False
        
        rects[0][0]['rect'].centerx=SCREEN_WIDTH/2
        rects[0][1]['rect'].y=SCREEN_HEIGHT
        rects[0][2]['rect'].y=SCREEN_HEIGHT
        #첫줄만 빗방울, 회색이랑 검은색 발판 x, 스피드0, 발판 하나만 가운데에 있게 설정
        
        score=0
        life=0
        flag=1#default 가 발판 위에 있을 때
        
        check_over=False
        check_re=False
        while not check_over:
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    keys=pygame.key.get_pressed()
                    if keys[K_LEFT]:
                        
                        character['rect'].x-=10
                        if character['dir']==1:
                            characterImage = pygame.transform.flip(cloudieBackStretched,True,False)
                            character['dir']=0
                    elif event.key == K_RIGHT:
                        character['rect'].x+=10
                        
                        if character['dir']==0:
                            characterImage = pygame.transform.flip(cloudieBackStretched,True,False)
                            character['dir']=1
                    if event.key == K_SPACE and flag==1:
                        jump3()
                        for r in rects[1]:
                            if r['rect'].right>=character['rect'].centerx and r['rect'].left<=character['rect'].centerx and r['rect'].top==SCREEN_HEIGHT-rHeight:
                                on_rect=r
                                break
                            else:
                                continue
                            
                        if on_rect['rect'].right>=character['rect'].centerx and on_rect['rect'].left<=character['rect'].centerx and on_rect['rect'].top==SCREEN_HEIGHT-rHeight and on_rect['gray']==False and on_rect['black']==False and ((on_rect['red']==True) or (on_rect['orange']==True) or (on_rect['yellow']==True) or (on_rect['green']==True)):
                        #단색 발판을 밟았을 경우
                            score+=1 #점수1 획득
                            flag=1
                            
                        elif on_rect['rect'].right>=character['rect'].centerx and on_rect['rect'].left<=character['rect'].centerx and on_rect['rect'].top==SCREEN_HEIGHT-rHeight and on_rect['gray']==False and on_rect['black']==False:
                        #무지개 발판을 밟았을 경우
                            flag=1 
                        elif on_rect['rect'].right>=character['rect'].centerx and on_rect['rect'].left<=character['rect'].centerx and on_rect['rect'].top==SCREEN_HEIGHT-rHeight and on_rect['gray']==True and on_rect['black']==False:
                        #회색 발판을 밟았을 경우
                            life-=1 #생명1 감소
                            flag=1

                        else : #검은색 발판을 밟거나 착지하지 못했을 경우
                            flag=0
                            
                        #게임화면 아래로 나가는 발판을 리스트 맨 앞에서 맨 뒤로 보냄   
                        rects.append(rects.pop(0))
                        #발판이 근처에 없을 때 점프하면 미끄러지며 게임오버
                        if flag==0 or life<0: #무사착지를 못했거나 생명이 0보다 작을 때
                            pygame.mixer.music.stop()
                            pygame.mixer.Sound.play(dropSound)
                            for i in range (20):
                                character['rect'].width-=chWidth/22

                                character['rect'].left+=chWidth/36
                                character['rect'].height-=chHeight/22
                                character['rect'].top+=chHeight/24
                                time.sleep(0.015)
                                draw_screen3()
                                pygame.display.update()    
                            
                            check_over=True
          
                        
                            
                        #flag가 1일 때 -> 캐릭터가 무사착지 했을 때
                        else:
                            #발판들의 위치와 랜덤으로 지정, flag 다시 0으로
                            xList=[50,150,250,350,450,550]
                            num=5
                            for r in rects[5]:
                                r['rect'].top=SCREEN_HEIGHT-rHeight*6
                                xIndex=random.randint(0,num)
                                r['rect'].centerx=xList.pop(xIndex)
                                num-=1
                                r['rect'].width=random.randint(70,80)-random.randint(1,2)*score/3
                                
                                if r['dir']==1:
                                    r['speed']=10 #스피드10으로 지정
                                else:
                                    r['speed']=-10 #스피드 역방향10으로 지정
                                if random.randint(0,5)==0:#빗방울 존재확률 :20%
                                    r['RAINDROP']['raindrop']=True
                                    r['RAINDROP']['rect'].centerx=random.randint(r['rect'].left+15,r['rect'].right-15)
                                    r['RAINDROP']['rect'].centery=r['rect'].centery

                                else:
                                    r['raindrop']=False

                                if random.randint(0,20)==0:#회색 발판일 확률 :20%
                                    r['gray']=True
                                else:
                                    r['gray']=False
                                if random.randint(0,20)==0:#빨간 발판일 확률 :20%
                                    r['red']=True
                                else:
                                    r['red']=False
                                if random.randint(0,20)==0:#주황 발판일 확률 :20%
                                    r['orange']=True
                                else:
                                    r['orange']=False
                                if random.randint(0,20)==0:#노란 발판일 확률 :20%
                                    r['yellow']=True
                                else:
                                    r['yellow']=False
                                if random.randint(0,20)==0:#초록 발판일 확률 :20%
                                    r['green']=True
                                else:
                                    r['green']=False
                                if random.randint(0,20)==0:#파란 발판일 확률 :20%
                                    r['blue']=True
                                else:
                                    r['blue']=False
                                if random.randint(0,20)==0:#남색 발판일 확률 :20%
                                    r['navy']=True
                                else:
                                    r['navy']=False
                                if random.randint(0,20)==0:#보라 발판일 확률 :20%
                                    r['purple']=True
                                else:
                                    r['purple']=False
                                
                                #구름이가 길을 건넜을 때 0행 1~3열에 해당하는 발판들을 멈춘다
                                rects[0][0]['speed']=0
                                rects[0][1]['speed']=0
                                rects[0][2]['speed']=0
                                               
            for l_rects in rects:
                for r in l_rects:
                   
                    if r['rect'].left>=SCREEN_WIDTH:
                        r['rect'].right=0
                        r['RAINDROP']['rect'].right=0
                    elif r['rect'].right<=0:
                        r['rect'].left=SCREEN_WIDTH
                        r['RAINDROP']['rect'].left=SCREEN_WIDTH
                
                    r['rect'].centerx += r['speed']
                    r['RAINDROP']['rect'].centerx += r['speed']
            character['rect'].centerx +=on_rect['speed']
            #발판들이 위에서 정해진 속도인0에따라 멈추고, 구름이가 밟은 발판의 속도(0)에 맞춰서 구름이도 이동하지 않음
            
            if character['rect'].left>=SCREEN_WIDTH or character['rect'].right<=0  :
                check_over=True
            #구름이가 화면 밖으로 나가면 게임 오버
            if (character['rect'].centerx>on_rect['rect'].right or character['rect'].centerx<on_rect['rect'].left ) and flag==1 :
                pygame.mixer.music.stop()
                pygame.mixer.Sound.play(dropSound)
                for i in range (20):
                    character['rect'].width-=chWidth/22
                    character['rect'].left+=chWidth/36
                    character['rect'].height-=chHeight/22
                    character['rect'].top+=chHeight/24
                    time.sleep(0.015)
                    draw_screen3()
                    pygame.display.update()    
                check_over=True
            if on_rect['RAINDROP']['raindrop']==True and (on_rect['RAINDROP']['rect'].left<=character['rect'].right and on_rect['RAINDROP']['rect'].right>=character['rect'].left and on_rect['RAINDROP']['rect'].bottom>=character['rect'].top):
                on_rect['RAINDROP']['raindrop']=False
                life+=1
            draw_screen3()
            draw_text()
            pygame.display.update()
            time.sleep(0.01)

            if life>=10:#목숨 10개 이상이면 클리어
                pygame.mixer.music.stop()
                pygame.mixer.Sound.play(clearSound)
                check_clear = True
                while check_clear:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                    gameclear_screen3()
            
        while not check_re:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            button(SCREEN_WIDTH/2-55,SCREEN_HEIGHT/2-37,75,75,reButtonStretched,reButtonOverStretched,in_game3)
            button(SCREEN_WIDTH/2-55,SCREEN_HEIGHT/2+100,75,75,modeButtonStretched,modeButtonOverStretched,mode_screen)
        
            gameover_screen()  
            pygame.display.update()
            pygame.event.wait()

    for l_rects in rects:
        for r in l_rects:
            if r['red']==True:
                RAINBOWRED=pygame.transform.smoothscale(RAINBOWRED,(r['rect'].width,r['rect'].height))
                screen.blit(RAINBOWRED,(r['rect'].x,r['rect'].y))
            if r['orange']==True:
                RAINBOWORANGE=pygame.transform.smoothscale(RAINBOWORANGE,(r['rect'].width,r['rect'].height))
                screen.blit(RAINBOWORANGE,(r['rect'].x,r['rect'].y))
            if r['yellow']==True:
                RAINBOWYELLOW=pygame.transform.smoothscale(RAINBOWYELLOW,(r['rect'].width,r['rect'].height))
                screen.blit(RAINBOWYELLOW,(r['rect'].x,r['rect'].y))
            if r['green']==True:
                RAINBOWGREEN=pygame.transform.smoothscale(RAINBOWGREEN,(r['rect'].width,r['rect'].height))
                screen.blit(RAINBOWGREEN,(r['rect'].x,r['rect'].y))

            elif r['gray']==True:
                RAINBOWGRAY=pygame.transform.smoothscale(RAINBOWGRAY,(r['rect'].width,r['rect'].height))
                screen.blit(RAINBOWGRAY,(r['rect'].x,r['rect'].y))
            if r['RAINDROP']['raindrop']==True:                
                screen.blit(raindropStretched,(r['RAINDROP']['rect'].x,r['RAINDROP']['rect'].y))

    screen.blit(cloudieBackStretched,(character['rect'].x,character['rect'].y))
    draw_text()
    return

###############################################################################################################################################################################################
def main():
    pygame.mixer.music.load('title_bgm.mp3')
    pygame.mixer.music.play(-1)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(backGround,(0,0))
        screen.blit(titleStretched,(210,20))

        button(325,200,200,130,startButton,startButtonOver,in_game)
        button(325,335,200,130,tutorialButton,tutorialButtonOver,tutorial_screen)
        button(325,460,200,130,modeButton,modeButtonOver,mode_screen)
        pygame.display.update()
        pygame.event.wait()
    pygame.quit

if __name__ == '__main__':
    main()
