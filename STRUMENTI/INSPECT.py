"""
	Il modulo inspect è un modulo molto utile che contiene molte funzioni che ci possono aiutare a ottenere
	informazioni riguardo oggetti vivi come moduli, classi, metodi, funzioni, tracebacks, frame objects e code objects.

	Ci sono quattro servizi principali che possono essere forniti dal modulo :
		- type checking 
		- source code
		- inspecting classi e funzioni
		- esaminare lo stack
"""


#	TIPE CHECKING

"""
	getmembers(object)

	Restituisce tutti i membri ( attributi e metodi ) di un oggetto sotto forma di lista di tuple ( name, value) ordinate in base al nome.
"""
r = 10
inspect.getmembers(r)

"""
	[('__abs__', <method-wrapper '__abs__' of int object at 0x7f8c4002ea50>), ('__add__', <method-wrapper '__add__' of int object at 0x7f8c4002ea50>), 
	('__and__', <method-wrapper '__and__' of int object at 0x7f8c4002ea50>), ('__bool__', <method-wrapper '__bool__' of int object at 0x7f8c4002ea50>), 
	('__ceil__', <built-in method __ceil__ of int object at 0x7f8c4002ea50>), ('__class__', <class 'int'>), ('__delattr__', <method-wrapper '__delattr__' of 
	int object at 0x7f8c4002ea50>), ('__dir__', <built-in method __dir__ of int object at 0x7f8c4002ea50>), ......
"""



#	SOURCE CODE

"""
	inspect.getsource(object)
	Restituisce il codice sorgente di un oggetto ( in python tutto è un oggetto )

	inspect.getsourcelines(object)
	Restituisce il codice sorgente linea per linea. ( lista di stringhe )

	inspect.getdoc(object)
	Restituisce la documentazione relativa all'oggetto

"""


#	CLASS TREE

import inspect

class A:
	pass

class B(A):
	pass 

class C(B):
	pass 

tree = inspect.getclasstree([A,B,C])
print(tree[0])	#	(<class 'object'>, ())
print(tree[1])	#	[(<class '__main__.A'>, (<class 'object'>,)), [(<class '__main__.B'>, (<class '__main__.A'>,)), [(<class '__main__.C'>, (<class '__main__.B'>,))]]]



#	ESTRARRE SIGNATURE E ARGOMENTI DI UNA FUNZIONE
#
#	inspect.signature(function)
class Person:
	def __init__(self, name):
		self.name = name

a = Person("lorenzo")
print(inspect.signature(a.__init__))	#	(name)

#	inspect.getfullargspec(function)





#	UNWRAPPING FUNCTIONS
# 	Quando, per esempio, c'è un decoratore che wrappa una funzione, potremmo aver bisogno della funzione wrappata.

inspect.unwrap(function)

#	Restituisce quindi la funzione originale wrappata.

def decoratore(func):
	def wrapper(*args, **kwargs):
		print("Decoro")
		return func(*args, **kwargs)
	return wrapper

@decoratore
def addizione(a,b):
	return a+b

print(addizione(1,2))
#	Decoro
#	3

print(inspect.unwrap(addizione)(5,10))
#	15


"""
	GETTING TRACEBACK FRAMES

"""




















