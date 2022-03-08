import pygame
import tensorflow as tf
import imgeditor
width,height=400,400
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Draw")
model=tf.keras.models.load_model("model")

pygame.font.init()
font = pygame.font.Font(None, 24)

def default():
    text1 = font.render('Press "Enter" to process.',True,"white")
    text2 = font.render('Presss "Delete" to clear.',True,"white")
    text3 = font.render('Output: ',True,"white")
    textRect1 = text1.get_rect()
    textRect2 = text2.get_rect()
    textRect3 = text2.get_rect()
    textRect1.center = (0.4*width, 0.075*height)
    textRect2.center = (0.4*width, 0.15*height)
    textRect3.center = (0.98*width, 0.1*height)
    screen.blit(text1,textRect1)
    screen.blit(text2,textRect2)
    screen.blit(text3,textRect3)
    pygame.draw.rect(screen, "blue", pygame.Rect(0.2*width, 0.3*height, 0.55*width, 0.65*height),  2)

def printresult(number):
    text = font.render(chr(number+64),True,"white")
    textRect = text.get_rect()
    textRect.center = (0.92*width, 0.1*height)
    screen.blit(text,textRect)

def capture(display,name,pos,size):
    image = pygame.Surface(size) 
    image.blit(display,(0,0),(pos,size)) 
    pygame.image.save(image,name)

default()

loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RETURN :
                capture(screen, "temp.png",(0.2*width+2,0.3*height+2),(0.55*width-4,0.65*height-4))
                number=imgeditor.recognize(model)
                printresult(number)

            if event.key == pygame.K_DELETE:
                screen.fill((0,0,0))
                default()

                
    px, py = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed() == (1,0,0):
        pygame.draw.rect(screen, "white", (px,py,20,20))

    pygame.display.update()
    
pygame.init()
pygame.quit()