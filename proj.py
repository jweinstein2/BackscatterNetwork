import scipy
from math import cos, sin, sqrt, pi
import sys
import os.path

f = scipy.fromfile(open('added.txt'), dtype=scipy.float32)
g = scipy.fromfile(open('notadd.txt'), dtype=scipy.float32)
bits = scipy.fromfile(open('bitfile'), dtype=scipy.float32)

bitter = open('/Users/Andre/Desktop/bits.txt', 'w')
for line in bits:
	bitter.write(str(line)+'\n')

# print(len(f))
tot=0
avglist=[]
bitlist=[]

bit = 1
prevAvg=0
for i in range(0,len(f)):
	# print(f[i])
	# print(g[i])

	tot+=abs(f[i])
	
	if i%7999==0 and i!=0:
		avg=tot/8000
		
		if i==7999:
			prevAvg = avg

		if abs(avg - prevAvg) > 0.4:
			bitFlip = True
		else:
			bitFlip = False

		if bitFlip:
			if bit == 1:
				bit = 0
			else:
				bit = 1

		bitlist.append(bit)

		prevAvg=avg
		tot=0
		avglist.append(avg)
	if i == 799900:
		break
# for item in avglist:
# 	print(item)
for item in bitlist:
	print(item)



	#print('\n')
	# if i%==0:
	# 	print(tot/100)
	# 	tot=0

	# 	