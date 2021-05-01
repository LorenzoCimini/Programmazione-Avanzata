"""
	https://pythonschool.net/basics/iteration-exercises/

	Create a program which will convert a given decimal up to 255 into its 8-bit binary equivalent.
"""

class eight_bit_converter():
	def __init__(self):
		self.numero = 0

	def __iter__(self):
		return self

	def __next__(self):
		self.numero += 1

		self.tmp = self.numero
		self.result = " "
		while True:
			if self.tmp == 1 : 
				result = str(1) + self.result
				break
			else :
				if self.tmp % 2 == 0 : 
					self.result = str(0) + self.result
					self.tmp = int(self.tmp / 2)
				else : 
					self.result = str(1) + self.result 
					self.tmp = int(self.tmp / 2)

		self.diff = 8 - len(result)
		return (str(0) * self.diff) + result

"""	In questo caso però non posso manipolare la stringa prima del return per rendere la stringa sempre 8-bit."""
def recursion(number):
	if number == 1 : 
		return "1"
	else :
		if number % 2 == 0 : return "0" + recursion(int(number/2))
		else : return "1" + recursion(int(number/2))




if __name__ == '__main__':
	print (recursion(9)[::-1])
	 
	convertitore = eight_bit_converter()
	lista = iter(convertitore)
	
	print ( [ next(convertitore) for i in range(1,20)][8])

