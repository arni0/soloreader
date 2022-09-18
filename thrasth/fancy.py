import cmd
import sys
import os


screen_width = 100

class player:
    def __init__(self):
        self.name = ''
        self.feeling = ''
        self.astrological = ''
        self.position = 'ground'
        self.won = False
        self.solves = 0
player1 = player()

################
# Title Screen #
################
def title_screen_options():
	#Allows the player to select the menu options, case-insensitive.
	option = input("> ")
	if option.lower() == ("play"):
		print("setup_game()")
	elif option.lower() == ("quit"):
		sys.exit()
	elif option.lower() == ("help"):
		help_menu()		
	while option.lower() not in ['play', 'help', 'quit']:
		print("Invalid command, please try again.")
		option = input("> ")
		if option.lower() == ("play"):
			print("setup_game()")
		elif option.lower() == ("quit"):
			sys.exit()
		elif option.lower() == ("help"):
			help_menu()

def title_screen():
	#Clears the terminal of prior code for a properly formatted title screen.
	os.system('clear')
	#Prints the pretty title.
	print('#' * 45)
	print('# Welcome to this text-based puzzle RPG for #')
	print("#      Bryan Tong's CS10 Final Project!     #")
	print('#' * 45)
	print("                 .: Play :.                  ")
	print("                 .: Help :.                  ")
	print("                 .: Quit :.                  ")
	title_screen_options()


#############
# Help Menu #
#############
def help_menu():
	print("")
	print('#' * 45)
	print("Written by Bryan Tong")
	print("Version Final (1.0.2a)")
	print("~" * 45)
	print("Type a command such as 'move' then 'left'")
	print("to nagivate the map of the cube puzzle.\n")
	print("Inputs such as 'look' or 'examine' will")
	print("let you interact with puzzles in rooms.\n")
	print("Puzzles will require various input and ")
	print("possibly answers from outside knowledge.\n")
	print("Please ensure to type in lowercase for ease.\n")
	print('#' * 45)
	print("\n")
	print('#' * 45)
	print("    Please select an option to continue.     ")
	print('#' * 45)
	print("                 .: Play :.                  ")
	print("                 .: Help :.                  ")
	print("                 .: Quit :.                  ")
	title_screen_options()


#################
# Game Handling #
#################
# quitgame = 'quit'
title_screen()