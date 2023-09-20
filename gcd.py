#!/usr/local/python/3.10.8/bin/python3
import math

a = input("First number: ")
while not str.isdigit(a):
    a= input("Invalid input, try again: ")
b = input("Second number: ")
while not str.isdigit(b):
    b= input("Invalid input, try again: ")

gcd = math.gcd(int(a),int(b))
print(gcd)