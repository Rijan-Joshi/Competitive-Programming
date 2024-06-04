import sys
import csv
from csv import DictReader


def main():
    # check_cli()
    infos = []
    with open(sys.argv[1]) as file:
        reader = DictReader(file)
        for row in reader:
           last, first = row['name'].split(',')
           infos.append([first, last, row['house']])           

    with open(sys.argv[2], 'w', newline='') as file:
        writer = csv.writer(file)
        for info in infos:
            writer.writerow(info)

# def check_cli():

if __name__ == "__main__": 
    main()