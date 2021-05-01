import inspect

def memoization(func):
	def wrapper(*args):
		classe = inspect.getcallargs(func, *args)['self'].__class__

		cache_id = (func.__name__ + "_cache")
		
		#	Se non c'è la cache del metodo fib la creo
		if cache_id not in classe.__dict__ and (func.__name__ == "fib" or func.__name__ == "fact"):
			parameter = args[1]
			setattr(classe, cache_id, dict())
			classe.__dict__[cache_id][parameter] = func(*args)
			return func(*args)

		#	Se c'è la cache di fib controllo se ho già calcolato precedentemente il risultato
		#	della chiamata a func con il parametro 'parametro'
		elif cache_id in classe.__dict__ and (func.__name__ == "fib" or func.__name__ == "fact"):
			parameter = args[1]
			if parameter in classe.__dict__[cache_id].keys():
				print("restituisco già ho")
				return classe.__dict__[cache_id][parameter]
			else:
				return func(*args)

	return wrapper
		

def logging(func):
	def wrapper(*args):
		log = open('log.txt' , "a+")
		log.write("Nome del metodo : {0} - Argomenti : {1}\n" . format(func.__name__ , args[1]))
		log.close
		return func(*args)

	return wrapper


class MyMath:
	def __init__(self):
		pass

	#	@memoization
	@logging
	def fib(self, n, a=0, b=1, index=0):
		while True:
			if index == n:
				return a
			else:
				a,b = b, a+b
				index += 1

	#	@memoization
	@logging
	def fact(self, n):
		return 1 if n == 1 else (n * self.fact(n-1))

calcolatore = MyMath()
print(calcolatore.fact(5))
print(calcolatore.fact(5))
print(calcolatore.fib(10))