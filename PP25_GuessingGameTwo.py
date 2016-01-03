import time, math


def start():
	
	print ('\nThink of a number between 1 and 100')
	time.sleep(1)
	print ('Don\'t tell me what it is...')
	time.sleep(1.5)

	numberList = list(range(1, 101))
	number = math.ceil(len(numberList) / 2)
	counter = 1

	return (numberList, number, counter)


def computerNumberGuess():

	x = start()

	numberList = x[0]
	number = x[1]
	counter = x[2]

	while True:
		
		guessResult = str(input('\nIs it higher, lower or equal to ' + str(number) + \
			'? \n(H for higher, L for lower, E for equal. Type \'EXIT\' at any point to leave): '))

		if guessResult.lower() == 'exit':
			break
		
		elif guessResult.lower() == 'h':
			numberList = list(range(number + 1, (numberList[-1] + 1)))
			number += math.ceil(len(numberList) / 2)
			counter += 1
		
		elif guessResult.lower() == 'l':
			numberList = list(range(numberList[0], number))
			number -= math.ceil(len(numberList) / 2)
			counter += 1

		elif guessResult.lower() == 'e':
			print ('\nYou were thinking of the number ' + str(number) + '.') 
			time.sleep(1)
			print ('This was found in ' + str(counter) + ' guesses.')
			time.sleep(1.5)
			pass

			playAgain = str(input('\nWould you like to play again? \n(Y for yes, N for no): '))
			
			if playAgain.lower() == 'y':
				
				x = start()

				numberList = x[0]
				number = x[1]
				counter = x[2]

				continue
			
			else:
				break


if __name__ == '__main__':
	computerNumberGuess()


