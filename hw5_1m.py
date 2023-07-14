#Problem 1: Minesweeper  
#setting the board 
import time#time function

row={}
for j in range(0,9):
	col=[]
	for i in range(0,9):
		col.append(" 0 ")
	row[j]=col
#print(row)
#print out the game board
print("   "+" a  "+" b  "+" c  "+" d  "+" e  "+" f  "+" g  "+" h  "+" i  ")
#assign the numbers to col	
a,b,c,d,e,f,g,h,i=0,1,2,3,4,5,6,7,8
for l in range(1,10):
	print("  "+"+---"*9+"+")
	print(l,"|"+'|'.join(row[l-1])+"|")
print("  "+"+---"*9+"+")

def matchFX(matrix1,matrix2):
	re=[]
	for i in range(0,9):
		for j in range(0,9):
			if matrix1[i][j]==" X ":
				re.append((i, j))
	re1=[]
	for i in range(0,9):
		for j in range(0,9):
			if matrix2[i][j]==" F ":
				re1.append((i, j))
	if re==re1:
		win=True
		



win=False
gameover=False
firstcell=False
#forming the game after the first option
while True:
	#ask user to select the first cell, leave space for the game 
	if  firstcell==False:
		print("Enter the column followed by the row (ex: a5). TO add or remove a flag, add 'f' to the cell (ex: a5f).type 'help' to show this message again")
		first=input("Enter the cell (10 mines left): ")
		if first[0] not in ['a','b','c','d','e','f','g','h','i']:
			print("Invalid cell :Enter the column followed by the row (ex: a5). TO add or remove a flag, add 'f' to the cell (ex: a5f)")
			continue
		if (int(first[1:])-1 )not in range(0,9):
			print("Invalid cell :Enter the column followed by the row (ex: a5). TO add or remove a flag, add 'f' to the cell (ex: a5f)")
			continue
	
	#time function
	start_time = time.time()
	if first[:1]=="a":
		col=0
	if first[:1]=="b":
		col=1
	if first[:1]=="c":
			col=2
	if first[:1]=="d":
		col=3
	if first[:1]=="e":
		col=4
	if first[:1]=="f":
		col=5
	if first[:1]=="g":
		col=6
	if first[:1]=="h":
		col=7
	if first[:1]=="i":
		col=8
	if first[1:]=="1":
		firstnum=col
	if first[1:]=="2":
		firstnum=col+9
	if first[1:]=="3":
		firstnum=col+18
	if first[1:]=="4":
		firstnum=col+27
	if first[1:]=="5":
		firstnum=col+37
	if first[1:]=="6":
		firstnum=col+45
	if first[1:]=="7":
		firstnum=col+54
	if first[1:]=="8":
		firstnum=col+63
	if first[1:]=="9":
		firstnum=col+72
	row[int(first[1:])-1][col]=" 0 "
	#setting 10 random mines
	import random
	mines=[]
	
	r=[]
	for i in range(0,80):
		r.append(i)
	r.remove(firstnum)
	if firstnum==0:
		r.remove(firstnum+1)
		r.remove(firstnum+9)
	if firstnum==8:
		r.remove(firstnum-1)
		r.remove(firstnum+9)
				
	if firstnum==72:
		r.remove(firstnum+1)
		r.remove(firstnum-9)
			
	if firstnum==80:
		r.remove(firstnum-1)
		r.remove(firstnum-9)
	if col!=0 and firstnum!= 0 and firstnum!=72 and firstnum!=80 and firstnum!=8:
		r.remove(firstnum+1)
		r.remove(firstnum-1)
		r.remove(firstnum+9)
		r.remove(firstnum-9)
	if col==0 and firstnum!= 0 and firstnum!=72:
		r.remove(firstnum+1)
		r.remove(firstnum+9)
		r.remove(firstnum-9)
	if col==8 and firstnum!= 8 and firstnum!=80:
		r.remove(firstnum-1)
		r.remove(firstnum+9)
		r.remove(firstnum-9)	
		# Use the new tuple in the rest of your code
	while len(mines)<10:
		# Define the original range tuple
		mine = random.choice(r)
		if mine not in mines:
			mines.append(mine)

		#print(mines)
	for mine in mines:
		if 0<=mine<=8:
			row[0][mine]=" "+"X"+" "
		if 9<=mine<=17:
			row[1][mine-10]=" "+"X"+" "
		if 18<=mine<=26:
			row[2][mine-19]=" "+"X"+" "
		if 27<=mine<=35:
			row[3][mine-28]=" "+"X"+" "
		if 36<=mine<=44:
			row[4][mine-37]=" "+"X"+" "
		if 45<=mine<=53:
			row[5][mine-46]=" "+"X"+" "
		if 54<=mine<=62:
			row[6][mine-55]=" "+"X"+" "
		if 63<=mine<=71:
			row[7][mine-64]=" "+"X"+" "
		if 72<=mine<=80:
			row[8][mine-73]=" "+"X"+" "
	#assign values near the mine
	#correct
	totalmines=0
	i=0
	while i<=8:
		for j in range(0,9):
			if row[i][j]!=' X ':
				totalmines=0
				if i==0 and j==0:#when i=0,j=0
					if row[i][j+1]==" X ":
						totalmines+=1
					if row[i+1][j+1]==" X ":
						totalmines+=1
					if row[i+1][j]==" X ":
						totalmines+=1
					row[i][j]=' '+str(totalmines)+' '
				totalmines=0
				if i==0 and j==8:			
					if row[i][j-1]==" X ":
						totalmines+=1
					if row[i+1][j-1]==" X ":
						totalmines+=1
					if row[i+1][j]==" X ":
						totalmines+=1
					row[i][j]=' '+str(totalmines)+' '
				totalmines=0
				if i==0 and j!=0 and j!=8: #when i=0
					if row[i][j+1]==" X ":
						totalmines+=1
					if row[i+1][j+1]==" X ":
						totalmines+=1
					if row[i+1][j]==" X ":
						totalmines+=1
					if row[i+1][j-1]==" X ":
						totalmines+=1
					if row[i][j-1]==" X ":
						totalmines+=1
					row[i][j]=' '+str(totalmines)+' '
				totalmines=0
				if i==8 and j==0:
					if row[i][j+1]==' X ':
						totalmines+=1
					if row[i-1][j+1]==' X ':
						totalmines+=1
					if row[i-1][j]==' X ':
						totalmines+=1
					row[i][j]=' '+str(totalmines)+' '
				totalmines=0
				if i==8 and j==8:
					if row[i][j-1]==' X ':
						totalmines+=1
					if row[i-1][j-1]==' X ':
						totalmines+=1
					if row[i-1][j]==' X ':
						totalmines+=1
					row[i][j]=' '+str(totalmines)+' '
				totalmines=0
				if i==8 and j!=0 and j!=8: #when i=0
					if row[i][j+1]==" X ":
						totalmines+=1
					if row[i-1][j+1]==" X ":
						totalmines+=1
					if row[i-1][j]==" X ":
						totalmines+=1
					if row[i-1][j-1]==" X ":
						totalmines+=1
					if row[i][j-1]==" X ":
						totalmines+=1
					row[i][j]=' '+str(totalmines)+' '
				totalmines=0
				if i!=0 and i!=8 and j==0:
					if row[i+1][j]==' X ':
						totalmines+=1
					if row[i+1][j+1]==' X ':
						totalmines+=1
					if row[i][j+1]==' X ':
						totalmines+=1
					if row[i-1][j+1]==' X ':
						totalmines+=1
					if row[i-1][j]==' X ':
						totalmines+=1
					row[i][j]=' '+str(totalmines)+' '
				totalmines=0
				if i!=0 and i!=8 and j==8:
					if row[i+1][j]==' X ':
						totalmines+=1
					if row[i+1][j-1]==' X ':
						totalmines+=1
					if row[i][j-1]==' X ':
						totalmines+=1
					if row[i-1][j-1]==' X ':
						totalmines+=1
					if row[i-1][j]==' X ':
						totalmines+=1
					row[i][j]=' '+str(totalmines)+' '
				totalmines=0
				if i!=0 and i!=8 and j!=0 and j!=8:
					if row[i+1][j]==' X ':
						totalmines+=1
					if row[i+1][j+1]==' X ':
						totalmines+=1
					if row[i][j+1]==' X ':
						totalmines+=1
					if row[i-1][j+1]==' X ':
						totalmines+=1
					if row[i-1][j]==' X ':
						totalmines+=1
					if row[i-1][j-1]==' X ':
						totalmines+=1
					if row[i][j-1]==' X ':
						totalmines+=1
					if row[i+1][j-1]==' X ':
						totalmines+=1
					row[i][j]=' '+str(totalmines)+' '
				totalmines=0
		i+=1

	#print("   "+" a  "+" b  "+" c  "+" d  "+" e  "+" f  "+" g  "+" h  "+" i  ")
	#assign the numbers to col	
	#a,b,c,d,e,f,g,h,i=0,1,2,3,4,5,6,7,8
	#for l in range(1,10):
	#	print("  "+"+---"*9+"+")
	#	print(l,"|"+'|'.join(row[l-1])+"|")
	#print("  "+"+---"*9+"+")




	#setting the game board
	row1={}
	for j in range(0,9):
		col1=[]
		for i in range(0,9):
			col1.append("   ")
		row1[j]=col1
	#print out the game board after the user's first option
	def num_arround_zero(matrix1, matrix2, x, y, target):
		if matrix1[x][y]== ' 1 ' or ' 2 ' or ' 3 ' or ' 4 ' or ' 5 ' or ' 6 ' or ' 7 ' or ' 8 ' :
			matrix2[x][y] = matrix1[x][y]
		if matrix1[x][y] == target:
			matrix2[x][y] = matrix1[x][y]
	# Call the num_arround_zero function and print the resulting matrix
	target = ' 0 '
	num_arround_zero(row, row1, int(first[1:])-1, col, target)

	def dfs(matrix, visited, row, col, result):
	    # Check if the current position is out of bounds, already visited, or not 0
	    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or visited[row][col] or matrix[row][col] != ' 0 ':
	        return
	    
	    # Mark the current position as visited and add it to the result list
	    visited[row][col] = True
	    result.append((row, col))
	    
	    # Recursively call dfs on the neighboring positions
	    dfs(matrix, visited, row - 1, col, result)
	    dfs(matrix, visited, row + 1, col, result)
	    dfs(matrix, visited, row, col - 1, result)
	    dfs(matrix, visited, row, col + 1, result)

	#call the dfs function
	visited = [[False] * len(row[0]) for _ in range(len(row))]
	result = []
	dfs(row, visited, int(first[1:])-1, col,result)
	#print(result)
	#paste the loction of 0 and other nembers near user's input

	def paste(matrix1,matrix2,a,b):
		matrix1[a][b]=matrix2[a][b]
		if b+1<=8:
			matrix1[a][b+1]=matrix2[a][b+1]
		if b-1>=0:
			matrix1[a][b-1]=matrix2[a][b-1]
		if a+1<=8:
			matrix1[a+1][b]=matrix2[a+1][b]
		if a-1>=0:
			matrix1[a-1][b]=matrix2[a-1][b]
	for i in range(0,len(result)):
			paste(row1,row,result[i][0],result[i][1])

	#print out the game booard after the user's first option picked
	if firstcell==False:
		print("   "+" a  "+" b  "+" c  "+" d  "+" e  "+" f  "+" g  "+" h  "+" i  ")
		#assign the numbers to col	
		a,b,c,d,e,f,g,h,i=0,1,2,3,4,5,6,7,8
		for l in range(1,10):
			print("  "+"+---"*9+"+")
			print(l,"|"+'|'.join(row1[l-1])+"|")
		print("  "+"+---"*9+"+")
	firstcell=True

	result=[]
	x=input("Enter the cell (10 mines left): ")#ask user input
	if x=="help":
		print("Enter the column followed by the row (ex: a5). TO add or remove a flag, add 'f' to the cell (ex: a5f).type 'help' to show this message again")
		continue
	if x[0] not in ['a','b','c','d','e','f','g','h','i']:
		print("Invalid cell :Enter the column followed by the row (ex: a5). TO add or remove a flag, add 'f' to the cell (ex: a5f)")
		continue
	#transforming the user input into index
	if x[0]=='a':
		k=0
	if x[0]=='b':
		k=1
	if x[0]=='c':
		k=2
	if x[0]=='d':
		k=3
	if x[0]=='e':
		k=4
	if x[0]=='f':
		k=5
	if x[0]=='g':
		k=6
	if x[0]=='h':
		k=7
	if x[0]=='i':
		k=8
	else:
		if len(x)>2:
			if int(x[1:2])-1 not in range(0,8):
				print("Invalid cell :Enter the column followed by the row (ex: a5). TO add or remove a flag, add 'f' to the cell (ex: a5f)")
				continue
			if row1[int(x[1])-1][k] !="   ":
				print("Invalid cell: that cell is already shown")
				continue	
			if row1[int(x[1])-1][k] =="   ":
				if x[2]=='f':
					row1[int(x[1])-1][k]=" F "
			if row1[int(x[1])-1][k] ==" F ":
				if x[2]=='f':
					row1[int(x[1])-1][k]="   "
			if row1[int(x[1])-1][k] !="   " and " F ":
				print("Invalid cell: There's a cell there")
				continue

			matchFX(row,row1)
			if win==True:
				end_time = time.time()
				elapsed_time = end_time - start_time
				print("You win. It took you"+str(f"Elapsed time: {elapsed_time:.2f} seconds")+".")
				print("   "+" a  "+" b  "+" c  "+" d  "+" e  "+" f  "+" g  "+" h  "+" i  ")
				#assign the numbers to col	
				a,b,c,d,e,f,g,h,i=0,1,2,3,4,5,6,7,8
				for l in range(1,10):
					print("  "+"+---"*9+"+")
					print(l,"|"+'|'.join(row[l-1])+"|")
				print("  "+"+---"*9+"+")
				again=input("Play again(y/n)?: ")
				if again=="y":
					firstcell=False
					continue
				if again=='n':
					break
		if len(x)<=2:
			if int(x[1:])-1 not in range(0,8):
				print("Invalid cell :Enter the column followed by the row (ex: a5). TO add or remove a flag, add 'f' to the cell (ex: a5f)")
				continue
			if row1[int(x[1:])-1][k] !="   ":
				print("Invalid cell: that cell is already shown")
				continue  
			if row1[int(x[1:])-1][k] ==" F ":
				print("Invalid cell: There's a flag there")
				continue
			if row1[int(x[1:])-1][k] =="   ":
				if row[(int(x[1:])-1)][k]==' X ':
					print("Game over")
					print("   "+" a  "+" b  "+" c  "+" d  "+" e  "+" f  "+" g  "+" h  "+" i  ")
					#assign the numbers to col	
					a,b,c,d,e,f,g,h,i=0,1,2,3,4,5,6,7,8
					for l in range(1,10):
						print("  "+"+---"*9+"+")
						print(l,"|"+'|'.join(row[l-1])+"|")
					print("  "+"+---"*9+"+")
					break
			if row[int(x[1:])-1][k]!=' X 'and ' 0 ':
				row1[int(x[1:])-1][k] =row[int(x[1:])-1][k]
				print("   "+" a  "+" b  "+" c  "+" d  "+" e  "+" f  "+" g  "+" h  "+" i  ")
				#assign the numbers to col	
				a,b,c,d,e,f,g,h,i=0,1,2,3,4,5,6,7,8
				for l in range(1,10):
					print("  "+"+---"*9+"+")
					print(l,"|"+'|'.join(row1[l-1])+"|")
				print("  "+"+---"*9+"+")
				
			if row[int(x[1:])-1][k]==' 0 ':
				dfs(row, visited,int(x[1:])-1, k,result)
				for i in range(0,len(result)):
					paste(row1,row,result[i][0],result[i][1])
				print("   "+" a  "+" b  "+" c  "+" d  "+" e  "+" f  "+" g  "+" h  "+" i  ")
				#assign the numbers to col	
				a,b,c,d,e,f,g,h,i=0,1,2,3,4,5,6,7,8
				for l in range(1,10):
					print("  "+"+---"*9+"+")
					print(l,"|"+'|'.join(row1[l-1])+"|")
				print("  "+"+---"*9+"+")
			continue

				
		
						
			