# Python program to find SHA256 hexadecimal hash string of a file
import hashlib
import csv
import time

import numpy as np


def dec2bin(num):
    l = []
    if num < 0:
        return '-' + dec2bin(abs(num))
    while True:
        num, remainder = divmod(num, 2)
        l.append(str(remainder))
        if num == 0:
            return ''.join(l[::-1])

def get_b_hash(byte):
    get_hash = hashlib.sha256(byte).digest()
    conver2ord_hash = int.from_bytes(get_hash, byteorder='big', signed=False)
    readable_hash = dec2bin(conver2ord_hash)
    return readable_hash

# filename = input("Enter the input file name: ")
filename = "/Users/apple/Sites/csv/Test.csv"
# filename2 = input("Enter the input file name: ")
filename2 ="/Users/apple/DownloadFromWUSTL/new_peaks.csv"

with open(filename, "w") as f:
    writer = csv.writer(f)  # write entire file as bytes
    with open(filename2, "rb") as f2:  # rb 很关键
        byte = f2.read()
        count = 0
        times =[]
        TimeStart = time.time()
        for i in range(0,np.iinfo(np.int32).max):
            nonce = bytes(i)
            byte = byte + nonce
            readable_hash = get_b_hash(byte)
            # print(readable_hash)
            if readable_hash[1:7] == "000000":
                count+= 1
                print(readable_hash)
                TimeEnd = time.time()
                times.append((TimeEnd - TimeStart)*1000)
                TimeStart = TimeEnd
            if count == 50:
                writer.writerow(times)
                break

