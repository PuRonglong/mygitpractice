name = 'Swaroop'

if name.startswith('Swa'):
	print 'Yes, the string starts with Swa string.'

if name.find('a') != -1:
	print 'Yes, the string contains a.'

if 'w' in name:
	print 'Yes, w is in name.'

delimiter = "__*__"
coutries = ['Japan', 'China', 'India', 'Braril']

print delimiter.join(coutries)