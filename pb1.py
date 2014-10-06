st = ''
for i in range (1999,3201): 
	if i % 5 != 0 and i % 7 == 0: 
		st+=str(i)+", "
print (st)
