import re

rules = [\
	
	('[1]$' , '1$' , '_uno' ),
	('[2]$' , '$' , '_due' ),
	('[3]$' , '$' , '_tre' )
]

def crea_regole(cosa_cercare,dove_sostituire,sostituzione):			# Genera funzioni
	def trova(parola):
		return re.search(cosa_cercare , parola)
	def sostituisci(parola):
		return re.sub(dove_sostituire , sostituzione , parola)
	return (trova,sostituisci)

def generatore(rules):
	for (cosa_cercare,dove_sostituire,sostituzione) in rules:
		yield crea_regole(cosa_cercare , dove_sostituire , sostituzione)

def metodo(parola):
	for trova,sostituisci in generatore(rules):
		if trova(parola):
			return sostituisci(parola)


if __name__ == '__main__':
	parola = "cane1"
	print(metodo(parola))