import string


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

    if "I" and "J" in alphabet:
        alphabet.remove("J")
        alphabet[alphabet.index("I")] = alphabet[alphabet.index("I")].replace(
            "I", "I/J"
        )

    # Add the letters in the key to the front of the alphabet
    for letter in reversed(letters):
        alphabet.insert(0, letter)
    # Create a matrix
    matrix = []
    # Fill the matrix with the letters in the alphabet
    for i in range(0, 5):
        matrix.append(alphabet[i * 5 : (i + 1) * 5])
    return matrix


def getDigraphs(message):
    digraphs = []
    for i in range(0, len(message), 2):
        digraphs.append(message[i : i + 2])
    return digraphs


def printMatrix(matrix):
    for i in range(0, 5):
        print(
            matrix[i]
            .__str__()
            .replace("'", "")
            .replace(",", "\t")
            .replace("[", "")
            .replace("]", "")
        )


def getLetterPosition(matrix, letter):
    for i in range(0, 5):
        for j in range(0, 5):
            if matrix[i][j] == letter:
                return (i, j)
    return "Letter not found"


def encrypt(message, key):
    message = message.upper()
    matrix = getMatrix(key)

    if len(message) % 2 != 0:
        message += "X"

    digraphs = getDigraphs(message)
    printMatrix(matrix)
    print(digraphs)

    encryptMessage1 = ""
    encryptMessage2 = ""

    for digraph in digraphs:
        pos1 = getLetterPosition(matrix, digraph[0])
        pos2 = getLetterPosition(matrix, digraph[1])
        if len(pos1) == 2 and len(pos2) == 2:
            if pos1[0] == pos2[0]:
                print("Same row")
                print(
                    matrix[pos1[0]][(pos1[1] + 1) % 5]
                    + matrix[pos2[0]][(pos2[1] + 1) % 5]
                )
                encryptMessage1 += (
                    matrix[pos1[0]][(pos1[1] + 1) % 5]
                    + matrix[pos2[0]][(pos2[1] + 1) % 5]
                )
            elif pos1[1] == pos2[1]:
                print("Same column")
                print(
                    matrix[(pos1[0] + 1) % 5][pos1[1]]
                    + matrix[(pos2[0] + 1) % 5][pos2[1]]
                )
                encryptMessage1 += (
                    matrix[(pos1[0] + 1) % 5][pos1[1]]
                    + matrix[(pos2[0] + 1) % 5][pos2[1]]
                )
            else:
                print("Different row and column")
                print(matrix[pos1[0]][pos2[1]] + matrix[pos2[0]][pos1[1]])
                encryptMessage1 += matrix[pos1[0]][pos2[1]] + matrix[pos2[0]][pos1[1]]

    encryptMessage2 = encryptMessage1

    if "I/J" in encryptMessage1:
        encryptMessage1 = encryptMessage1.replace("I/J", "I")
        encryptMessage2 = encryptMessage2.replace("I/J", "J")

    print(encryptMessage1)
    print(encryptMessage2)


def decrypt(message, key):
    message = message.upper()
    matrix = getMatrix(key)

    if len(message) % 2 != 0:
        message += "X"

    digraphs = getDigraphs(message)
    printMatrix(matrix)
    print(digraphs)

    decryptMessage1 = ""
    decryptMessage2 = ""

    for digraph in digraphs:
        pos1 = getLetterPosition(matrix, digraph[0])
        pos2 = getLetterPosition(matrix, digraph[1])
        if len(pos1) == 2 and len(pos2) == 2:
            if pos1[0] == pos2[0]:
                print("Same row")
                print(
                    matrix[pos1[0]][(pos1[1] - 1) % 5]
                    + matrix[pos2[0]][(pos2[1] - 1) % 5]
                )
                decryptMessage1 += (
                    matrix[pos1[0]][(pos1[1] - 1) % 5]
                    + matrix[pos2[0]][(pos2[1] - 1) % 5]
                )
            elif pos1[1] == pos2[1]:
                print("Same column")
                print(
                    matrix[(pos1[0] - 1) % 5][pos1[1]]
                    + matrix[(pos2[0] - 1) % 5][pos2[1]]
                )
                decryptMessage1 += (
                    matrix[(pos1[0] - 1) % 5][pos1[1]]
                    + matrix[(pos2[0] - 1) % 5][pos2[1]]
                )
            else:
                print("Different row and column")
                print(matrix[pos1[0]][pos2[1]] + matrix[pos2[0]][pos1[1]])
                decryptMessage1 += matrix[pos1[0]][pos2[1]] + matrix[pos2[0]][pos1[1]]

    decryptMessage2 = decryptMessage1

    if "I/J" in decryptMessage1:
        decryptMessage1 = decryptMessage1.replace("I/J", "I")
        decryptMessage2 = decryptMessage2.replace("I/J", "J")

    print("d1", decryptMessage1)
    print("d2", decryptMessage2)


encrypt("Have His Carcase", "monarchy")
decrypt("BOUFRMBMLI", "monarchy")
decrypt("BOUFRMBMLJ", "monarchy")
