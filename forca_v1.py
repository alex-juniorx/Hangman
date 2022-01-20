# -*- coding: utf-8 -*-
# Hangman Game

import random

# Board game: possible status.
board = ['''
    +---+
    |   |
    |
    |
    |
    |
=========''', '''
    +---+
    |   |
    |   O
    |
    |
    |
=========''', '''
    +---+
    |   |
    |   O
    |   |
    |
    |
=========''', '''
    +---+
    |   |
    |   O
    |  /|
    |
    |
=========''', '''
    +---+
    |   |
    |   O
    |  /|\\
    |
    |
=========''', '''
    +---+
    |   |
    |   O
    |  /|\\
    |  /
    |
=========''', '''
    +---+
    |   |
    |   O
    |  /|\\
    |  / \\
    |
=========''']


# Game class
class Hangman:

	# Constructor
	def __init__(self, word):
		self.word = word

	# Player guess
	def guess(self):
		return input('PLEASE, GUESS A LETTER: ').upper()
		
	# Method to verify if the game is over
	def hangman_over(self, count_status, correct_letters, wrong_letters):
		if count_status == 6:
			return True
		else:
			return False
		
	# Method to verify if the player has won
	def hangman_won(self, count_status, correct_letters, wrong_letters):
		for letter in self.word:
			if letter not in correct_letters:
				return False
		return True

	# Method to write the secret word with hidden letters
	def hide_word(self, correct_letters):
		display = ''
		for letter in self.word:
			if letter in correct_letters:
				display += letter
			else:
				display += '_'
		return display
		
	# Method to display the game status
	def print_game_status(self, count_status, correct_letters, wrong_letters):
		print(board[count_status])
		print('\nWORD: ', self.hide_word(correct_letters))
		print('\nCORRECT LETTERS: ')
		for letter in correct_letters:
			print(letter, ', ', end='')
		print('\nWRONG LETTERS:')
		for letter in wrong_letters:
			print(letter, ', ', end='')

# Function to select a random word from the word bank
def rand_word():
        with open("palavras.txt", "rt") as f:
                bank = f.readlines()
        return bank[random.randint(0,len(bank)-1)].strip().upper()

# Main function - Game execution
def main():
	# Instantiation of a game
	game = Hangman(rand_word())
	count_status = 0
	correct_letters = []
	wrong_letters = []
	alphabet = 'ABCDEFGHIJKLMNOPQRSTUWVXYZABCDEFGHIJKLMNOPQRSTUWVXYZ'

	print('-----------------------HANGMAN-----------------------')

	# While the game is not over and the player has not won: status is displayed, player is asked to guess a letter and the guess is verified
	while game.hangman_over(count_status, correct_letters, wrong_letters) == False and game.hangman_won(count_status, correct_letters, wrong_letters) == False:
		game.print_game_status(count_status, correct_letters, wrong_letters)
		print('\n....................................................')
		guess = game.guess()
		# Condition to avoid a bad entry
		if len(guess) > 1 or guess not in alphabet:
			print('SORRY, THAT IS NOT A VALID ENTRY!')
		else:
			# Condition to avoid the player from repeating their guess
			if guess not in correct_letters and guess not in wrong_letters:
				if guess in game.word:
					correct_letters.append(guess)
				else:
					wrong_letters.append(guess)
					count_status += 1
			else:
				print('HEY, YOU HAVE ALREADY CHOSEN LETTER \'', guess, '\'. TRY ANOTHER ONE!')

	# When the game is over, the final status and result are displayed
	game.print_game_status(count_status, correct_letters, wrong_letters)
	if game.hangman_won(count_status, correct_letters, wrong_letters):
		print('\n\nCONGRATULATIONS, YOU WON! :D')
	else:
		print('\n\nOH NO, YOU LOSE! :(', '\nTHE SECRET WORD WAS: ', game.word)

# Game is triggered		
if __name__ == "__main__":
	main()

