
names = []
with open("./Input/Names/invited_names.txt") as f:
    names = [line.strip() for line in f.readlines()]

letter = []
with open("./Input/Letters/starting_letter.txt") as read_file:
    letter = read_file.read()

for i in names:
    with open(f"./Output/ReadyToSend/letter_for_{i}.txt", "w") as write_file:
        x = letter.replace("[name]", i)
        write_file.write(x)


