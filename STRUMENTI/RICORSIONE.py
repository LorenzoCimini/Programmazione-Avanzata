"""
	Dato un albero binario di ricerca, stampare tutti i nodi .

"""

class Albero:
	def __init__(self,contenuto, sx= None, dx= None):
		self.contenuto = contenuto
		self.sx = sx
		self.dx = dx

	def __str__(self):
		return self.stampa_albero(self)

	def stampa_albero(self, albero):
		if albero == None:
			return ''
		else:
			return str(albero.contenuto) + "\n" + self.stampa_albero(albero.sx) + self.stampa_albero(albero.dx)

	
foglia_1 	= 	Albero(1)
nodo_2 		= 	Albero(2,foglia_1)
nodo_4		=	Albero(4)
nodo_3 		= 	Albero(3, nodo_2, nodo_4)
nodo_6 		=	Albero(6)
nodo_8 		= 	Albero(8)
nodo_7 		= 	Albero(7, nodo_6, nodo_8)
root 		= 	Albero(5, nodo_3,nodo_7)

# print(root)








"""
	PRODOTTO CARTESIANO DI LISTE DI UNA LISTA

	Data una lista di liste calcolare il prodotto cartesiano di tutte le sottoliste e calcolare 
	il prodotto massimo di ogni elemento del prodotto cartesiano, e poi ritornare una tupla contenente 
	il prodotto e la sottolista associata

"""

#	Qui vado a creare una funzione ricorsiva che somma ogni elemento della prima lista nella lista di liste
#	con tutti gli altri elementi di ogni altra sottolista presente nell'array passato come parametro.
#	Il caso base è quello in cui la lista presa in input abbia una sola sottolista al suo interno,
#	in questo caso infatti andremo a ritornare una lista di sottoliste che contengono ogni elemento
#	del primo elemento della lista.

from functools import reduce

def prodotto(lista):
	if len(lista) == 1:
		return [ [x] for x in lista[0] ]
	else:
		return [[x]+y for x in lista[0] for y in prodotto(lista[1:])]

def max_product_2(lista):
	massimo = max( [reduce(lambda x,y : x*y , item) for item in prodotto(lista)]) 
	return ( massimo, [  item for item in prodotto(lista) if reduce(lambda x,y : x*y, item) == massimo])


# print( max_product_2([	[1,2,3,4] , [4,5,6,7] , [1]]))













"""
	Data una lista di interi, calcolare tutte le possibili combinazioni di essi ( di dimensione 2 )
	e infine, cacolare il massimo prodotto per ognuna e stampare il prodotto e la lista relativa.
"""

def prodotto_cartesiano(lista):
	return [ [x] + [y] if [y] != [[]] else [x] for x in lista for y in [elem for elem in lista+[[]] if elem != x]]

def soluzione(lista):
	return [ reduce(lambda x,y : x*y , elem) for elem in prodotto_cartesiano(lista)]


# print(soluzione([1,2,3,-3,5]))










"""
	PERMUTAZIONI

	L'operatore '*<var>' può essere utilizzato per spacchettare liste di liste.

	https://duckduckgo.com/?q=permutationf+of+a+list+functional+python&atb=v250-1&iax=images&ia=
	images&iai=https%3A%2F%2Fwww.wikitechy.com%2Ftechnology%2Fwp-content%2Fuploads%2F2017%2F05%2FNew
	Permutation.png"

	Guardando questa immagine si capisce la struttura ricorsiva insita nelle permutazioni.
"""

def makePerm(lista):
	if len(lista) == 0:
		return [[]]
	else:
		return  [ [e] + perm for e in lista for perm in makePerm([z for z in lista if z != e])]

# print(makePerm([1,2,3]))







"""
	897. Increasing Order Search Tree

	https://leetcode.com/problems/increasing-order-search-tree/

	Data la radice di un albero di ricerca binario, riorganizza l'albero in ordine in modo che 
	il nodo più a sinistra dell'albero sia ora la radice dell'albero e ogni nodo non abbia un figlio 
	sinistro e un solo figlio destro.
"""

esercizio = [5,3,6,2,4,None,8,1,None,None,None,7,9]

def soluzione(lista):
	"""
		Ordino la lista, con i valori None tolti, e creo il risultando aggiungendo mano a mano
		una lista formata dai i valori in ordine crescente e un valore None.
		Otterrò : [ [1,None] , [2,None] ]
		Quindi farò un reduce
	"""
	return reduce(lambda x,y:x+y, [ [x,None] for x in sorted([z for z in lista if z != None] , key = lambda x: x)])

#	print(soluzione(esercizio))







"""
	1038. Binary Search Tree to Greater Sum Tree

	Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key 
	of the original BST is changed to the original key plus sum of all keys greater than the original
	key in BST

	https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
"""

root = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
root = [1,0,2]
root = [3,2,4,1]
root = [1,2,1,4]

def soluzione(lista):
	"""
		Per ogni elemento della lista, stampo l'elemento + la somma di tutti quelli maggiori a lui oppure None
		se l'elemento è None
	"""
	return [ x + sum([ z for z in lista if z != None and z > x]) if  x != None else None for x in lista]

# print(soluzione(root))






"""
	21. Merge Two Sorted Lists
	Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing 
	together the nodes of the first two lists.

"""

l1 = [1,2,4]
l2 = [1,3,4]

l1 = []
l2 = [0]

def soluzione(lista_1, lista_2):
	return sorted(lista_1 + lista_2, key= lambda x:x)

# print(soluzione(l1, l2))







"""
	SUBARRAY CONTIGUI DI UN ARRAY 

	53. Maximum Subarray

	Given an integer array nums, find the contiguous subarray (containing at least one number) 
	which has the largest sum and return its sum.

"""

nums = [-2,1,-3,4,-1,2,1,-5,4]

def contigui(lista):
	return [lista[i:i+j] for i in range(0,len(lista)) for j in range(1,len(lista)-i+1)]


def soluzione(lista):
	return (max([sum(x) for x in contigui(lista)]), [z for z in contigui(lista) if sum(z) == max([sum(z) for z in contigui(lista)])])

# print(soluzione(nums))










"""
	152. Maximum Product Subarray
	Given an integer array nums, find the contiguous subarray (containing at least one number) 
	which has the largest product and return its product.
"""

from math import prod

lista = [2,3,-2,4]

def contiguos(lista):
	return [lista[i:i+j] for i in range(0,len(lista)) for j in range(1,len(lista)-i+1)]

def moltiplicazione(*valori):
	return reduce(lambda x,y: x*y, *valori)

def soluzione(lista):
	return (max([prod(x) for x in contiguos(lista)]), *[z for z in contiguos(lista) if prod(z) ==max([prod(x) for x in contiguos(lista)])])

# print(soluzione(lista))








"""
	697. Degree of an Array

	Given a non-empty array of non-negative integers nums, the degree of this array is defined as 
	the maximum frequency of any one of its elements.

	Your task is to find the smallest possible length of a (contiguous) subarray of nums, 
	that has the same degree as nums.

"""


nums = [1,2,2,3,1,4,2]

def contiguos(lista):
	return [lista[i:i+j] for i in range(0,len(lista)) for j in range(1, len(lista)-i+1)]

def frequency(lista):
	return max([lista.count(x) for x in lista])

def soluzione(lista):
	return [soluzione for soluzione in contiguos(lista) if frequency(soluzione) == frequency(lista)][0]

#print(soluzione(nums))










"""
	GENERATORE

	Costruisci un generatore che restituisce all'iterazione n, un numero uguale alla somma
	delle sue cifre elevate alla posizione che occupano all'interno del numero n.
	( La cifra più a sinistra ha indice 1 )

	ES : n = 82 -> 8^1 + 2^2 = 12
"""


def generatore(n=1):
	digits = [x for x in str(n)]
	number = range(1,len(digits)+1)
	lista = [[int(digits[i]),number[i]] for i in range(0,len(digits))]
	yield sum([	pow(x,i) for x,i in lista])
	yield from generatore(n+1)


"""for i in generatore():
	if i > 100: break
	print(i)"""










"""
	35. Search Insert Position

	Given a sorted array of distinct integers and a target value, return the index if the target 
	is found. If not, return the index where it would be if it were inserted in order.

	Example 1:
	Input: nums = [1,3,5,6], target = 5
	Output: 2
	
	Example 2:
	Input: nums = [1,3,5,6], target = 2
	Output: 1

"""


def soluzione(lista,target):
	return lista.index(target) if target in lista else sorted((lista + [target]), key=lambda x:x).index(target)

"""nums = [1,3,5,6]
target = 7
print(soluzione(nums,target))"""









"""
	4. Median of Two Sorted Arrays
	Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of 
	the two sorted arrays.

"""


def soluzione(lista_1, lista_2):
	return sorted((lista_1 + lista_2), key = lambda x:x)[int(len(lista_1+lista_2)/2)]


"""nums1 = [1,2]
nums2 = [3,4]
print(soluzione(nums1,nums2))"""







"""
	167. Two Sum II - Input array is sorted

	Given an array of integers numbers that is already sorted in ascending order, find two numbers such 
	that they add up to a specific target number.
	Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, 
	where 1 <= answer[0] < answer[1] <= numbers.length.
	You may assume that each input would have exactly one solution and you may not use the same element 
	twice.

"""

numbers = [2,3,4]
target = 6

def prodotto_cartesiano(lista):
	return [ [x] + [y] for x in lista for y in [z for z in lista if z != x]]

def soluzione(lista, target):
	return [lista.index(x)+1 for x in [x for x in prodotto_cartesiano(lista) if sum(x) == target][0]]



 # print(soluzione(numbers, target))









"""
 	238. Product of Array Except Self

 	Given an array nums of n integers where n > 1,  return an array output such that output[i] is 
 	equal to the product of all the elements of nums except nums[i].

 """

input = [1,2,3,4]


def soluzione(lista):
	return [ prod([z for z in lista if z != lista[i]])	for i in range(0,len(lista))	]


# print(soluzione(input))













"""
	ESERCIZIO ESAME

	Data una lista di liste dovevo calcolarmi il prodotto cartesiano di tutte le sottoliste e calcolare 
	il prodotto massimo di ogni elemento del prodotto cartesiano, e poi ritornare una tupla contenente il prodotto e la sottolista associata

"""

input = [ [1,2,3] , [3,4,5] , [6,7,8] ]

def soluzione(lista):
	if len(lista) == 1:
		return [ [x] for x in lista[0] ]
	else:
		return [[x] + y for x in lista[0] for y in soluzione(lista[1:]) ]

def prodotto(lista):
	return ([x for x in soluzione(lista) if prod(x) == max([prod(x) for x in soluzione(lista)])],max([prod(x) for x in soluzione(lista)]))

# print(prodotto(input))












"""
	147. Insertion Sort List

	https://leetcode.com/problems/insertion-sort-list/
	Sort a linked list using insertion sort.

"""

input = [4,1,2,3]

def soluzione(lista):
	if len(lista) == 1:
		return lista
	else:
		return [min(lista)] + soluzione([z for z in lista if z != min(lista)])

#	print(soluzione(input))












"""
	98. Validate Binary Search Tree
	https://leetcode.com/problems/validate-binary-search-tree/

"""


class Albero:
	def __init__(self, contenuto, sx=None, dx=None):
		self.contenuto = contenuto
		self.sx = sx
		self.dx = dx


nodo_1 = Albero(1)
nodo_3 = Albero(3)
nodo_6 = Albero(6)
nodo_4 = Albero(4,nodo_3, nodo_6)
root   = Albero(5,nodo_1, nodo_4)

albero = [root,nodo_1,nodo_4,nodo_3,nodo_6]

def soluzione(albero):
	return all([True if (nodo.sx == None or nodo.sx.contenuto < nodo.contenuto) and (nodo.dx == None or nodo.dx.contenuto > nodo.contenuto) else False for nodo in albero ])

# print(soluzione(albero))










"""
	12. Integer to Roman

	https://leetcode.com/problems/integer-to-roman/

"""

patterns = 	{ \
					1 : 	'I'		,
					4 : 	'IV'	,
					5 : 	'V'		,
					9 : 	'IX'	,
					10: 	'X'		,
					40: 	'XL'	,
					50:		'L'		,
					90: 	'XC'	,
					100:	'C'		,
					400:	'CD'	,
					500:	'D'		,
					900:	'CM'	,
					1000:	'M'		
			}



def digits_countdown(numero):
	if len(str(numero)) == 1:
		return [numero]
	else:
		return [str(numero)[0] + "0" * (len(str(numero))-1)] + digits_countdown(str(numero)[1:])


def soluzione(numero):
	result = ''
	for scomposizione in digits_countdown(numero):
		if int(scomposizione) in list(patterns):
			result += patterns[int(scomposizione)]
		elif int(scomposizione) == 0:
			pass 
		else:
			partial = []
			for prodotto, valori in combinazioni(list(patterns)):
				if int(scomposizione) == prodotto:
					partial.append([prodotto,valori])
			result += patterns[partial[len(partial)-1][1][0]] * partial[len(partial)-1][1][1]

	return result

def combinazioni(lista):
	return [(reduce(lambda x,y : x*y , [x,i]) , [x,i]) for x in list(patterns) for i in [2,3,6,7,8]]











"""
	867. Transpose Matrix + esercizio esame

	dati dei gradi che potevano essere (-360, -270, -180, -90, 0, 90, 180, 270, 360, ecc) 
	ruotare una matrice in senso orario o antiorario

	https://leetcode.com/problems/transpose-matrix/

"""

# 	La trasposta di una matrice è la matrice stessa con le righe che divetano colonne e le colonne che 
#	diventano righe
def transpose(matrix):
	return [ [x[i][j] for i in range(len(matrix))]	for j in range(len(matrix[0]))]

def turn_minus_90(matrix):
	return [ [matrix[i][j] for i in range(len(matrix)-1,-1,-1)] for j in range(len(matrix[0]))]

def turn_plus_90(matrix):
	return [ [matrix[i][j] for i in range(len(matrix)) ] for j in range(len(matrix[0])-1,-1,-1) ]

def rotazione(gradi, matrix):
	if gradi == 0:
		return matrix
	else:
		return rotazione(gradi+90,turn_plus_90(matrix)) if gradi < 0 else rotazione(gradi-90, turn_minus_90(matrix))

matrix = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

"""for i in matrix:
	print(i)
print("\n")
for i in rotazione(+90, matrix):
	print(i)
print("\n")
for i in rotazione(-90, matrix):
	print(i)"""







"""
	ESERCIZIO ESAME

	Calcolare tutte le possibli combinazioni (di tutte le grandezze) di 
	numeri in una lista e di queste calcolare il massimo prodotto per ognuna per poi stampare il massimo 
	prodotto e la lista relativa

"""


array = [1,2,3]


def combinazioni(lista):
	if not lista:
		return [[]]
	else:
		return [x for x in combinazioni(lista[:-1]) + [elemento + [lista[-1]] for elemento in combinazioni(lista[:-1])] if x != [] ]


def max_in_list(lista):
	return max(	[reduce(lambda x,y:x*y, x) for x in lista]	)


def soluzione(lista):
	return (max_in_list(combinazioni(lista)), [x for x in combinazioni(lista) if prod(x) == max_in_list(combinazioni(lista))])



# print(soluzione(array))








"""
	ESERCIZIO ESAME
	dato un albero binario di interi e un numero n, trovare tutti i cammini radice-foglia la cui somma sia n. 
"""


class Albero:
	def __init__(self, contenuto, sx=None, dx=None):
		self.contenuto = contenuto
		self.sx = sx
		self.dx = dx


nodo_1 	= 	Albero(1)
nodo_3 	= 	Albero(3)
nodo_6 	= 	Albero(6)
nodo_4 	= 	Albero(4,nodo_3, nodo_6)
root   	= 	Albero(5,nodo_1, nodo_4)

"""
		5
	   / \
	  1	  4
	  	 / \
	  	3	6
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



def soluzione(root,n):
	return [x for x in funzione(root) if sum(x) == n]

# print(soluzione(root,12))










"""	
	Trovare la sottostringa palindroma più lunga

"""

def sotto_stringhe(stringa):
	return [ stringa[i:i+j] for i in range(len(stringa)) for j in range(1,len(stringa)-i+1)]

def is_palindrome(stringa):
	return stringa == stringa[::-1]

def all_palindrome(stringa):
	return [x for x in sotto_stringhe(stringa) if is_palindrome(x) and len(x) > 1 and x != stringa]

def max_palindrome(stringa):
	return sorted(all_palindrome(stringa), key= lambda x: len(x), reverse=True)[0]

# print(max_palindrome('ottotot'))




"""
	trova la sottostringa + grande in comune tra s1 e s2
"""


stringa_1 = "ciaostoprovandodaquiinpoiniente"
stringa_2 = "ciaostoprovandocosafare"


def sotto_stringhe(stringa):
	return [ stringa[i:i+j] for i in range(len(stringa)) for j in range(1,len(stringa)-i+1)]

def soluzione(stringa_1, stringa_2):
	return sorted([x for x in sotto_stringhe(stringa_1) if x in sotto_stringhe(stringa_2)], key= lambda x:len(x), reverse=True)[0]

# print(soluzione(stringa_1,stringa_2))










"""

	Data una stringa, ritorna num minimo di char per renderla palindroma. 
	Posso aggiungerli a destra e a sinistra

"""


stringa = "adebe"

def ricorsiva(stringa, acc=[]):
	if len(stringa) == 1:
		return ''
	else:
		if is_palindrome(stringa): return acc
		else:
			return ricorsiva(stringa[1:] , acc + [stringa[0:1]])


def soluzione(stringa):
	return ((len(ricorsiva(stringa))) > 0 and \
					("Il numero minimo di caratteri e': {0}\nDi fatto rende la stringa : {1}, la quale e' palindroma" \
						.format(reduce(lambda x,y:x+y,(list(reversed(ricorsiva(stringa))))),stringa+reduce(lambda x,y:x+y,(list(reversed(ricorsiva(stringa)))))))) \
				or (True and "Non e' possibile")

# print(soluzione("prova"))



"""
	RIVER SIZES

	https://www.algoexpert.io/questions/River%20Sizes

"""

matrix=[ [1, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 1]]

 

def get_positions(matrix):
	return [[x,y] for x in range(len(matrix)) for y in range(len(matrix[0])) if matrix[x][y] == 1]

def soluzione(matrix):
	already_visited = []

	def BFS(positions, matrix_of_ones, directions= [[0,1],[1,0],[-1,0],[0,-1]], counter= 1, acc=1):
		if positions not in already_visited:
			already_visited.append(positions)
			for direction in directions:
				new_position = [positions[0] + direction[0], positions[1] + direction[1]]
				if new_position in matrix_of_ones and new_position not in already_visited:
					acc = BFS(new_position, matrix_of_ones, directions, counter, acc+counter)
			return acc

	return [x for x in [ BFS(positions, [x for x in get_positions(matrix) if x != positions] ) for positions in get_positions(matrix)] if x != None]


# print(soluzione(matrix))




"""
	https://www.algoexpert.io/questions/Validate%20Subsequence

	VALIDATE SUBSEQUENCE

	Date due array non vuoti, scrivi una funzione che determina se o meno il secondo array
	e' una sottosequenza del primo.
	I numeri nel primo array non devono essere strettamente adiacenti ma, devono rispettare
	l'ordine in cui si trovano nella seconda lista.

"""
def is_in(array,element):
	return [False] if (element not in array or len(array) == 0) else array.index(element)+1

def soluzione(array,sequence):
	if len(sequence) == 1 and is_in(array, sequence[0]) != [False]:
		return [True]
	else:
		return [True] + soluzione(array[is_in(array,sequence[0]):],sequence[1:]) if is_in(array, sequence[0]) != [False] else [False]

def isValidSubsequence(array,sequence):
    return all(soluzione(array,sequence))


"""
	Dato un albero binario di interni e un numero n, trovare tutti i cammini radice-foglia la cui somma
	sia n.
"""

class Albero:
	def __init__(self, contenuto, sx=None, dx=None, root=False):
		self.contenuto = contenuto
		self.sx = sx
		self.dx = dx


nodo_1 	= 	Albero(1)
nodo_2 	= 	Albero(2,nodo_1)
nodo_3 	= 	Albero(3)
nodo_6 	= 	Albero(6)
nodo_4 	= 	Albero(4,nodo_3, nodo_6)
root   	= 	Albero(5,nodo_2, nodo_4)


def DFS(nodo , path =[], paths =[]):
	if not nodo:
		return "Nessun nodo"
	elif nodo.sx and nodo.dx :
		return DFS(nodo.sx, path + [nodo.contenuto], paths) + DFS(nodo.dx, path + [nodo.contenuto], paths)
	elif nodo.sx :
		return DFS(nodo.sx, path + [nodo.contenuto], paths)
	elif nodo.dx :
		return DFS(nodo.dx, path + [nodo.contenuto], paths)
	elif not nodo.dx and not nodo.dx:
		return paths + [path + [nodo.contenuto]]

def soluzione(root,n):
	return [x for x in DFS(root) if reduce(lambda x,y:x+y,x) == n]

# print(soluzione(root,8))











"""	
	https://leetcode.com/problems/reverse-words-in-a-string/

	Given an input string s, reverse the order of the words.

	A word is defined as a sequence of non-space characters. The words in s will be 
	separated by at least one space.

	Return a string of the words in reverse order concatenated by a single space.
	Note that s may contain leading or trailing spaces or multiple spaces between two words. 
	The returned string should only have a single space separating the words. 
	Do not include any extra spaces.


"""


stringa =  "  Bob    Loves  Alice   "

def soluzione(stringa):
	return [word for word in (stringa.strip()).split(' ') if word not in ['',','] ][::-1]

# print(soluzione(stringa))









"""
	3. Longest Substring Without Repeating Characters

	Given a string s, find the length of the longest substring without repeating characters.

"""

s = ""


def combinations(stringa):
	return [ stringa[i:i+j] for i in range(len(stringa)) for j in range(1,len(stringa)-i+1)]

def inside(stringa):
	return [True if stringa.count(x) <= 1  else False for x in stringa]

def delete_duplicates(stringa):
	return [ x for x in combinations(stringa) if all(inside(x)) == True]

def soluzione(stringa):
	return sorted(delete_duplicates(stringa), key=lambda x: len(x), reverse=True)[0] if len(stringa) > 0 else "Stringa vuota"


# print(soluzione(s))



"""
	23. Merge k Sorted Lists
"""

lista = []


def soluzione(lista):
	return sorted(reduce(lambda x,y:x+y, [x for x in lista])) if len(lista) > 0 else []



# print(soluzione(lista))





"""
	17. Letter Combinations of a Phone Number
"""


dizionario = {
				'2':['a','b','c'],
			  	'3':['d','e','f']	

				}

digits = "23"



def cartesiano(lista):
	if len(lista) == 1:
		return [ [x] for x in lista[0]]
	else:
		return [ [x] +  y for x in lista[0] for y in cartesiano(lista[1:])]

def soluzione(digits):
	return cartesiano([ dizionario[x] for x in digits ])

# print(soluzione(digits))






"""
	22. Generate Parentheses
"""

parentesi_aperta = "("
parentesi_chiusa = ")"

def permutations(lista):
	if len(lista) == 0:
		return [[]]
	else:
		return [ [lista[i]] + perm for i in range(len(lista)) for perm in permutations((lista[:i]) + lista[i+1:])]


def delete_duplicates(lista):
	if len(lista) == 0:
		return []
	else:
		return [lista[0]] + delete_duplicates([z for z in lista if z != lista[0]])


def soluzione(n):
	return delete_duplicates(permutations([ x for x in ['(' for i in range(n)] + [')' for i in range(n)] ]))


#	L'idea e' quella di eliminare mano a mano dalla stringa tutte le parentesi aperte/chiuse
#	che trovo nella stringa.
#	Se non ce ne sono piu' e la stringa rimane non vuota allora sara' sbilanciata.
def is_valid(combination):
	#	0 = True 		|		 n > 0 = False
	if '()' not in combination:
		return len(combination)
	else:
		return is_valid(combination[:combination.index("()")]+combination[combination.index("()")+2:])

# print(soluzione(3))
# print(soluzione(3))


# print([reduce(lambda x,y: x+y, x) for x in soluzione(3) if is_valid(reduce(lambda x,y: x+y, x)) == 0])








"""
	scrivere la funzione che controlli che un certo linguaggio sia ben parentesizzato

"""

stringa = "[{{()}}]"

def is_valid(stringa, char):
	if char not in stringa:
		return len(stringa)
	else:
		return is_valid((stringa[:stringa.index(char)] + stringa[stringa.index(char)+2:]),char)

def soluzione(stringa):
	if len([x for x in [ is_valid(reduce(lambda x,y:x+y,[z for z in stringa if z == char[0] or z == char[1]]), char) for char in ['()','{}','[]'] ] if x != 0]) > 0:
		return "Non ben parentizzato"
	else:
		return "Ben parentizzata"

# print(soluzione(stringa))




"""
	39. Combination Sum
"""

candidates = [1]


def combinations(lista):
	if len(lista) == 0:
		return [[]]
	else:
		return combinations(lista[:-1]) + [ elemento + [lista[-1]] for elemento in combinations(lista[:-1])]


def less_n(target,lista):
	return [(x,y,int((target-x)/y)) for x in [z for z in lista if z != target ] for y in lista if (target - x)%y == 0 ]


def costruisci(first,second,times):
	return [first] + [second for i in range(times)]


def soluzione(target,lista):
	return [ costruisci(*x) for x in less_n(target, lista)] + [x for x in combinations(lista) if sum(x) == target]

# print(soluzione(2, candidates))










"""
	HAWAII
"""

stringa = "HAWAII + IDAHO + IOWA + OHIO == STATES"


def get_uniques(stringa):
	return [x for x in set(stringa) if x not in ["=" , "+", " "]]

def get_permutations(array):
	if len(array) == 0:
		return [[]]
	else:
		return [ [array[i]] + perm for i in range(len(array)) for perm in get_permutations((array[:i]) + array[i+1:])]

def get_first_lecters(stringa):
	return set([ x[0] for x in stringa.split(' ') if x not in ['==',"+"]])

def combinations(stringa):
	return [ [get_uniques(stringa), numbers[:len(get_uniques(stringa))]] for numbers in get_permutations([x for x in range(0,10)])]

def check(lecters, numbers, stringa):
	return [True if lecters[i] in get_first_lecters(stringa) and numbers[i] != 0 or lecters[i] not in get_first_lecters(stringa) else False for i in range(len(lecters))]

def take_just_ok(stringa):
	return [x for x in combinations(stringa) if all(check(x[0], x[1], stringa)) == True]

def create_sentence(lecters, numbers, stringa):
	return [  numbers[lecters.index(x)] if x not in ['==',"+", "=", ' '] else x for x in stringa ]

def soluzione(stringa):
	return [x for x in [ reduce(lambda x,y: str(x) + str(y) , (create_sentence(x[0],x[1],stringa))) for x in take_just_ok(stringa)] if eval(x) == True]

# print(soluzione(stringa))








lista = [1, -5, -2, 3, -3]


def all_combinations(lista):
	if not lista:
		return [[]]
	return all_combinations(lista[:-1]) + [x + [lista[-1]] for x in all_combinations(lista[:-1])]

def prodotto(lista):
	return max([prod(x) for x in all_combinations(lista)])

def soluzione(lista):
	return ((prodotto(lista)), [x for x in all_combinations(lista) if prod(x) == prodotto(lista)])


print(soluzione(lista))






















