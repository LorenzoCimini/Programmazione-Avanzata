"""
	Let's write a module (a pool of functions) that given a quite large text (over than 2000 words) counts
	how frequent each word occurs in the text. In particular the module should provide the function freqs that
	given a filename and a number would return a list of words (with their frequencies) 
	that occur more than the given number; the list is sorted by frequency with the higher first.

	The text is read from a file and it is a real text with punctuation (i.e., commas, semicolons, ...) that
	shouldn't be counted.
	
	Note that words that differ only for the case should be considered the same.
"""

text = \
			"It is a long established fact that a reader will be distracted by the\
			readable content of a page when looking at its layout. The point of using Lorem\
			Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using\
			'Content here, content here', making it look like readable English. \
			Many desktop publishing packages and web page editors now use Lorem Ipsum \
			as their default model text, and a search for 'lorem ipsum' will uncover many web \
			sites still in their infancy. Various versions have evolved over the years, sometimes \
			by accident, sometimes on purpose (injected humour and the like)."

def check(parola , parole):
	if len(parole) == 0 : return 0
	else :
		return 1 + check(parola, parole[1:]) if parola == parole[0] else 0 + check(parola ,parole[1:])

def function():
	global text 

	characters_to_delete = ['!' , "'" , '.' , ',' , ':' , '\n' , '\t' , '(' , ')' , '-']
	for character in characters_to_delete:
		text = text.replace(character , ' ')
	words = [word.upper() for word in (text.split(' ')) if word != '']
	unique_words = set(words)
	return { parola:check(parola, words) for parola in words}


def freqs(n):
	return sorted( { key:value for (key,value) in (function()).items() if value > n}.items(), key=lambda element: element[1] , reverse=True)


if __name__ == '__main__':
	print(freqs(2))
