import pygame
import random

pygame.init()
WIDTH, HEIGHT= 800,600
win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hangman Game")
clock = pygame.time.Clock()
run= True
ENDSCREEN = False
# COLOURS

BLACK = (0,0,0)
WHITE = (255,255,255)

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
Game_word=random.choice(words)

def drawscreenword():
    onScreenWord=""
    for i in Game_word.upper():
        if i ==" ":
            onScreenWord+="  "
            continue
        if i in guessed:
            onScreenWord+= i + " "
        else:
            onScreenWord+= "_ "
    screenWord = word_Font.render(onScreenWord,1,BLACK)
    win.blit(screenWord,(WIDTH/2-width()/2,HEIGHT/2))
    return onScreenWord
#Draws everything on the screen
def draw():
    win.fill(WHITE)
    ## the WORD to be guessed working loop
    drawscreenword()

    ## Displays the alphaebts on the scrren to select form
    for letter in letters:
        x, y, ltr, visible= letter
        if visible:
            pygame.draw.circle(win,BLACK,(x,y),RADIUS, 3)
            word=ltr_Font.render(ltr,1,BLACK)
            win.blit(word,(x-(GAP*2-RADIUS),round(y-RADIUS/2)))

    pygame.display.update()
    

def check_collsion(x,y,mx,my):
    dis = round(( (mx-x)**2 + (my-y)**2 )**0.5 )
    return dis


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
    if not ENDSCREEN:
        draw()

    guessedWord = drawscreenword()
    
    if "_ " not in guessedWord:
        ENDSCREEN= True
        win.fill(WHITE)
        Endscreen = word_Font.render("You WON!!",1,BLACK)
        win.blit(Endscreen,(WIDTH/2,HEIGHT/2))
        pygame.display.update()

    clock.tick(60)
pygame.quit()
quit()