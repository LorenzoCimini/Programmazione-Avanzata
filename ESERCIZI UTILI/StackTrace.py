"""
	Let us consider a class MyMath with the following methods: fib, fact and taylor implementing the 
	Fibonacci's series, the factorial and the Taylor's series for a generic function and a level of 
	approximation respectively. Then implement the following decorators:

	-	@stack_trace applied to a method prints its stack trace, i.e., the list of calls made to carry 
		out the invocation.

"""
import inspect


def StackTracer(func):
	space = 0
	def wrapper(*args, **kwargs):
		"""
			-	Catturo il frame nel quale viene eseguita la funzione ( in questo caso è wrappato dal frame del decoratore ) - avrei anche potuto
				utilizzare il parametro f_back per ottenere il frame della funzione chiamante.
			-	Ottengo il nome della funzione contenuta nel frame catturato.
			-	Ottengo anche i parametri passati alla funzione 
		"""
		nonlocal space
		current_frame = inspect.currentframe()
		called_function = (current_frame.f_locals)['func'].__name__
		parameters = inspect.getargvalues(current_frame)[3]['args'][1]
		
		print("{0} E' stata chiamata la funzione {1} con parametri : {2} " . format(' ' * space, called_function , parameters))
		space += 2
		return func(*args, **kwargs)
	return wrapper


class MyMath:
	def __init__(self):
		pass

	@StackTracer
	def factorial(self,n):
		if n == 1 : return 1 
		else :
			return n * self.factorial ( n - 1 )
	@StackTracer
	def fibo(self,n):
		if n == 0: return 0
		elif n == 1: return 1
		else : return self.fibo(n-1) + self.fibo(n-2)

calcolatore = MyMath()
print(calcolatore.factorial(4))
#print(calcolatore.fibo(5))
