import SortingFunctions as sf
import time
import random
import csv

values = []
for n in range(0,18):
    values.append(2**n)

times = {}

for n in values:
    test_list = []
    for i in range(n):
        test_list.append(random.random())

    t0 = time.time()

    sf.SelectionSort(test_list)

    t1 = time.time()

    times[n] = t1-t0


prior = 1
for key in times:
    try:
        value =times[key]/prior
        times[key] = [key,times[key], value]
        prior = times[key][1]
    except ZeroDivisionError:
        times[key] = [key,times[key], times[key]]
        prior = times[key][1]

header = ['N','Time','Ratio']

with open("timingtests.csv",'w',encoding = 'UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)

    for key in times:
        writer.writerow(times[key])
