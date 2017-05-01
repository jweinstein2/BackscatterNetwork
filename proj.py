import scipy
from math import cos, sin, sqrt, pi
import sys
import os.path
import csv

# - Helper Functions
def flipbit(x):
	return abs(x - 1)

f = scipy.fromfile(open('output/ab_backscatter'), dtype=scipy.float32)
# f = scipy.fromfile(open('output/a_backscatter'), dtype=scipy.float32)
a_data = scipy.fromfile(open('output/a_srcdata'), dtype=scipy.float32)
b_data = scipy.fromfile(open('output/b_srcdata'), dtype=scipy.float32)

# Write input bits in readable format to a file
# bitter = open('output/a_bits_readable.txt', 'w')
# for line in a_data:
# 	bitter.write(str(line)+'\n')

samples_per_bit = 40960
max_decoded_bits = 500
first_bit = int(a_data[0])
avglist=[]
bitlist=[]

thresholdlist=[]

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
		if abs(avg - prevAvg) > 500:
			bitlist.append( flipbit( prevbit ))
		else:
			bitlist.append( prevbit )

		tot=0

		avglist.append(avg)

# Print general info about decode
print('========== DECODED DATA ===========')
print('   avg    |  dbit | a_bit | b_bit ')
print('----------+-------+--------+-------')
for i in range(0, len(avglist)):
	thresh = ( int( a_data[i]) + (int( b_data[i]) * 2) )
	thresholdlist.append( thresh )
	print(str(avglist[i])[:9]
			+ " |   " + str(bitlist[i])
			+ "   |   " + str(int(a_data[i]))
			+ "   |   " + str(int(b_data[i]))
			+ '   |' + str(thresh))
print('===================================')

# output data points with expected to quickly graph
# with open("modatamoproblems.csv", "w") as f:
# 		writer = csv.writer(f)
# 		writer.writerow(avglist)
# 		writer.writerow(thresholdlist)

# Calculate the Bit Error Rate
BER = 0
for i in range(0, len(bitlist)):
	if bitlist[i] == a_data[i]:
		BER = BER + 1
BER = 100 - ((BER * 100.0) / len(bitlist))

print('============= SUMMARY =============')
print('             BER - ' + str(BER) + '%')
print('          length - ' + str( len(bitlist) ) + ' bits')
print(' samples per bit - ' + str(samples_per_bit))
print('===================================')
