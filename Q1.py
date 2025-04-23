import csv


with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Roll No', 'Name', 'Subject1', 'Subject2', 'Subject3'])
    writer.writerow([1, 'Alice', 85, 90, 88])
    writer.writerow([2, 'Bob', 78, 82, 80])
    writer.writerow([3, 'Charlie', 92, 88, 95])

print("CSV file 'data.csv' created successfully.")