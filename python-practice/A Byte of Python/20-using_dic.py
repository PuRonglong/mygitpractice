puronglong = {
	'name' : 'puronglong',
	'address' : 'puronglong@foxmail.com',
	'telephone' : '18844104751'
}

print 'puronglong`s address is %s'% puronglong['address']

for key, value in puronglong.items():
	print 'puronglong`s %s is %s'% (key, value)

if 'name' in puronglong:
	print 'name in puronglong.'