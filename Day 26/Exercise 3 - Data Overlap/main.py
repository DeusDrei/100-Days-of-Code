file1 = []
with open("file1.txt") as f:
    file1 = [line.strip() for line in f.readlines()]

file2 = []
with open("file2.txt") as f:
    file2 = [line.strip() for line in f.readlines()]

result = [int(i) for i in file1 if i in file2]
# Write your code above 👆
print(result)


