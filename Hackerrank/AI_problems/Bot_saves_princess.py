#!/usr/bin/python

# other solutions on https://codereview.stackexchange.com/questions/131592/hackerrank-bot-saves-princess-beginner-code

def displayPathtoPrincess(n,grid):
#print all the moves here
    mid_square = (n-1)/2
    mid_square = int(mid_square)
    if grid[0][0]=="p":
        first_move = "UP"
        second_move = "LEFT"
        
    if grid[0][n-1] == "p":      
        first_move="UP"
        second_move="RIGHT"
                 
    if grid[n-1][0] == "p":
        first_move="DOWN"
        second_move="LEFT"
    
    if grid[n-1][n-1] == "p":
        first_move="DOWN"
        second_move="RIGHT"
        
    for _ in range(mid_square):
        print(first_move)
        print(second_move)
      

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())  

displayPathtoPrincess(m,grid)