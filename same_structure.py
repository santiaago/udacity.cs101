#Same Structure

#Define a procedure, same_structure, that takes two inputs. It should output
#True if the lists contain the same elements in the same structure, and False
#otherwise. Two values, p and q have the same structure if:

#    Neither p or q is a list.

#    Both p and q are lists, they have the same number of elements, and each
#    element of p has the same structure as the corresponding element of q.


#For this procedure, you can use the is_list(p) procedure from Homework 6:

def is_list(p):
    return isinstance(p, list)


def same_structure(a,b):
    if is_list(a) == is_list(b):

        if not is_list(a):#Neither a or b is a list.
            print "Passed: Neither "+str(a)+" or "+str(b)+" is a list."
            return True
        if len(a) != len(b):#Not the same number of elems
            print "Failed: len(a)="+str(len(a))+" != len(b)="+str(len(b))
            return False
        is_samestruct = True
        for i in range(len(a)):
            if not same_structure(a[i],b[i]):
                is_samestruct = False
                break
        return is_samestruct
    else:
        print "Failed a and b are not the same structure"
        return False


#Here are some examples:

print same_structure(3, 7)
#>>> True

print same_structure([1, 0, 1], [2, 1, 2])
#>>> True

print same_structure([1, [0], 1], [2, 5, 3])
#>>> False

print same_structure([1, [2, [3, [4, 5]]]], ['a', ['b', ['c', ['d', 'e']]]])
#>>> True

print same_structure([1, [2, [3, [4, 5]]]], ['a', ['b', ['c', ['de']]]])
#>>> False
print same_structure(3, [7])
#>>> False
print same_structure([1, [0], 1], [2, [5], 3])
#>>> True
print same_structure([1, [0], 1], [2, 5, [3]])
#false
print same_structure([1, [], 1], [2, [5], 3]) 
#== False
print same_structure([1,2,3,[1,[1],2], [[1,2]]], [1,2,3,[1,[],2], [[1,2]]]) 
#== False
print same_structure([1,2,3,[1,1,2], [[1,2]]], [1,2,3,[1,[],2], [[1,2]]]) 
#== False
print same_structure([1], 7) 
#== False
print same_structure([[1,2,3,['d']],4,[1,['g','g',[]]]], [['h',1,'f',[8]],'y',['k',[4,7,8]]]) 
#== False
print same_structure ([1,[1]],[1,[1,2,3]]) #== False
print same_structure([1,2,3,[1,1,2], [[1,2]]], [1,2,3,[1,[],2], [[1,2]]]) #== False