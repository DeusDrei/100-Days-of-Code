# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
word = ""
total = 0
total1 = 0
for i in name1.lower():
    if i in "true":
        total += 1
for i in name2.lower():
    if i in "true":
        total += 1
for i in name1.lower():
    if i in "love":
        total1 += 1
for i in name2.lower():
    if i in "love":
        total1 += 1
word += str(total) + str(total1)

if int(word) > 90 or int(word) < 10:
    print(f"Your score is {word}, you go together like coke and mentos.")
elif int(word) >= 40 and int(word) <+ 50:
    print(f"Your score is {word}, you are alright together.")
else:
    print(f"Your score is {word}.")
