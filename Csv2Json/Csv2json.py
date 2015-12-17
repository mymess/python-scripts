import csv
import json




with open("hygxyz.csv", "rt") as f:	
	try:
	    reader = csv.reader(f)
	    with open("stars.js", "wa") as output:
	    	ouput.write("starData = ")
		    for row in reader:
		        json.dump(row, output)
	finally:
	    f.close()

