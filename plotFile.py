import numpy as np
import matplotlib.pyplot as plt
import math
import struct
from pathlib import Path
import sys


array2D_binary = []
inputFile = 'exported_binary\\'+'cobrab-9-1.ep-vpl676'

# reading line by line
with open(inputFile, "r") as file:
    line = file.readline()
    while line:
        # print(line)
        line = line[:-1]
        linearray_binary = []
        for rowIndex, digit in enumerate(line):
            linearray_binary.append(int(digit))
        #print("array", linearray_binary)
        array2D_binary.append(linearray_binary)
        line = file.readline()


# prepare data for plotting
lastline_0 = array2D_binary.pop()
lastline_1 = array2D_binary.pop()
lastline_2 = array2D_binary.pop()
lastline_3 = array2D_binary.pop()
line_0 = array2D_binary.pop(0)
mat = np.array(array2D_binary)


# parse array
total_bytes = 0
for index, linearray_binary in enumerate(array2D_binary):
    total_bytes += len(linearray_binary)
    if (index < 20):
        print(index, len(linearray_binary))
        # print(linearray_binary)
print("Total Bytes", total_bytes)

# start plotting
plot1 = plt.figure(1)
plt.imshow(mat)
plt.title("Disk")

plt.show()
