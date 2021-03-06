import scipy
from math import cos, sin, sqrt, pi
import sys
import os.path
import csv
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

def calculateBER():
	samples_per_bit = 40960
	max_decoded_bits = 100

	# - Helper Functions
	def flipbit(x):
		return abs(x - 1)

	def bits_from_average(avg):
		# Returns (a, b)
		if avg >= t3:
			return 2
		if avg >= t1:
			return 1
		return 0


	# - Calculate Thresholds
	avg_neither = scipy.fromfile(open('output/avg_neither'), dtype=scipy.float32)[samples_per_bit:samples_per_bit + 100]
	avg_a = scipy.fromfile(open('output/avg_a'), dtype=scipy.float32)[samples_per_bit:samples_per_bit + 100]
	avg_b = scipy.fromfile(open('output/avg_b'), dtype=scipy.float32)[samples_per_bit:samples_per_bit + 100]
	avg_both = scipy.fromfile(open('output/avg_both'), dtype=scipy.float32)[samples_per_bit:samples_per_bit + 100]

	# The center of each of the 4 bands (uses only first 100 bits)
	try:
		neither = sum(avg_neither) / len(avg_neither)
		a = sum(avg_a) / len(avg_a)
		b = sum(avg_b) / len(avg_b)
		both = sum(avg_both) / len(avg_both)
	except ZeroDivisionError:
		print("ERROR: divide by 0")
		return -1
	# Get the three thresholds based on averages of the four bands
	if (a > b):
		temp = a
		a=b
		b=temp

	t1 = (neither + a) / 2
	t2 = (a + b) / 2
	t3 = (b + both) / 2

	#Print Threshold Information
	print ('========== DECODED DATA ===========')
	print ('     - ' + str(neither))
	print ('  t1 - ' + str(t1))
	print ('     - ' + str(a))
	print ('  t2 - ' + str(t2))
	print ('     - ' + str(b))
	print ('  t3 - ' + str(t3))
	print ('     - ' + str(both))
	print ('===================================')

	#Open files
	f = scipy.fromfile(open('output/ab_backscatter'), dtype=scipy.float32)
	a_sig = scipy.fromfile(open('output/a_signal'), dtype=scipy.float32)
	b_sig = scipy.fromfile(open('output/b_signal'), dtype=scipy.float32)

	a_data = scipy.fromfile(open('output/a_srcdata'), dtype=scipy.float32)
	b_data = scipy.fromfile(open('output/b_srcdata'), dtype=scipy.float32)

	#Calculate offset and create new list of values
	offset = int(samples_per_bit/2)
	values = []
	for i in range(0,offset):
		values.append(abs(a_sig[i]))

	for i in range(offset, len(a_sig)):
		values.append(abs(a_sig[i]) + abs(b_sig[i-offset]))

	#Decoding by comparing averages across half windows to previous half window
	tot=0
	prevAvg = 0 
	window = 0
	aBits = [0]
	bBits = [0]
	avgList=[]
	for i in range(0,max_decoded_bits*samples_per_bit):
		tot+= abs(values[i])

		if i %(samples_per_bit/2)==0 and i!=0:
			avg = tot/(samples_per_bit/2)

			avgList.append(avg)

			newThresh = bits_from_average(avg)

			if (newThresh-prevAvg) > 0:
				if window == 0:
					aBits.append(1)
				else:
					bBits.append(1)
			elif newThresh == prevAvg:
				if window == 0:
					aBits.append(aBits[-1])
				else:
					bBits.append(bBits[-1])
			else:
				if window == 0:
					aBits.append(0)
				else:
					bBits.append(0)
			
			prevAvg = newThresh

			window = int(not window)
			tot=0
	aBits.pop(0)
	bBits.pop(0)

	#Generate graph for Figure 4 (first 5 bits)
	# objects = ('A0', 'A0\nB0', 'A1\nB0', 'A1\nB1', 'A2\nB1', 'A2\nB2', 'A3\nB2', 'A3\nB3', 'A4\nB3', 'A4\nB4')
	# y_pos = np.arange(len(objects))
	# averages = avgList[:10]
	 
	# plt.bar(y_pos, averages, align='center', alpha=0.5)
	# plt.xticks(y_pos, objects)
	# plt.ylabel('Average')
	# plt.title('Averages for Half Periods')
	 
	# plt.show()


	#Generate averages of full windows for interpretation below
	avglist = []
	i=0
	while i<(len(avgList)-2):
		avglist.append((avgList[i]+avgList[i+1])/2)
		i+=2

	# Print general info about decode
	print('========== DECODED DATA ===========')
	print('   avg    |  dbits | a_bit | b_bit ')
	print('----------+--------+-------+-------')
	for i in range(0, len(bBits)):
		print(str(avglist[i])[:9]
				+ " | " + str((aBits[i], bBits[i]))
				+ " |   " + str(int(a_data[i]))
				+ "   |   " + str(int(b_data[i])))
	print('===================================')

	# output data points with expected to quickly graph
	# with open("modatamoproblems.csv", "w") as f:
	# 		writer = csv.writer(f)
	# 		writer.writerow(avglist)
	# 		writer.writerow(thresholdlist)

	# Calculate the Bit Error Rate
	BER = 0
	for i in range(0, len(bBits)):
		if aBits[i] == a_data[i]:
			BER = BER + 1
		if bBits[i] == b_data[i]:
			BER = BER + 1
	BER = 100 - ((BER * 100.0) / (len(bBits) * 2))

	print('============= SUMMARY =============')
	print('             BER - ' + str(BER)[:5] + '%')
	print('          length - ' + str( len(aBits) ) + ' bits')
	print(' samples per bit - ' + str(samples_per_bit))
	print('===================================')

	return BER

if __name__ == "__main__":
	calculateBER()