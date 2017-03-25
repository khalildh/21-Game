import pygame
import card_list
import random

pygame.init()

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
GREY = (255/2, 255/2, 255/2)
GREEN = (  0, 255,   0)
GREEND = (  0, 150,   0)
GREENL = (144, 238, 144)
RED =   (255,   0,   0)
BLUE =  (  0,   0, 255)
BLUEL = (199, 239, 252)
YELLOW = (255, 255, 0)
BROWN = (139,69,19)
BROWND = (92, 64, 51)

size =(700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Card Shuffler")



def livePic():
    global card_count
    card_count = -1
    
    def mainLoop(card_count):           
        done = False
        clock = pygame.time.Clock()
        
        while not done:
            if card_count == -1:
                good_card_list = card_list.reset_cards()
                card_count += 1
                print(card_count)
                print(good_card_list) 
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    card_count += 1
                    print(card_count)
                    if card_count == 53:
                        card_count = -1
            
            def draw(card_count):
                screen.fill(GREENL)
                card = pygame.image.load(good_card_list[card_count][0])
                screen.blit(card, [0, 0])
                
                pygame.display.flip()
                clock.tick(60)
                
            draw(card_count)
    
    mainLoop(card_count)
    pygame.quit()
                


if __name__ == "__main__":
    livePic()