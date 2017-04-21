import scipy
from math import cos, sin, sqrt, pi
import sys
import os.path

# - Helper Functions
def flipbit(x):
	return abs(x - 1)

f = scipy.fromfile(open('output/a_backscatter'), dtype=scipy.float32)
# g = scipy.fromfile(open('/output/notadd.txt'), dtype=scipy.float32)
bits = scipy.fromfile(open('output/a_srcdata'), dtype=scipy.float32)

# Write input bits in readable format to a file
bitter = open('output/bits_readable.txt', 'w')
for line in bits:
	bitter.write(str(line)+'\n')

samples_per_bit = 8000
max_decoded_bits = 100
first_bit = 1
avglist=[]
bitlist=[]

tot = 0
for i in range(1 ,len(f) + 1):
	# Check if we've hit our max bits decoded
	if (i > max_decoded_bits * samples_per_bit):
		print('manually stopping b/c hit max')
		break

	power = abs( f[i - 1] )
	tot += power

	# If we are at the cutoff between two windows
	if i % (samples_per_bit) == 0:
		avg = tot / samples_per_bit
		prevAvg = avg if len(avglist) == 0 else avglist[-1]

		prevbit = first_bit if len(bitlist) == 0 else bitlist[-1]
		if abs(avg - prevAvg) > 0.4:
			bitlist.append( flipbit( prevbit ))
		else:
			bitlist.append( prevbit )

		tot=0
		avglist.append(avg)

# print('======== AVG LIST ========')
# for item in avglist:
# 	print(item)
# print('==========================')

# print('======== BIT LIST ========')
# for item in bitlist:
# 	print(item)
# print('==========================')

# print('======== ORIGINAL BIT LIST ========')
# for bit in bits:
# 	print(int(bit))
# print('===================================')

BER = 0
for i in range(0, len(bitlist)):
	if bitlist[i] == bits[i]:
		BER = BER + 1
BER = (BER * 100.0) / len(bitlist)

print('=========== SUMMARY ===========')
print('      BER - ' + str(BER) + '%')
print('   length - ' + str( len(bitlist) ) + ' bits')
print('===============================')
