from math import cot

class PoligonoRegolare:
	def __init__(self,numero_lati,lunghezza_lati):
		self._numero_lati = numero_lati
		self._numero_lati = lunghezza_lati

	def calculate_area(self):
		return 1/4 * self.numero_lati * ((self.lunghezza_lati)**2) * cot(3.14/self.numero_lati)

	def calculate_perimeter(self):
		return numero_lati * self.lunghezza_lati

	def __str__(self):
		return "{0}{1}" . format(self.numero_lati , self.lunghezza_lati)





if __name__ == '__main__':
	d