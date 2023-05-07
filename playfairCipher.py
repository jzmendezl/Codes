import os
import string


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def getMatrix(key):
    # Make the key uppercase
    key = key.upper()
    # Remove the spaces from the key
    if " " in key:
        key = key.replace(" ", "")
    # Create a list of all the letters in the key
    letters = list(key)
    # Create a list of all the letters in the alphabet
    alphabet = list(string.ascii_uppercase)
    # Remove the letters in the key from the alphabet
    for letter in letters:
        # print(letter)
        if letter in alphabet:
            alphabet.remove(letter)
            # print(alphabet)
        else:
            # print("The letter " + letter + " is not in the alphabet")
            continue

    if "I" in alphabet and "J" in alphabet:
        alphabet[alphabet.index("I")] = alphabet[alphabet.index("I")].replace(
            "I", "I/J"
        )

    # Add the letters in the key to the front of the alphabet
    for letter in reversed(letters):
        if letter == "I":
            letter = letter.replace("I", "I/J")
        if letter == "J":
            letter = letter.replace("J", "I/J")
        alphabet.insert(0, letter)

    if "I" in alphabet:
        alphabet.remove("I")

    if "J" in alphabet:
        alphabet.remove("J")

    # Create a matrix
    matrix = []
    # Fill the matrix with the letters in the alphabet
    for i in range(0, 5):
        matrix.append(alphabet[i * 5 : (i + 1) * 5])
    return matrix


def getDigraphs(message):
    for i in range(0, len(message), 2):
        if message[i] == "I" and message[i + 1] == "J":
            message = message[:i] + "IX" + message[i + 1 :]
        if message[i] == "J" and message[i + 1] == "I":
            message = message[:i] + "JX" + message[i + 1 :]
        if message[i] == message[i + 1]:
            message = message[: i + 1] + "X" + message[i + 1 :]

    if len(message) % 2 != 0:
        message += "X"

    digraphs = []
    for i in range(0, len(message), 2):
        digraphs.append(message[i : i + 2])
    return digraphs


def printMatrix(matrix):
    print("\n\nMatrix\n\n")
    for i in range(0, 5):
        print(
            matrix[i]
            .__str__()
            .replace("'", "")
            .replace(",", "\t")
            .replace("[", "")
            .replace("]", "")
        )
    print("\n")


def getLetterPosition(matrix, letter):
    for i in range(0, 5):
        for j in range(0, 5):
            if matrix[i][j] == letter:
                return (i, j)
    return "Letter not found"


def encrypt(message, key):
    print("\nEncrypting")
    message = message.replace(" ", "")
    message = message.upper()
    matrix = getMatrix(key)

    digraphs = getDigraphs(message)

    printMatrix(matrix)
    print("Digraphs\n\n", digraphs, "\n\n")

    encryptMessage = ""

    for digraph in digraphs:
        pos1 = getLetterPosition(matrix, digraph[0])
        pos2 = getLetterPosition(matrix, digraph[1])
        if len(pos1) == 2 and len(pos2) == 2:
            if pos1[0] == pos2[0]:
                # print("Same row")
                # print(
                #     matrix[pos1[0]][(pos1[1] + 1) % 5]
                #     + matrix[pos2[0]][(pos2[1] + 1) % 5]
                # )
                encryptMessage += (
                    matrix[pos1[0]][(pos1[1] + 1) % 5]
                    + matrix[pos2[0]][(pos2[1] + 1) % 5]
                )
            elif pos1[1] == pos2[1]:
                # print("Same column")
                # print(
                #     matrix[(pos1[0] + 1) % 5][pos1[1]]
                #     + matrix[(pos2[0] + 1) % 5][pos2[1]]
                # )
                encryptMessage += (
                    matrix[(pos1[0] + 1) % 5][pos1[1]]
                    + matrix[(pos2[0] + 1) % 5][pos2[1]]
                )
            else:
                # print("Different row and column")
                # print(matrix[pos1[0]][pos2[1]] + matrix[pos2[0]][pos1[1]])
                encryptMessage += matrix[pos1[0]][pos2[1]] + matrix[pos2[0]][pos1[1]]

    return encryptMessage


def decrypt(message, key):
    print("\nDecrypting")
    message = message.upper()
    matrix = getMatrix(key)

    if len(message) % 2 != 0:
        message += "X"

    digraphs = getDigraphs(message)
    printMatrix(matrix)
    print("\n\nDigraphs\n\n", digraphs, "\n\n")

    decryptMessage = ""

    for digraph in digraphs:
        pos1 = getLetterPosition(matrix, digraph[0])
        pos2 = getLetterPosition(matrix, digraph[1])
        if len(pos1) == 2 and len(pos2) == 2:
            if pos1[0] == pos2[0]:
                # print("Same row")
                # print(
                #     matrix[pos1[0]][(pos1[1] - 1) % 5]
                #     + matrix[pos2[0]][(pos2[1] - 1) % 5]
                # )
                decryptMessage += (
                    matrix[pos1[0]][(pos1[1] - 1) % 5]
                    + matrix[pos2[0]][(pos2[1] - 1) % 5]
                )
            elif pos1[1] == pos2[1]:
                # print("Same column")
                # print(
                #     matrix[(pos1[0] - 1) % 5][pos1[1]]
                #     + matrix[(pos2[0] - 1) % 5][pos2[1]]
                # )
                decryptMessage += (
                    matrix[(pos1[0] - 1) % 5][pos1[1]]
                    + matrix[(pos2[0] - 1) % 5][pos2[1]]
                )
            else:
                # print("Different row and column")
                # print(matrix[pos1[0]][pos2[1]] + matrix[pos2[0]][pos1[1]])
                decryptMessage += matrix[pos1[0]][pos2[1]] + matrix[pos2[0]][pos1[1]]

    print("Match: ", decryptMessage)


def menu():
    clear_screen()
    print("\n\n**************Welcome to Playfair Cipher**************\n\n")

    while True:
        print("**************Menu**************\n\n")
        print("Select an option\n\n")
        print("1. Encode")
        print("2. Decode")
        print("3. Exit")
        opc = input("\n\nEnter the option\t")
        while not opc.isdigit():
            print("Invalid selection. Please choose a valid option.")
            opc = input("\n\nEnter the option\t")
        opc = int(opc)
        if opc == 1:
            message = input("\n\nEnter the message to encode: \t")
            key = input("\n\nEnter the key: \t")
            print("\n\nThe encode message is: ", encrypt(message, key), "\n\n")
            input("Press Enter to continue...")
        elif opc == 2:
            message = input("\n\nEnter the message to decode: \t")
            key = input("\n\nEnter the key: \t")
            print("\n\nThe decode message is: ", decrypt(message, key), "\n\n")
            input("Press Enter to continue...")
        elif opc == 3:
            print("Good Bye...")
            break
        else:
            clear_screen()
            print("Invalid selection. Please choose a valid option.")
            input("Press Enter to continue...")


menu()
