def letterToIndex(letter):
    from string import ascii_lowercase
    alphabet = ascii_lowercase + ''
    idx = alphabet.find(letter)
    if idx == -1:       # means that it wasn't in the alphabet
        print("error:", letter, "is not in the alphabet")
    return idx

def indexToLetter(idx):
    from string import ascii_lowercase
    alphabet = ascii_lowercase + ''
    letter = ''
    if idx >= len(alphabet):
        print("error:", idx, "is too large.")
    elif idx < 0:
        print("error:", idx, "is too small.")
    else:
        letter = alphabet[idx]
    return letter


# Be sure to include multiple examples of all of them in use
# Character functions

print(chr(75))
print(ord('&'))

from mapper2 import *
print(letterToIndex('M'))

print(indexToLetter(-24))


from crypto import *

print(scramble2Encrypt("THE MEETING IS AT 5 OCLOCK"))
