import numpy as np
import csv
import matplotlib.pyplot as plt

feature = []
target = []

file = open("Salary.csv" , "r")
reader = csv.reader(file)
for i in reader:
    if i[0] == "YearsExperience":
        continue
    feature.append(float(i[0]))
    target.append(float(i[1]))

def stepW(m , w , b):
    sum = 0
    for i in range(1 , m):
        rep = ((w*feature[i] + b) - target[i])*feature[i]
        sum += rep
    return sum/m

def stepB(m , w , b):
    sum = 0
    for i in range(1 , m):
        rep = (w*feature[i] + b - target[i])
        sum += rep
    return sum/m

w = 0
b = 0
l = 0.0001
m = len(feature) - 1
# applying gradient decent
escape = 1
while round(escape , 3)!= 0:
    tempw = w - l*stepW( m , w , b)
    tempb = b - l*stepB( m , w , b)
    w = tempw
    b = tempb
    escape = stepW( m , w , b)
    print(escape)

print("W =" , w , "\nB =", b )

# linear function obtained
i = 1
while i != 0:
    x = float(input("Enter years of experience : "))
    y = w*x + b
    print("salary = " , y , "\n")
    i = int(input("enter 0 to exit : "))
    