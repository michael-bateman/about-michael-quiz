# Instructions | [survey.py](https://github.com/michael-bateman/about-michael-quiz/blob/master/survey.py)
## Background
The goal of writing this program was for my grade 9 computer science class as a homework task.

## Goal
Since this was assigned as homework, the goal of the homework was to make an "adventure game' however, I made a quiz instead.  We were required to use `raw_input()`.  More information on that can be found on [the Python built in function documentation](https://docs.python.org/2/library/functions.html#raw_input).

For viewing, you can find the code [here](https://github.com/michael-bateman/about-michael-quiz/edit/master/INSTRUCTIONS.md#code) or you can clone the repository by following [these instructions](https://github.com/michael-bateman/about-michael-quiz/edit/master/INSTRUCTIONS.md#clonetherepository).

## Clone the repository
You can clone the repository if you have [Git](https://git-scm.com) installed.
```bash
$ clone https://github.com/michael-bateman/about-michael-quiz.git
```

## How to run the file
Make sure you have cloned the repository.  If you have not, follow the instructions above.
Navigate to the directory:
```bash
$ cd about-michael-quiz
```
Run the file:
```bash
$ python survey.py
```
Done! It should now run.

## What it does
This program is a simple Python code that is a 5 question plus a bonus question quiz about Michael.

## Imports
This program uses modules to a minimum.  In fact, it is possible to use the program without modules at all!  They just put a nice touch on the game.  The following modules were used:
* [Sys](https://docs.python.org/2/library/sys.html)
* [Time](https://docs.python.org/2/library/time.html)
* [Random](https://docs.python.org/2/library/random.html)

__Note:__ *All of the modules above should come preinstalled with Python*

### Sys | [Documentation](https://docs.python.org/2/library/sys.html)
The `sys` module is not needed but it allows you to quit the game when started.  The command to quit on the start screen can be issued by pressing the `q` button.  The following code is used at the beginning of the game in case you want to quit.
```python
sys.exit()
```

### Time | [Documentation](https://docs.python.org/2/library/time.html)
The `time` module is not needed but it is used for two things.
A delay is used at the beginning of the program to allow for the logo to show, and then to wait 5 seconds before displaying the instructions.  The following code is used to achieve this:
```python
time.sleep(5)
```
The `time` module is also used to record your score in case you wanted your score recorded in the `results.txt` file.  The following code is to get the time and the date.
```python
date = time.strftime("%d/%m/%Y") #This is the date
time = time.strftime("%H:%M:%S") #This is the time
```

### Random | [Documentation](https://docs.python.org/2/library/random.html)
The `random` module is used just for fun, and it chooses a random number between 0 and 9,999,999,999 that assigns the game a random game number.  The following code is used to get a random game number:
```python
gameno = random.randint(0,9999999999)
```

## Code
For those who want to see the code and don't want to download anything, it is listed below.
```python
'''
survey.py - Michael Bateman
Feb 2/17
'''

# imports
import sys
import time
import random

# functions

# main code

file = open("images/1.txt","r")
print file.read(1-100)
file.close()

file = open("images/2.txt","r")
print file.read(1-100)
file.close()

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

				file = open("../results.txt","w")
				file.write("Name: ")
				file.write(str(name))
				file.write(" Date: ")
				file.write(str(date))
				file.write(str(time))
				file.write(" Game # ")
				file.write(str(gameno))
				file.write(" Score: ")
				file.write(str(score))
				file.close()
				print "Your score has been saved in a file called 'results.txt'."
				savefalse = False
			elif (save == "b"):
				print "Have a good day! Goodbye"
				savefalse = False
			else:
				print "Invalid selection.  Please try again."

	else:
		print "Whoops...", str(start), "is an invalid key"
		print ""
```

## Issues
If you are having issues, please let me know in [issue tracker](https://github.com/michael-bateman/about-michael-quiz/issues)
