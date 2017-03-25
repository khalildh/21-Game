import pygame
import card_list
import random
import time

pygame.init()

font = pygame.font.Font(None, 25)

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
pygame.display.set_caption("21 Game")

class  Player():
    
    def __init__(self):
        self.gameScore = 100
        self.cardsHeld = []
        self.score = 0
        
        




#print(User.cardsHeld)




def livePic():
    global card_count
    global roundCount
       
    card_count = -1
    roundCount = 0
    
    def mainLoop(card_count, roundCount):           
        done = False
        clock = pygame.time.Clock()
        User = Player()
        global cardVal
        cardVal = 0
        
        while not done:
             
            def start(card_count):
                global good_card_list
                global cardVal
                cardVal = 0
                if card_count == -1:
                    
                    good_card_list = card_list.reset_cards()
                    card_count += 1
                    #print(card_count)
                    #print(good_card_list)
                    
                    if len(User.cardsHeld) < 2:
                        print("Ya", len(User.cardsHeld))
                        User.cardsHeld.append(good_card_list[cardVal])
                        User.score += User.cardsHeld[cardVal][1]
                        cardVal += 1
                        User.cardsHeld.append(good_card_list[cardVal])
                        User.score += User.cardsHeld[cardVal][1]
                        cardVal += 1
                        
                        print(User.score)
                    
            start(card_count)
             
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    cardVal = len(User.cardsHeld)
                    User.cardsHeld.append(good_card_list[cardVal])
                    User.score = User.score + User.cardsHeld[cardVal][1]
                    print(User.cardsHeld[cardVal])
                    print(User.score)
                    cardVal += 1
                    print(cardVal)
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        print("Your Round Score  was: {} ".format(21 - User.score))
                        if User.score <= 21:
                            User.gameScore -= (21 - User.score) 
                        elif User.score > 21:
                            User.gameScore -= (User.score - 21)
                        roundCount += 1
                        User.cardsHeld = []
                        User.score = 0                         
                        start(-1)
                        
                    
            
                
            
            def draw(card_count, roundCount):
                screen.fill(BLUEL)
                nextCard = 0
                for i in range(len(User.cardsHeld)):
                    #card = pygame.image.load(good_card_list[card_count][0])
                    card = pygame.image.load(User.cardsHeld[i][0])
                    screen.blit(card, [nextCard, 0])
                    nextCard += 140
                
                output_string = "This is Round {}".format(roundCount + 1)
                text = font.render(output_string, True, BLACK)
                screen.blit(text, [250, 250])
                
                output_string = "Your current score is {}".format(User.score)
                text = font.render(output_string, True, BLACK)
                screen.blit(text, [250, 300])
                
                output_string = "The Game score is {}".format(User.gameScore)
                text = font.render(output_string, True, BLACK)
                screen.blit(text, [250, 350])                 
                
                pygame.display.flip()
                clock.tick(60)
                
                
                
                
            draw(card_count, roundCount)
    
    mainLoop(card_count, roundCount)
    pygame.quit()
                


if __name__ == "__main__":
    livePic()
#"""