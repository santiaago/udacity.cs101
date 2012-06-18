def find_last(s,t):
	pos = 0
	last = -1
	while(True):
		pos = s.find(t,pos)
		if(pos==-1):
			break
		last = pos
		print pos
		pos = pos +1
	
	return last

#find_last('alo','a')