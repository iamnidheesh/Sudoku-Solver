def output(grid,myfile) :

	solution = open(myfile,'w')
	pprint(grid,myfile)

def pprint(grid,myfile) :
	for i in range(9) :
		for j in range(9) :
			print(grid[i][j],end = " ",file = myfile)
			if(j == 2 or j == 5) :
				print("|",end = " ",file = myfile)
		if(i == 2 or i == 5) :
			print("",file = myfile)
			print("---------------------",file = myfile)
		else :
			print("",file = myfile)

def pprint(grid) :
	for i in range(9) :
		for j in range(9) :
			print(grid[i][j],end = " ")
			if(j == 2 or j == 5) :
				print("|",end = " ")
		if(i == 2 or i == 5) :
			print()
			print("---------------------")
		else :
			print()