#Multi-word Queries

#Triple Gold Star

#For this question, your goal is to modify the search engine to be able to
#handle multi-word queries.  To do this, we need to make two main changes:

#    1. Modify the index to keep track of not only the URL, but the position
#    within that page where a word appears.

#    2. Make a version of the lookup procedure that takes a list of target
#    words, and only counts a URL as a match if it contains all of the target
#    words, adjacent to each other, in the order they are given in the input.

#For example, if the search input is "Monty Python", it should match a page that
#contains, "Monty Python is funny!", but should not match a page containing
#"Monty likes the Python programming language."  The words must appear in the
#same order, and the next word must start right after the end of the previous
#word.

#Modify the search engine code to support multi-word queries. Your modified code
#should define these two procedures:

#    crawl_web(seed) => index, graph
#        A modified version of crawl_web that produces an index that includes
#        positional information.  It is up to you to figure out how to represent
#        positions in your index and you can do this any way you want.  Whatever
#        index you produce is the one we will pass into your multi_lookup(index,
#        keyword) procedure.

#    multi_lookup(index, list of keywords) => list of URLs
#        A URL should be included in the output list, only if it contains all of
#        the keywords in the input list, next to each other.


def multi_lookup(index, query):
    def positions(line,url):
        res = []
        for e in line:
            if e[0]== url:
                res.append(e[1])#append position
        return res

    #print "multi_lookup"
    results= []
    for keyword in query:
        if keyword in index:
            results.append(lookup(index,keyword))
    #print 'results: '
    #for r in results:
    #    print str(r)
    #return empty list if not all keywords are in the results (ie: keyword missing ie: multilookup fail)
    if len(query) != len(results):
        return []
    if len(query)==0:
        return []
    listUrl= []
    currentPositions= []
    for urlNpositions in results[0]:
        url = urlNpositions[0]
        p = urlNpositions[1]
        #print "looking for url:"+str(url)
        listUrl.append(url)
        for line in results[1:]:
            currentPositions = positions(line,url)
            #print 'current positions of url:'+str(url)+' are:'+str(currentPositions)
            #print "P="+str(p)
            if (p+1) not in currentPositions:
                try:
                    #print 'removing '+str(url) 
                    i = listUrl.index(url)
                    listUrl.pop(i)
                    break#only pop once for each  line
                except:
                    pass
            p = p + 1 #update position count
    #result should only have unique urls
    res = []
    for url in listUrl:
        if url not in res:
            res.append(url)
    return res

            

def crawl_web(seed): # returns index, graph of inlinks
    tocrawl = [seed]
    crawled = []
    graph = {}  # <url>, [list of pages it links to]
    index = {} 
    while tocrawl: 
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            outlinks = get_all_links(content)
            graph[page] = outlinks
            union(tocrawl, outlinks)
            crawled.append(page)
    return index, graph


def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)

def add_page_to_index(index, url, content):
    words = content.split()
    i = 0
    for word in words:
        add_to_index(index, word, [url,i])
        i=i+1
        
def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]

def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None
    



cache = {
   'http://www.udacity.com/cs101x/final/multi.html': """<html>
<body>

<a href="http://www.udacity.com/cs101x/final/a.html">A</a><br>
<a href="http://www.udacity.com/cs101x/final/b.html">B</a><br>

</body>
""", 
   'http://www.udacity.com/cs101x/final/b.html': """<html>
<body>

Monty likes the Python programming language
Thomas Jefferson founded the University of Virginia
When Mandela was in London, he visited Nelson's Column.

</body>
</html>
""", 
   'http://www.udacity.com/cs101x/final/a.html': """<html>
<body>

Monty Python is not about a programming language
Udacity was not founded by Thomas Jefferson
Nelson Mandela said "Education is the most powerful weapon which you can
use to change the world."
</body>
</html>
""", 
}

def get_page(url):
    if url in cache:
        return cache[url]
    else:
        print "Page not in cache: " + url
        return None
    





#Here are a few examples from the test site:

index, graph = crawl_web('http://www.udacity.com/cs101x/final/multi.html')
#print index
#print graph
#print lookup(index, 'Python')
#print lookup(index, 'Monty')

print multi_lookup(index, ['Python'])
#>>> ['http://www.udacity.com/cs101x/final/b.html', 'http://www.udacity.com/cs101x/final/a.html']

print multi_lookup(index, ['Monty', 'Python'])
#>>> ['http://www.udacity.com/cs101x/final/a.html']

print multi_lookup(index, ['Python', 'programming', 'language'])
#>>> ['http://www.udacity.com/cs101x/final/b.html']

print multi_lookup(index, ['Thomas', 'Jefferson'])
#>>> ['http://www.udacity.com/cs101x/final/b.html', 'http://www.udacity.com/cs101x/final/a.html']

print multi_lookup(index, ['most', 'powerful', 'weapon'])
#>>> ['http://www.udacity.com/cs101x/final/a.html']
print "1"
print sorted(multi_lookup(index, ['the']))
#['http://www.udacity.com/cs101x/final/a.html', 'http://www.udacity.com/cs101x/final/b.html']
print "2"
print sorted(multi_lookup(index, ['the', 'Python']))
#['http://www.udacity.com/cs101x/final/b.html']
print "3"
print sorted(multi_lookup(index, ['the', 'University']))
#['http://www.udacity.com/cs101x/final/b.html']
print "4"
print sorted(multi_lookup(index, ['the', 'World']))
print 5
print sorted(multi_lookup(index, []))
print 6
print sorted(multi_lookup(index, ['']))
print sorted(multi_lookup(index, [' ']))
print sorted(multi_lookup(index, ['not_exist']))
print sorted(multi_lookup(index, ['python']))
print sorted(multi_lookup(index, ['Python', 'not_exist']))
print sorted(multi_lookup(index, ['not_exist', 'Python']))
print sorted(multi_lookup(index, ['Python', 'Python']))
print sorted(multi_lookup(index, ['University', 'Virginia']))
print sorted(multi_lookup(index, ['Python','Monty']))
print sorted(multi_lookup(index, ['programming', 'language']))
print sorted(multi_lookup(index, ['programming', 'language', 'Udacity']))
print sorted(multi_lookup(index, ['Python', 'programming', 'language']))
print sorted(multi_lookup(index, ['Thomas', 'Jefferson', 'founded']))
print sorted(multi_lookup(index, ['is']))
print sorted(multi_lookup(index, ['is', 'not', 'about']))
print sorted(multi_lookup(index, ['<html>', '<body>']))
print sorted(multi_lookup(index, ['Thomas', 'Jefferson', 'founded', 'the', 'University', 'of', 'Virginia']))
print sorted(multi_lookup(index, ['the']))
print sorted(multi_lookup(index, ['the', 'Python']))
print sorted(multi_lookup(index, ['the', 'University']))
print sorted(multi_lookup(index, ['the', 'World']))
print sorted(multi_lookup(index, ['', 'Virginia']))
print multi_lookup(index, ['Python','Monty'])



