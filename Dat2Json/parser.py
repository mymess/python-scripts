


with open("boundaries2.dat", "r") as f:
	rows = f.readlines()
	s = ''
	with open("constellation-boundaries.js", "w") as out:
		s += "var constBoundaries = [ "
		
		for row in rows:
			tokens = row.split(' ')			
			ra = tokens[0]
			dec = tokens[1]			
			
			s += "['{0}','{1}'],".format(ra, dec) 
						
		s[:-1]
		s += ']'
		out.write( s )