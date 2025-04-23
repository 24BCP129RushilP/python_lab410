import csv

# Read the CSV file and convert it into a dictionary
data = {}
with open('data.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        total = int(row['Subject1']) + int(row['Subject2']) + int(row['Subject3'])
        data[row['Roll No']] = {
            'Name': row['Name'],
            'Subject1': row['Subject1'],
            'Subject2': row['Subject2'],
            'Subject3': row['Subject3'],
            'Total': total
        }

print("Data from CSV file:", data)