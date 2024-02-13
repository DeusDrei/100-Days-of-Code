alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def ceasar(direction, text, shift):
    final = ""
    if direction == "decode":
        shift *= -1
    for i in text:
        if i in alphabet:
            x = alphabet.index(i)
            new_position = x + shift
            final += alphabet[new_position]
        else:
            final += i
    print(f"Here is the {direction}d text: {final}")


from art import logo

print(logo)

while True:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()

    while direction not in ("encode", "decode"):
        direction = input(
            "Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()

    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    shift = shift % 26
    ceasar(direction, text, shift)
    ask = input("Use again? (y/n) ")
    if ask != "y":
        print("Goodbye!")
        break

