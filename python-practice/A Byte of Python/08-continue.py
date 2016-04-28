while True:
	s = raw_input('enter some string:')
	if s == 'quit':
		break
	if len(s) < 3:
		continue
	print 'too long.'