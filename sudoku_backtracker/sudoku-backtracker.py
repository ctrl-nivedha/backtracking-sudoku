# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 19:48:46 2020

@author: Mro

"""

row= False
col= False

board = [
    [0,3,0,0,0,5,0,8,0],
    [0,5,0,0,0,9,0,0,0],
    [0,0,0,0,2,0,0,3,0],
    [3,0,0,0,0,0,0,9,0],
    [0,0,5,0,0,0,6,0,0],
    [0,9,0,0,0,0,0,0,8],
    [0,1,0,0,3,0,0,0,0],
    [7,0,0,2,0,0,0,0,0],
    [0,4,0,0,0,0,0,2,0]
]



#print board
def printboard(bo):
    for i in range(len(bo)):
        if(i==3 or i==6):
                print("---------------------")
        for j in range(len(bo[i])):
            if(j==3 or j==6):
                print("|", end=' ')

            print(bo[i][j], end=' ')
        
        print(end='\n')



#check emmpty
def checkempty(bo):
    global row, col
    for i in range(len(bo)):
        for j in range(len(bo[i])):
            if bo[i][j]==0:
                row=i
                col=j
                return True
            
    return False
                
            


        
#backtracking func
def solve(bo):
    global row, col
    if checkempty(bo):
        x=row
        y=col
    else: 
        return True
   
    for i in range(1,10):
        #check row
       if (checkrow(bo,x,y,i) and checkcol(bo,x,y,i) and checkbox(bo,x,y,i)):
           
           bo[x][y]=i
          
           
           if solve(bo):
               return True
           else:
               bo[x][y]=0;
    return False 
    
  
      
            
            
            
        #check column
        #checkcol()
        #check box
        #checkbox()
        
 


def checkrow(bo,x,y,n):
    
    for j in range(len(bo[x])):
        if bo[x][j]==n and j!=y:
            return False
    
    
    return True
    
def checkcol(bo,x,y,n):
    
    for i in range(len(bo)):
        if bo[i][y]==n and i!=x:
            return False
    
    
    return True

def checkbox(bo,x,y,n):
    a = x // 3
    b = y // 3

    for i in range(a*3, a*3 + 3):
        for j in range(b * 3, b*3 + 3):
            if bo[i][j] == n and (i,j) != (a,b):
                return False

    return True
    
    
      

        
#main
def main():
    printboard(board)
    solve(board)
    print("----------------------------------")
    print('\n')
    print("----------------------------------")
    
    printboard(board)     
main()