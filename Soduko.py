board=[]
print("Enter board (if value is empty enter 0)")
t=len
for i in range(9):
    board.append(list(map(int,input().split())))
print('---------------------------------------------------')

def print_board(bo):
    t=len
    for i in range(t(bo)):
        if i%3==0 and i!=0:
            print("------|-------|-------")
        for j in range(t(bo[0])):
            if j%3==0 and j!=0:
                print("| ",end="")
            if j==8:
                print(bo[i][j])
            else:
                print(str(bo[i][j])+" ",end="")  

def find_empty(bo):
    t=len
    for i in range(t(bo)):
        for j in range(t(bo)):
            if bo[i][j]==0:
                return i,j
    return None            

def isvalid(bo,num,pos):
    x,y=pos
    ans=True
    t=len
    for i in range(t(bo)):
        if bo[i][y]==num and i!=x:
            return False
    for j in range(t(bo)):
        if bo[x][j]==num and j!=y:
            return False
    #Checking  3 X 3  cube that if there are no duplicates

    box_row=x//3
    box_col=y//3
    for i in range(3*box_row,3*(box_row+1)):
        for j in range(3*box_col,3*(box_col+1)):
            if bo[i][j]==num and (i,j) !=pos:
                return False
    return True            

def solve_soduko(bo):

    f=find_empty(bo)
    if not f:
        return True
    else:
        row,col=f
    for i in range(1,len(bo)+1):
        
        if isvalid(bo,i,(row,col)):
            bo[row][col]=i
            
            if solve_soduko(bo):
                return True
            else:
                bo[row][col]=0 
    return False

print('Given board')
print_board(board)
print("After Solving....",'\n')
solve_soduko(board)
print_board(board) 
