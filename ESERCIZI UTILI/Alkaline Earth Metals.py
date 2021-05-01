"""
	Assign a list that contains the atomic numbers and the names of the six alkaline earth metals 
	-barium (56), beryllium (4), calcium (20), magnesium (12), radium (88), and strontium (38)--
	to a variable called alkaline_earth_metals.

	V 1. Write a one-liner that returns the highest atomic number in alkaline_earth_metals.
	V 2. Using one of the list methods, sort alkaline_earth_metals in ascending order (from the lightest to the heaviest).
	V 3. Transform the alkaline_earth_metals into a dictionary using the name of the metals as the dictionary's key.
	V 4. Create a second dictionary containing the noble gases -- helium (2), neon (10), argon (18), krypton (36), 
	   xenon (54), and radon (86) -- and store it in the variable noble_gases.
	5. Merge the two dictionaries and print the result as couples (name, atomic number) sorted 
	   in ascending order on the element names.

	Note that Python's dictionaries neither preserve the insertion order nor are sorted in some way.


"""



def ascending_order(list_of_metals):
	return sorted(list_of_metals, key = lambda ele : ele[1])


def highest(list_of_metals):
	return sorted(list_of_metals , key = lambda ele : ele[1] , reverse = True)[0][1]

def create_dict(list_of_metals):
	return dict(list_of_metals)

def merge_dicts(first , second):
	tmp = dict()
	tmp.update(first)
	tmp.update(second)

	return { key:value for key,value in sorted(tmp.items() , key= lambda ele : ele) }

if __name__ == '__main__':
	alkaline_earth_metals = \
		[ 
			('barium' , 56) , ('beryllium' , 4) , ('calcium' , 20) ,
			('magnesium' , 12) , ('radium' , 88) , ('strontium' , 38)
		]
	
	# print("Il numero atomatico più grande e' {0}" . format(highest(alkaline_earth_metals)))
	# print("La lista degli elementi ordinata in ordine ascendente : \n {0}"  . format(ascending_order(alkaline_earth_metals)))
	# print("Il dizionario e' : {0} " . format(create_dict(alkaline_earth_metals)))

	noble_gases = { \
		'helium' : 2 , 'neon' : 10 , ' argon' : 18 , 'krypton' : 16 , 
		'xenon' : 54 , 'radeon' : 86
	}

	print(merge_dicts(create_dict(alkaline_earth_metals) , noble_gases))