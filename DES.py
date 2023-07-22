import copy

# Main function for finding K1 and K2
def DES(key):
    KEY = key.copy()

    # Perform a P10 Permutation on KEY
    KEY = doP10Permutation(KEY)

    # Perform a left shift by 1 (LS-1)
    KEY = shiftLeft(KEY, 1)

    # Create K1 as a copy of KEY
    K1 = copy.deepcopy(KEY)

    # Perform a P8 Permutation on K1
    K1 = doP8Permutation(K1)

    print("======================================")
    print(" K1:")
    print("  ", K1)

    # Perform a left shift by 2 (LS-2)
    KEY = shiftLeft(KEY, 2)

    # Create K2 as a copy of KEY
    K2 = copy.deepcopy(KEY)

    # Perform a P8 Permutation on K2
    K2 = doP8Permutation(K2)

    print("======================================")
    print(" K2:")
    print("  ", K2)
    return [K1, K2]


# Calculates a P10 Permutation from the called KEY.
def doP10Permutation(key):
    p10Permutation = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]

    returnKey = [0] * 10

    for i in range(0, len(p10Permutation)):
        returnKey[i] = key[p10Permutation[i] - 1]

    return returnKey


# Calculates a P8 Permutation from the called KEY.
def doP8Permutation(key):
    p8Permutation = [6, 3, 7, 4, 8, 5, 10, 9]

    returnKey = [0] * 8
    tempKey = key.copy()

    for i in range(0, len(p8Permutation)):
        returnKey[i] = tempKey[p8Permutation[i] - 1]

    return returnKey


# Shifts left the Binary LISTS by amount rotations.
#  NOTE: It shifts the individual lists themselves, not as a whole.
def shiftLeft(key, rotations):
    keyLeft = key[:5]
    keyRight = key[5:]

    keyLeft = keyLeft[rotations:] + keyLeft[:rotations]
    keyRight = keyRight[rotations:] + keyRight[:rotations]

    key = keyLeft + keyRight

    return key
