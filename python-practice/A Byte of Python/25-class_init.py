class Person:
	def __init__(self, name):
		self.name = name

	def sayHi(self):
		print 'Hello World', self.name

p = Person('puronglong')

p.sayHi()