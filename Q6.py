# Merge lines alternatively from two files
with open('file1.txt', mode='r') as file1, open('file2.txt', mode='r') as file2, open('merged.txt', mode='w') as merged:
    lines1 = file1.readlines()
    lines2 = file2.readlines()
    max_len = max(len(lines1), len(lines2))
    
    for i in range(max_len):
        if i < len(lines1):
            merged.write(lines1[i])
        if i < len(lines2):
            merged.write(lines2[i])

print("Lines merged into 'merged.txt'.")