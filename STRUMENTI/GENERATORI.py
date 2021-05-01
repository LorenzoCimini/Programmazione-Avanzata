#	GENERATORI
#	I generatori sono delle funzioni che generano un solo valore alla volta.
#	Essi possiedono uno stato - che puo' essere utilizzato per far ricominciare il generatore dal punto 
#	in cui l'avevamo fermato -
#	Per fare tutto cio', il nostro generatore utilizzera' la keyword YIELD che :
#		- blocchera' l'esecuzione del generatore
#		- memorizzera' in memoria lo stato delle variabili elencate nello yield.
#	saremo noi, successivamente, a far ripartire l'esecuzione del generatore con il metodo next().
#	La funzione next() riesuma la computazione dallo yield e continua fino a quando
#	non ne raggiunge un altro o la funzione finisce.
#	Di fatto quindi lo Yield andra' a sostuire il return classico di una funzione.
#	
#
#	I generatori quindi, per questa loro caratteristica, sono adatti per elaborare liste di grandi dimensioni con 
#	infiniti valori.
#	Attenzione : Quando il generatore esaurisce gli elementi dell'iteratore, se lo richiamo ulteriormente mostra un errore


def generatore():
	yield "A" 
	yield "B"
	yield "C"


def generatore_2():					# Possono essere trattati come un oggetto iterable ( una lista )
	for i in range (1,10):
		yield i

# ESEMPIO SERIE DI FIBONACCI
def generatore_fibo():
	(a,b) = 0,1
	while True:
		yield b
		(a,b) = (b,b+a)


if __name__ == '__main__':
	generatore = generatore()
	print(next(generatore))
	print(next(generatore))
	print(next(generatore))

	fibonacci = generatore_fibo()

	for i in range(1,10):
		print(next(fibonacci))

#	I generatori sono un tipo di iterabile, come le liste e le tuple. Ma a differenza delle liste, 
#	i generatori non permettono l'indicizzazione con indici arbitrari, ma possono comunque essere iterati 
#	attraverso i cicli for.

#	Perciò i generatori, al contrario delle tradizionali funzioni, mi permettono di generare un valore alla volta
#	e, eventualmente, processarlo invece di dover aspettare che la funzione generi tutti i valori e a quel punto
#	controllarli uno alla volta.
#	Mi può essere molto ultile perchè, potrei evitare di caricare tutti i valori ( esempio delle regole di inglese )

#	Invece di costruire un vettore contenente tutti i valori e restituirli in una volta,
#	un generatore fornisce i valori uno alla volta, il che richiede meno memoria e permette così
#	al chiamante di iniziare a elaborare i primi valori immediatamente.
#	In breve, un generatore assomiglia a una funzione ma si comporta come un iteratore.



