import numpy as np
import matplotlib.pyplot as plt
import math
import struct
from pathlib import Path
import sys
from configparser import ConfigParser


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


if len(sys.argv) > 2:
    fileName = sys.argv[2]
    machine = sys.argv[1]
else:
    fileName = 'cobrab-1-1.3072'
    machine = 'nole1'
    print("No ARGS, proceeding with default values")

print("running script on "+fileName+" for machine "+machine)

config_machine = ConfigParser()
config_machine.read('config_machine.ini')

# bytes written before starting writing the design
# Nole 9 ex: 66
prefix_values = config_machine.getint(machine, 'prefix_values')
# Nole 9 EX:
# Line = 5376 bits + 32 extra bits
# Line = 672 Bytes + 4 Bytes
values_per_line = config_machine.getint(machine, 'values_per_line')


inputFile = 'files\\'+fileName
outputFile = 'exported\\'+fileName
vplstring = ""
if not(values_per_line == 0):
    vplstring = "-vpl"+str(values_per_line)
outputFileDecimal = 'exported_decimal\\'+fileName
outputFileBinary = 'exported_binary\\'+fileName


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
            # print(f'line {rowIndex}: {line[0]}')
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
    if(index < 10):
        print(index, len(lineArray_decimal))
        # print(lineArray_decimal)
print("Total Bytes", total_bytes, len(array2D_decimal))


# export data to file
workingonprefix = True

file_outputFile = open(outputFile, "wb")
file_outputFileDecimal = open(outputFileDecimal, "w")
file_outputFileBinary = open(outputFileBinary, "w")
cuttent_value_index = 0
for index, lineArray_decimal in enumerate(array2D_decimal):
    # writing exact file (Bytes)
    lineArray_Byte = bytes(lineArray_decimal)
    file_outputFile.write(lineArray_Byte)

    # writing different formats (Decimal, Binary)
    for index, value_decimal in enumerate(lineArray_decimal):
        if workingonprefix:
            if prefix_values == 0:
                file_outputFileDecimal.write("\n")
                file_outputFileBinary.write("\n")
                workingonprefix = False
            prefix_values -= 1
        else:
            cuttent_value_index += 1
            if not (values_per_line == 0) and cuttent_value_index % values_per_line == 0:
                file_outputFileDecimal.write("\n")
                file_outputFileBinary.write("\n")

        file_outputFileDecimal.write(f"{value_decimal:03}"+" ")
        # file_outputFileBinary.write(f"{value_decimal:b}") # decimal may be represented in less than 8 binary digits
        file_outputFileBinary.write(str(get_bin(value_decimal, 8)) + " ")

    if values_per_line == 0:
        file_outputFileDecimal.write("\n")
        file_outputFileBinary.write("\n")

file_outputFile.flush()
file_outputFileDecimal.flush()


print("exported "+outputFile)
print("exported "+outputFileDecimal)
print("exported "+outputFileBinary)
