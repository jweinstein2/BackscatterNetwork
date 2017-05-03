import subprocess
import time
import sys
import os
import re
import csv

#Swap comment below to change which file you are testing on
#from power_superposition import calculateBER
from window_size import calculateBER

numiter = 40

def replace(file, pattern, subst):
    # Read contents from file as a single string
    file_handle = open(file, 'r')
    file_string = file_handle.read()
    file_handle.close()

    # Use RE package to allow for replacement (also allowing for (multiline) REGEX)
    file_string = (re.sub(pattern, subst, file_string))

    # Write contents to file.
    # Using mode 'w' truncates the file.
    file_handle = open(file, 'w')
    file_handle.write(file_string)
    file_handle.close()

jvalues = []
BERvalues = []

readableBER = open('a_bits_readable.txt', 'w')
# 	bitter.write(str(line)+'\n')

for i in range(0,numiter):
    j = i / float(numiter)
    jvalues.append(j)

    # Update the variables
    replace("src/config", "a = [\d]*[.]*[\d]*", "a = " + str(j))


    # Run threshold.py to generate accurate thesholds
    os.system("gtimeout --signal=SIGINT 4 /opt/local/Library/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/MacOS/Python -u /Users/Andre/Desktop/CS434Project/threshold.py")

    # Run received_signal.py
    os.system("gtimeout --signal=SIGINT 10 /opt/local/Library/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/MacOS/Python -u /Users/Andre/Desktop/CS434Project/received_signal.py")

    os.system("sleep 1")

    # Run decode.py and collect the BER
    BER = calculateBER()
    # print str(j) + " : " + str(BER)[0:5]
    print(str(j) + " - " + str(BER)[0:5])
    BERvalues.append(BER)
    readableBER.write(str(BER)[0:5] + "\n")

# output data points with expected to quickly graph
with open("/Users/Andre/Desktop/CS434Project/powerBER.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(jvalues)
    writer.writerow(BERvalues)