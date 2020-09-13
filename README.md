# rockpaperscissor
This game is built with python 3.8

If you are tired of having no playmate, then a 5-minute stint of rock, paper, scissors with the computer and designed by you, yourself will improve your mood.
We again use the random function here. You make a move first and then the program makes one. To indicate the move, you can either use a single alphabet or input an entire string. A function will have to be set up to check the validity of the move.
Using another function, the winner of that round is decided. You can then either give an option of playing again or decide a pre-determined number of moves in advance. A scorekeeping function will also have to be created which will return the winner at the end.
User inputs will be validated using external packages.

Externl Packages:
	* word2number: Using This package a word which is equalent to a number will be automatically converted to the maped number. ex: four = 4
	https://pypi.org/project/word2number/
	*pyinputplus: a package to  validate user inputs https://pypi.org/project/PyInputPlus/
	

This Game is build based of the following conditions:
	1- scissor > paper
	2- paper > rock
	3- rock > scissor

How To Play The Game:
1- First install Python to you OS
	* Linux: https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-20-04-server
	* Windows: https://www.goodhousekeeping.com/uk/consumer-advice/technology/a30378443/how-to-install-windows-10/

2-run the project in the terminal using the filename.py
3-First You will see to type a command 
	* Start -> start the game
	* Exit -> Exit from game
4- You will be asked to enter the number of games you want to play vs computer
	* Note: only integer numbers are allowed
5- Then according to game number you will be asked to pick from rock, scissor and paper
6- Now with each of your guess programm will also pick on randomly
7- after loops finishes the excecution then the winner will be announces
8- at end you will be asked to try again or not

