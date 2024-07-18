import csv

data = [
    ['Name', "Age", 'City'],
    ['John', '30', 'New York'],
    ['Anna', '28','London'],
    ['Mike', '32', 'Chicago']
]


with open('data.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(data)


with open('data.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)


