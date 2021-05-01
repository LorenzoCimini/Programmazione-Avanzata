import itertools
"""
	MODULO ITERTOOLS
	Itertool di Python è un modulo che fornisce varie funzioni che lavorano su iteratori per produrre 
	iteratori complessi.
	In altre parole quindi, le funzioni del metodo itertools lavorano sugli iteratori per produrre iteratori
	ancora più complessi.

"""
#	ZIP
#	Prende come input due liste e restituisce un oggetto zip che contiene
#	tutte le tuple costruibili combinando i loro elementi.
#	Attenzione : Crea tuple con gli elementi negli indici presenti in entrambi gli iterable.
#				 Se una lista ha 4 elementi e l'altra 3 allora il risultato del metodo zip 
#				 avrà solo 3 elementi e il 4 della prima lista verrà eliminato.
#				 Nel caso volessimo conservarli tutti allora avremo bisogno del metodo zip_longest()

a = [1,2,3]
b = ['a' , 'b' , 'c']
print(list(zip(a,b)))
#	[(1, 'a'), (2, 'b'), (3, 'c')]

a = a = [1,2,3,4]
b = ['a' , 'b' , 'c']
print(list(itertools.zip_longest(a,b)))
#	[(1, 'a'), (2, 'b'), (3, 'c'), (4, None)]




#	MAP
#	Applica una funzione da un singolo parametro ad ogni elemento dell'iterable alla volta.

print(list(map(len,['abc','bcd'])))
#	[3, 3]

#	Poiché gli iteratori sono iterabili, è possibile comporre zip () e map () per produrre 
#	un iteratore su combinazioni di elementi in più di un iterabile. Ad esempio, quanto segue somma
#	gli elementi corrispondenti di due elenchi:

print(list(map(sum, zip([1, 2, 3], [4, 5, 6]))))
#	[5, 7, 9]


#	ENUMERATE
#	Quando si utilizzano gli iteratori, è necessario tenere traccia del numero di elementi nell'iteratore.
#	Ciò è ottenuto da un metodo integrato chiamato enumerate ().

print(list(enumerate({'lunedi' , 'martedi' , 'mercoledi'})))
#	[(0, 'mercoledi'), (1, 'lunedi'), (2, 'martedi')]


#	COUNT(stard,step)
#	Crea un iteratore che ritorna i valori a partire da start fino all'infinito aumentando di volta 
#	in volta in misura uguale a 'step'

c2=itertools.count(2.5,2.5)
for i in c2:
    if i>25:
        break
    else:
        print (i,end=" ") 
#	Output:2.5 5.0 7.5 10.0 12.5 15.0 17.5 20.0 22.5 25.0



#	CYCLE
#	Crea un iteratore che restituisce elementi dall'iterabile e salva una copia di ciascuno. 
#	Quando l'iterabile è esaurito, restituisce l'elemento dalla copia salvata. Ripete indefinitamente.

lista = [1,2,3]
ciclo = itertools.cycle(lista)

count=0
for i in l2:
    #It will end in infinite loop. So have to define terminating condition.
    if count > 15:
        break
    else:
        print (i,end=" ")
#	Output:1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1
        count+=1

#	PERMUTATIONS























