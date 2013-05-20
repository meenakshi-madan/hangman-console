import random
import re

wordset = file('words4k.txt').read().upper().split()
LETTERS = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
def newWord():
  word = wordset[random.randrange(len(wordset))]
	if(len(word) <5):
		return newWord()
	else:
		return word
	
	
def start_game():
	word = newWord()
	game = list('_' * len(word))
	limbs = 5
	endGame = False
	#print word
	
	print "Bob has " + str(limbs) + " limbs to break"
	print "Your word for this round is " + str(len(word)) + " letters long"
	print "Let's start!"
	print ' '.join(game)
	while(not endGame):
		guess = raw_input("Guess a letter ")
		if guess.upper() not in LETTERS:
			print "Nono you enter just one letter"
			print " \n"
		elif guess.upper() in word:
			for j in [m.start() for m in re.finditer(guess.upper(), word)]:
				game[j] = guess.upper()
				#print j
				#print game[j]
				#print game
				
			#print game	
			print ' '.join(game)
			print "Good guess!"
			print "Number of limbs left for poor Bob: " + str(limbs)
			if '_' not in game:
				endGame = True
				print "You win!"
				print word
				print " \n\n\n"
			print " \n"
		else:
			limbs -= 1
			print ' '.join(game)
			print "Oops! Wrong guess"
			print "Number of limbs left for poor Bob: " + str(limbs)
			print " \n"
			if limbs == 0:
				endGame = True
				print "You lose!"
				print ' '.join(game)
				print word
				print " \n\n\n"
	
	
def showRules():
		print "\n\n"
		print "If you like guessing games, testing your vocabulary, or killing innocent people, you'll love this game."
		print "The idea is to guess the letters that make up a secret random word"
		print "For every correct guess, the places where the letter occurs is revealed"
		print "For every wrong guess, poor Bob loses a limb"
		print "The game ends when Bob has no more limbs to lose OR when you have correctly guess the entire word"
		print "\n\n"

selection = 'S'
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
