"""
	MANAGED ATTRIBUTES
	Con questa tecnica, ci prefiggiamo l'obiettivo di riuscire a separare il compito funzionale di una classe
	da una feature complementare che si vuole aggiungere ad essa.

	Esempio : implementazione conto corrente
 	Il conto corrente dovrebbe teoricamente concentrarsi solo sulla movimentazione del denaro.
 	Nella realtà quello che succede è che la gestione di questa cosa è molto più complicata dal momento che
 	di mezzo intercorrono fattori importantissimi come, per esempio, sicurezza ecorrettezza delle operazioni.
 	Proprio per queste ragioni dovranno per forza di cose esistere delle funzioni che andranno a contornare 
 	la nostra classica movimentazione di denaro.

 	Per fare queste differenziazione python ci mette a disposizione tre approcci :
 		-	PROPERTIES
 		-	DESCRIPTOR PROTOCOL
 		- 	OPERATOR OVERLOADING
"""

#	Applichiamo quindi questi diversi approcci alla classe 'account'

class account:
	def __init__(self, initial_amount):
		self.amount = initial_amount

	def balance(self):
		return self.amount

	def withdraw(self, amount):
		self.amount = self.amount - amount

	def deposit(self, amount):
		self.amount = self.amount + amount

	def __str__(self):
		return "L'amount disponibile e' {0} " . format(self.amount)



"""
	Ci accorgiamo subito che, in base a questa implementazione, sarebbe possibile fare un prelievo dal conto
	di una quantità di denaro maggiore a quella realmente disponibile dal momento che non c'è nessun controllo
	su questa operazione.
	Entrano in gioco quindi le funzioni complementari citate all'origine di questo problema.

"""





"""	
	PROPERTIES
	In poche parole, le properties allegano del codice (in questo casosafe_get e safe_set) agli accessi 
	dell'attributo amount.
	Gli attributi acceduti dai metodi complementari devono trattare quest'ultimi come privati, ovvero con l'_.
	Operando in questo modo quindi, abbiamo associato dei metodi get,set e delete all'attributo amount che,
	di conseguenza, OGNI VOLTA CHE VERRA' ACCEDUTO PER ESSERE PRELEVATO O RICHIESTO CHIAMERA' IN AUTOMATICO
	I METODI safe_get e safe_set.
"""

#	PROPERTIES PER RENDERE SAFE OPERAZIONI DI PRELIEVO

class safe_account(account):
	def __init__(self , initial_amount):
		self._amount = initial_amount

	def safe_get(self):
		return self._amount 

	def safe_set(self , amount):
		assert amount == 0 , "Non sono possibili prelievi dal momento che non ci sono fondi"
		self._amount = amount

#	In questo modo 'attacchiamo' i metodi safe_get e safe_set all'attributo 'amount' della classe account.
	amount = property(safe_get , safe_set , None , "Gestione del conto sui prelievi eccessivi" )


a = safe_account(100)
a.withdraw(200)	# -> AssertionError: Non sono possibili prelievi dal momento che non ci sono fondi

#	La properties può essere anche implementata all'interno della classe stessa e non dobbiamo quindi per forza
#	estenderla

class account:
	def __init__(self, initial_amount):
		self.amount = initial_amount

	def balance(self):
		return self.amount

	def withdraw(self, amount):
		self.amount = self.amount - amount

	def deposit(self, amount):
		self.amount = self.amount + amount

	def safe_get(self):
		return self._amount 

	def safe_set(self , amount):
		assert amount > 0 , "Non sono possibili prelievi dal momento che non ci sono fondi"
		self._amount = amount

	def __str__(self):
		return "L'amount disponibile e' {0} " . format(self.amount)

	amount = property(safe_get , safe_set , None , "Gestione conto")

#	PROPERTIES PER CALCOLARE DINAMICAMENTE IL BALANCE
#	Un altro esempio di utilizzo di properties 

class account_with_calculated_balance:
	def __init__(self, initial_amount):
		self._deposits = initial_amount
		self._withdraws = 0

	def deposit(self,amount):
		self._deposits += amount

	def withdraw(self,amount):
		self._withdraws += amount

	def calculate_balance(self):
		return self._deposits - self._withdraws

	def zeroing_balance(self):
		self._deposits = 0
		self.withdraws = 0
#	In questo modo quindi vado a costuire l'attributo direttamente con la property
	balance = property(calculate_balance , None , zeroing_balance , "Managing")


a = account_with_calculated_balance(1000)
a.withdraw(100)
print(a.balance)





"""
	DESCRITTORI ( Già visti nella lezione OOP )

	Lavorano nello stesso modo identico delle properties ma, con una sintassi diversa.
	'Descriptors let objects customize attribute lookup, storage, and deletion.'

"""

#	UTILIZZO DEI DESCRITTORE PER GESTIRE I PRELIEVI ECCESSIVI 

class safe_balance:
	def __get__(self, instance, owner):
		print("get")
		return instance._amount

	def __set__(self, instance, amount):
		print("SET")
		assert amount > 0 , "Errore importo"
		instance._amount = amount


class account:
	def __init__(self, amount):
		self.amount = amount

	def deposit(self, amount):
		self.amount += amount

	def withdraw(self, amount):
		self.amount -= amount

	amount = safe_balance()


#	UTILIZZO DEI DESCRITTORE PER CALCOLARE DINAMICAMENTE IL BALANCE

class dinamic_balance:
	def __get__(self, instance, owner):
		return instance._depositi - instance._prelievi

	def __delete__(self, instance):
		instance.depositi = 0
		instance.prelievi = 0


class account:
	def __init__(self, deposito_iniziale):
		self._depositi = deposito_iniziale
		self._prelievi = 0

	def deposit(self, amount):
		self._depositi += amount

	def withdraw(self, amount):
		self._prelievi += amount

	amount = dinamic_balance()



"""
	OPERATOR OVERLOADING
	Con questa tecnica andremo a lavorare, questa volta,a livello di classe e di conseguenza tutti gli 
	attributi di quest'ultima subiranno il protocollo descritto.
	Il protocollo qui è più articolato, infatti avremo :
	-    __getattr__        Viene usata quando non esiste l'attributo in questione
	-    __getattribute__   Viene usata quando si accede ad un qualsiasi attributo
	-    __setattr__        Viene chiamata quando andiamo ad assegnare un valore
	-    __delattr__        Viene chiamato ogni qualvolta andiamo a eliminare un attributo

	Di fatto quindi andremo a modificare il PROTOCOLLO DI DEFAULT che avviene durante qualsiasi operazione 
	che facciamo su qualsiasi oggetto delle classi 
"""
#	!!! IMPORTANTE LA DIFFERENZA TRA __getattr__ e __getattribute__
 
#	UTILIZZO DELL'OVERLOADING PER CALCOLARE DINAMICAMENTE IL BALANCE

class safe_account(account):

    def __setattr__(self,attr,amount):
        assert amount > 0 , 'Not admitted operation: the final balance {0} MUST be positive' . format(amount)
        self.__dict__[attr] = amount



#	UTILIZZO DELL'OVERLOADING PER CALCOLARE DINAMICAMENTE IL BALANCE

    def __getattr__(self,attr):
        if attr = 'balance':
            return self._deposits - self._withdrawals
        else: raise AttributeError(attr) # Altrimenti sollevo che l'attributo è quello sbagliato.

    def __delattr__(self,attr):
        if attr == 'balance':
            self.deposit = 0
            self.withdrawals = 0
        else: raise AttributeError(attr) # Altrimenti sollevo che l'attributo è quello sbagliato.







