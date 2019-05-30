# -*- coding: utf-8 -*-
"""
Created on Fri May 17 10:33:50 2019

@author: RS ji
"""
import random
cardlist = ['ace', '2','3','4','5','6','7','8','9','10','J','Q','K']
card_count = {'ace':4,'2':4,'3':4,'4':4,'5':4,'6':4,'7':4,'8':4,'9':4,'10':4,'J':4,'Q':4,'K':4}
card_value = {'ace':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}

class Player:
    def __init__(self):
        self.total = 0
        self.diff = 21
        self.cards = {'ace':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'J':0,'Q':0,'K':0}
    def hit(self, new_card):
        if new_card == 'ace':
            if 21-self.total >= 11:
                self.total += 11
            else:
                self.total += card_value[new_card]
        else:
            self.total += card_value[new_card]
        card_count[new_card]-=1
        self.cards[new_card]+=1
        self.diff = 21-self.total
        print(f'Your total is: {self.total}')
        if(self.total >21):
            print('Bust condition!')
            return -1
        if 21-self.total > 0:
            return self.diff

print('Welcome to BackJack! \n')
human = Player()
comp = Player()
ch = 'y'
new_card = ''
while ch == 'y':
    s = random.shuffle(cardlist)
    new_card = cardlist[0]
    human.hit(new_card)
    print(f"Human gets a {new_card}")
    if human.diff<0:
        print('Sorry! You have lost')
    ch = input("Do you want to Hit again!")
if human.diff<0:
    print("Computer has won!")
    
else:
    while comp.diff>0:
        s = random.shuffle(cardlist)
        new_card = cardlist[0]
        print(f"Computer gets a {new_card}")
        comp.hit(new_card)
    if comp.diff<0:
        print("Human has won!")
    else:
        print(f"Human total: {human.total}\n")
        print(f"Computer total: {comp.total}\n")
        if comp.diff < human.diff:
            print("Computer has won!")
        else:
            print("Human has won!")
print("The list of cards with human are:")
for key,value in human.cards.items():
    if value>0:
        print(f"{key}:{value}\n")
print("The list of cards with computer are:")
for key,value in comp.cards.items():
    if value>0:
        print(f"{key}:{value}\n")
   