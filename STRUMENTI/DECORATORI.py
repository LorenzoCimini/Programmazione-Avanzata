"""
	DECORATORI
	Hanno lo scopo di realizzare un comportamento simile a quello ottenuto con i vari approcci dei managed 
	attributes, ma in modo più potente.

	Esistono due tipologie di decoratori :
		-	Decoratori di funzioni
		-	Decoratori di classi
	Quindi i decoratori possono essere sia classi che funzioni ma, la loro tipologia varierà in base
	al target di decorazione e non in base alla forma che hanno.
	Possiamo quindi dire che, se avessimo un decoratore sotto forma di classe e un decoratore sotto forma di funzione
	che vanno a decorare una funzione, allora questi due decoratori sono entrambi di funzioni.

	La struttura classica di un decoratore è quella della clousure perchè andremo di fatto a 'wrappare'
	una funzione con il nostro decoratore che, appunto, decorerà quest'ultima.

"""




#	DECORATORI DI FUNZIONI

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner


def ordinary():
    print("I am ordinary")


ordinary() 	#	I am ordinary 
decorata = make_pretty(ordinary)
decorata() #	I got decorated \n I'm ordinary


#	Questo è il modo con il quale le closure ci hanno abitutato a lavorare ma, python ci mette
#	a disposizione una sintassi ancora più semplice per realizzare lo stesso meccanismo, ovvero :

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")


ordinary() #	I got decorated \n I'm ordinary

#	Come appena detto questo è zucchero sintattico dal momento che non aggiunge/toglie niente
#	al meccanismo di decorazione bensì serve esclusivamente a migliorare la leggibilità del codice.

#	DECORAZIONE FUNZIONE CON PARAMETRI :

def decoratore(function):
	def wrapper(*numeri_da_moltiplicare):
		print("STO DECORANDO")
		if 5 in numeri_da_moltiplicare : 
			print("Non posso moltiplicare il 5")
			return
		else :
			return function(*numeri_da_moltiplicare)
	return wrapper

def moltiplicazione(*numeri_da_moltiplicare):
	risultato = 1

	for numero in numeri_da_moltiplicare:
		risultato *= numero
	return numero

print(moltiplicazione(10,12,8,8))



# DECORATORE DI FUNZIONE SOTTO FORMA DI CLASSE 

class wrapper:
	def __init__(self, func):
		self.func = func

	def __call__(self, *args):
		print("Sto decorando")
		return self.func(*args)


@wrapper
def moltiplicazione(*numeri_da_moltiplicare):
	risultato = 1

	for numero in numeri_da_moltiplicare:
		risultato *= numero
	return risultato

print(moltiplicazione(10,12,8,8,5))
#	Sto decorando
#	38400

"""
	Come abbiamo visto quindi possiamo andare a decorare, attraverso un metodo oppure una classe,
	una funzione.
	In questo caso il decoratore viene detto DI FUNZIONE.

"""



"""
	CLASS DECORATOR
	Qui ovviamente il nostro decoratore tornerà sempre e solo una classe.
	La struttura quindi è quella di una clousure di una classe che, alla fine, ritornerà una classe.
	Lo scopo quindi è quello di andare a fare l'overloading di come si accede alla nostra classe 
	attraverso i classici metodi di overloading ( __getattr__ , __getattribute__ , __setattr__ , __delattr__)

"""

"""

	Il problema che sorge in questo caso è quello del puntatore alla classe wrappata.
	Infatti, nella classe decoratrice, il self ovviamente si riferirà alla classe stessa e non alla
	classe che stiamo wrappando.
	Per risolvere questo problema viene creato un attributo 'classe_decorata' ( nel nostro caso ) al 
	quale andremo ad associare l'oggetto della classe originale e sul quale andremo a deviare
	ogni chiamata.

	Questa operazione di 'deviamento' viene fatta attraverso i metodi getattr e setattr.
	Tutto questo per creare appunto un collegamento che mi possa permettere di accedere a tutti
	i metodi/informazioni dell'oggetto che stiamo wrappando.
"""

def decorator(cls):
    class wrapper:
        def __init__(self, *args):
            print("I'm creating {0} {1} " . format(cls.__name__ , args))
            print("Questo è il link alla classe decorata")
            print(str(cls(*args)) + "\n\n\n")
            
            self.classe_decorata = cls(*args) 

        def __getattr__(self,name): 
            print("STO ACQUISENDO DA :  {0} L'ATTRIBUTO : {1} " . format(self.classe_decorata , name))
            return getattr(self.classe_decorata , name)
#			Alla classe decorata prelevo l'attributo di nome 'name'

        def __setattr__(self, attribute, value): 
#		Sto quindi di fatto facendo l'operazione citata alla riga 8
        	print(attribute)
        	if attribute == 'classe_decorata':
        		self.__dict__[attribute] = value
        	else:
        		setattr(self.classe_decorata , attribute, value)
#				Setto alla classe decorata l'attributo 'attribute' con il valore value se non esiste.
#				Se non ci fosse questo la creerebbe all'interno del decoratore.
    return wrapper


@decorator
class C:
    def __init__(self,x,y): 
    	self.attr = 'spam'



#	ESEMPI DI APPLICAZIONI CONCRETE DI DECORATORI - TIMER - DECORAZIONE DI FUNZIONI
#	Il nostro obiettivo qui è quello di misurare il tempo di computazione necessario a comprehensions
#	e map() per creare una lista.


import time

class decoratore:
	def __init__(self, function):
		self.function = function
		self.alltime = 0							# Creo l'attributo alltime all'interno delle funzioni

	def __call__(self, *args , **kwargs):
		start = time.process_time()					# Prendo il tempo di inizio
		funzione = self.function(*args , **kwargs)	# La eseguo
		elapsed = time.process_time() - start		# Calcolo tempo passato
		self.alltime = self.allTime + elapsed		# Aggiorno l'attributo dell'oggetto funzione 
		print(' {0} : {1:.5f}, {2:.5f}' . format ( self.function.__name__ , elapsed , self.alltime))
		return funzione 							# Ritorno la funzione decorata

@decoratore
def listcomp(n):
	return [ x * 2 for x in range(n)]

@decoratore
def listmap(n):
	return list(map( lambda x : x * 2 , range(n)))


result = listcomp(5)
listcomp(50000)
listcomp(500000)
listcomp(1000000)
print(result)
print(’allTime = {0}’.format(listcomp.alltime)) print(’’)

result = mapcall(5)
mapcall(50000)
mapcall(500000)
mapcall(1000000)
print(result)
print("allTime = {0}".format(mapcall.alltime)) 
print("map/comp = {0}".format(round(mapcall.alltime / listcomp.alltime, 3)))


"""
listcomp: 0.00000, 0.00000										
listcomp: 0.03000, 0.03000
listcomp: 0.41000, 0.44000
listcomp: 0.85000, 1.29000 
[0, 2, 4, 6, 8]
allTime = 1.29


mapcall: 0.00000, 0.00000 
mapcall: 0.07000, 0.07000 
mapcall: 0.71000, 0.78000 
mapcall: 1.41000, 2.19000 
[0,2,4,6,8]
allTime = 2.19 

map/comp = 1.698
"""


#	ESEMPI DI APPLICAZIONI CONCRETE DI DECORATORI - TRACER - DECORAZIONE DI CLASSE
#	L'obiettivo di questo decoratore è quello di tracciare qualsiasi accesso ai nostri campi

def decoratore(classe):
	class wrapper:
		def __init__(self, *args):
			self.classe_decorata = classe(*args)
			self.fetches = 0

		def __getattr__(self, name):
			print("STO PRELEVANDO {0}" .format(name))
			self.fetches += 1
			return getattr(self.classe_decorata,name)

	return wrapper

class Person:
	def __init__(self, nome, cognome, stipendio):
		self.nome = nome
		self.cognome = cognome
		self.stipendio = stipendio

	def __str__(self):
		return "Nome : {0} - Cognome : {1} - Stipendio {2}\n" . format(self.nome, self.cognome, self.stipendio)


lorenzo = Person("Lorenzo" , "Cimini" , 1000)
print(lorenzo.nome)

elisabetta = Person("Elisabetta" , "Giordano" , 2000)
print(elisabetta.cognome)

print((lorenzo.fetches , elisabetta.fetches))

"""
	STO PRELEVANDO nome
	Lorenzo
	STO PRELEVANDO cognome
	Giordano
	(1, 1)	-> Ogni persona ha un suo fetches - sono due istanze separate
			   Quindi i decoratori, dal momento che decorano la classe, andranno
			   ovviamente ad agire su ogni istanza di quest'ultima.	
"""





#	ESEMPI DI APPLICAZIONI CONCRETE DI DECORATORI - SINGLETON - DECORAZIONE DI CLASSE
#	L'obiettivo è di implementare il meccanismo che ci permette di realizzare il pattern 'singleton'.

class Wrapper:
	def __init__(self, classe):
		self.classe_decorata = classe
		self.instance = None 					#	Associerò la prima istanza a questa variabile.

	def __call__(self , *args):
		if self.instance == None:
			self.instance = self.classe_decorata(*args)
		return self.instance

	

@Wrapper
class Person:
	def __init__(self, nome, cognome, stipendio):
		self.nome = nome
		self.cognome = cognome
		self.stipendio = stipendio

	def __str__(self):
		return "Nome : {0} - Cognome : {1} - Stipendio : {2} " . format(self.nome, self.cognome, self.stipendio)



lorenzo = Person("Lorenzo" , "Cimini" , 1000)
print(lorenzo)

elisabetta = Person("Elisabetta" , "Giordano" , 2000)
print(elisabetta)

"""
	Nome : Lorenzo - Cognome : Cimini - Stipendio : 1000
	Nome : Lorenzo - Cognome : Cimini - Stipendio : 1000

"""




#	ESEMPI DI APPLICAZIONI CONCRETE DI DECORATORI - PRIVATENESS - DECORAZIONE DI CLASSE
"""	
	L'obiettivo è quello di creare un decoratore che prenda in input una serie di parametri
	privati della classe che vogliamo decorare e renderli realmente tali dal momento che in python i 
	parametri privati sono comunque accessibili.

	Questo meccanismo si realizza attraverso 2 clousure, le quali permetteranno di veicolare all'interno
	del decoratore i parametri che quest'ultimo dovrà rendere effettivamente privati.

"""

def Private(*private_attributes):
	def onDecorator(aClass):
		class onInstance:
			def __init__(self, *args, **kwargs):
				self.classe_decorata = aClass(*args , **kwargs)

			def __getattr__(self, attribute):
				if attribute in private_attributes: raise TypeError("Trying to get private attributes")
				else :return getattr(self.classe_decorata , attribute)

			def __setattr__(self, attribute, value):
				if attribute == 'classe_decorata' : 
					self.__dict__[attribute] = value
				elif attribute in private_attributes: 
					raise TypeError("Trying to set private attributes")
				else : setattr(classe_decorata, attribute, value)

		return onInstance
	return onDecorator


@Private('nome' , 'size')
class Person:
	def __init__(self, nome, cognome, stipendio):
		self.nome = nome
		self.cognome = cognome
		self.stipendio = stipendio

	def size(self):
		return stipendio * 10 

lorenzo = Person("Lorenzo" , "Cimini", 1000)
print(lorenzo.nome)		#	TypeError: Trying to get private attributes
print(lorenzo.size)		#	TypeError: Trying to get private attributes




































