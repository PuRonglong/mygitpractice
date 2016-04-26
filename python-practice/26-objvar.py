class Person:
	population = 0
	
	def __init__(self, name):
		self.name = name
		print '(Initializing %s.)' % self.name
		Person.population += 1

	def __del__(self):
		print '%s say bye.' % self.name

		Person.population -= 1

		if Person.population == 0 :
			print 'del: I am the last one.'
		else:
			print 'There are still %d people.' % Person.population

	def sayHi(self):
		print '%s say Hi.' % self.name

	def howMany(self):
		if Person.population == 1:
			print 'howMany: I am the last one.'
		else:
			print 'We have %d persons here.' % Person.population

Tom = Person('Tom')
Tom.sayHi()
Tom.howMany()

Bob = Person('Bob')
Bob.sayHi()
Bob.howMany()