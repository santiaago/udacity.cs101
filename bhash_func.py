#Define a function, hash_string,
#that takes as inputs a keyword
#(string) and a number of buckets,
#and outputs a number representing
#the bucket for that keyword.

#print hash_string('a',12) => 1
#print hash_string('b',12) => 2
#print hash_string('a',13) => 6

#print hash_string('au',12) => 10
#print hash_string('udacity',12) => 11

def hash_string(keyword,buckets):
    s = 0
    for c in keyword:
        s = s+ ord(c)
    return  s%buckets

#Creating an Empty Hash Table
#Define a procedure, make_hashtable,
#that takes as input a number, nbuckets,
#and outputs an empty hash table with
#nbuckets empty buckets.

def make_hashtable(nbuckets):
    h = []
    for i in range(nbuckets):
        h.append([])
    return h
