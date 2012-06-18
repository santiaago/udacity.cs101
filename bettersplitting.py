#1 Gold Star

#The built-in <string>.split() procedure works
#okay, but fails to find all the words on a page
#because it only uses whitespace to split the
#string. To do better, we should also use punctuation
#marks to split the page into words.

#Define a procedure, split_string, that takes two
#inputs: the string to split and a string containing
#all of the characters considered separators. The
#procedure should output a list of strings that break
#the source string up by the characters in the 
#splitlist.

#out = split_string("This is a test-of the,string separation-code!", " ,!-")
#print out => ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

#out = split_string("After  the flood   ...  all the colors came out."," .")
#print out => ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

def split_string(source,splitlist):
	words = []
	words = source.rsplit(splitlist[0])
	
	for s in splitlist[1:]:
		words = split_list(words,s)
	return words

def split_list(words,spliter):
	#print "spliting "+str(words)
	#print "spliter "+str(spliter)
	res = []
	for w in words:
		temp = w.rsplit(spliter)
		for elem  in temp:
			res.append(elem)
	#remove empty cars
	new = []
	for w in res:
		if w != '':
			new.append(w)
	#print "result: "+str(new)
	return new