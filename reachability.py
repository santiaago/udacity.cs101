#Reachability

#Single Gold Star

#Define a procedure, reachable(graph, node), that takes as input a graph and a
#starting node, and returns a list of all the nodes in the graph that can be
#reached by following zero or more edges starting from node.  The input graph is
#represented as a Dictionary where each node in the graph is a key in the
#Dictionary, and the value associated with a key is a list of the nodes that the
#key node is connected to.  The nodes in the returned list may appear in any
#order, but should not contain any duplicates.


def reachable(graph, node):
    res = []
    res.append(node)
    try:
        v = graph[node]
        for n in v:
            try:
                if n not in res:
                    res.append(n)
                r = []
                try:
                    r = graph[n]
                except:
                    pass
                for i in r:
                    if i not in res:
                        v.append(i)
            except:
                pass
    except:
        pass
    return res


#For example,

graph = {'a': ['b', 'c'], 'b': ['a', 'c'], 'c': ['b', 'd'], 'd': ['a'], 'e': ['a']}

print reachable(graph, 'a')
#>>> ['a', 'c', 'd', 'b']

print reachable(graph, 'd')
#>>> ['d', 'a', 'c', 'b']

print reachable(graph, 'e')
#>>> ['e', 'a', 'c', 'd', 'b']
graph = {'a': ['b'], 'b': ['h'], 'c': ['h'], 'd':[], 'e': ['j'], 'f': ['a','c','e'], 'g': ['a'], 'h': ['g'], 'i': ['h','e'], 'j': ['d']}
print reachable(graph, 'a')
print reachable(graph, 'b')
print reachable(graph, 'c')
print reachable(graph, 'd')
print reachable(graph, 'e')
print reachable(graph, 'f')
print reachable(graph, 'g')
print reachable(graph, 'h')
print reachable(graph, 'i')
print reachable(graph, 'j')



graph = {'a': ['b', 'c'], 'b': ['a', 'c'], 'c': ['b', 'd'], 'd': ['a'], 'e': ['a']}
print sorted(reachable(graph, 'a')) == sorted(['a', 'c', 'd', 'b'])
print sorted(reachable(graph, 'd')) == sorted(['d', 'a', 'c', 'b'])
print sorted(reachable(graph, 'e')) == sorted(['e', 'a', 'c', 'd', 'b'])
print sorted(reachable(graph, 'c')) == sorted(['a', 'c', 'd', 'b'])

graph = {'a': ['b'], 'b': ['h'], 'c': ['h'], 'd':[], 'e': ['j'], 'f': ['a','c','e'], 'g': ['a'], 'h': ['g'], 'i': ['h','e'], 'j': ['d']}
print sorted(reachable(graph, 'a')) == sorted(['a', 'b', 'h', 'g'])
print sorted(reachable(graph, 'b')) == sorted(['b', 'h', 'g', 'a'])
print sorted(reachable(graph, 'c')) == sorted(['c', 'h', 'g', 'a', 'b'])
print sorted(reachable(graph, 'd')) == sorted(['d'])
print sorted(reachable(graph, 'e')) == sorted(['e', 'j', 'd'])
print sorted(reachable(graph, 'f')) == sorted(['f', 'a', 'c', 'e', 'b', 'h', 'j', 'g', 'd'])
print sorted(reachable(graph, 'g')) == sorted(['g', 'a', 'b', 'h'])
print sorted(reachable(graph, 'h')) == sorted(['h', 'g', 'a', 'b'])
print sorted(reachable(graph, 'i')) == sorted(['i', 'h', 'e', 'g', 'j', 'a', 'd', 'b'])
print sorted(reachable(graph, 'j')) == sorted(['j', 'd'])


graph = {'a': ['m', 'c'], 'b': ['a', 'c']}
print reachable(graph, 'q')
print reachable(graph, 'a')