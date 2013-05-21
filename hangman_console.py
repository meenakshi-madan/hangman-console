import random
import re

wordset = file('words4k.txt').read().upper().split()  #list of 4000 dictionary words
LETTERS = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')   #to check if input is a single character

#returns a random 5+ letter word from the dictionary
def newWord():
	word = wordset[random.randrange(len(wordset))]
	if(len(word) <5):
		return newWord()
	else:
		return word
	
#starts a new game of hangman	
def start_game():
	word = newWord()   #fetch a new random word for this game
	game = list('_' * len(word))   #initialize game list to blank spaces (underscores)
	limbs = 5  #limbs for poor Bob. Decrease to make the game tougher, increase to make it easier
	endGame = False  #boolean variable to keep track of when the game is over
	#print word
	
	print "Bob has " + str(limbs) + " limbs to break"
	print "Your word for this round is " + str(len(word)) + " letters long"
	print "Let's start!"
	print ' '.join(game)
	
	#repeat while there are limbs to spare and the word hasn't been guessed fully
	while(not endGame):
		guess = raw_input("Guess a letter ") #user enters a guess
		
		#guess must be a single letter
		if guess.upper() not in LETTERS:
			print "Nono you enter just one letter"
			print " \n"
			
		#if the guess the correct
		elif guess.upper() in word:
			#replace the underscores in game variable where the guessed letter occurs
			for j in [m.start() for m in re.finditer(guess.upper(), word)]:
				game[j] = guess.upper()
				#print j
				#print game[j]
				#print game
				
			#print game	
			print ' '.join(game)
			print "Good guess!"
			print "Number of limbs left for poor Bob: " + str(limbs)
			
			#if no more letters left to guess i.e all underscores have been replaced by correctly guessed letters
			if '_' not in game:
				endGame = True
				print "You win!"
				print word
				print " \n\n\n"
			print " \n"
		
		#wrong guess
		else:
			limbs -= 1
			print ' '.join(game)
			print "Oops! Wrong guess"
			print "Number of limbs left for poor Bob: " + str(limbs)
			print " \n"
			
			#if no more limbs left to spare
			if limbs == 0:
				endGame = True
				print "You lose!"
				print ' '.join(game)
				print word
				print " \n\n\n"
	
#displays rules of the game	
def showRules():
		print "\n\n"
		print "If you like guessing games, testing your vocabulary, or killing innocent people, you'll love this game."
		print "The idea is to guess the letters that make up a secret random word"
		print "For every correct guess, the places where the letter occurs is revealed"
		print "For every wrong guess, poor Bob loses a limb"
		print "The game ends when Bob has no more limbs to lose OR when you have correctly guess the entire word"
		print "\n\n"


		
selection = 'S'   #Selection input from user
while(selection.upper() != 'X'):
	print "Welcome to Meenakshi's hangman game!"
	print "To start a new game, enter S"
	print "To review the rules, enter R"
	print "To exit press X"	
	selection = raw_input()
	if(selection.upper() == 'S'):
		start_game()
	elif(selection.upper() == 'R'):
		showRules()
