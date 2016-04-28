number = 23
running = True
while running:
	guess = int(raw_input('enter your number:'))
	if guess < number:
		print 'the number is higher.'
	elif guess > number:
		print 'the number is lower.'
	elif guess == number:
		print 'you are right.'
		running = False
		print 'over.'