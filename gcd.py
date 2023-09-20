#!/usr/local/python/3.10.8/bin/python3
import math
import sys

if len(sys.argv)>1:
    gcd = math.gcd(int(sys.argv[1]), int(sys.argv[2]))
    print(gcd)
else:
    print("No inputs were found")