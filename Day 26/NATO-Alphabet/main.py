import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
compare = {row.letter: row.code for (index, row) in data.iterrows()}

def generate_phonetic():
    ask = input("Enter a word: ").upper()
    try:
        new_list = [compare[i] for i in ask]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(new_list)


generate_phonetic()



