card_value = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13,"A":14}
card = {"rank":"", "suite":"", "value":""}
suite = ["H","C","D","S"]

def create_card(rank:str, suite:str):
    card.update({"rank":rank,"suite":suite,"value":card_value[rank]})
    return card


def create_deck():
    global deck 
    deck = []
    for k in card_value:
        for j in suite:
            create_card(k, j)
            deck.append(card.copy())       
    return deck
    


def shuffle(deck:list[dict]):
    return deck
print(shuffle(create_deck()))

player = {"A"}
computer = {"6"}
def comper_cards(p1_card:dict,p2_card:dict):
    if computer > player:
        return str(computer)
    if player > computer:
        return str(player)
    else:    
        return "WAR"