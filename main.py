#===================================
# Aaron Urrea
#  COMPIT-424
#  September 13, 2022
#===================================


from DES import DES
from encrypt import encrypt


def main():
    # Gets user input for a 10-bit key
    keyInput = input("Please type a 10-bit key: ")
    if(len(keyInput) != 10):
        print("This is not a 10-bit key!")
        return 1

    # Translates string input to binary List
    key = []
    for i in range(10):
        currChar = keyInput[i]
        if currChar != str('0') and currChar != str('1'):
            print("This is an invalid key!")
            return 1
        key.append(int(keyInput[i]))

    # Gets user input for a 8-bit plaintext
    plaintextInput = input("Please type an 8-bit plaintext: ")
    if(len(plaintextInput) != 8):
        print("This is not an 8-bit plaintext!")
        return 1

    # Translates string input to binary List
    plaintext = []
    for i in range(8):
        currChar = plaintextInput[i]
        if currChar != str('0') and currChar != str('1'):
            print("This is an invalid plaintext!")
            return 1
        plaintext.append(int(plaintextInput[i]))

    print("======================================")
    print(" 10-Bit Key:")
    print("  ", key)
    print("======================================")
    print(" Plaintext:")
    print("  ", plaintext)

    # Retrieves K1 and K2
    keys = DES(key)

    # Encrypts current plaintext
    encrypt(plaintext, keys)

    return 0


# Main, duh
if __name__ == '__main__':
    main()