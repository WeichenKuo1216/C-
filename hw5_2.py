board={}
import random
#setting the game board
def boardsetting(board):
	for i in range(1,41):#$size of the board=40
		board[i]="_"
	return board
boardsetting(board)

#setting the format of outputs
def print_b(board):
	for elements in board:
		print(board[elements],end='')
	return ''
#print_b(board)
#print_b(board)

#setting penalty steps
penalty=board.copy()
penalty_num=[]
def penaltysteps(board1,board2):
	for i in range(1,int((41-1)*0.3)):
		step=random.randint(1,41)
		penalty_num.append(step)
	for key in penalty:
		if key in penalty_num:
			penalty[key]="P"
	return (board1,board2)
penaltysteps(board,penalty)
#setting game of rolling dice
def roll_dice(dice):
	dice=random.randint(1,7)
	return dice
def conditions(numa,numb,board1,board2):
	if numa>=40:
		numa=40
	if numb>=40:
		numb=40
	if numa==numb:
		if board2[numa]==board2[numb]=="P":
			board1[numa]='x'

		elif board2[numa]==board2[numb]=="_":
			board1[numa]='X'
	else:
		if  board2[numa]=='_':
			board1[numa]='A'
		elif board2[numa]=='P':
			board1[numa]='a'
		if  board2[numb]=='_':
			board1[numb]='B'
		elif board2[numb]=='P':
			board1[numb]='b'
	return (numa,numb,board1,board2)
a=0
b=0
#setting how the game'll be played
def game(board1,board2,a,b):
	a_dice=[]
	b_dice=[]
	gameover=False
	a_stop=0
	b_stop=0
	#operate the game
	astart=0
	bstart=0
	#A plays the game
	while gameover==False:
		astep=roll_dice(a)
		astart+=astep
		a_dice.append(astart)
		#B plays the game		
		bstep=roll_dice(b)
		bstart+=bstep
		b_dice.append(bstart)		
		#conditions
		if astart>=40:
			astart=40
		if bstart>=40:
			bstart=40
		if astart==bstart:
			if board2[astart]==board2[bstart]=="P":
				board1[astart]='x'
				print(print_b(board1),"(A: ",astep,'B: ',bstep,")")
				print(print_b(board1),"(A: ",a_stop,'B: ',b_stop,")")	
			elif board2[astart]==board2[bstart]=="_":
				board1[astart]='X'	
				print(print_b(board1),"(A: ",astep,'B: ',bstep,")")
		else:
			if  board2[astart]=='_' and board2[bstart]=='_':
				board1[astart]='A'
				board1[bstart]='B'
				print(print_b(board1),"(A: ",astep,'B: ',bstep,")")	



			elif board2[astart]=='P'and board2[bstart]=='_':
				board1[astart]='a'
				board1[bstart]='B'
				print(print_b(board1),"(A: ",astep,'B: ',bstep,")")
				
					
				

					
			elif board2[bstart]=='P' and board2[astart]=='_' :
				board1[bstart]='b'
				board1[astart]='A'
				print(print_b(board1),"(A: ",astep,'B: ',bstep,")")
				
				
				
			elif board2[bstart]=='P' and board2[astart]=='P' :
				board1[bstart]='b'
				board1[astart]='a'
				print(print_b(board1),"(A: ",astep,'B: ',bstep,")")
				print(print_b(board1),"(A: ",a_stop,'B: ',b_stop,")")

		if board1[astart]=='a'and board1[bstart]=='B':	
			board1[bstart]='_'
			bstep=roll_dice(b)
			bstart+=bstep
			board1[bstart]='B'
			print(print_b(board1),"(A: ",a_stop,'B: ',bstep,")")
		if board[astart]=='A' and board1[bstart]=='b':
			board1[astart]='_'
			astep=roll_dice(a)
			astart+=astep
			board1[astart]='A'

			print(print_b(board1),"(A: ",astep,'B: ',b_stop,")")
		if board1[astart]=='a' and board1[bstart]=='b':	
			print(print_b(board1),"(A: ",a_stop,'B: ',b_stop,")")
		#print(print_b(board1),"(A: ",astep,'B: ',bstep,")")

		if board1[40]!="_":
			gameover=True
			break
		boardsetting(board1)
	

game(board,penalty,a,b)#call game function to play the game

#define who's the winner
final=board[40]
if final=='X' or final=='x':
	print("Both players win!")	
elif final=='A'or final=='a':
	print("Player A wins!")
elif final=='B'or final=='b':
	print("Player B wins!")
print(print_b(penalty))




