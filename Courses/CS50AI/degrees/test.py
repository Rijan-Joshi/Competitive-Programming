import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

filename = "./small/people.csv"

with open(filename) as file:
    reader = csv.DictReader(file)
    for line in reader:
        print(line['id'], line['name'], line['birth'])

