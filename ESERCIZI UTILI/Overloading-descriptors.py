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


import functools

class grade_avarage:
	def __get__(self, instance, owner):
		voti = [ voto for corso,voto in instance.lectures.items() ]
		return (functools.reduce(lambda x,y : x + y , voti )) / len(voti)


class Student(Person):
	def __init__(self, name, lastname, birthday, lectures):
		self.name = name 
		self.lastname = lastname
		self.birthday = birthday
		self.lectures = lectures

	def __repr__(self):
		return "Nome : {0}\nCognome: {1}\nCompleanno: {2}\nVoti: {3}" . format(self.name, self.lastname, self.birthday , self.lectures)

	grade_avarage = grade_avarage()




class DaySalary:
	def __get__(self, instance, owner):
		return instance.pay_per_hour * 8 

	def __set__(self, instance, value):
		instance.pay_per_hour = value / 8 

class WeekSalary:
	def __get__(self, instance, owner):
		return instance.day_salary * 7

	def __set__(self, instance, value):
		instance.pay_per_hour = (value / 7) / 8

class MonthSalary:
	def __get__(self, instance, owner):
		return instance.week_salary * 4

	def __set__(self, instance, value):
		instance.pay_per_hour = ((value / 4) / 7) / 8

class YearSalary:
	def __get__(self, instance, owner):
		return instance.month_salary * 12

	def __set__(self, instance, value):
		instance.pay_per_hour = (((value / 12) / 4) / 7 ) / 8

class Worker(Person):
	def __init__(self, name, lastname, birthday, pay_per_hour):
		self.name = name
		self.lastname = lastname
		self.birthday = birthday
		self.pay_per_hour = pay_per_hour

	def __str__(self):
		return "Orario : {0:8.2f} Giornaliero: {1:8.2f} Settimanale : {2:8.2f} , Mensile : {3:8.2f} , Annuale : {4:8.2f} " . \
				format (self.pay_per_hour , self.day_salary , self.week_salary , self.month_salary, self. year_salary)

	day_salary = DaySalary()
	week_salary = WeekSalary()
	month_salary = MonthSalary()
	year_salary = YearSalary()


lorenzo = Worker("Lorenzo" , "Cimini" , "11/07/1997" , 20)
lorenzo.month_salary = 1000
print(lorenzo)






















