# IMPORTING MODULES

import random
import numpy
import tkinter as tk
from tkinter import messagebox


# To move left
def a(mat):
    return(main(mat))

# To move right
def d(mat):
    mat=reverse(mat)
    mat=main(mat)
    mat=reverse(mat)
    return(mat)

# To move dowN
def s(mat):
    mat=transpose(mat)
    mat=reverse(mat)
    mat=main(mat)
    mat=reverse(mat)
    mat=transpose(mat)
    return(mat)

# To move up
def w(mat):
    mat=transpose(mat)
    mat=main(mat)
    mat=transpose(mat)
    return(mat)


# For reversing numbers in rows of matrix
def reverse(mat):
    for row in range(0,4):
        mat[row]=mat[row][::-1]
    return(mat)

# Function for Deleting zero in list 
# Calling done in main function
def delete_zero(mat1):
    count=mat1.count(0)
    for i in range(0,count):
        mat1.remove(0)
    return(add(mat1))

# Main operation in the game
def add(mat2):
    lst=[0,0,0,0]
    if( len(mat2)==0):
        return([0,0,0,0])
    elif(len(mat2)==1):
        return([mat2[0],0,0,0])
    pos=0
    for i in range (0,len(mat2)):
        if(len(mat2)==1):
            lst[pos]=mat2[0]
            break
        elif(len(mat2)==0):
            break
        elif(mat2[0]==mat2[1]):
            x=mat2[0]
            lst[pos]=mat2[0]*2
            pos+=1
            mat2.remove(x)
            mat2.remove(x)
        else:
            x=mat2[0]
            lst[pos]=mat2[0]
            mat2.remove(x)
            pos+=1
    return(lst)


# To find transpose of matrix
def transpose(mat):
    mat=numpy.transpose(mat)
    mat=mat.tolist()
    return mat


# Function for deleting zero in matrix
def main(mat):
    for row in range(0,4):
        mat[row]=delete_zero(mat[row])
    return(mat)


# To Check if game is over or not 

def checkover(mat):
    for i in range(4):
        for j in range(4):
            if(mat[i][j]== 0):
                return False
    for i in range(3):
        for j in range(3):
            if(mat[i][j]== mat[i + 1][j] or mat[i][j]== mat[i][j + 1]):
                return False
    for j in range(3):
        if(mat[3][j]== mat[3][j + 1]):
            return False
    for i in range(3):
        if(mat[i][3]== mat[i + 1][3]):
            return False
    return True


# MAIN BODY OF THE CODE AND GUI

def initialize_matrix():
    return [[0, 0, 0, 0] for _ in range(4)]


def add_random_tile(mat):
    zeros = [(i, j) for i in range(4) for j in range(4) if mat[i][j] == 0]
    if zeros:
        i, j = random.choice(zeros)
        mat[i][j] = 2
    elif checkover(mat):
        game_over()


def game_over():
    messagebox.showinfo("Game Over", "Game Over!")
    root.destroy()


def update_gui():
    for i in range(4):
        for j in range(4):
            cell_value = matrix[i][j]
            cell_label = cells[i][j]
            if cell_value !=0:
                cell_label.config(text=str(cell_value), bg=tile_colors.get(cell_value, default_color))
            else:
                cell_label.config(text=str(''), bg=tile_colors.get('', default_color))


def on_key(event):
    if event.keysym == 'Up':
        move('w')
    elif event.keysym == 'Down':
        move('s')
    elif event.keysym == 'Left':
        move('a')
    elif event.keysym == 'Right':
        move('d')


def move(direction):
    try:
        global matrix
        if direction == 'w':
            matrix = w(matrix)
        elif direction == 's':
            matrix = s(matrix)
        elif direction == 'a':
            matrix = a(matrix)
        elif direction == 'd':
            matrix = d(matrix)
        add_random_tile(matrix)
        update_gui()
    except:
        print("game over")


root = tk.Tk()

root.title("2048 Game")

matrix = initialize_matrix()

add_random_tile(matrix)

default_color = "#cdc1b4"

tile_colors = {
    2: "#eee4da",
    4: "#ede0c8",
    8: "#f2b179",
    16: "#f59563",
    32: "#f67c5f",
    64: "#f65e3b",
    128: "#edcf72",
    256: "#edcc61",
    512: "#edc850",
    1024: "#edc53f",
    2048: "#edc22e"
}

cells = [[tk.Label(root, text=str(matrix[i][j]), font=('Helvetica', 24), width=4, height=2, relief="solid")
        for j in range(4)] for i in range(4)]

for i in range(4):
    for j in range(4):
        cells[i][j].grid(row=i, column=j, padx=5, pady=5)

update_gui()

root.bind('<Key>', on_key)

root.mainloop()