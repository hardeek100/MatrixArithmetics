import random
import os

def ate(X, Y):
    return random.randrange(1, X-1), random.randrange(1, Y-1)

def ground(head, headX, headY, fruitX, fruitY, X, Y):
    for i in range(X):
        for j in range(Y):
            if((i == 0 or j == 0) or (i == X-1 or j == Y-1)):
                print("#", end = '')
            elif(i == fruitX and j == fruitY):
                print('O', end = '')
                    
            elif(i == headX and j == headY):
                print(head, end = '')
            
            else:
                print(' ', end = '')
            
        print()
    os.system("cls")

def move(fY, Y):
    fY += 1
    if (fY == Y):
        fY = 1
    return fY

def stage():
    
    X = 10
    Y = 20
    jX = random.randrange(1, X)
    jY = random.randrange(1,Y)
    fX , fY = ate(X, Y)
    head = '>'
    headX = 1
    headY = 1
    b = 0
    score = 0
    count = 0
    while score != 5:
        ground(head, headX, headY, fX, fY, X, Y)
        if(b == 0):
            headY = move(headY, Y)
            head = '>'
        elif(b == 1):
            headX = move(headX, X)
            head = 'V'
        if(headX == fX and headY == fY):
            fX , fY = ate(X, Y)
            score += 1
        if(headX == jX or headY == jY):
            jX, jY = random.randrange(1,X-1), random.randrange(1,Y-1)
            b = not b 
        
        count += 1
        print("Score: ", score, "FruitX: ", fX, "fruitY: ", fY)
        print("headX: ", headX, "headY: ", headY, "jX: ", jX, "jY: ", jY)
    print("Total steps: ", count)

stage()
