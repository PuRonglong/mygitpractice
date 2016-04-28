def func():
	global x
	print 'first, x = ', x
	x = 2
	print 'second, x = ', x

x = 50
func()
print 'third, x = ', x