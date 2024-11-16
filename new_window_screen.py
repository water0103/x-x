#https://www.youtube.com/watch?v=sQDFydEtBLE&t=984s
import pygame

windowsize = 800    #new window size = 800 * 800
window = pygame.display.set_mode((windowsize , windowsize))     #using pygame display fuction to show a new window with 800 *800
time = pygame.time.Clock()  #time fuction

running = True
while(running):
    time.tick(5)    #I am not sure about it
    window.fill((0 , 0 , 0))    #define the new window background color
    for event in pygame.event.get():    #make sure it can quit, although we won't run that
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()   #continuous update display so that it can run
pygame.quit