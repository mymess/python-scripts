import csv
import json




with open("hygxyz.csv", "rt") as f:	
	try:
	    reader = csv.reader(f)
	    # header
	    header = reader.next()
	    #sun
	    reader.next() 

	    rows = iter(reader)
	    mapping = [header.index(x) for x in header]

	    with open("stars.js", "w+") as output:
	    	#ouput.write("starData = [\n")
			for row in rows:
				a = [row[i] for i in mapping]
				json.dump(a, output)
				output.write(",\n");
			output.write("];");
	finally:
	    f.close()

