'''
survey.py - Michael Bateman
Feb 2/17
'''

# imports
import sys

# functions

# main code

file = open("images/1.txt","r")
print file.read(1-100)
file.close()

file = open("images/2.txt","r")
print file.read(1-100)
file.close()

file = open("instructions/instructions.txt","r")
print file.read(1-100)
file.close()

start = raw_input()
start = start.lower()

if (start == "q"):
	sys.exit()
elif (start == "s"):
	score = 0
	print "What is Michael's favourite food?"
	print "a)Pizza b)Pasta c)Fish d)Hot Dogs"
	one = raw_input()
	one = one.lower()
	if (one == "b"):
		score = score + 1
		print "Correct! Score:", str(score)
	else:
		print "Incorrect. Score:", str(score)
	print ""

	print "What instrument does Michael mainly play?"
	print "a)Tuba b)Saxophone c)Trumpet d)Trombone"
	two = raw_input()
	two = two.lower()
	if (two == "d"):
		score = score + 1
		print "Correct! Score:", str(score)
	else:
		print "Incorrect. Score:", str(score)
	print ""

	print "What time does Michael wake up during the school week?"
	print "a)4:25am b)5:25am c)6:25am d)7:25am"
	three = raw_input()
	three = three.lower()
	if (three == "b"):
		score = score + 1
		print "Correct! Score:", str(score)
	else:
		print "Incorrect. Score:", str(score)
	print ""

	print "How much storage does Michael's iPhone have?"
	print "a)32GB b)64GB c)128GB d)256GB"
	four = raw_input()
	four = four.lower()
	if (four == "a"):
		score = score + 1
		print "Correct! Score:", str(score)
	else:
		print "Incorrect. Score:", str(score)
	print ""

	print "Does Michael like Windows computers?"
	print "a)Yes b)No"
	five = raw_input()
	five = five.lower()
	if (five == "b"):
		score = score + 1
		print "Correct! Score:", str(score)
	else:
		print "Incorrect. Score:", str(score)
	print ""

	print "Would you like a bonus question?"
	print "NOTE: If you get the bonus question wrong, your score will reset to 0.  Question worth 3 points.  The bonus question is NOT multiple choice."
	print "a)Bonus b)No Bonus"
	bonus1 = raw_input()
	bonus1 = bonus1.lower()
	if (bonus1 == "a"):
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
			print "Whoops! Invalid selection. Score:", str(score)

	else:
		print "Maybe another time you will want to complete the bonus question!"
		print "Percentage:", (str(score)/8)

else:
	print "Whoops...", str(start), "is an invalid key"