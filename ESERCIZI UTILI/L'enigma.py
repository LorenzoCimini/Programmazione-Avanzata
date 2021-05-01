#	The riddle:
#       	HAWAII + IDAHO + IOWA + OHIO == STATES
#	
#	- the letters spell out actual words and a meaningful sentence
#	- each letter can be translated to a digit (0-9) no initial can be translated to 0
#	- to the same letter corresponds the same digit along the whole sentence and no digit 
#	  can be associated to two different letters
#	- the resulting arithmetic equation represents a valid and correct equation

#	That is, the riddle above:
#	          HAWAII + IDAHO + IOWA + OHIO == STATES
#	          510199 + 98153 + 9301 + 3593 == 621246
import re, itertools

def check_firsts(tentativo, firsts):
	""" Ritorna True se c'è una prima lettera == 0 ( devo brekkare il loop ) """
	for lettera in firsts:
		if tentativo[lettera] == 0:
			return False 
	return True

def solve(puzzle):
	# Tutte le lettere contenute nel puzzle 
	stringa = re.findall('\S' , puzzle.upper())
	parole = re.findall('[A-Z]' , puzzle)
	
	# Tutte le parole contenute nel puzzle - escluse le ripetizioni 
	parole_uniche = set(parole)
	assert len(parole_uniche) <= 10, 'Errore'

	# Prime lettere di ogni parola
	prime_lettere = {word[0] for word in puzzle.split(" ") if word[0] not in ['+' , '-' , '=']} 

	for tentativo in itertools.product(range(0,len(parole_uniche)-1) , repeat = len(parole_uniche)):
		result = ''
		tentativo = dict(zip(parole_uniche, tentativo)) 
		#	Procedo con il sostituire ogni lettera ( diversa dagli operatori ) del puzzle con il numero associato
		#	a questa ultima all'interno del tentativo corrente.
		#	Dopodichè valuto l'espressione risultante.
		if check_firsts(tentativo,prime_lettere):
			for index in range(0,len(stringa)):
				if stringa[index] not in ['=' , '+' , '-']:
					result += str(tentativo[stringa[index]])
				else:
					result += str(stringa[index]) 
			if eval(result) : return result
		

if __name__ == '__main__':
	puzzle = "HAWAII + IDAHO + IOWA + OHIO == STATES"
	print(solve(puzzle))