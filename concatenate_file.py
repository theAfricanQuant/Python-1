# This program concatenates multiple files in the form fit1, fit2, fit3, ... fit24
# into one file called out.csv

with open("out.csv","a") as fout:
	# first file: 
	for line in open("<full_path>/fit1.csv"):     
		fout.write(line)
	# now the rest:
	for num in range(2,25):    #You can change the number of files to concatenate by changing 25 to a different number Note: range(2,25) is exclusive [2,25)
		with open(f"<full_path>/fit{str(num)}.csv") as f:
			next(f) # skip the header    
			for line in f:          
				fout.write(line)
