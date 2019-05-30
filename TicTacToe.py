# -*- coding: utf-8 -*-
"""
Created on Thu May  2 17:00:45 2019

@author: RS ji
"""

mydict = {'1':' ', '2':' ', '3':' ', '4':' ', '5':' ', '6':' ', '7':' ', '8':' ', '9':' '}
player1 = {'sign':'0'}
player2 = {'sign':'0'}
flag = 0
i = 0
p = 1
w = 0

print('Welcome')
while flag == 0:
    player1['sign'] = input('Player1 ! Please select your sign (0 or X):')
    
    if player1['sign'] == '0':
        player2['sign'] = 'X'
        flag = 1
    elif player1['sign'] == 'X':
        player2['sign'] = '0'
        flag = 1
    else:
        print('Invalid Input! Please enter 0 or X !')
print('{l}|{c}|{r}'.format(l=mydict['7'], c=mydict['8'], r=mydict['9']))
print('-----')
print('{l}|{c}|{r}'.format(l=mydict['4'], c=mydict['5'], r=mydict['6']))
print('-----')
print('{l}|{c}|{r}'.format(l=mydict['1'], c=mydict['2'], r=mydict['3']))

while i<9:
    n = 1
    if i%2==0:
        p = 1
        pos = input('Player1! Please select your position: ')
        if mydict[pos] == ' ':
            mydict[str(pos)]= player1['sign']
        else:
            print('This position has already been selected!')
            i-=1
    else:
        p = 2
        pos = input('Player2! Please select your position: ')
        if mydict[pos] == ' ':
            mydict[str(pos)]= player2['sign']
        else:
            print('This position has already been selected!')
            i-=1
    print('{l}|{c}|{r}'.format(l=mydict['7'], c=mydict['8'], r=mydict['9']))
    print('-----')
    print('{l}|{c}|{r}'.format(l=mydict['4'], c=mydict['5'], r=mydict['6']))
    print('-----')
    print('{l}|{c}|{r}'.format(l=mydict['1'], c=mydict['2'], r=mydict['3']))
    if i>=6:
        if mydict['1'] == mydict['2'] == mydict['3'] or mydict['4'] == mydict['5'] == mydict['6'] or mydict['7'] == mydict['8'] == mydict['9'] or mydict['1'] == mydict['4'] == mydict['7']:
            w = 1
            break
        elif mydict['2'] == mydict['5'] == mydict['8'] or mydict['3'] == mydict['6'] == mydict['9'] or mydict['3'] == mydict['5'] == mydict['7'] or mydict['1'] == mydict['5'] == mydict['9']:
            w = 1
            break
    i+=1
if w == 1:
    if p == 1:
        print('Player 1 wins!')
    else:
        print('Player 2 wins!')
else:
    print('Its a DRAW')


        
    
