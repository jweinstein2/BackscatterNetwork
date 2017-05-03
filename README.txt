# CS434_Project README

Supporting Material

1. Code
  1.1 GNU Radio
    1.11 am_generator.grc
    1.12 treshold.grc
  1.2 Python
    1.21 power_superposition.py
    1.22 window_size.py
    1.23 test_powerlevel.py
  
1. Code
    1.1 GNU Radio
        1.11 am_generator.grc
              This generates the AM signal. Can swap between the cosine wave (no noise) and the audio input by 
              plugging and unplugging the source on the left hand side.
        1.12 treshold.grc
              This sends values to the files so that the python program can determine the averages needed to 
              calculate the thresholds.
        1.13 backscatter.grc
              This performs the actual backscattering, sending a stream of random bits, each repeated with 
              reference to the size of a bit period. These bits are used to multiply with the signal that 
              is added to the carrier (AM signal) and then are added together to emulate the reflecting of 
              the signal by the two transmitting devices.
        
    1.2 Python
        1.21 power_superposition.py
              This file implements the decoding algorithm discussed in the Power Superposition Model. It 
              calculates the averages of each threshold band based on the values from threshold.grc. It 
              then loops over the values of backscatter.grc, creating an average of every window. It compares 
              this average to the thresholds and determines the bits that each device is sending in that bit window.
        1.22 window_size.py
              This file implements the decoding algorithm discussed in the Time Offset Model. It also 
              calculates the averages of each threshold band, but it ignores the middle bands because 
              it only cares about thresholds 1 and 3 (see paper). It then takes the values sent from 
              device A and the values sent from device B, offsets, and adds them. It then decodes the 
              averages across half of a bit period and determines the value of the bit based on the threshold, 
              and determines the device sent based on which window it is in. 
        1.23 test_powerlevel.py
              This file is used to evaluate the performances of each model across a spectrum of power levels. 
              It modifies a file called config that contains the power levels used by the GRC files and reruns 
              the GRC files and either power_superposition.py or window_size.py. It takes the bit error rate 
              for each power level and stores them in an excel file, which we use to generate graphs. To change 
              the number of iterations (how many power levels between 0 and 1), change the value of the variable 
              'numiter'. To change whether it tests the Power Superposition Model or the Time Offset Model, 
              change the import that is commented at the top (noted in the file).
