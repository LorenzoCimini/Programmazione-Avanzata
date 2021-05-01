""" https://diveintopython3.net/generators.html """


# Partiamo dal concetto di funzioni annidate

def outerFunction(text):
	def innerFunction():
		print(text)
	innerFunction()


outerFunction("Hello")

""" 
	In questa semplice funzione annidata stiamo creando una funzione annidata rispetto a outerFunction()
	Questa funzione - innerFunction() - al suo interno utilizza una variabile che non è propria bensì
	appartiene allo scope dell'outerFunction()
	Infine quindi, andiamo semplicemente a chiamare l'esecuzione della innerFunction() all'interno dell'outerFunction().

"""

# Un altro esempio  di funzioni annidate - non funziona se ci sono duplicati all'interno della lista -

def pop(list):
	def get_last_item(my_list):
		return my_list[len(list) - 1]

	list.remove(get_last_item(list))
	return list 

a = [ 1 , 2 , 3 , 4 , 5 ]
print(pop(a)) #  [ 1 , 2 , 3 , 4 ]
print(pop(a)) #  [ 1 , 2 , 3 ]

"""
	
	Adesso, per convertire queste nested functions in clousures devo fare le seguenti cose :
		Dobbiamo avere una funzione contenuta in un altra
		La funzione contenuta deve riferirsi ad un valore definito nella funzione nella quale è contenuta 
		La funzione che contiene la nested function deve ritornare la nested function - senza ()
	Quindi avremo che il risultato dell'innerFunction dipenderà dal valore di una variabile dichiarata
	al suo esterno.
	Le clousures hanno la seguente importante proprietà, ovvero quella che l'oggetto associato alla funzione clousure
	ricorderà il valore del suo ritorno anche se le funzioni non saranno più presenti in memoria.

"""

def outerFunction(text):
	def innerFunction():
		print(text)
	return innerFunction

a = outerFunction("Hello") # qui quindi sarà associata la innerFunction()
print(a()) # Hello \n None 
a() # Hello

"""
	Qui, anche se eliminassi dopo la prima istruzione del main() la outerFunction() il risultato associato ad a
	rimarrebbe sempre, mentre se richiamassi nuovamente la funzione riceverei un errore perchè essa non esiste più.

"""

# Altro esempio

def nth_power(exponent):
	def pow_of(base):
		return pow(base,exponent)
	return pow_of

square = nth_power(2) # qui otterrò la funzione pow_of con l'esponente 2
print(square(2)) # adesso non faccio altro che passare alla funzione potenza la base e essa ritornerà con la potenza.

cube = nth_power(3)
print(cube(3)) # 27

"""

	Quindi, conclusione :
		Le clousures vengono utilizzate in molti contesti come per esempio i decoratori ma, allo stesso tempo, 
		sono molto utilizzate per evitare di scrivere classi che dovrebbero contenere ( di solito ) esclusivamente un metodo.
		In questo modo, attraverso le clousures possiamo non scomodare le classi e ottenere lo stesso risultato desiderato.

"""


"""
************* ESERCIZIO **************
If you grew up in an English-speaking country or learned English in a formal school setting, you’re probably familiar with the basic rules:
	If a word ends in S, X, or Z, add ES. Bass becomes basses, fax becomes faxes, and waltz becomes waltzes.
	If a word ends in a noisy H, add ES; if it ends in a silent H, just add S. What’s a noisy H? One that gets combined with other letters to make a sound that you can hear. So coach becomes coaches and rash becomes rashes, because you can hear the CH and SH sounds when you say them. But cheetah becomes cheetahs, because the H is silent.
	If a word ends in Y that sounds like I, change the Y to IES; if the Y is combined with a vowel to sound like something else, just add S. So vacancy becomes vacancies, but day becomes days.
	If all else fails, just add S and hope for the best.
	Da queste regole derivo i seguenti pattern :
"""

patterns = (\

    ('[sxz]$',           '$',  'es'),
    ('[^aeioudgkprt]h$', '$',  'es'),
    ('(qu|[^aeiou])y$',  'y$', 'ies'),
    ('$',                '$',  's')                                 
  )

"""
	Il mio obiettivo quindi sarà quello di applicare questa serie di regole alle mie parole in modo tale da 
	trasformarle da parole singolari e plurali.

	Ho quindi i miei pattern che, per il momento, memorizzo nel sorgente.
	Non ho altro che un insieme di tuple di 3 elementi :
		Cosa sto cercando nella stringa
		Dove lo sto cercando
		Se lo trovo con cosa devo sostuire quella parte della stringa 


	RE - Regular Expression Operations
	Una espressione regolare è una speciale sequenza di caratteri che ci aiuta a matchare o trovare altre stringhe 
	/insiemi di stringhe, usando una sintassi specializzata che contiene un pattern,

	. 	-> rappresenta qualsiasi elemento tranne una nota a capo
	^ 	-> inizio di una stringa
	$ 	-> fine di una stringa 
	* e + -> 0 ( o 1 ) ripetizioni della precedente regular expression
	? 	-> Presenza o meno del pattern che lo precede
	[] 	-> Insieme di caratteri 
	() 	-> Gruppo di matching 

	- match()	Determina se la RE corrisponde all'inizio della stringa.
	- search()	ricerca all'interno di una stringa, trovando tutte le posizioni corrispondenti alla RE.
	- findall()	Trova tutte le sottostringhe corrispondenti alla RE, e le restituisce in una lista.
	- finditer()	Trova tutte le sottostringhe corrispondenti alla RE, e le restituisce in un iteratore.


"""

"""
	Partiamo dal dire che ovviamente non abbiamo bisogno di scrivere una funzione per ogni match and apply
	perchè non le chiameremo mai direttamente.

	def match_sxz(noun):
    return re.search('[sxz]$', noun)

	def apply_sxz(noun):
    return re.sub('$', 'es', noun)

	def match_h(noun):
    return re.search('[^aeioudgkprt]h$', noun)

	def apply_h(noun):
    return re.sub('$', 'es', noun)

    .....
    .....

    rules = ((match_sxz, apply_sxz),              
         (match_h, apply_h),
         (match_y, apply_y),
         (match_default, apply_default)
         )


     Una cosa del genere quindi è da evitare sopratutto perchè, nel caso le regole fossero tantissime, 
     saremmo obbligati a scrivere tantissime funzioni.

     Cominciamo quindi a scrivere una clousure che costruirà dinamicamente le mie coppie di funzioni che verranno utilizzate
     rispettivamente per cercare e sostituire le parti di parola che vogliamo convertire in plurale.
"""

def build_match_and_apply_functions( pattern , search , replace ):
	def matches_rule(word):
		return re.search(pattern, word)
	def apply_rule(word):
		return re.sub( search , replace , word )
	return (matches_rule , apply_rule)


def plural(noun):
	rules = [ build_match_and_apply_functions(pattern , search , replace) for (pattern , search , replace) in patterns]
	for matches_rule, apply_rule in rules: 
		if matches_rule(noun):
			return apply_rule(noun)



if __name__ == '__main__': 
	print(plural("sax"))

"""

	Quindi creeremo una lista di coppie formate da < funzione che cerca , funzione che sostituisce se si è trovato >
	dove l'ultima funzione è una funzione che matcha sempre, ovvero quella associata al pattern finale :
		('$',                '$',  's')        
	In questo caso la funzione vedrà se la parola ha una fine - tutte le stringhe hanno una fine - e, perciò,
	in questo caso verrà sempre applicata la funzione associata a questo pattern, che opera aggiungendo una s alla fine della parola.

	Come possiamo vedere, un difetto di questo approccio consiste nel fatto che per ogni parola dobbiamo ogni volta scorrere tutta la lista di regole
	finquando troviamo la regola che matcha alla nostra parola.
	Questo può essere computazionalmente costoso e perciò verrà risolto con i generatori che vedremo in

"""

# ********** ULTERIORE PASSAGGIO **************
"""
	Ovviamente in questo caso la best practise è dividere il codice sorgente dall'insieme di regole che che devono essere
	applicate alle parole
	Per fare questo cominciamo a salvare le regole in un file esterno :

	sxz]$               $    es
	[^aeioudgkprt]h$     $    es
	[^aeiou]y$          y$    ies
	$                    $    s

	plural-rules.txt

	Andremo a modificare il sorgente in questo modo quindi :

"""

def plural(noun):
	rules = []
	with open('plural-rules.txt', encoding='utf-8') as pattern_file:
	for line in pattern_file:
		pattern, search, replace = line.split(None, 3) # splitta ogni spazio bianco per 3 volte e poi lascia il resto da solo
		rules.append(build_match_and_apply_functions(pattern , search , replace))

	for matches_rule, apply_rule in rules: 
		if matches_rule(noun):
			return apply_rule(noun)



# ESEMPIO FUNZIONANTE 
# Questo programma va a sostituire materialmente le parole con quelle corrette.

import re

rules = [\
	
	('[1]$' , '$' , '_uno' ),
	('[2]$' , '$' , '_due' ),
	('[3]$' , '$' , '_tre' )
]

def clousure( regola , dove_cercare , con_cosa_sostituire ):
	def cerca(word):
		return re.search(regola , word)
	def sostituisci(word):
		return re.sub(regola , con_cosa_sostituire ,  word) # re.sub( cosa sostuire dentro la stringa , con cosa sostituirlo , parole dove fare l'operazione )
	return (cerca , sostituisci)

def convert_number_in_words(words):
	i = 0

	for word in words:
		words[i] = controlla_regole(word)
		i = i + 1

	return words

def controlla_regole(word):
	lista_di_regole = [ clousure(regola , dove_cercare , cosa_sostituire) for regola , dove_cercare , cosa_sostituire in rules]

	for regola_cerca , regola_applica in lista_di_regole:
		if regola_cerca(word) : return regola_applica(word)



if __name__ == '__main__':
	
	list_of_words = [ \
		"ciao1",
		"ciao2",
		"ciao3",
		"lupo1",
		"lupo2",
		"lupo3"
	]

	list_of_words = convert_number_in_words(list_of_words)

	for word in list_of_words:
		print (word)

	















