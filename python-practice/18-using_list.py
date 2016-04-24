mylist = ['apple', 'mango', 'carrot', 'banana']

print 'I have', len(mylist), 'items in my bag.'

print 'These items are:'

for item in mylist:
	print item

print 'And i need another one: rice'

mylist.append('rice')

print 'This is mylist at last:'

for item in mylist:
	print item

print 'I need to sort my shopping list.'

print 'This is my shopping list by sort:'

mylist.sort()
for item in mylist:
	print item

print 'I will buy the first one.'

del mylist[0]

print 'I have bought the first one and mylist like this:'

for item in mylist:
	print item