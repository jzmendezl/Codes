import os


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def encode(key, message):
    encodeMessage = ""
    if message == message.upper():
        for letter in message:
            if letter.isalnum():
                if 48 <= ord(letter) <= 57:
                    letter = chr((ord(letter) - 48 + key) % 10 + 48)
                if letter == "Ñ":
                    letter = chr((ord(letter) - 165 + key) % 10 + 165)
                letter = chr((ord(letter) - 65 + key) % 26 + 65)
            encodeMessage += letter
        return encodeMessage
    elif message == message.lower():
        for letter in message:
            if letter.isalnum():
                if 48 <= ord(letter) <= 57:
                    letter = chr((ord(letter) - 48 + key) % 10 + 48)
                if letter == "ñ":
                    letter = chr((ord(letter) - 165 + key) % 10 + 165)
                letter = chr((ord(letter) - 97 + key) % 26 + 97)
            encodeMessage += letter
        return encodeMessage
    else:
        message = message.upper()
        for letter in message:
            if letter.isalnum():
                if 48 <= ord(letter) <= 57:
                    letter = chr((ord(letter) - 48 + key) % 10 + 48)
                letter = chr((ord(letter) - 65 + key) % 26 + 65)
            encodeMessage += letter
        return encodeMessage


def decode(key, message):
    decodeMessage = ""
    if message == message.upper():
        for letter in message:
            if letter.isalnum():
                if 48 <= ord(letter) <= 57:
                    letter = chr((ord(letter) - 48 - key) % 10 + 48)
                letter = chr((ord(letter) - 65 - key) % 26 + 65)
            decodeMessage += letter
        return decodeMessage
    else:
        for letter in message:
            if letter.isalnum():
                if 48 <= ord(letter) <= 57:
                    letter = chr((ord(letter) - 48 - key) % 10 + 48)
                letter = chr((ord(letter) - 97 - key) % 26 + 97)
            decodeMessage += letter
        return decodeMessage


def positionLetter(message):
    pos = ""
    alpha = ""
    for letter in message:
        if letter.isalpha():
            if letter == letter.upper():
                alpha += "{:3}".format(letter) + " "
                pos += "{:3}".format(str(ord(letter) - 65)) + " "
            else:
                alpha += "{:3}".format(letter) + " "
                pos += "{:3}".format(str(ord(letter) - 97)) + " "
    return "The position of the letters on the message is:\n\n" + alpha + "\n\n" + pos


def positionAplha(key=3):
    alpha = ""
    posAlpha = ""
    codealpha = ""

    for letter in range(26):
        alpha += "{:3}".format(chr(letter + 65)) + " "
        posAlpha += "{:3}".format(str(letter)) + " "
        codealpha += "{:3}".format(chr((letter + key) % 26 + 65)) + " "
    return (
        "The alphabet position is: \n\n"
        + alpha
        + "\n\n"
        + posAlpha
        + "\n\n"
        + codealpha
    )


def menu():
    clear_screen()
    print("\n\n**************Welcome to Caesar Cipher**************\n\n")

    while True:
        print("**************Menu**************\n\n")
        print("Select an option\n\n")
        print("1. Encode")
        print("2. Decode")
        print("3. Info")
        print("4. Exit")
        opc = input("\n\nEnter the option\t")
        while not opc.isdigit():
            print("Invalid selection. Please choose a valid option.")
            opc = input("\n\nEnter the option\t")
        opc = int(opc)
        if opc == 1:
            # alpha = input("\n\nEnter the type of alphabet of the text: \t")
            message = input("\n\nEnter the message to encode: \t")
            key = int(input("\n\nEnter the key: \t"))
            print("\n\nThe encode message is: ", encode(key, message), "\n\n")
            input("Press Enter to continue...")
        elif opc == 2:
            # alpha = input("\n\nEnter the type of alphabet of the text: \t")
            message = input("\n\nEnter the message to decode: \t")
            key = int(input("\n\nEnter the key: \t"))
            print("\n\nThe decode message is: ", decode(key, message), "\n\n")
            input("Press Enter to continue...")
        elif opc == 3:
            # print("\n\nThe alphabet is: ", alpha, "\n")
            print(positionAplha(key), "\n\n")
            print(positionLetter(message), "\n\n")
            print("The message is: ", message, "\n")
            print("The key is: ", key, "\n")
            input("Press Enter to continue...")
        elif opc == 4:
            print("Good Bye...")
            break
        else:
            clear_screen()
            print("Invalid selection. Please choose a valid option.")
            input("Press Enter to continue...")


menu()
