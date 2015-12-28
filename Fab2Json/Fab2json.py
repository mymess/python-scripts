

with open("constellationship.fab", "rt") as f:	
	try:
	    
	    rows = f.readlines()

	    with open("constellations.js", "w+") as output:

	    	s = 'var constellations = ['

	    	for row in rows:
				tokens = row.split(' ')
				s += "{0}:[ ".format(tokens[0])
				for i in xrange(3, len(tokens)-1, 2 ):
					t1 = tokens[i]
					t2 = tokens[i+1]
					s += "[{0},{1}],".format(t1, t2)
				s = s[:-1] + ' ],\n'
				


	    	s = s[:-2]
	    	s += ' ]'
	    	output.write( s );
	finally:
	    f.close()

