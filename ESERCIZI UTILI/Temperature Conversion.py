"""
	Beyond the well-known Celsius and Fahrenheit, there are other six temperature scales: Kelvin, Rankine, Delisle, Newton, Réaumur, and Rømer (Look at:

		http://en.wikipedia.org/wiki/Comparison_of_temperature_scales
	to read about them).

	1. Write a function (table) that given a pure number returns a conversion table for it (as a string) among any of the 8 temperature scales (remember that functions are objects as well).
	2. Write a function (toAll) that given a temperature in a specified scale returns a string for all the corresponding temperatures in the other scales, the result must be sorted on the temperatures and the scale must be specified.
"""

def fromC(x):
	return x

def toC(x):
	return x

def fromFahrenheit(x):
	return (x - 32) * 5/9

def toFahrenheit(x):
	return (x * 9/5) + 32

def table(x):
	res = " "
	temperature = toT['Celsius'](x)
	
	for name,func in toT.items():
		res = res + "{0} : {1} " .format(name, func(temperature))
	return res

def toAll(scale,temperature):
	temperature = fromT[scale](temperature)
	del toT[scale]
	res = ""

	for name,func in toT.items():
		res = res + "{0} : {1} " .format(name, func(temperature))
	return res

if __name__ == '__main__':
	fromT = { 'Celsius' : fromC , 'Fahrenheit' : fromFahrenheit}
	toT = {'Celsius' : toC , 'Fahrenheit' : toFahrenheit }

	# print(table(100))
	print(toAll('Celsius' , 100))
