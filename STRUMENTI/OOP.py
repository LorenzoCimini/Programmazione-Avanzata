"""
	In python TUTTO è un oggetto dal momento che è Object Based 
	CARATTERISTICHE PECULIARI DELL'OOP IN PYTHON :
		-	Come sappiamo, una classe rappresenta un template dal 
			quale noi andremo ad instanziare oggetti ( appartenenti a quella classe) che avranno, proprio
			per questo motivo, la stessa forma.
			Questa caratteristica viene meno in python dal momento che, dinamicamente, abbiamo la possibilita' di
			aggiungere metodi/campi ad un oggetto in qualsiasi momento in modo tale che esso risultera', alla fine
			dell'appena citata operazione, un oggetto difforme da quello del template ( classe ) di partenza.

		-	Il metodo costruttore, in ogni classe, è il metodo __init__ e deve essere unico.
			( per esempio in Java questo non succede dal momento che il costruttore e' il metodo che prende il
			  nome della classe e può essere fatto un overloading di quest'ultimo ).
			Per bypassare questo 'limite' potrei costruire un costruttore banale - quindi senza nessun parametro oltre al self -
			per poi demandare il compito di costruire l'oggetto ad un altro metodo ma, in questo caso, 
			l'oggetto potrebbe essere costruito e, da qui, chiamare metodi della classe che potrebbero generare errori.

		-	Il this ( riferimento all'istanza attuale ) deve essere esplicitato in ogni metodo della classe.

		-	Il metodo costruttore può essere anche un metodo banale - quindi senza nessun parametro oltre al self -
			per poi demandare il compito di costruire l'oggetto ad un altro metodo ma, in questo caso, 
			l'oggetto potrebbe essere costruito e, da qui, chiamare metodi della classe che potrebbero generare errori.

		- 	Per configurare campi della classe come privati ( accessibili solo da metodi della classe ) si
			può utilizzare il simbolo '_' prima del nome del campo (_width) ma, anche questo limite e' facilmente
			bypassabile rendendo di fatto python un linguaggio molto atipico per quanto riguarda l'OOP.

"""
#	Esempio di classe in Python.
	class rectangle:
		def __init__(self, width, height): 
			self._width = width
			self._height = height
		
		def calculate_area(self):
			return self._width*self._height
		def calculate_perimeter(self):
			return 2*(self._height + self._width)
		def __str__(self): # E' il sinonimo di toString() in java.
			return "I'm a rectangle! My sides are : {0} , {1} \n My area is {2}}" . format(self._width , self._height , self.calculate_area())

"""

	CARATTERISTICHE PECULIARI DELL'EREDITARIETA' IN PYTHON

		-	L'ereditarieta' quindi, se non per il riutilizzo del codice, diventa fondamentalmente inutile dal momento che in python
			una classe rappresenta esclusivamente un punto di partenza per le sue istanze ( posso modificarle quando voglio e come voglio )
			Vengono utilizzate quindi solo per il raggruppamento e il riuso di funzionalità comuni di più oggetti.

		-	Infatti, il DUCK TYPING, ci dice che in Python, al contrario di altri linguaggi dove per capire se un oggetto può fare una cosa
			si osserva il suo tipo - classe da cui deriva -, quello che dobbiamo vedere sono i metodi dell'oggetto.
			Di conseguenza, diremo che un oggetto è una figura geometrica non perchè deriva dalla classe FiguraGeometrica bensi' perchè
			ha i metodi area() e perimetro() - è un esempio -.

		-	Di conseguenza anche il polimorfismo perde i propri punti di forza.


"""

class C:
	def __init__(self):
		self.class_attribute = "a value"
	def __str__(self): 					#	E' l'equivalente del metodo toString() in Java.
		return self.class_attribute

#	Come posso aggiungere dinamicamente campi ad una classe/istanza di una classe?

prima_figura = C()
prima_figura.altro_campo = 10			#	Qui ho appena aggiunto un ulteriore campo all'istanza prima_figura - solo a questa istanza -
C.altro_campo = 'lato'					#	Qui invece ho aggiunto un nuovo campo alla classe e quindi tutti gli oggetti di quella classe lo avranno

"""
	__dict__

	Ogni oggetto ( quindi qualsiasi cosa dal momento che è object based ) in python possiede un dizionario, accedibile tramite il campo __dict__ ,
	il quale contiene Tutti gli attributi di un oggetto nel formato chiave:valore.
	Questo campo può anche essere utilizzato per andare a modificare le informazioni della singola istanza in un altro modo rispetto a quello
	appena visto oppure semplicemente per vedere quali sono gli attributi disponibili dell'oggetto in questione.

"""

c1 = C()
c1.__dict__ 							#	Con print(c1) otterrei {'class_attribute' : 'a value'}
c1.__dict__['class_attribute'] = 'ciao'	#	Con print(c1) adesso otterrei {'class_attribute' : 'ciao'}

#	La cosa appena vista può succedere anche con i metodi nel seguente modo :

def introspet(self):
	saluto = ''

	for k,v in self.__dict__.items():	#	Sto scorrendo tutti i campi presenti nel dizionario dell'istanza attuale prendendo nome_del_campo e valore da essi
		saluto += k + " : " + v + " : "
	return saluto

C.__str__ = introspect

"""

	DESCRITTORI 

	Mentre un attributo e' solo un valore mutabile, un descrittore consente di eseguire codice arbitrario durante la lettura o 
	l'impostazione (o l'eliminazione) di un valore. 
	Un altro uso potrebbe essere il rifiuto di accettare un nuovo valore generando un'eccezione __set__, rendendo effettivamente "l'attributo" di sola lettura.
	Ora ci sono altri modi, probabilmente migliori, per ottenere lo stesso effetto in Python (ad esempio se Celsius
	fosse una property, che è lo stesso meccanismo di base ma colloca tutta la sorgente all'interno della classe

"""

class Celsius:

    def __get__(self, instance, cls=None):
        return 5 * (instance.fahrenheit - 32) / 9

    def __set__(self, instance, value):
        instance.fahrenheit = 32 + 9 * value / 

    def __delete__(self,instance):
		print("{0}.__delete__({1} , {2})" . format(self,obj))


class Temperature:
	"""	Questa è una classe con un singolo descrittore ma ne possono essere implementati diversi """

    celsius = Celsius()

    def __init__(self, initial_f):
        self.fahrenheit = initial_f


t = Temperature(212)
print(t.celsius)		#	100.0
t.celsius = 			
print(t.fahrenheit)		#	32.0




"""
	I metodi speciali sono dei metodi standard di ogni oggetto che possono essere tranquillamente essere
	riscritti dallo sviluppatore.
	Abbiamo già visto __init__ , __str__ , __get__ , __set__ e __delete__
	Ma vediamone altri :
		-	__len__ -> Può essere implementata per rappresentare 'la grandezza del nostro oggetto '
"""

class Gara():
	
	def __init__(self, giorno_inizio , giorno_fine):
		pass
	
	def __len__(self):
		return self.giorno_fine - self.giorno_inizio 

	def __gt__(self, seconda_gara_da_confrontare):				# Grather than '>'
		return len(self) > len(seconda_gara_da_confrontare)

	def __lt__(self , secondo_oggetto):							# Less than '<'
		...

	def __eq__(self , secondo_oggetto):							# Equal  '='
		...	

	def __le__(self , secondo_oggetto):							# less equal '<='
		...

	def __ge__(self , secondo_oggetto):							# Grather egual '>='
		...

#	Tutti questi metodi saranno accessibili tramite __dict__ e tramite i simboli associati all'operazione.
#	Gara1 > Gara2 oppure Gara1.__gt__(Gara2)

"""
	SUPER
 	La funzione super  è indispensabile quando abbiamo a che fare con classi che ereditano il loro comportamento da altre classi.
	Spesso una classe figlia estende il comportamento di un metodo della classe madre per cui è comodo poter accedere al metodo originario.
	Il primo parametro di super è il nome della classe a partire dalla quale vogliamo risalire nella gerarchia.
	Il secondo parametro è un’istanza della suddetta classe.

"""

class Base():
	def __init__(self,colore):
		self.colore = colore


class Estesa(Base):
	def __init__(self , colore , misura ):
		super(Estesa, self).__init__(colore)
		self.misura = misura

"""

	Attraverso il campo __slots__ all'interno della definizione della nostra classe ci permette di dichiarare
	esplicitamente quali attributi mi aspetto che ogni istanza di quella classe abbia con i seguenti risultati :
		-	Accesso agli attributi più veloce
		-	Spazio di memoria risparmiato
"""

class Mylist2(list):
	__slots__ = [] 
					# 	Qui non posso aggiungere nessun'altro campo diverso da quelli contenuti nella 
					#	definizione della classe
	
class Mylist3(self):
	__slots__ = ['color'] 
					# 	Qui non posso aggiungere nessun'altro campo diverso da color oltre a quelli contenuti 
					#	nella definizione della classe




















