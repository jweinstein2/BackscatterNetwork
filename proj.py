import scipy
from math import cos, sin, sqrt, pi
import sys
import os.path
import csv

samples_per_bit = 40960
max_decoded_bits = 500

# - Helper Functions
def flipbit(x):
	return abs(x - 1)

def bits_from_average(avg):
	# Returns (a, b)
	if avg >= t3:
		return (1, 1)
	if avg >= t2:
		return (0, 1)
	if avg >= t1:
		return (1, 0)
	return (0, 0)

# - Calculate Thresholds
avg_neither = scipy.fromfile(open('output/avg_neither'), dtype=scipy.float32)[samples_per_bit:samples_per_bit + 100]
avg_a = scipy.fromfile(open('output/avg_a'), dtype=scipy.float32)[samples_per_bit:samples_per_bit + 100]
avg_b = scipy.fromfile(open('output/avg_b'), dtype=scipy.float32)[samples_per_bit:samples_per_bit + 100]
avg_both = scipy.fromfile(open('output/avg_both'), dtype=scipy.float32)[samples_per_bit:samples_per_bit + 100]

# The center of each of the 4 bands (uses only first 100 bits)
neither = sum(avg_neither) / len(avg_neither)
a = sum(avg_a) / len(avg_a)
b = sum(avg_b) / len(avg_b)
both = sum(avg_both) / len(avg_both)

# Get the three thresholds based on averages of the four bands
t1 = (neither + a) / 2
t2 = (a + b) / 2
t3 = (b + both) / 2

# Make sure that our bands are in correct order.
lst = [neither, t1, a, t2, b, t3, both]
if (sorted(lst) != lst):
	print 'ERROR: assumption [neither < a < b < both] violated'
	quit()

print ('========== DECODED DATA ===========')
print ('     - ' + str(neither))
print ('  t1 - ' + str(t1))
print ('     - ' + str(a))
print ('  t2 - ' + str(t2))
print ('     - ' + str(b))
print ('  t3 - ' + str(t3))
print ('     - ' + str(both))
print ('===================================')


f = scipy.fromfile(open('output/ab_backscatter'), dtype=scipy.float32)
# f = scipy.fromfile(open('output/a_backscatter'), dtype=scipy.float32)
a_data = scipy.fromfile(open('output/a_srcdata'), dtype=scipy.float32)
b_data = scipy.fromfile(open('output/b_srcdata'), dtype=scipy.float32)

# Write input bits in readable format to a file
# bitter = open('output/a_bits_readable.txt', 'w')
# for line in a_data:
# 	bitter.write(str(line)+'\n')

avglist=[]
abitlist=[]
bbitlist=[]

# thresholdlist=[]

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
		bits = bits_from_average(avg)

		abitlist.append(bits[0])
		bbitlist.append(bits[1])

		tot=0

		avglist.append(avg)

# Print general info about decode
print('========== DECODED DATA ===========')
print('   avg    |  dbits | a_bit | b_bit ')
print('----------+--------+-------+-------')
for i in range(0, len(avglist)):
	dbits = bits_from_average(avglist[i])
	# thresh = ( int( a_data[i]) + (int( b_data[i]) * 2) )
	# thresholdlist.append( thresh )
	print(str(avglist[i])[:9]
			+ " | " + str((abitlist[i], bbitlist[i]))
			+ " |   " + str(int(a_data[i]))
			+ "   |   " + str(int(b_data[i])))
			# + '   |' + str(thresh))
print('===================================')

# output data points with expected to quickly graph
# with open("modatamoproblems.csv", "w") as f:
# 		writer = csv.writer(f)
# 		writer.writerow(avglist)
# 		writer.writerow(thresholdlist)

# Calculate the Bit Error Rate
BER = 0
for i in range(0, len(abitlist)):
	if abitlist[i] == a_data[i]:
		BER = BER + 1
	if bbitlist[i] == b_data[i]:
		BER = BER + 1
BER = 100 - ((BER * 100.0) / (len(abitlist) * 2))

print('============= SUMMARY =============')
print('             BER - ' + str(BER)[:5] + '%')
print('          length - ' + str( len(abitlist) ) + ' bits')
print(' samples per bit - ' + str(samples_per_bit))
print('===================================')
