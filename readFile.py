import numpy as np
import matplotlib.pyplot as plt
import math
import struct
from pathlib import Path
import sys


def get_bin(x, n=0):
    """
    Get the binary representation of x.

    Parameters
    ----------
    x : int
    n : int
        Minimum number of digits. If x needs less digits in binary, the rest
        is filled with zeros.

    Returns
    -------
    str
    """
    return format(x, 'b').zfill(n)


# Streaming Channel & Detection Frame Selection
if len(sys.argv) > 1:
    fileName = sys.argv[1]
else:
    fileName = 'cobrab-9-1.ep'


inputFile = 'files\\'+fileName
outputFile = 'exported\\'+fileName
values_per_line = 8
vplstring = ""
if not(values_per_line == 0):
    vplstring = "-vpl"+str(values_per_line)
outputFileDecimal = 'exported_decimal\\'+fileName+vplstring
outputFileBinary = 'exported_binary\\'+fileName+vplstring


# data = Path(fileName).read_bytes()
# multiple = struct.unpack('ii', data[:8])
# print(multiple)


array2D_decimal = []

"""
# reading byte by byte
lineIndex = 0
with open(inputFile, "rb") as file:
    byte = file.read(1)
    while byte:
        print("byte "+str(lineIndex), byte)
        lineIndex += 1
        byte = file.read(1)
"""

# reading line by line
with open(inputFile, "rb") as file:
    lines = file.readlines()
    rowIndex = 0
    for rowIndex, line in enumerate(lines):
        if(rowIndex < 0):
            firstbyteofline = line[0]
            # print(f'line {rowIndex}: {firstbyteofline}')
            print(f'line {rowIndex}: {line}')
        linearray_decimal = []
        for byteIndex, bytevalue in enumerate(line):
            if(byteIndex < 0):
                print(f'byte {byteIndex}: {bytevalue}')
            linearray_decimal.append(bytevalue)
        array2D_decimal.append(linearray_decimal)


# parse array
total_bytes = 0
for index, lineArray_decimal in enumerate(array2D_decimal):
    total_bytes += len(linearray_decimal)
    if (index > -1):
        print(index, len(lineArray_decimal))
        # print(lineArray_decimal)
print("Total Bytes", total_bytes)


# export data to file
file_outputFile = open(outputFile, "wb")
file_outputFileDecimal = open(outputFileDecimal, "w")
file_outputFileBinary = open(outputFileBinary, "w")
cuttent_value_index = 0
for index, lineArray_decimal in enumerate(array2D_decimal):

    lineArray_Byte = bytes(lineArray_decimal)
    file_outputFile.write(lineArray_Byte)

    for index, value_decimal in enumerate(lineArray_decimal):
        if not (values_per_line == 0) and cuttent_value_index % values_per_line == 0:
            file_outputFileDecimal.write("\n")
            file_outputFileBinary.write("\n")
        file_outputFileDecimal.write(str(value_decimal)+" ")
        # file_outputFileBinary.write(f"{value_decimal:b}")
        file_outputFileBinary.write(str(get_bin(value_decimal, 8)))

        cuttent_value_index += 1

    if values_per_line == 0:
        file_outputFileDecimal.write("\n")
        file_outputFileBinary.write("\n")

file_outputFile.flush()
file_outputFileDecimal.flush()


"""
# prepare data for plotting
#lastline = array2D_decimal.pop()
#line_0 = array2D_decimal.pop(0)
#line_1 = array2D_decimal.pop(0)
#line_2 = array2D_decimal.pop(0)
mat = np.array(array2D_decimal)

# start plotting
plot1 = plt.figure(1)
plt.imshow(mat)
plt.title("Disk")

"""


"""
plot1 = plt.figure(2)
plt.plot(line_0)
plt.title("Line_0")
"""

"""
plt.show()
"""
