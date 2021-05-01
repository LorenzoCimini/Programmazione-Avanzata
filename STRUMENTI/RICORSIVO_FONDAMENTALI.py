"""
	TUTTE LE COMBINAZIONI POSSIBILI ( DI QUALSIASI LUNGHEZZA ) DI UNA LISTA 
"""

def combinations(lista):
	"""
		1° PASSO : 
					lista = [1,2,3]		-> 1° chiamata : c = combinations(1,2) + [elemento+[lista[-1]] for elemento in combinations(lista[:-1])]
		2° PASSO :
					lista = [1,2]		-> 2° chiamata : c = combinations(1) + [elemento+[lista[-1]] for elemento in combinations(lista[:-1])]
		3° PASSO :
					lista = [1]			-> 3° chiamata : c = combinations() + [elemento+[lista[-1]] for elemento in combinations(lista[:-1])]
		4° PASSO :
					CASO BASE -> 		return [[]]

		... adesso comincio a ricostruire il risultato

		3° PASSO :
					 c = [[]] + Ogni elemento in [[]] sommato a 1 -> [[], [1]]
		2° PASSO :
					 c = [[],[1]] + Ogni elemento in [[][1]] sommato a 2 -> [[][1][2][1,2]]
		1° PASSO :
					 c = [[][1][2][1,2]] + Ogni elemento in [[][1][2][1,2]] sommato a 3 -> [[][1][2][1,2][3],[1,3][2,3][1,2,3]]

		-> Ritorno [[][1][2][1,2][3],[1,3][2,3][1,2,3]]

	"""
	if not lista:
		return [[]]
	else:
		return combinations(lista[:-1]) + [elemento+[lista[-1]] for elemento in combinations(lista[:-1])]



"""
	TUTTE LE COMBINAZIONI CONTIGUE DI UNA LISTA
"""

def contigue(lista):
	return [lista[i:i+j] for i in range(len(lista)) for j in range(1,len(lista)-i+1)]





"""
	PRODOTTO CARTESIANO DI SOTTOLISTE
"""

def soluzione(lista):
	if len(lista) == 1:
		return [[x] for x in lista[0]]
	else:
		return [[x] + y for x in lista[0] for y in soluzione(lista[1:])]



"""
	PERMUTAZIONI

	L'operatore '*<var>' può essere utilizzato per spacchettare liste di liste.

	https://duckduckgo.com/?q=permutationf+of+a+list+functional+python&atb=v250-1&iax=images&ia=
	images&iai=https%3A%2F%2Fwww.wikitechy.com%2Ftechnology%2Fwp-content%2Fuploads%2F2017%2F05%2FNew
	Permutation.png"

	Guardando questa immagine si capisce la struttura ricorsiva insita nelle permutazioni.
"""

def permutations(lista):
	if len(lista) == 0:
		return [[]]
	else:
		return [ [lista[i]] + perm for i in range(len(lista)) for perm in permutations((lista[:i]) + lista[i+1:])]











"""
	FUNZIONE RICORSIVA CHE STAMPA TUTTI I CAMMINI PRESENTI IN UN ALBERO BINARIO
"""

def funzione(nodo, path=[], percorsi =[]):
	if not nodo:
		return []
	if nodo.sx and nodo.dx:
		return funzione(nodo.sx, path + [nodo.contenuto], percorsi) + funzione(nodo.dx, path + [nodo.contenuto], percorsi)
	elif nodo.sx:
		return funzione(nodo.sx, path + [nodo.contenuto], percorsi)
	elif nodo.dx:
		return funzione(nodo.dx, path + [nodo.contenuto], percorsi)
	elif not nodo.sx and not nodo.dx:
		return percorsi + [path+[nodo.contenuto]]


"""
	Implementare algoritmi in funzionale per :
		- BFS ( Breadth First Search )

		is a vertex based technique for finding a shortest path in graph. It 
		uses a Queue data structure which follows first in first out. In BFS, one vertex 
		is selected at a time when it is visited and marked then its adjacent are visited
		and stored in the queue. It is slower than DFS.
		

		- DFS (	Depth 	First Search )

		It uses the Stack data structure, performs two stages, first visited vertices are 
		pushed into stack and second if there is no vertices then visited vertices are 
		popped.
"""

class Albero:
	def __init__(self, contenuto, sx=None, dx=None, root=False):
		self.contenuto = contenuto
		self.sx = sx
		self.dx = dx
		self.root = root


nodo_1 	= 	Albero(1)
nodo_2 	= 	Albero(2,nodo_1)
nodo_3 	= 	Albero(3)
nodo_6 	= 	Albero(6)
nodo_4 	= 	Albero(4,nodo_3, nodo_6)
root   	= 	Albero(5,nodo_2, nodo_4,True)



"""
		5
	   / \
	  2	  4
	 /	 / \
	1 	3	6

	 BFS OUTPUT : [5,2,4,1,3,6]
	 DFS OUTPUT : [5,2,1,4,3,6]

"""


def BFS(nodo):
	if not nodo:
		return "Nessun albero"
	if nodo.sx and nodo.dx: 
		return [nodo.contenuto] + [nodo.sx.contenuto] + [nodo.dx.contenuto] + BFS(nodo.sx) + BFS(nodo.dx) if nodo.root == True \
				else [nodo.sx.contenuto] + [nodo.dx.contenuto] + BFS(nodo.sx) + BFS(nodo.dx)
	elif nodo.sx:
		return [nodo.sx.contenuto] + BFS(nodo.sx)
	elif nodo.dx:
		return [nodo.dx.contenuto] + BFS(nodo.dx)
	elif not nodo.sx and not nodo.dx: return []



def DFS(nodo):
	if not nodo:
		return "Nessun albero"
	elif nodo.sx and nodo.dx :
		return [nodo.contenuto] + DFS (nodo.sx) + DFS(nodo.dx)
	elif nodo.sx :
		return [nodo.contenuto] + DFS(nodo.sx)
	elif nodo.dx :
		return [nodo.contenuto] + DFS(nodo.dx)
	elif not nodo.sx and not nodo.dx :
		return [nodo.contenuto]























