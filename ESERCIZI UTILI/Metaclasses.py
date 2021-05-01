#	https://cazzola.di.unimi.it/pa-es6.html
"""
	Scopo di questo esercizio è quello di creare una metaclasse che vada a creare un campo all'interno della 
	classe Person il quale ci permetterà di avere un conteggio del numero di istanze create da quest'ultima.
"""

class MegaClass(type):
	def __new__(mega, cls_name, supers, attributes):
	#	In realtà potrei aggiungerlo al dizionario anche qui
		return super().__new__(mega, cls_name, supers, attributes)

	#	Nella fase di inizializzazione della classe vado a creare l'apposito attributo
	def __init__(cls_obj, cls_name, supers, attributes):
		if 'counter' not in attributes.keys():
			setattr(cls_obj, 'counter', 0)

	#	Ogni volta che creo una istanza aggiorno il contatore.
	def __call__(cls, *args):
		setattr(cls, 'counter' , getattr(cls, 'counter') + 1)



"""
	L'obiettivo è quello di creare una metaclasse che trasformi ogni istanza creata della classe Person
	in una istanza della classe Worker.

"""

class MegaClassWorker(type):
	def __new__(mega, cls, supers, dictionary):
		return super().__new__(mega, cls, supers, dictionary)

	def __call__(cls, *args):
		if cls.__name__ == 'Person':
			return super(MegaClassWorker, Worker).__call__(*args)
		else : 
			return super().__new__(*args)



class Worker():

	def __init__(self, name, lastname, birthday, pay_per_hour = 10):
		self.name = name
		self.lastname = lastname
		self.birthday = birthday
		self.pay_per_hour = pay_per_hour

	def get_day_salary(self):
			return self.pay_per_hour * 8

	def set_day_salary(self, value):
			self.pay_per_hour = value / 8

	def __str__(self):
		return name, lastname, birthday, pay_per_hour

	day_salary = property(get_day_salary, set_day_salary, None, "Properties")





"""
	L'obiettivo è quello di creare una metaclasse che permetta ai metodi della classe base di essere
	attivati esclusivamente quando chiamati due volte.
"""

# [1]
import types

def Decoratore(func):
	counter = 0
	def Wrapper(*args, **kwargs):
		nonlocal counter
		counter += 1

		if counter == 2 : 
			counter = 0
			return func(*args, **kwargs)
		else : 
			return "Deve essere chiamato due volte - attuale = {0} " . format(counter)
	return Wrapper



def MetaDecoratore(decoratore):
	class MegaTwice(type):
		def __new__(mega, classname, supers, attributes):
			for name, value in attributes.items():
				if type(value) == types.FunctionType and name != '__init__':
					attributes[name] = decoratore(value)
			return super().__new__(mega, classname, supers, attributes)
	return MegaTwice


class Person(metaclass = MetaDecoratore(Decoratore)):

	def __init__(self, name, lastname, birthday):
		self.name = name
		self.lastname = lastname
		self.birthday = birthday

	def __str__(self):
		return "Nome : {0} - Cognome : {1} - Compleanno : {2} \n " . format(self.name, self.lastname, self.birthday)

	def prova(self):
		print("ciao!")





lorenzo = Person("Lorenzo" , "Cimini" , "11/07/1997")
print(lorenzo)
print(lorenzo)
print(lorenzo.prova())


# [2]


import types 

def Decoratore(func):
	counter = 0
	def Wrapper(*args, **kwargs):
		nonlocal counter
		counter += 1

		if counter == 2 :
			counter = 0
			return func(*args, **kwargs)
		else:
			return "Ancora una volta"
	return Wrapper

class MetaClasse(type):
	def __new__(meta, classname, supers, attributes):
		for attr_name, attr_value in attributes.items():
			if type(attr_value) == types.FunctionType and attr_name != '__init__':
				attributes[attr_name] = Decoratore(attr_value)
		return super().__new__(meta, classname, supers, attributes)


class Person(metaclass = MetaClasse):

	def __init__(self, name, lastname, birthday):
		self.name = name
		self.lastname = lastname
		self.birthday = birthday

	def __str__(self):
		return "Nome : {0} - Cognome : {1} - Compleanno : {2} \n " . format(self.name, self.lastname, self.birthday)

	def prova(self):
		print("ciao!")


lorenzo = Person("Lorenzo" , "Cimini" , "11/07/1997")
print(lorenzo)
print(lorenzo)
print(lorenzo.prova())


















































