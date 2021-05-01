if __name__ == '__main__':

### COMPREHENSIONS
#   Sono un meccanismo per definire un insieme.
#   Le abbiamo affrontato mille volte nella matematica del continuo.
#   Sono un modo semplice per descrivere un insieme non elencando ogni singolo elemento ma restituendo una proprieta'
#   Tutti gli x appartenenti a R {tali che x/2 < 1000}
#   Si applica a quasi tutte le strutture dati di phyton come per esempio liste, insiemi, dizionari ecc..

# STRUTTURA DI CREAZIONE DI LISTE
# 	output_list = [output_exp for var in input_list if (var satisfies this condition)]
#
#
# STRUTTURA DI CREAZIONE DI DIZIONARI
#	output_dict = {key:value for (key, value) in iterable if (key, value satisfy this condition)}
#
#
#
#	In particolare possiamo ottenre :
#	new_list = []

#		for i in old_list:
#	    	if filter(i):
#       		new_list.append(expressions(i))
#
#	con :	new_list = [expression(i) for i in old_list if filter(i)]

[x+1 if x >= 120000 else x+5 for x in feet]
#	Creazione lista tramite comprehension - numeri da 1 a 10
[elem for elem in range(1,11)] # 1,2,3,4,5,6,7,8,9,10

#   Creazione set tramite comprehension - numeri positivi da 0 a 20
{elem*2 for elem in range(1,11)} # 2,4,6,8,10,12,14,16,18,20

#   Creazione dizionare tramite comprehension - dizionario composto da n associato a n^2
[elem:elem**2 for elem in range(1,10)] # 1:1 , 2:4 , 3:9 ....

#   Le comprehension possono ridurre gli elementi di un dataset dopo un vincolo
[ elem for elem in range(1,101) if (int(elem**.5))**2 == elem] # selezionare i numeri da 1 a 100 che hanno la radice quadrata perfetta

#   seleziono gli odd numbers da questo insieme di numeri
{x for x in (1,22,31,23,10,10,11,11,-1,34,76,778,10101,5,44) if x%2 != 0}
#   un 11 verrà buttato -> proprietà dei set

#   Possono anche essere usate per selezionare valori multipli
a_dict = {'a' : 1 , 'b' : 2 ,'c' : 3}
{value:key for key, value in a_dict.items()} # Vado ad invertire chiavi e valori

english = ['a' , 'b'] #...
greek = ['alpha' , 'beta'] #...
[(english[i], greek[i]) for i in range(0, len(english))]
#   Vado a creare un set composto da ciascuna lettera sia dell'alfabeto inglese che dell'alfabeto greco

{(x,y) for x in range(3) for y in range(5)} # Creo il prodotto cartesiano in questo range



###  ESEMPIO DI UTILIZZO DELLE COMPREHENSIONS NEL CALCOLO DEI NUMERI PRIMI

# CASO SENZA COMPREHENSIONS - QUESTO E' UN ALGORITMO CLASSICO PER LA RICERCA DEI NUMERI PRIMI
def is_prime(x):
    div = 2
    while div <= math.sqrt(x):
        if x%div == 0 : return False # Qui se vedo che non è primo interrompo subito - la versione funzionale non ha questa feature.
        else: div += 1
    return True

if __name__ = "__main__":
    primes = []
    for i in range(1,50):
        if is_prime(i) : primes.append(i)
    print(primes)

# CASO CON COMPREHENSIONS - PROGRAMMAZIONE FUNZIONALE CON COMPREHENSIONS
def is_prime(x):
    div = [elem for elem in range(2, int(math.sqrt(x))+1) if x%elem == 0 ] # Creo una lista contente i divisori di x
    return len(div) == 0 # Ritorno true se la dimensione della lista è uguale a  0.. altrimenti non è primo e ritorno false

if __name__ = "__main__" :
    print([elem for elem in range(1,50) if is_prime(elem)])

# Ordine le liste attraverso l'algoritmo quicksort che sfrutta le comprehensions.
def quicksort(s):
    if len(s) == 0 : return []
    else :
        # Phyton indenta tutto con regole stringenti e ama andare a capo.. lo \ vuol dire che la riga non è finita.
        return quicksort([x for x in s[1:] if x < s[0]]) +\
         [s[0]] +\
         quicksort([x for x in s[1:] if x >= s[0]])



			




