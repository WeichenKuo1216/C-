#Problem 2: The Blackjack Game 
import random
ranks=["A",'2','3','4','5','6','7','8','9','10','J','Q','K']
suits=['Spade','Heart','diamond','Club']
value=None
#creat shuffle deck
def creatshuff():
	deck={}
	for suit in suits:
		for rank in ranks:
			deck[suit+rank]=rank
	return deck

def value_assignment(deck):
	for key in deck:
		if deck[key]=='A':
			deck[key]=11
		if deck[key]=='2':
			deck[key]=2
		if deck[key]=='3':
			deck[key]=3
		if deck[key]=='4':
			deck[key]=4
		if deck[key]=='5':
			deck[key]=5
		if deck[key]=='6':
			deck[key]=6
		if deck[key]=='7':
			deck[key]=7
		if deck[key]=='8':
			deck[key]=8
		if deck[key]=='9':
			deck[key]=9
		if deck[key]=='J'or deck[key]=='Q' or deck[key]=='K' or deck[key]=='10':
			deck[key]=10
	return deck
#draw cards
def draw_card(deck,num):
	cards={}
	d_list=[]
	for key in deck:
		d_list.append(key)
	for i in range(num):
		card= random.choice(d_list)
		cards[card]=deck[card]

	del deck[card]
	return cards

def value_determinate(total,cards,name):
	if total>21:#bust
		print(name," current value is a bust (>21) ")
		print("With the hand: ",cards)
	#if the user's value under 21, ask the user	uf he/she wants to hit another card
	if total<21:
		print(name," current value is: ",total)
		print("With the hand: ",cards)
	if total==21:
		print(name," current value is BLACK JACK! (21)")
		print("With the hand: ",cards)
while True:
	while True:
		name='your'
		uservalue=0
		deck=creatshuff()
		deck=value_assignment(deck)
		#user draw
		user=draw_card(deck,2)
		cards=user.copy()
		for key in user:
			uservalue+=user[key]
		value_determinate(uservalue,user,name)
		if uservalue==21:
			break
		if uservalue!=21:
			while True:
				x=input("Hit or Stay? (Hit=1, Stay=0 )")
				if x=='1':
					user.update(draw_card(deck,1))
					for key in user:
						uservalue+=user[key]
						cards.update(user)
					value_determinate(uservalue,user,name)
					if uservalue>21:
						break
					elif uservalue==21:
						break
					elif uservalue<21:
						continue
				elif x=='0':
					break
			break
		break
	while True:
		name="Dealer's"
		dealervalue=0
		deck=creatshuff()
		deck=value_assignment(deck)
		#dealer draw
		dealer=draw_card(deck,2)
		cards=dealer.copy()
		for key in dealer:
			dealervalue+=dealer[key]
		value_determinate(dealervalue,dealer,name)
		if dealer!=21:
			while True:
				dealer.update(draw_card(deck,1))
				cards.update(dealer)
				for key in dealer:
					dealervalue+=dealer[key]
				value_determinate(dealervalue,dealer,name)
				if dealervalue>21:
					break
				elif dealervalue==21:
					break
				elif dealervalue<21:
					continue
			break
		break
	
	if uservalue>21 and dealervalue>21:
		print('*'*3+"You tied the dealer. Nobody wins."+'*'*3 )
		again=input("Want to play anain?(y/n): ")
		if again=='y':
			print("-"*10)
			continue
		if again=='n':
			break
	if dealervalue<=21 and uservalue<=21:		
		if uservalue> dealervalue:
			print( '*'*3+ "You beats the Dealer!"+'*'*3 )
			again=input("Want to play anain?(y/n): ")
			if again=='y':
				print("-"*10)
				continue
			if again=='n':
				break
	if dealervalue<=21 and uservalue<=21:
		if dealervalue>uservalue:
			print( '*'*3+ "Dealer wins"+'*'*3 )
			again=input("Want to play anain?(y/n): ")
			if again=='y':
				print("-"*10)
				continue
			if again=='n':
				break
	if uservalue<=21 and dealervalue<=21:
		if uservalue==dealervalue:
			print('*'*3+"You tied the dealer. Nobody wins."+'*'*3 )
			again=input("Want to play anain?(y/n): ")
			if again=='y':
				print("-"*10)
				continue
			if again=='n':
				break
	if uservalue>21 and dealervalue<21:
		print( '*'*3+ "Dealer wins"+'*'*3 )
		again=input("Want to play anain?(y/n): ")
		if again=='y':
			print("-"*10)
			continue
		if again=='n':
			break
	if uservalue<21 and dealervalue>21:
		print( '*'*3+ "You beats the Dealer!"+'*'*3 )
		again=input("Want to play anain?(y/n): ")
		if again=='y':
			print("-"*10)
			continue
		if again=='n':
			break
