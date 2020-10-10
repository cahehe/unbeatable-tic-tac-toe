#Unbeatable traditional tic tac toe game developed using the minimax Algorithm

from math import inf
import random
import sys

class ticTac:
	def __init__(self):
		self.board = [i for i in range(1,10)]
		self.human = ""
		self.AI = ""
		self.moves = 0
	
	def availMoves(self):#Scans the board and checks which spots are not filled. returns the list of spots.
		return [i - 1 for i in self.board if type(i) != str]
	
	def numAvailMoves(self): #Calculates total number of available moves.
		movesAvail = self.availMoves()
		num = 0
		for i in movesAvail:
			if type(i) != str:
				num += 1
		return num
		
	def goFirst(self): #Pick which player goes first
		print("Would you like to go first? Y/N")
		while True:
			pick = input()
			if pick == "Y" or pick == "y":
				return self.human
			elif pick == "N" or pick == "n":
				return self.AI
			else:
				print("Please pick a valid choice")
	
	def display(self): #Print out the board
		print(" ",self.board[0],"|", self.board[1], "|", self.board[2])
		print(" -----------")
		print(" ",self.board[3],"|", self.board[4], "|", self.board[5])
		print(" -----------")
		print(" ",self.board[6],"|", self.board[7], "|", self.board[8])
	
	def start(self): #Start the game		
		print("Starting game!")
		self.human = self.pickPlayer()	
		turn = self.goFirst()
		while self.moves != 9: 
			#Let each player take turns while displaying the board
			if turn == self.human: #if it's human's turn
				self.display()
				avail = self.availMoves()
				print("available moves are ",avail)
				print("Your(",self.human, ") turn")
				move = input("Choose respective number to place move\n")
				valid = self.checkMoveValid(move)
				if valid == False: #If move is not valid, try again
					continue
				self.makeMove(int(move) - 1, turn)
				
			else: #else it must be AI's turn
				self.aiTurn()
				
			if self.isWinner(turn):   #Check if there is a winner			
				break
			self.moves += 1
			turn = self.switch(turn)
			print("turn is ", turn)
		#After filling up the board, let's check one last time if there is a winner or if it's tie
		self.display()
		if self.isWinner(turn): #check winner one last time
			print("Player (" + turn + ") Won!")
		elif self.isTie():#Check if we have a tie
			print("We have a tie!")
		self.restart() #Ask user if they want to play again
	
	def aiTurn(self):
		if self.numAvailMoves() == 9:#if AI is going first, pick a random move						
			firstMove = random.randrange(1,10)
			self.makeMove(firstMove, self.AI)
		else:#Else use minimax
			move = self.minimax(self.AI)
			self.makeMove(move[0],self.AI)
	
	def makeMove(self,index,player): #make move according to player's turn and index inputted.
		self.board[index] = player
		
		
	def pickPlayer(self):#Asking user to pick a player
		while True:
			print("Please pick: X/Y")
			print("Player 1: X")
			print("Player 2: O")
			pick = input()
			if pick == "X" or pick == "x":
				self.opponent = "O"
				self.AI = "O"
				print("You picked X!")
				return "X"
			elif pick == "O" or pick == "o":
				self.opponent = "X"
				self.AI = "X"
				print("You picked O!")
				return "O"
			else:
				print("Invalid entry. Please try again")
	
	def switch(self,turn):#Switch turns
		if turn == "X":
			return "O"
		else:
			return "X"
	
	def restart(self): #Restarting game.
		again = input("Would you like to play again? Y/N\n")
		if again == "y" or again == "Y":
			index = 1
			for i in range(9):	#empty the board and fill them with their respective indexes.
				self.board[i] = i + 1
			self.moves = 0		#Reset moves to 0 since we are restarting
			self.start()			
		elif again == "n" or again == "N":
			print("Ending Program")
			sys.exit()
		
	def isTie(self):
		if self.numAvailMoves() == 0:  #If the board is filled and we have no winner, it is a tie.
			return True
			
	def checkMoveValid(self,move):
		move = int(move)
		if move > 9 or move < 1: #Check if move is out of range
				print("Out of range. Please try again")
				return False	
		if type(self.board[move - 1]) != int: #Check if spot is already taken
			print("\nAlready taken. Please choose a different number.")
			return False
			
		return True
		
	def isWinner(self,turn): #Check if we have a winner
		winner = self.checkWinner(turn)
		if winner:		
			return True
		return False
		
	def gameOver(self):	#Check if the game is over
		if self.checkWinner(self.human):			
			return True 
		if self.checkWinner(self.AI):
			return True 
		if self.numAvailMoves() == 0:			
			return True
	
	def aiWon(self):#Check if AI has won
		return self.isWinner(self.AI)
		
	def humanWon(self):#Check if human player has won
		return self.isWinner(self.human)
		
	def checkWinner(self,turn):
		if self.board[0] == turn and self.board[1] == turn and self.board[2] == turn: #Horiontal at the top
			return True
		if self.board[3] == turn and self.board[4] == turn and self.board[5] == turn: #Horizontal at the middle
			return True
		if self.board[6] == turn and self.board[7] == turn and self.board[8] == turn: #Horizontal at the bottom
			return True
		if self.board[0] == turn and self.board[3] == turn and self.board[6] == turn: #Vertical first column
			return True
		if self.board[1] == turn and self.board[4] == turn and self.board[7] == turn:#Vertical mid column
			return True
		if self.board[2] == turn and self.board[5] == turn and self.board[8] == turn: #vertical last column
			return True
		if self.board[0] == turn and self.board[4] == turn and self.board[8] == turn: #top left bottom right diagnol
			return True
		if self.board[6] == turn and self.board[4] == turn and self.board[2] == turn:#bottom left top right diagnol
			return True
		return False	
			
	
	def minimax(self, player):#AI is trying to maximize while human minimize.
		if self.gameOver():    #if game is over, return the score according the the result
			if self.aiWon():	
				return [-1,100]#index 0 is the move and index 1 is the score.			
			if self.humanWon():
				return [-1,-100]
			if self.isTie():				
				return [-1,0]
				
		if player == self.AI:
			top = [-1,-inf]
		else:
			top = [-1,+inf]		

		for index in self.availMoves(): #try every available move 
			self.makeMove(index,player)
			value = self.minimax(self.switch(player)) 	#Recursively call the function with each move and check its value. The value returned will be the best or only move for opponent.
			self.makeMove(index, index + 1)
			value[0] = index

			if player == self.AI:
				if value[1] > top[1]:
					top = value  # max value
			else:
				if value[1] < top[1]:
					top = value  # min value

		return top
		
game = ticTac()
game.start()

	
