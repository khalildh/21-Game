import random

Clubs10 = "cardClubs10.png", 10
Clubs2 = "cardClubs2.png", 2
Clubs3 = "cardClubs3.png", 3
Clubs4 = "cardClubs4.png", 4
Clubs5 = "cardClubs5.png", 5
Clubs6 = "cardClubs6.png", 6
Clubs7 = "cardClubs7.png", 7
Clubs8 = "cardClubs8.png", 8
Clubs9 = "cardClubs9.png", 9
ClubsA = "cardClubsA.png", 1
ClubsJ = "cardClubsJ.png", 10
ClubsK = "cardClubsK.png", 10
ClubsQ = "cardClubsQ.png", 10
Diamonds10 = "cardDiamonds10.png", 10
Diamonds2 = "cardDiamonds2.png", 2
Diamonds3 = "cardDiamonds3.png", 3
Diamonds4 = "cardDiamonds4.png", 4
Diamonds5 = "cardDiamonds5.png", 5
Diamonds6 = "cardDiamonds6.png", 6
Diamonds7 = "cardDiamonds7.png", 7
Diamonds8 = "cardDiamonds8.png", 8
Diamonds9 = "cardDiamonds9.png", 9
DiamondsA = "cardDiamondsA.png", 1
DiamondsJ = "cardDiamondsJ.png", 10
DiamondsK = "cardDiamondsK.png", 10
DiamondsQ = "cardDiamondsQ.png", 10
Hearts10 = "cardHearts10.png", 10
Hearts2 = "cardHearts2.png", 2
Hearts3 = "cardHearts3.png", 3
Hearts4 = "cardHearts4.png", 4
Hearts5 = "cardHearts5.png", 5
Hearts6 = "cardHearts6.png", 6
Hearts7 = "cardHearts7.png", 7
Hearts8 = "cardHearts8.png", 8
Hearts9 = "cardHearts9.png", 9
HeartsA = "cardHeartsA.png", 1
HeartsJ = "cardHeartsJ.png", 10
HeartsK = "cardHeartsK.png", 10
HeartsQ = "cardHeartsQ.png", 10
#Joker = "cardJoker.png", 0
#Joker = "cardJoker.png", 0
Spades10 = "cardSpades10.png", 10
Spades2 = "cardSpades2.png", 2
Spades3 = "cardSpades3.png", 3
Spades4 = "cardSpades4.png", 4
Spades5 = "cardSpades5.png", 5
Spades6 = "cardSpades6.png", 6
Spades7 = "cardSpades7.png", 7
Spades8 = "cardSpades8.png", 8
Spades9 = "cardSpades9.png", 9
SpadesA = "cardSpadesA.png", 1
SpadesJ = "cardSpadesJ.png", 10
SpadesK = "cardSpadesK.png", 10
SpadesQ = "cardSpadesQ.png", 10

all_cards_list = [Clubs10, Clubs2, Clubs3, Clubs4, Clubs5, Clubs6, Clubs7, Clubs8, Clubs9, ClubsA, ClubsJ, ClubsK, ClubsQ, Diamonds10, Diamonds2, Diamonds3, Diamonds4, Diamonds5, Diamonds6, Diamonds7, Diamonds8, Diamonds9, DiamondsA, DiamondsJ, DiamondsK, DiamondsQ, Hearts10, Hearts2, Hearts3, Hearts4, Hearts5, Hearts6, Hearts7, Hearts8, Hearts9, HeartsA, HeartsJ, HeartsK, HeartsQ, Spades10, Spades2, Spades3, Spades4, Spades5, Spades6, Spades7, Spades8,Spades9, SpadesA, SpadesJ, SpadesK, SpadesQ]

""" Removed The Jokers from All cards List
Joker, Joker
"""


def reset_cards():
    card_list_copy = list(all_cards_list)
    shuffled_cards = []

    for i in range(0, len(card_list_copy)):
        random_card = card_list_copy[random.randrange(0, len(card_list_copy))]
        shuffled_cards.append(random_card)    
        card_list_copy.remove(random_card)
    
    return shuffled_cards
    


