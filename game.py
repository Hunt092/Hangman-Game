import pygame
import random

pygame.init()
WIDTH, HEIGHT= 800,600
win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hangman Game")
clock = pygame.time.Clock()
#### global variables
commits=0
run= True
ENDSCREEN = False
# COLOURS

BLACK = (0,0,0)
WHITE = (255,255,255)
RED   = (255,0,0)
GREEN = (0,255,0)
##FONTS
ltr_Font =pygame.font.SysFont("comicsms",40)
word_Font =pygame.font.SysFont("comicsms",60)
Endscreen_Font =pygame.font.SysFont("comicsms",100)
##Varibalbes
GAP=15
RADIUS=20

# Albhabets VARIABLE
start_X = round((WIDTH-(RADIUS*2+GAP)*13)/2)
start_Y = 450
A=65
letters=[]
for i in range(26):
        x = ((i%13)*(start_X+GAP)+GAP)+start_X
        y = ((i//13)*(GAP*2+RADIUS*2)+ start_Y)
        ltr= chr(A+i)
        letters.append([x,y,ltr,True])

## Word and guessed word Vatiable:
guessed=[]
words=["HUNT","BUTTER","Snow","cheeze"]
Game_word=random.choice(words).upper()

def drawscreenword():
    onScreenWord=""
    for i in Game_word:
        if i ==" ":
            onScreenWord+="  "
            continue
        if i in guessed:
            onScreenWord+= i + " "
        else:
            onScreenWord+= "_ "
    screenWord = word_Font.render(onScreenWord,1,BLACK)
    win.blit(screenWord,(WIDTH/2,HEIGHT/2))
    return onScreenWord


#Draws everything on the screen
def draw():
    win.fill(WHITE)
    ## the WORD to be guessed working loop
    drawscreenword()
    man=pygame.image.load('assets\MAN{}.png'.format(commits))
    win.blit(man,(5,10))
    ## Displays the alphaebts on the scrren to select form
    for letter in letters:
        x, y, ltr, visible= letter
        if visible:
            pygame.draw.circle(win,BLACK,(x,y),RADIUS, 3)
            word=ltr_Font.render(ltr,20,BLACK)
            win.blit(word,(x-(GAP*2-RADIUS),round(y-RADIUS/2)))

# default text box and also getting its rectangle 
def text_objects(text , font, colour):
    textSurface = font.render(text, True , colour)
    return textSurface , textSurface.get_rect()

# Creates a Button 
def Button(msg,x,y,w,h,ac,iac,mc,action=None):      

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #print(click)
        #print(mouse)

        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(win, ac,(x,y,w,h))
            if click[0]==1 and action!=None:
                action()
        else:
            pygame.draw.rect(win, iac,(x,y,w,h))
                 
        smallText = pygame.font.SysFont("comicsansms",20,True)
        textSurf, textRect = text_objects(msg, word_Font,mc)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        win.blit(textSurf, textRect) 
    

def check_collsion(x,y,mx,my):
    dis = round(( (mx-x)**2 + (my-y)**2 )**0.5 )
    return dis

def ShowEndScreen(msg=str):
    
    win.fill(WHITE)
    Endscreen = Endscreen_Font.render(msg,10,BLACK)
    win.blit(Endscreen,(WIDTH/2-150,HEIGHT/2-50))
    Button("Play Again?",WIDTH//2-WIDTH//4,HEIGHT//4+HEIGHT//2,round(WIDTH*0.5),100,GREEN,RED,BLACK)


while run:
   
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False
        if event.type ==pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            mx, my = pos
            for letter in letters:
                x,y,ltr, visible = letter
                if visible:
                    if RADIUS > check_collsion(x,y,mx,my):
                        guessed.append(ltr)
                        letter[3]=False
                        if ltr not in Game_word:
                            commits+=1

    if not ENDSCREEN:
        draw()
        #print(commits)

    guessedWord = drawscreenword()
    
    if "_ " not in guessedWord:
        ENDSCREEN= True
        ShowEndScreen("You Won!!")
       
    if commits==6:
        ENDSCREEN= True
        ShowEndScreen("You Lost!!")
    
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()