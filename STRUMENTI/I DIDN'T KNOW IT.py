"""
	Sommando due liste vado a concatenare i loro elementi 
"""

print ( [1,2,3] + [4,5,6] )
#	[1,2,3,4,5,6]
#	PS : Questa cosa è anche ottenibile utilizzando itertools.chain(<lista1> , <lista2>)




"""
	YIELD FROM 
	E' una nuova feature introdotta con python 3.3.
	Ci permette di rendere generatori delle liste oppure altri generatori
"""

def generator():
    for i in range(10):
        yield i
    for j in range(10, 20):
        yield j

# DIVENTA :

def generator1():
	for i in range(10):
		yield i

def generator2():
	for y in range(10,20):
		yield y

def main_generator():
	yield from generator1()
	yield from generator2()

for i in main_generator():
	print(i)

#	0,1,2,3,4,5,....,19





#	GENERATORE INFINITO CON YIELD FROM

def generatore_infinito_classico():
	n = 0
	while True:
		yield n 
		n += 1

def generatore_infinito_with_yieldfrom( n = 0 ):	# Parametro di default che sovrascrivo nella chiamata riga 58
	yield n 
	yield from (generatore_infinito(n+1))




#	YIELDARE DA UNA COMPREHENSION

def generatore():
	yield from [ x for x in range(10)]



"""	
	*args 

	args ci permette di passare potenzialmente un numero illimitato e variabile di parametri alla 
	nostra funzione, args infatti è l'abbreviazione di arguments.
	I parametri vengono passati come una tupla e in questo caso il simbolo * viene definito operatore 
	di unpacking proprio perché "spacchetta" tutte le variabili che vengono passate alla funzione.

"""

def moltiplica(*numeri_da_moltiplicare):
    risultato = 1
    for numero in numeri_da_moltiplicare:
        risultato *= numero
    return risultato

print(moltiplica(2, 4, 13, 10, 12, 33))
print(moltiplica(3, 5))
print(moltiplica(10, 14, 2))


"""
	**kwargs

	**kwargs invece sta per keyword arguments, è molto simile ad *args, con la differenza che i parametri 
	non vengono raggruppati in una tupla, ma in un dizionario contenente tutti i parametri passati 
	con nome chiave 

"""

def info_pizza(**pizza):
    for key, value in pizza.items():
        print("{0} = {1}".format(key, value))

info_pizza(nome="margherita", prezzo=5, ingredienti=["pomodoro", "mozzarella"])





















