"""
	https://cazzola.di.unimi.it/pa-es2.html
	sin(x) can be approximate by the Taylor's series:

		SIN X = X - X^3 / 3! + X^5 / 5! - ....

	Let's write a library to implement sin(x, n) by using the Taylor's series (where n is the level of approximation, i.e., 1 only one item, 2 two items, 3 three items and so on).

	Let's compare your function with the one implemented in the math module at the growing of the approximation level.

	Hint. Use a generator for the factorial and a comprehension for the series.

"""
import re, functools

odd = lambda x :  True if x%2 != 0 else False

def sin(x,n):
	series = [ pow(x,i) / next(fattoriale(i)) for i in range(1, n*2 ) if odd(i) ]
	
	index = 1
	result = 0
	for element in series:
		if odd(index) : result +=  element 
		else :	result -= element
		index += 1
	return result

def fattoriale(i):
	accumulatore = 1
	index = 1
	while index != i:
		index += 1
		accumulatore *= index
		
	yield accumulatore
		
if __name__ == '__main__':
	# print(sin(0.24,5))

