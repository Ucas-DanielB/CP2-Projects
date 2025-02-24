#Daniel Blanco, Reading Files
import csv
users = {}
content = open('Notes/sample.csv', 'r')
with open('Notes/sample.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        users = users.update({row[0]:row[2]})

print(users)