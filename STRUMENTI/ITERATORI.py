"""
	In python un iteratore e' un oggetto su cui e' possibile iterare, ritorna un elemento per volta
	e implementa lo "iterator protocol", che consiste in due metodi:
		__iter__ -> Definisce le caratteristiche dell'operatore e viene eseguito :
					-	Atto di creazione dell'oggetto iteratore
					-	Atto di reinizializzazione dell'oggetto iteratore

		__next__ -> Definisce la risposta dell'iteratore quando viene richiamato con il metodo next

		StopIteration : Viene chiamato quando l'iteratore non contiene piu' elementi

		Instead of storing the entire range, [0,1,2,..,9], in memory, the generator stores a definition 
		for (i=0; i<10; i+=1) and computes the next value only when needed (AKA lazy-evaluation).

"""

#	Dizionari, liste, tuple e stringhe sono tutti oggetti iterabili, ovvero dei veri e propri 
#	contenitori da cui puoi ottenere l'iteratore tramite il metodo iter() e il valore successivo
#	applicando next() all'iteratore.

lista = [1,2,3]
iteratore = iter(lista)

print(next(iteratore))

#	Possiamo utlizzare anche, per esempio, il ciclo for per iterare su tutti gli elementi del contenitore
#	lista creato con il metodo iter()

for item in lista:			 #	In questo caso quindi il metodo next() e' implicito.
	print(item)

"""
Per creare un oggetto iteratore dobbiamo implementare i due metodi citati inizialmente:
	->  __iter__() 
	->  __next__() 
	-> Costruttore della classe __init__(). 
"""

class Fib:
	def __init__(self,max):
#		 Numero massimo al quale mi voglio fermare a iterare
		self.max = max

	def __iter__(self):
		self.a = 0
		self.b = 1
		return self

	def __next__(self):
		if self.b > self.max : raise StopIteration
		else:
			self.a , self.b = self.b , self.a + self.b
			return self.a

fib = Fib(1000)
iteratore = iter(fib)
for i in iteratore:
		print(i)

print("******************\n\n\n")

"""
	Proviamo adesso a risolvere il problema lasciato irrisolto della lettura dei file.
	Nell'esercizio riguardante l'applicazione di regole per la trasformazione di una parola inglese
	con il suo plurale rimaneva il problema che il generatore dovesse riaprire il file ogni volta che 
	iteravamo.
	Proviamo quindi a costruire un iteratore che risolva questo problema 
"""
import re

class Iteratore:

	def __init__(self):
		"""
			Questa operazione verrà fatta all'inizializzazione dell'oggetto Iteratore()
			e consiste nell'inizializzare la cache associata alla nuova instanza e a definire
			il path del file con le regole di formattazione
		"""
		self.pattern_file = open('/Users/lorenzocimini/Desktop/Università/Programmazione/ProgrammazioneAvanzata/rules.txt')
		self.cache = []
	
	def __iter__(self):
		"""
			Verrà chiamato ogni volta che l'iteratore verrà reinizializzato.
			Quindi ogni volta che cominceremo a cercare delle regole nell'iteratore.
		"""
		self.cache_index = 0 
		return self
	
	def __next__(self):
		"""
			Verrà chiamato ogni volta che viene chiamato il metodo next() sull'iteratore esplicitamente 
			o, implicitamente, dal metodo for.
			Provedderà ad aggiornare il numero delle volte che abbiamo iterato e a controllare che
			le regole associate all'index in cui ci troviamo siano già state prodotte e, in tal caso,
			ritornare le regole associate alla posizione uguale all'index-1 nella cache.
		"""
		self.cache_index += 1 
		
		if len(self.cache) >= self.cache_index:  
			return self.cache[self.cache_index-1]

		elif self.pattern_file.closed: raise StopIteration 
		
		else :
			line = self.pattern_file.readline()
			if not line : 
				self.pattern_file.close()
				raise StopIteration
			else:
				pattern, search, replace = line.split(None,3) 
				funcs = clousure(pattern , search , replace)
				self.cache.append(funcs)
				return funcs

def clousure(cosa_cercare, dove_cercare, sostituisci):
	"""
		Classica clousure che crea dinamicamente le regole
	"""

	def search(word):
		return re.search(cosa_cercare, word)
	def replace(word):
		return re.sub(cosa_cercare, sostituisci, word)
	return (search, replace)

plurale = Iteratore()
iteratore = iter(plurale)

def metodo(parola):
	"""
		Questo metodo prende come input una lista e restituisce la parola 
		trasformata applicando, dove possibile, le regole contenute nel file
		rules.txt
	"""
	for search, replace in iteratore:
		if search(parola):
			return replace(parola)

#	MAIN()
parole = ['ciao1' , 'trapano2' , 'paddle2' , 'paddle3' , 'paddle1']
for parola in parole:
	print(metodo(parola))


























