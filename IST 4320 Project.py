import random
import tkinter
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy
# Creates an empty board
sign = 0
global board
board = [[" " for x in range(4)] for y in range(4)]
#rules
def winner(OP, ox):
	return ((OP[0][0] == ox and OP[0][1] == ox and OP[0][2] == ox) or
			(OP[1][0] == ox and OP[1][1] == ox and OP[1][2] == ox) or
			(OP[2][0] == ox and OP[2][1] == ox and OP[2][2] == ox) or
			(OP[0][0] == ox and OP[1][0] == ox and OP[2][0] == ox) or
			(OP[0][1] == ox and OP[1][1] == ox and OP[2][1] == ox) or
			(OP[0][2] == ox and OP[1][2] == ox and OP[2][2] == ox) or
			(OP[0][0] == ox and OP[1][1] == ox and OP[2][2] == ox) or
			(OP[0][2] == ox and OP[1][1] == ox and OP[2][0] == ox))
# Configure text 
def get_text(i, j, gb, l1, l2):
	global sign
	if board[i][j] == ' ':
		if sign % 2 == 0:
			l1.config(state=DISABLED)
			l2.config(state=ACTIVE)
			board[i][j] = "X"
		else:
			l2.config(state=DISABLED)
			l1.config(state=ACTIVE)
			board[i][j] = "O"
		sign += 1
		option[i][j].config(text=board[i][j])
	if winner(board, "X"):
		gb.destroy()
		box = messagebox.showinfo("Winner", "WINNER: Player 1")
	elif winner(board, "O"):
		gb.destroy()
		box = messagebox.showinfo("Winner", "WINNER: Player 2")
	elif(isfull()):
		gb.destroy()
		box = messagebox.showinfo("Tie Game", "Tie Game")
# Check if the player can push the button or not
def isfree(i, j):
	return board[i][j] == " "
# Check the board is full or not
def isfull():
	flag = True
	for i in board:
		if(i.count(' ') > 0):
			flag = False
	return flag
# Create the GUI
def gameboard_pl(gameboard, l1, l2):
	global option
	option = []
	for i in range(3):
		m = 3+i
		option.append(i)
		option[i] = []
		for j in range(3):
			n = j
			option[i].append(j)
			get_t = partial(get_text, i, j, gameboard, l1, l2)
			option[i][j] = Button(
				gameboard, bd=5, command=get_t, height=4, width=8)
			option[i][j].grid(row=m, column=n)
	gameboard.mainloop()
# computer move
def pc():
	possibility = []
	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] == ' ':
				possibility.append([i, j])
	move = []
	if possibility == []:
		return
	else:
		for let in ['O', 'X']:
			for i in possibility:
				copy = deepcopy(board)
				copy[i[0]][i[1]] = let
				if winner(copy, let):
					return i
		sides = []
		for i in possibility:
			if i in [[0, 0], [0, 2], [2, 0], [2, 2]]:
				sides.append(i)
		if len(sides) > 0:
			move = random.randint(0, len(sides)-1)
			return sides[move]
		border = []
		for i in possibility:
			if i in [[0, 1], [1, 0], [1, 2], [2, 1]]:
				border.append(i)
		if len(border) > 0:
			move = random.randint(0, len(border)-1)
			return border[move]
# Configure text 
def get_text_pc(i, j, gb, l1, l2):
	global sign
	if board[i][j] == ' ':
		if sign % 2 == 0:
			l1.config(state=DISABLED)
			l2.config(state=ACTIVE)
			board[i][j] = "X"
		else:
			option[i][j].config(state=ACTIVE)
			l2.config(state=DISABLED)
			l1.config(state=ACTIVE)
			board[i][j] = "O"
		sign += 1
		option[i][j].config(text=board[i][j])
	x = True
	if winner(board, "X"):
		gb.destroy()
		x = False
		box = messagebox.showinfo("Winner", "Player won")
	elif winner(board, "O"):
		gb.destroy()
		x = False
		box = messagebox.showinfo("Winner", "Computer won")
	elif(isfull()):
		gb.destroy()
		x = False
		box = messagebox.showinfo("Tie Game", "Tie Game")
	if(x):
		if sign % 2 != 0:
			move = pc()
			option[move[0]][move[1]].config(state=DISABLED)
			get_text_pc(move[0], move[1], gb, l1, l2)
# Create the GUI 
def gameboard_pc(game_board, l1, l2):
	global option
	option = []
	for i in range(3):
		m = 3+i
		option.append(i)
		option[i] = []
		for j in range(3):
			n = j
			option[i].append(j)
			get_t = partial(get_text_pc, i, j, game_board, l1, l2)
			option[i][j] = Button(
				game_board, bd=5, command=get_t, height=4, width=8)
			option[i][j].grid(row=m, column=n)
	game_board.mainloop()
# Gameboard vs computer
def withpc(board):
	board.destroy()
	board = Tk()
	board.title("Tic Tac Toe")
	l1 = Button(board, text="Player : X", width=10)
	l1.grid(row=1, column=1)
	l2 = Button(board, text="Computer : O",
				width=10, state=DISABLED)

	l2.grid(row=2, column=1)
	gameboard_pc(board, l1, l2)
# vs mode board game
def withplayer(game_board):
	game_board.destroy()
	game_board = Tk()
	game_board.title("Tic Tac Toe")
	l1 = Button(game_board, text="Player 1 : X", width=10)
	l1.grid(row=1, column=1)
	l2 = Button(game_board, text="Player 2 : O",
				width=10, state=DISABLED)
	l2.grid(row=2, column=1)
	gameboard_pl(game_board, l1, l2)
# main function
def play():
	start = Tk()
	start.geometry("250x250")
	start.title("Tic-Tac-Toe")
	wpc = partial(withpc, start)
	wpl = partial(withplayer, start)
	option1 = Button(start, text="Single Player", command=wpc,
				foreground='blue',
				background="light blue", bg="blue",
				fg="light blue", width=700, font='times', bd=15)

	option2 = Button(start, text="Multi Player", command=wpl, foreground='blue',
				background="light blue", bg="blue", fg="light blue",
				width=700, font='times', bd=15)

	option3 = Button(start, text="Exit", command=start.quit, foreground='blue',
				background="light blue", bg="blue", fg="light blue",
				width=700, font='times', bd=15)
	option1.pack(side='top')
	option2.pack(side='top')
	option3.pack(side='top')
	start.mainloop()
# main function
if __name__ == '__main__':
	play()
