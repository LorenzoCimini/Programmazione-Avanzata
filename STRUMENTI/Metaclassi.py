"""
	METACLASSI
	Il termine metaprogrammazione si riferisce alla possibilità per un programma di conoscere o 
	manipolare se stesso. Python supporta una forma di metaprogrammazione per classi chiamate metaclassi.

	Note :
      - Tutto il codice relativo alla metaclasse verrà eseguito nel momento della creazione della classe e non runtime, quindi
      non mentre verranno create istanze della classe.

      - Nei decoratori dobbiamo fare il wrapping della classe ( il nome della classe cambierà quindi - prenderà 
      quello della classe wrapper) questo non accade nel caso delle metaclassi - quindi non c'è questo 
      rebinding del nome della classe -

	In Python 3, tutte le classi sono classi di nuovo stile. Pertanto, in Python 3 è ragionevole fare 
	riferimento al tipo di un oggetto e alla sua classe in modo intercambiabile.
	Prima di Python 3 invece, ogni istanza di una classe veniva implementata attraverso un singolo
	built-in type chiamato 'instance'. ( Di conseguenza type(var) erà sempre 'instance' )

"""

class Foo:
	pass

x = Foo()
print(x.__class__)	#	<class '__main__.Foo'>
print(type(x))		#	<class '__main__.Foo'>

#	Ma quale è il tipo della classe Foo()

print(type(Foo)) 	#	<class '__main__.Foo'>

"""
	Il tipo di ogni classe di python 3 è 'type'.
	Type è una metaclasse, della quale quindi, le classi sono istanze. 
	Perciò, proprio come un oggetto ordinario è un'istanza di una classe, qualsiasi 'nuova classe' 
	in Python ( qualsiasi classe in Python 3 ) è un'istanza del tipo metaclasse.

	E' possibile anche chiamare la funzione type() con 3 argomenti :
	-	<name>	: Specifica il nome della classe
	-	<bases>	: Specifica la tupla di classi base dalle quali la classe eredità ( le superclassi )
	-	<dct>	: Specifica il namespace dictionary contenente le definizioni per il corpo della classe.
				  che diventerà l'attributo __dict__ della classe ( gli attributi che la formano ).

	In altre parole, andando a chiamare la funzione type() in questo modo, andremo a creare dinamicamente
	una nuova classe.
"""

class = type(classname, superclasses, attributedict)


"""
	Consideriamo adesso la procedura classica di creazione di una classe :

	class Foo:
		pass

	f = Foo()

	Quando l'interprete incontra l'espressione Foo(), vengono eseguite le seguenti operazioni :
	
		-	Viene chiamato il metodo __call __ () della classe genitore di Foo. 
			Poiché Foo è una classe standard di nuovo stile, la sua classe genitore è la metaclasse 
			'type', quindi viene invocato il metodo __call __ () di type.

		-	Il metodo __call __ () a sua volta richiama quanto segue: 
			-	__new__() 	: 	Metodo che crea le istanze della classe 
			-	__init__()	:	Crea istanza della classe quando l'oggetto type è chiamato.

	Se Foo non definisce __new __ () e __init __ (), essi verranno ereditati dai parenti di Foo. 
	Ma se Foo definisce questi metodi, essi fanno l'override di quelli del parent, il che consente un 
	comportamento personalizzato durante l'istanza di Foo.

	Supponiamo quindi che vogliamo customizzare il comportamento di instanziazione di quando viene creata
	una classe come Foo.
	Seguendo il ragionamento appena fatto, basterà sovrascrivere il metodo __new__() della classe dalla
	quale Foo() eredità, ovvero type.
	Ma, se provassimo a modificare i metodo della classe 'type' otterremo il seguente errore :
					
					TypeError: can't set attributes of built-in/extension type 'type'
	
	Python quindi non permette di riassegnare il metodo __new__ della metaclasse type.

	Ma allora cosa possiamo davvero fare per andare a personalizzare l'istanziazione di una classe?
	Una possibile soluzione è quella di una metaclasse personalizzata e quindi essenzialmente, 
	invece di perdere tempo con la metaclasse type, possiamo definirci la nostra metaclasse, la quale
	ovviamente continuerà ad ereditare da type.

"""

#	DEFINIZIONE DI UNA METACLASSE
#	La definizione 'class Meta(type):' specifica che Meta deriva dal type. 
#	Poiché type è una metaclasse, anche Meta diventa una metaclasse.

class Meta(type):
	def __new__(cls, name, bases, dct):
		x = super().__new__(cls, name, bases, dct)
        x.attr = 100
        return x

"""
	Notare che un metodo personalizzato __new __ () è stato definito per Meta. 
	Questo non è stato possibile farlo direttamente alla metaclasse di tipo. 
	Il metodo __new __ () esegue le seguenti operazioni:

	-	Delega, tramite super () al metodo __new __ () della metaclasse genitore (type), il compito di 
		creare effettivamente una nuova classe. 
	-	Assegna l'attributo personalizzato 'attr' alla classe, con un valore di 100 

	-	Restituisce la classe appena creata


	Ora, dall'altro lato andremo a definire una nuova classe Foo e specificheremo che la sua metaclasse 
	è la metaclasse personalizzata Meta, piuttosto che il tipo di metaclasse standard.
	( INFATTI QUANDO CREIAMO UNA CLASSE, CHE ESSA EREDITA' DA TYPE E' IMPLICITO )
"""

class Foo(metaclass=Meta):
     pass

print(Foo.attr) 	#	100

"""

	QUINDI : ALLO STESSO MODO DELLE CLASSI, LE QUALI SONO DEI TEMPLATE PER LA CREAZIONE DI OGGETTI,
			 UNA METACLASSE RAPPRESENTA UN TEMPLATE PER LA CREAZIONE DI CLASSI.

	Ovviamente questo meccansimo può essere realizzato attraverso i decoratori e l'ereditarietà ( i quali 
	sono più semplici ) e perciò, ci sono pareri discordanti riguarda l'utilità di questo meccansimo.

	Note :
			- Gli attributi delle metaclassi vengono ereditati, come appena visto, dalle classi ma non
			  dalle istanze delle classi.

			- La dichiarazione di una eventuale metaclasse è ereditata anche dalle sottoclassi.

"""

class MetaOne(type):
    def __new__(meta, classname, supers, classdict):
        print("In MetaOne.new:" , classname)
        return type.__new__(meta, classname, supers,classdict)

    def toast(self):
        print('toast')

class Super(metaclass=MetaOne):
    def spam(self):
        print('spam')

class C(Super):
    def eggs(self):
        print('eggs')

X = C()
#	In MetaOne.new: Super
#	In MetaOne.new: C

X.eggs () 
#	eggs

X.spam()
#	spam

X.toast()
#	Error

"""
	Qui ricevo un errore perchè l'oggetto C non ha l'attributo 'toast' dal momento che le classi
	ereditano dalle superclassi ma non dalle metaclassi.
	Avremo quindi che nemmeno super avrà a disposizione il metodo 'toast' della metaclass 'MetaOne'.
	In definitiva perciò, il metodo 'toast' potrà essere utilizzato esclusivamente all'interno
	della metaclasse o, in alternativa, da una che la estenderà.
"""

#	ESERCIZIO METACLASSI
#	Il nostro obiettivo è quello di inserire all'interno di una classe ulteriori metodi rispetto
#	a quelli contenuti nella definizione classica di quest'ultima.

def eggsfunc(obj): return "Aggiunto eggfunc"
def hamfunc(obj,value): return "Aggiunto hamfunc"

class Extender(type):
	def __new__(meta, classname, supers, classdict):
		classdict['eggs'] = eggfunc
		classdict['ham'] = hamfunc 
		return type.__new__(meta, classname, supers, classdict)

class Client1(metaclass= Extender):
	def __init__(self, value):
		self.value = 10

	def spam(self):
		return self.value * 2

x = Client1(10)
x.eggs() 		#	Aggiunto eggfunc



#	ESEMPIO DI DECORAZIONE FINE-GRAINED
#	Voglio decorare in modo diverso in base a dei parametri

from types import FunctionType

def tracer(func):
	"""	Il mio solito decoratore che fa il tracer """
	calls = 0
	def onCall(*args , **kargs):
		nonlocal calls 
		print("call {0} to {1}" . format(calls , func.__name__))
		return func(*args , **kargs)
	return onCall

def decorateAll(decorator):
	""" Avrò bisogno di passare in qualche modo i vari decoratori alla metaclasse
		e perciò utilizzo una clousure """

    class MetaDecorate(type):
        def __new__(meta, classname, supers, classdict):
            for attr,attrval in classdict.items():
                if type(attrval) is FunctionType:
                    classdict[attr] = decorator(attrval)	 
                    #	Qui utilizzo il parametro della clousure.
                    #	Quindi, per ogni item del classidict della classe, se l'item è una funzione lo decoro
                    #	altrimenti passo.
            return type.__new__(meta, classname, supers, classict)
    return MetaDecorate
    #	Ovviamente alla fine ritornerò la metaclasse.

class Person(metaclass=decorateAll(tracer)):
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def giveRaise(self,percent):
        self.pay += (1.0 + percent)

    def lastName(self):
        return self.name.split()[-1]

bob = Person('Bob smith' , 50000)
sue = Person('Sue jones' , 100000)
print(bob.name , sue.name)
sue.giveRaise(.10)
print(sue.pay)
print(bob.lastName() , sue.lastName())








"""

	METODI SPECIALI NELLE METACLASSI

"""
class MetaClasse(type):
	"""
		In questo momento l'istanza della MetaClasse non è ancora stata creata e, perciò, questo
		metodo prende in input la metaclasse e i vari parametri della classe che si vuole creare
		a partire da essa.
		
		Alla fine quindi si ritornerà un oggetto di tipo MegaClasse da consegnare al metodo init
		per l'inizializzazione
	"""
	def __new__(mega, cls, supers, dizionario):		# Istanza non è stata ancora creata quindi passo la classe stessa
		print("Sono in Mega.new")
		return super().__new__(mega,cls,supers,dizionario)


	"""
		Il metodo __init__ non si comporta diversamente da come farebbe per qualsiasi classe.
		Infatti esso riceve l'instanza creata, in questo caso una classe, come argomento se __new__
		ha ritornato un instanza del tipo aspettato ( un oggetto di type 'MetaClass').
		Di conseguenza, se il __new__ non ritorna un oggetto di tipo 'Metaclass' come, per esempio,
		None oppure Metaclass stessa ( che è un oggetto di tipo Type ) il metodo __init__ non verrà 
		chiamato.

		init <classobject , classname, supers, attr>
	"""
	def __init__(cls, *args):
	#	Qui potrei fare varie personalizzazioni della classe creata.
	#	Ho a disposizione : cls_object, cls_name, supers, dizionario



	"""
		Ancora una volta, il comportamento di __call__ non è diverso da quello di qualsiasi altra classe. 
		Si chiama quando si tenta di creare un'istanza della metaclasse.
		
		Ovviamente, la chiamata a una classe dovrebbe restituire un'istanza, quindi non dimenticare di 
		chiamare super().__ call__ e restituirne il risultato, altrimenti potresti cortocircuitare 
		la creazione dell'istanza.

		Questo medoto ovviamente chiamerà i metodi __new__ e __init__ nella classe base per la creazione
		dell'istanza di quest'ultima.
	"""

	def __call__(cls, *args):
	#	Ho in input la classe del quale si vuole creare l'instanza e i suoi parametri da passare al costruttore
		return super().__call__(*args)
		return super(Metaclasse, classe_da_creare).__call__(*args)



class Dummy(metaclass = MetaClasse):

	def __new__(cls, *args):			# Istanza non è stata ancora creata quindi passo la classe stessa
		print("******** Sono in Dummy.new")
		return super().__new__(cls)

	def __init__(self, nome):
		print("****** Sono in Dummy.init")
		self.nome = nome

	def __call__(self, *args):
		print("********* Sono in Dummy.call")
		print(self, *args)

lorenzo = Dummy("lorenzo") #Perchè di fatto cosi la classe è callable.

"""
	Sono in Mega.new
	Sono in Mega.init
	Sono in Mega.call- esco
		******** Sono in Dummy.new
		****** Sono in Dummy.init
	Sono in Mega.call- esco
"""































