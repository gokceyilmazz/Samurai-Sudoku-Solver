

WHITE=(255,255,255)
Black =(0,0,0)
Grey = (105,105,105)
LightBlue=(96,216,232)

p=1
while p:

    try:
            f = open(r"C:\Users\Gökçe Yılmaz\Desktop\SamuraiSudoku-master\sudoku.txt", 'r')
            p = 0
    except FileNotFoundError:
            print("File not found")
board = f.read().split("\n")

#Positions and sizes

gridPos=(20,40,380,400,200,310,220,290)
cellSize= 30
gridSize=cellSize*21