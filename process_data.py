# coding=utf-8
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from copy import copy
from datetime import datetime

# Settings
data_file = 'data/data_2021-02-04_A.dat'
data_starts_at_line = 2
skip_data_points = 100

# Format data
file = open(data_file, 'r')
lines = file.readlines()
file.close()

data = []

for index, line in enumerate(lines):
    if index < data_starts_at_line - 1:
        continue
    if (index % skip_data_points) != 0:
        continue

    line = line.split()

    data.append({
        'id': line[0],
        'date': line[1],
        'time': line[2],
        'string': [
            line[7 + i*3]
            for i in range(0, 12)
        ]
    })

ids = []
hours = []
stringTemperatures = []
for _ in range(0, 12):
    stringTemperatures.append([])

for element in data:
    ids.append(element['id'])
    hours.append(float(element['id']) / 60.0 / 60.0)
    for i, temp in enumerate(element['string']):
        stringTemperatures[i].append(float(temp.replace(',','.')))
