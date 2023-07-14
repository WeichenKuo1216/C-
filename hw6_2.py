#Problem 2: Interactive Candy Crush Game
#set the look of the output
import random
def output_form(gameboard):
	for item in range(len(gameboard)):
		print('     '+str(item),end='')
	print('\n','------'*len(linelist)+'--')
	print(end='')
	for item in range(len(gameboard)):

		print(str(item)+'|',end='')
		for i in gameboard[item]:
			if len(str(i))==4:
				print(' '+str(i)+'|',end='')
			elif len(str(i))==3:
				print(' '+str(i)+' |',end='')
			elif len(str(i))==2:
				print('  '+str(i)+' |',end='')
			elif len(str(i))==1:
				print('  '+str(i)+'  |',end='')
		print('\n'+'_|'+'_____|'*len(gameboard[item])+'\n',end='')
#set how'll the game be played
points=0
def candyCrush(board,point):
	m, n = len(board), len(board[0])
	changed = False
	# Crush candies vertically
	for j in range(n):
		for i in range(2, m):
			if abs(board[i][j]) == abs(board[i - 1][j]) == abs(board[i - 2][j]) != 0:
				board[i][j] = board[i - 1][j] = board[i - 2][j] = -abs(board[i][j])
				point+=10
				changed = True

	    # Crush candies horizontally
	for i in range(m):
		for j in range(2, n):
			if abs(board[i][j]) == abs(board[i][j - 1]) == abs(board[i][j - 2]) != 0:
				board[i][j] = board[i][j - 1] = board[i][j - 2] = -abs(board[i][j])
				point+=10
				changed = True

	    # Drop candies
	for j in range(n):
		idx = m - 1
		for i in range(m - 1, -1, -1):
			if board[i][j] > 0:
				board[idx][j] = board[i][j]
				idx -= 1
		while idx >= 0:
			board[idx][j] = random.choice([1,2,3,4,5,6])
			idx -= 1
	if not changed:
		return output_form(board), point
	else:
		return candyCrush(board, point),point
#ask user to input wigth and height of the board
while True:
	print("!!!WELCOME TO THE CANDYCRUSH GAME!!!")#basic introduction of the game
	print('Reach target point to win!')
	print('You have 20 chance!')
	x=int(input('Input the width of the board: '))#ask user to input the numbers of which gameboard's form depends on
	y=int(input('Input the height of the board: '))
	target=x*y*100#set target points
	chance=20
	print('target points:',target)
	#set game board
	linelist=[]
	for i in range(y):
		item=[]
		for j in range(x):
			item.append(random.choice([1,2,3,4,5,6]))
		linelist.append(item)
	#play the game
	#show the original gameboard
	output_form(linelist)
	print('------'*len(linelist)+'--')
	#play the game
	total=0

	while total<target:
		x=int(input('Input the number row of the candy you want to switch: '))#ask user to input the number row of the candy he/she want to switch:
		y=int(input('Input the number column of the candy you want to switch: '))#ask user to input the number column of the candy he/she want to switch:   
		z=input('Input which deriction you want to switch(left right up down): ')#ask user to deside which derection he/she wants to switch
		k=[]
		if z=='left':#switch left
			k.append(linelist[x][y])
			k.append(linelist[x][y-1])
			linelist[x][y]=k[1]
			linelist[x][y-1]=k[0]
		if z=='right':#switch right
			k.append(linelist[x][y])
			k.append(linelist[x][y+1])
			linelist[x][y]=k[1]
			linelist[x][y+1]=k[0]

		if z=='down':#switch down
			k.append(linelist[x][y])
			k.append(linelist[x+1][y])
			linelist[x][y]=k[1]
			linelist[x+1][y]=k[0]
		if z=='up':#switch up
			k.append(linelist[x][y])
			k.append(linelist[x-1][y])
			linelist[x][y]=k[1]
			linelist[x-1][y]=k[0]
		chance-=1
		k=[]
		#define the result of the game
		if total>=target:
			print('You win! Your score is: ',total)
			break
		if chance==0:
			print('You lose!')
			break
		result = candyCrush(linelist,points)#call function candyCrush()
		total+=result[1]
		print("Total points: ",total)
		print("Chances left: ",chance)
	#ask user if he/she wants to play again
	again=input("Do you want to play again?(y/n)")
	if again=='y':
		print("Okay,let's start a new game!!!")
		continue
	if again=='n':
		print('Okay,thank you for playing this game!!!')
		break




