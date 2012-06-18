#Spelling Correction

#Double Gold Star

#For this question, your goal is to build a step towards a spelling corrector,
#similarly to the way Google used to respond,

#    "Did you mean: audacity"


#when you searched for "udacity" (but now considers "udacity" a real word!).

#One way to do spelling correction is to measure the edit distance between the
#entered word and other words in the dictionary.  Edit distance is a measure of
#the number of edits required to transform one word into another word.  An edit
#is either: (a) replacing one letter with a different letter, (b) removing a
#letter, or (c) inserting a letter.  The edit distance between two strings s and
#t, is the minimum number of edits needed to transform s into t.

#Define a procedure, edit_distance(s, t), that takes two strings as its inputs,
#and returns a number giving the edit distance between those strings.

#Note: it is okay if your edit_distance procedure is very expensive, and does
#not work on strings longer than the ones shown here.

#The built-in python function min() returns the mininum of all its arguments.

#print min(1,2,3)
#>>> 1

def edit_distance(s,t):
    
    len_s = len(s)
    len_t = len(t)

    #build levenshtein matrix
    matrix = [range(len_s+1)]*(len_t+1)
    for row in range(len_t+1):
        matrix[row] = range(row,row+len_s+1)
    
    for indexT in range(0,len_t):

        for indexS in range(0,len_s):

            if s[indexS] == t[indexT]:
                matrix[indexT+1][indexS+1] = min ( matrix[ indexT + 1 ][ indexS ] + 1 , matrix[ indexT ][ indexS + 1 ] + 1 , matrix[ indexT ][ indexS ] )
            else:
                matrix[indexT+1][indexS+1] = min ( matrix[ indexT + 1 ][ indexS ] + 1 , matrix[ indexT ][ indexS + 1 ] + 1 , matrix[ indexT ][ indexS ] + 1 )

    return matrix[len_t][len_s]


def levenshtein(s1, s2):
    l1 = len(s1)
    l2 = len(s2)

    matrix = [range(l1 + 1)] * (l2 + 1)
    for zz in range(l2 + 1):
        matrix[zz] = range(zz,zz + l1 + 1)
    for zz in range(0,l2):
        for sz in range(0,l1):
            if s1[sz] == s2[zz]:
                matrix[zz+1][sz+1] = min(matrix[zz+1][sz] + 1, matrix[zz][sz+1] + 1, matrix[zz][sz])
            else:
                matrix[zz+1][sz+1] = min(matrix[zz+1][sz] + 1, matrix[zz][sz+1] + 1, matrix[zz][sz] + 1)
    print "That's the Levenshtein-Matrix:"
    #printMatrix(matrix)
    return matrix[l2][l1]
    


#For example:

# Delete the 'a'
print edit_distance('audacity', 'udacity')
#>>> 1

# Delete the 'a', replace the 'u' with 'U'
print edit_distance('audacity', 'Udacity')
#>>> 2

# Five replacements
print edit_distance('peter', 'sarah')
#>>> 5

# One deletion
print edit_distance('pete', 'peter')
#>>> 1
t=[
            ['audacity',        'udacity',      1],
            ['audacity',        'Udacity',      2],
            ['peter',           'sarah',        5],
            ['pete',            'peter',        1],
            ['udc',             'audacity',     5],
            ['audacity',        'udc',          5],
            ['audacity',        'udacious',     4],
            ['python',          'pytohn',       2],
            ['udacity',         'university',   6],
            ['university',      'udacity',      6],
            ['edata',           'database',     5],
            ['smothered',       'moth',         5],
            ['moth',            'smothered',    5],
            ['smothered',       'other',        4],
            ['other',           'smothered',    4],
            ['the',             'smothered',    6],
            ['smothered',       'the',          6],
            ['there',           'smothered',    4],
            ['smothered',       'there',        4],
            ['horror',          'mirror',       2],
            ['beehive',         'behave',       2],
            ['audacity',        'xurdrity',     4],
            ['A man, a plan, a canal - Panama!',        'Doc, note: I dissent. A fast never prevents a fatness. I diet on cod.',        54],
            ['amanaplanacanalpanama',        'docnoteidissentafastneverpreventsafatnessidietoncod',        42],
            ['klebsiella pneumonia',        'salivating puma',        15]
        ]
for y in t:
	print "edit_distance('",y[0],"','",y[1],"') = ",edit_distance(y[0],y[1]),y[2]