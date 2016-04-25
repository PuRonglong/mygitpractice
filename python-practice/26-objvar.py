class Person:
	population = 0

	def __init__(self, name):
		self.name = name
		print '(Initializing %s.)' % self.name
		Person.population += 1

	def __det__(self, name):
		print '%s say bye.' % self.name
		Person.population -= 1

		if Person.population == 0:
			print '__det___: I am the last one.'
		else:
			print 'There are still %s people.' % Person.population

	def sayHi(self):
		print '%s say Hi.' % self.name

	def howmany(self):
		if Person.population == 1:
			print 'howmany: I am the last one.'
		else:
			print 'We have %s persons here.' % Person.population

Tom = Person('Tom')
Tom.sayHi()
Tom.howmany()

Bob = Person('Bob')
Bob.sayHi()
Bob.howmany()