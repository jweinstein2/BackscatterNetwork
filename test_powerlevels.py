import subprocess
import time
import sys
import os
import re

from decode import calculateBER

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

for i in range(0,100):
    j = i / 100.0
    jvalues.append(j)

    # Update the variables
    replace("src/config", "a = [\d]*[.]*[\d]*", "a = " + str(j))


    # Run threshold.py to generate accurate thesholds
    os.system("gtimeout 2 /opt/local/Library/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/MacOS/Python -u /Users/jaredweinstein/Desktop/CS434Project/threshold.py")

    # Run received_signal.py
    os.system("gtimeout 6 /opt/local/Library/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/MacOS/Python -u /Users/jaredweinstein/Desktop/CS434Project/received_signal.py")

    # Run decode.py and collect the BER
    BER = calculateBER()
    BERvalues.append(BER)

# output data points with expected to quickly graph
with open("/Users/jaredweinstein/Desktop/CS434Project/powerBER.csv", "w") as f:
		writer = csv.writer(f)
		writer.writerow(avglist)
		writer.writerow(thresholdlist)
