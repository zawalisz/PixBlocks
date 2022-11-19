sentence  = str(input("Write sentence: "))
max = 0
letters=[]

for i in sentence:
	if i not in letters:
		if sentence.count(i) > max:
			letters = [i]
			max = sentence.count(i)
		elif sentence.count(i) == max:
			letters.append(i)
		
if len(letters) == 1:
	print(letters[0])
else:
	print(letters)