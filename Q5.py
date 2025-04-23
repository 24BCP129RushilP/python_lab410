# Copy contents of one file to another with lowercase to uppercase conversion
with open('source.txt', mode='r') as source, open('destination.txt', mode='w') as destination:
    for line in source:
        destination.write(line.upper())

print("Contents copied to 'destination.txt' with lowercase converted to uppercase.")