'''
survey.py - Michael Bateman
Feb 2/17
'''

# imports
import sys
import time
import random

# functions

def openPicture():
	file = open("images/1.txt","r")
	print file.read(1-100)
	file.close()

	file = open("images/2.txt","r")
	print file.read(1-100)
	file.close()

# main code

openPicture()

time.sleep(5)

inc = True
while (inc == True):
	file = open("instructions/instructions.txt","r")
	print file.read(1-100)
	file.close()

	start = raw_input()
	start = start.lower()

	if (start == "q"):
		inc = False
		sys.exit()
	elif (start == "s"):
		inc = False
		score = 0

		qone = True
		while (qone == True):
			print "What is Michael's favourite food?"
			print "a)Pizza b)Pasta c)Fish d)Hot Dogs"
			one = raw_input()
			one = one.lower()
			if (one == "b"):
				score = score + 1
				qone = False
				print "Correct! Score:", str(score)
			elif (one == "a" or one == "c" or one == "d"):
				qone = False
				print "Incorrect. Score:", str(score)
			else:
				print "Invalid selection.  Please try agian."
			print ""

		qtwo = True
		while (qtwo == True):
			print "What instrument does Michael mainly play?"
			print "a)Tuba b)Saxophone c)Trumpet d)Trombone"
			two = raw_input()
			two = two.lower()
			if (two == "d"):
				score = score + 1
				qtwo = False
				print "Correct! Score:", str(score)
			elif (two == "a" or two == "b" or two == "c"):
				qtwo = False
				print "Incorrect. Score:", str(score)
			else:
				print "Invalid selection.  Please try agian."
			print ""

		qthree = True
		while (qthree == True):
			print "What time does Michael wake up during the school week?"
			print "a)4:25am b)5:25am c)6:25am d)7:25am"
			three = raw_input()
			three = three.lower()
			if (three == "b"):
				score = score + 1
				qthree = False
				print "Correct! Score:", str(score)
			elif (three == "a" or three =="c" or three == "d"):
				qthree = False
				print "Incorrect. Score:", str(score)
			else:
				print "Invalid selection.  Please try agian."
			print ""

		qfour = True
		while (qfour == True):
			print "How much storage does Michael's iPhone have?"
			print "a)32GB b)64GB c)128GB d)256GB"
			four = raw_input()
			four = four.lower()
			if (four == "a"):
				score = score + 1
				qfour = False
				print "Correct! Score:", str(score)
			elif (four == "b" or four == "c" or four =="d"):
				qfour = False
				print "Incorrect. Score:", str(score)
			else:
				print "Invalid selection.  Please try agian."
			print ""

		qfive = True
		while (qfive == True):
			print "Does Michael like Windows computers?"
			print "a)Yes b)No"
			five = raw_input()
			five = five.lower()
			if (five == "b"):
				score = score + 1
				qfive = False
				print "Correct! Score:", str(score)
			elif (five == "a" or five == "b" or five == "c"):
				qfive = False
				print "Incorrect. Score:", str(score)
			else:
				print "Invalid selection.  Please try agian."
			print ""

		qbonus = True
		while (qbonus == True):
			print "Would you like a bonus question?"
			print "NOTE: If you get the bonus question wrong, your score will reset to 0.  Question worth 3 points.  The bonus question is NOT multiple choice."
			print "a)Bonus b)No Bonus"
			bonus1 = raw_input()
			bonus1 = bonus1.lower()
			if (bonus1 == "a"):
				qbonus = False
				print ""
				print "What is Michael's favourite number?"
				print "NON Multiple Choice.  Type 'G' to give up"
				bonus2 = raw_input()
				bonus2 = bonus2.lower()
				if (bonus2 == "8"):
					score = score + 3
					print "Correct! Good Job! Score:", str(score)
				elif (bonus2 == "g"):
					score = 0
					print "Oh no! You gave up. Score:", str(score)
				else:
					score = 0
					print "Incorrect. Score:", str(score)
			elif (bonus1 == "b"):
				qbonus = False
				print "Maybe another time you will want to complete the bonus question!"
				print "Score:", str(score)
			else:
				print "Invalid selection.  Please try agian."

		savefalse = True
		while (savefalse == True):
			print "Would you like your score to be saved to your computer?"
			print "a)Yes b)No"
			save = raw_input()
			save = save.lower()
			if (save == "a"):
				print ""
				name = raw_input("Name:")
				gameno = random.randint(0,9999999999)
				date = time.strftime("%d/%m/%Y")
				time = time.strftime("%H:%M:%S")

				file = open("results-" + str(name) + ".txt","w")
				file.write("Name: " + str(name) + "   Date: " + str(date) + " " + str(time) + "   Game # " + str(gameno) + "   Score: " + str(score))
				file.close()
				print "Your score has been saved in a file called 'results.txt-" + str(name) + "'."
				savefalse = False
			elif (save == "b"):
				print "Have a good day! Goodbye"
				savefalse = False
			else:
				print "Invalid selection.  Please try again."
				print ""

	else:
		print "Whoops...", str(start), "is an invalid key"
		print ""