import copy

# Main function for encrypting plaintext
def encrypt(plaintext, keys):
    # Perform deep copy from keys to KEYS
    KEYS = copy.deepcopy(keys)

    PLAINTEXT = plaintext.copy()

    P1 = 0
    P2 = 0

    # The actual calculations, duh
    for i in range(2):
        #print()
        #print("======================================")
        #print(" Round ", i+1)
        #print("======================================")
        #print(" Plaintext:")
        #print("  ", PLAINTEXT)
        #print("======================================")

        # Perform initial permutation, only if first round
        if i == 0:
            PLAINTEXT = initialPermutation(PLAINTEXT)

            #print(" Initial Permutation:")
            #print("  ", PLAINTEXT)
            #print("======================================")

            # Split PLAINTEXT in half
            P1 = PLAINTEXT[:4].copy()
            P2 = PLAINTEXT[4:].copy()

            #print(" Split of Plaintext:")
            #print("  Left Half (P1):")
            #print("  ", P1)
            #print("  Right Half (P2):")
            #print("  ", P2)
            #print("======================================")

        # Send right half of PLAINTEXT to expanded permutation
        PLAINTEXT = expandedPermutation(P2)
        #print(" Expanded Permutation on Right Half:")
        #print("  Right Half:")
        #print("  ", PLAINTEXT)
        #print("======================================")

        # Perform XOR operation with right half of PLAINTEXT and KEYS[i]
        PLAINTEXT = XOROperation(PLAINTEXT, KEYS[i])
        #print(' XOR on Expanded Half with K' + str(i+1) + ":")
        #print("  K" + str(i+1) + ":")
        #print("  ", KEYS[i])
        #print("  Right Half:")
        #print("  ", PLAINTEXT)
        #print("======================================")

        # Split Plaintext for SBoxes
        PLAINTEXT = PLAINTEXT[:4] + PLAINTEXT[4:]

        # Perform SBOX operation with right half of PLAINTEXT
        PLAINTEXT = sBoxOperation(PLAINTEXT)
        #print(" SBOX Operation")
        #print("  S0 Result:")
        #print("  ", PLAINTEXT[:2])
        #print("  S1 Result:")
        #print("  ", PLAINTEXT[2:])
        #print("  SBox Result:")
        #print("  ", PLAINTEXT)
        #print("======================================")

        # Perform P4 Permutation with right half of PLAINTEXT
        PLAINTEXT = p4Permutation(PLAINTEXT)
        #print(" P4 Permutation")
        #print("  Right Half:")
        #print("  ", PLAINTEXT)
        #print("======================================")

        # Perform XOR operation with both halves of PLAINTEXT
        PLAINTEXT = XOROperation(P1, PLAINTEXT)
        #print(" XOR Operation with P1 and PLAINTEXT:")
        #print("  XOR Result:")
        #print("  ", PLAINTEXT)
        #print("======================================")

        # Only if it's the first round, perform the switch
        if i == 0:
            # Set P1 as our original P2
            #  Set our P2 as our current Plaintext
            P1 = P2.copy()
            P2 = PLAINTEXT

        # If it's the second round, perform inverse of initial permutation
        elif i == 1:
            PLAINTEXT = PLAINTEXT + P2
            #print("  New Plaintext::")
            #print("  ", PLAINTEXT)
            #print("======================================")

            PLAINTEXT = initialPermutationInverse(PLAINTEXT)
            #print(" Inverse of Initial Permutation:")
            #print("  ", PLAINTEXT)
            #print("======================================")

            print("======================================")
            print(" Ciphertext:")
            print("  ", PLAINTEXT)
            print("======================================")


# The initial permutation
def initialPermutation(plaintext):
    initPermutation = [2, 6, 3, 1, 4, 8, 5, 7]

    returnPlaintext = [0] * 8

    for i in range(0, len(initPermutation)):
        returnPlaintext[i] = plaintext[initPermutation[i] - 1]

    return returnPlaintext


# Algorithm for the expanded permutation
def expandedPermutation(plaintext):
    expaPermutation = [4, 1, 2, 3, 2, 3, 4, 1]

    returnPlaintext = [0] * 8

    for i in range(0, len(expaPermutation)):
        returnPlaintext[i] = plaintext[expaPermutation[i] - 1]

    return returnPlaintext


# Algorithm for XOR operation between two binary lists
def XOROperation(left, right):
    returnPlaintext = [0] * len(left)

    for i in range(0, len(returnPlaintext)):
        if left[i] == right[i]:
            returnPlaintext[i] = 0
        elif left[i] != right[i]:
            returnPlaintext[i] = 1

    return returnPlaintext


# Algorithm for calculating both S0 and S1 for any given plaintext
def sBoxOperation(plaintext):
    returnPlaintext = []

    # Split our plaintext in half, and take the left side
    leftHalf = plaintext[:4]

    # Take first and fourth indices of left half, and convert from binary to integer
    leftRow = int("".join(str(x) for x in [leftHalf[0], leftHalf[3]]), 2)

    # Take second and third indices of left half, and convert from binary to integer
    leftColumn = int("".join(str(x) for x in [leftHalf[1], leftHalf[2]]), 2)

    S0 = [[1, 0, 3, 2],
          [3, 2, 1, 0],
          [0, 2, 1, 3],
          [3, 1, 3, 2]]

    # The left half of our plaintext now becomes the number at the row and column in S0
    #  NOTE: This number is an integer
    leftHalf = S0[leftRow][leftColumn]

    # This is just a weird formatting thing, if left half is less than 2, then it won't format properly
    if leftHalf < 2:
        returnPlaintext.append(0)

    # Append to our plaintext the conversion of the integer to 2-bit binary list
    returnPlaintext += ([int(i) for i in list('{0:0b}'.format(leftHalf))])

    # Split our plaintext in half, and take the right side
    rightHalf = plaintext[4:]

    # Take first and fourth indices of left half, and convert from binary to integer
    rightRow = int("".join(str(x) for x in [rightHalf[0], rightHalf[3]]), 2)

    # Take second and third indices of left half, and convert from binary to integer
    rightColumn = int("".join(str(x) for x in [rightHalf[1], rightHalf[2]]), 2)

    S1 = [[0, 1, 2, 3],
          [2, 0, 1, 3],
          [3, 0, 1, 0],
          [2, 1, 0, 3]]

    # The left half of our plaintext now becomes the number at the row and column in S0
    #  NOTE: This number is an integer
    rightHalf = S1[rightRow][rightColumn]

    # This is just a weird formatting thing, if left half is less than 2, then it won't format properly
    if rightHalf < 2:
        returnPlaintext.append(0)

    # Append to our plaintext the conversion of the integer to 2-bit binary list
    returnPlaintext += ([int(i) for i in list('{0:0b}'.format(rightHalf))])

    return returnPlaintext


# Calculates the P4 Permutation of any given plaintext
def p4Permutation(plaintext):
    initPermutation = [2, 4, 3, 1]

    returnPlaintext = [0] * 4

    for i in range(0, len(initPermutation)):
        returnPlaintext[i] = plaintext[initPermutation[i] - 1]

    return returnPlaintext


# The initial permutation inverse
def initialPermutationInverse(plaintext):
    initPermutation = [4, 1, 3, 5, 7, 2, 8, 6]

    returnPlaintext = [0] * 8

    for i in range(0, len(initPermutation)):
        returnPlaintext[i] = plaintext[initPermutation[i] - 1]

    return returnPlaintext
