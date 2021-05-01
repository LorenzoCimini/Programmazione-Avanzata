import math

if __name__ == '__main__':

	#	map( <funzione> , <lista> )

	#	Essa applica ad ogni elemento della lista la nostra funzione.
	print ( map( math.sqrt, [ x for x in range(1,20)] ) )



	#	filter ( <funzione> , <Lista> )
	#	
	#	Prende dalla lista esclusivamente i valori che verificano la funzione.

	def odd(x):
		return x%2 != 0

	print ( filter ( odd , [ x for x in range(1,10) ] ) ) 

	

	#	reduce ( <funzione> , <lista> )
	#
	#	Prende la funzione e la applica a tutti gli elementi della lista ritornando un solo elemento risultato della funzione

	def moltiplicazione(x,y):
		return x*y

	print ( reduce ( moltiplicazione , [ elem for elem in range(1,10) ] ) )


	print("**********")

	

	#	IF FUNZIONALE - IF CORTO CIRCUITATO
	#	Qui, andiamo a sostituire l'if tradizionale con l'if cortocircuitato.
	#	Quest'ultimo controllera' la prima condizione e, se vera, controllera' la seconda ( che e' sempre vera )
	#	Altrimenti passera' direttamente al controllo dell'OR.

	def controlla_se_pari(number):
		return (number%2 == 0 and True) or False

	lista = list ( filter ( controlla_se_pari , [x for x in range(1,20 ) ] ) )
	print(lista)


	#	LAMBDA
	#	E' la keyword attraverso la quale possiamo creare funzioni anonime.
	#	Una funzione anonima e' una funzione che ci permette di eseguire un blocco di codice come se esso fosse
	#	una funziona, ma senza nome.
	#	Posso definirle ovunque.

	print ( reduce ( lambda x,y : x * y , [ x for x in range(1,10) ] ) ) # Esempio di reduce con la moltiplicazione fatto prima

	addizione = lambda x,y : x + y
	print(addizione(10,20))

	# 	Mentre per quanto riguarda l'if nella programmazione funzionale possa essere una forzatura che in molte situazioni 
	# 	è inutile, quello che seguo invece è trucco molto utile per la semplificazione del codice.
	# 	Mentre una sequenza in un linguaggio iterativo è un insieme di statement separati dal ; e verrà eseguito il primo statement, 
	#	il secondo e cosi via, nel caso della programmazione funzionale non avremo statament bensì funzioni
	#	Avremo quindi la possibilità di creare una sequenza nel seguente modo:
	sequenza = lambda f:f()  # andrà semplicemente a eseguire la funzione
	map ( sequenza , [f1,f2,f3])
	#	è molto utile perche spesso e volentieri abbiamo una serie di operazioni che o non vengono applicate oppure vengono eseguite con diversi ordini
	#	e invece di avere un lungo codice ( spesso incomprensibile ) quello che succede è meglio organizzare in batch di chiamate di funzione e poi fare una chiamata di questo tipo.