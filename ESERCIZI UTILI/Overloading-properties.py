import functools

"""
	Let us consider a class Person with the following attributes: name, lastname, birthday with the 
	obvious meaning and the corresponding setter and getters and the __repr__ to print it.

	-	Extend the class Person in the class Student by adding a dictionary lectures with the lecture 
		name as a key and the mark as a value, and the property grade_average to calculate the marks 
		average
	-	Extend the class Person in the class Worker by adding an attribute pay_per_hour and the properties 
		day_salary, week_salary, month_salary, and year_salary considering 8 working hours a day, 5 
		working days a week, 4 weeks a month, 12 months a year; note that to set one of the properties 
		implies to recalculate the pay_per_hour value
	-	Extend the class Person in the class Wizard by adding a property age that when used as a getter 
		calculates the correct age in term of passed days from the birthday to the current day and when 
		used as a setter it will change the birthday accordingly rejuvenating or getting old magically.

"""

class Person:
	def __init__(self ,name , lastname, birthday):
		self._name = name 
		self._lastname = lastname
		self._birthday = birthday

	def get_name(self):
		return self.name

	def set_name(self, name):
		self.name = name 

	def get_lastname(self):
		return self.lastname

	def set_lastname(self, lastname):
		self.lastname = lastname

	def get_birthday(self):
		return self.birthday

	def set_birthday(self, birthday):
		self.birthday = birthday

	def __repr__(self):
		return "Nome : {0}\nCognome: {1}\nCompleanno: {2}" . format(self.name, self.lastname, self.birthday)



class Student(Person):
	def __init__(self, name, lastname, birthday, lectures):
		self._name = name 
		self._lastname = lastname
		self._birthday = birthday
		self._lectures = lectures

	def __repr__(self):
		return "Nome : {0}\nCognome: {1}\nCompleanno: {2}\nVoti: {3}" . format(self.name, self.lastname, self.birthday , self.lectures)

	def get_avarage(self):
		return (functools.reduce(lambda x,y : x + y , [ voto for corso,voto in self.lectures.items() ])) / len(voti)

	grade_avarage = property(get_avarage, None, None, "Calcolo media voti")




class Worker(Person):
	def __init__(self, name, lastname, birthday, pay_per_hour):
		self.name = name
		self.lastname = lastname
		self.birthday = birthday
		self.pay_per_hour = pay_per_hour

	def get_day_salary(self):
		return self.pay_per_hour * 8

	def set_day_salary(self, salary):
		self.pay_per_hour = salary / 8

	def get_week_salary(self):
		return self.day_salary * 5

	def set_week_salary(self, salary):
		self.pay_per_hour = (salary / 5) / 8

	def get_month_salary(self):
		return self.week_salary * 4

	def set_month_salary(self, salary):
		self.pay_per_hour = ((salary / 4) / 5) / 8

	def get_year_salary(self):
		return self.month_salary * 12

	def set_year_salary(self, salary):
		self.pay_per_hour = (((salary / 12) / 4) / 5) / 8

	def __str__(self):
		return "Oraria: {0:8.2f} , Giornaliera: {1:8.2f} , Settimanale: {2:8.2f} , Mensile: {3:8.2f} , Annuale{4:8.2f} "\
				.format(self.pay_per_hour , self.day_salary, self.week_salary, self.month_salary, self.year_salary) 

	day_salary = property(get_day_salary, set_day_salary, None, "Salario Giornaliero")
	week_salary = property(get_week_salary, set_week_salary, None, "Salario Settimanale")
	month_salary = property(get_month_salary, set_month_salary, None, "Salario Mensile")
	year_salary = property(get_year_salary, set_year_salary, None, "Salario Annuale")

from datetime import datetime,date

class Wizard(Person):
	def __init__(self, name, lastname, birthday):
		self.name = name
		self.lastname = lastname
		self.birthday = birthday


	def get_age(self):
		giorno, mese, anno = self.birthday.split('/')
		prima_data = datetime(int(anno), int(mese), int(giorno),0,0)
		seconda_data = datetime.today()
		return (seconda_data - prima_data).days

	def set_age(self, new_birthday):
		self.birthday = new_birthday


	age = property(get_age, set_age, None, "Wizard Age")




if __name__ == '__main__':
	lorenzo = Wizard("Lorenzo", "Cimini", "11/07/1997")
	print(lorenzo.age)
	lorenzo.age = "01/02/2021"
	print(lorenzo.age)

