# Script that calculates the number of digits and letters from a sentence.

x = raw_input("Write the sentence - please include numbers and letters: ")
d = 0
l = 0
for y in x:
	if y.isdigit():
		d+=1
	elif y.isalpha():
		l+=1
	else:
		pass

print "Letters: " +str(l) + "\nDigits: " + str(d)

