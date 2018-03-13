from ctypes import *
import time

start = time.time()

read = CDLL('/home/leon/Documents/assignmentOS/readDat.so')
printFile = read.read_in_dat
printFile.argtypes = [POINTER(c_char)]
printFile('mat100.dat')

end = time.time()
print(end - start)
