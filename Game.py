from math import *
import random

grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

print("Hello..! Welcome to 2048 :)")

def print_grid():
    print(" ")
    for i in range(4) :
        print("    " + str(grid[i][0]) + "  " + str(grid[i][1]) + "  " + str(grid[i][2]) + "  " + str(grid[i][3]))
    print(" ")


def get_random():
    i = random.randint(0,3)
    j = random.randint(0,3)
    if grid[i][j]==0 :
        if random.randint(1,100)<=80 :
            grid[i][j] = 2
        else :
            grid[i][j] = 4
    else :
        get_random()


def add(key):
    if key == 4:
        for i in range(4):
            for j in range(3):
                if grid[i][j]==grid[i][j+1] :
                    grid[i][j]+=grid[i][j+1];
                    grid[i][j+1] = 0
    elif key == 8:
        for j in range(4):
            for i in range(3):
                if grid[i][j]==grid[i+1][j] :
                    grid[i][j]+=grid[i+1][j];
                    grid[i+1][j] = 0
    elif key == 6 :
        for i in range(4):
            for j in range(3,-1,-1):
                if grid[i][j]==grid[i][j-1] :
                    grid[i][j]+=grid[i][j-1];
                    grid[i][j-1] = 0
    elif key == 2 :
        for j in range(4):
            for i in range(3,-1,-1):
                if grid[i][j]==grid[i-1][j] :
                    grid[i][j]+=grid[i-1][j];
                    grid[i-1][j] = 0
    else :
        print("OOPS...! Check your Input...")
        play()


def shift(key):
    #Check
    if key == 4:
        for i in range(4):
            for j in range(3):
                if grid[i][j]==0:
                    for k in range(j+1,4):
                        if grid[i][k]!=0 :
                            grid[i][j] = grid[i][k]
                            grid[i][k] = 0
                            break
    elif key == 8:
        for j in range(4):
            for i in range(3):
                if grid[i][j]==0:
                    for k in range(i+1,4):
                        if grid[k][j]!=0 :
                            grid[i][j] = grid[k][j]
                            grid[k][j] = 0
                            break
    elif key == 6 :
        for i in range(4):
            for j in range(3,-1,-1):
                if grid[i][j]==0:
                    for k in range(j-1,-1,-1):
                        if grid[i][k]!=0 :
                            grid[i][j] = grid[i][k]
                            grid[i][k] = 0
                            break
    elif key == 2 :
        for j in range(4):
            for i in range(3,-1,-1):
                if grid[i][j]==0:
                    for k in range(i-1,-1,-1):
                        if grid[k][j]!=0 :
                            grid[i][j] = grid[k][j]
                            grid[k][j] = 0
                            break


def move(key):
    shift(key)
    add(key)
    shift(key)
    get_random()
    play()


def check(x):
    for i in range(4):
        for j in range(3):
            if grid[i][j]==grid[i][j+1] or grid[i][j]==0 or grid[i][j+1]==0:
                move(x)
    for j in range(4):
        for i in range(3):
            if grid[i][j]==grid[i+1][j] or grid[i][j]==0 or grid[i+1][j]==0:
                move(x)
    for i in range(4):
        for j in range(3,-1,-1):
            if grid[i][j]==grid[i][j-1] or grid[i][j]==0 or grid[i][j-1]==0:
                move(x)
    for j in range(4):
        for i in range(3,-1,-1):
            if grid[i][j]==grid[i-1][j] or grid[i][j]==0 or grid[i-1][j]==0:
                move(x)
    
    print("     G A M E  O V E R !")


def play():
    print_grid()
    x = int(input(">>>> "))
    check(x)


get_random()
get_random()
play()
