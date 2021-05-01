# -*- coding: utf-8 -*-

import re

def create_dict():
	dizionario = dict()
	
	with open('synonyms-list.txt') as file:
		for line in file:
			due_meta = line.split(':', 2) 
			indice = due_meta[0]
			indice = indice.strip()
			valori = re.sub("\n", "" , due_meta[1] )
			valori = valori.split(',')
			for i in range(0, len(valori)):
				valori[i] = valori[i].strip()

			dizionario.update( { indice : valori })

	return dizionario

dizionario = create_dict()

def words_to_change(list):
	return [ (list.index(word),key.upper()) for word in list for key,value in dizionario.items() if word in value]

def change_synonyms(stringa):
	words = [ word.strip(".,:;") for word in stringa.split()]
	for elem in words_to_change(words):
		words[elem[0]] = elem[1]

	return ' '.join(words)


if __name__ == '__main__':
	stringa =  "The deadline, is approximately midnight. though it could vary."
	print(change_synonyms(stringa))
	
