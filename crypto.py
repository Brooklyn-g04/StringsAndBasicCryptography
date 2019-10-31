# transcription cipher

# encryption function
def scramble2Encrypt(plainText):
    evenChars = " "
    oddChars = " "
    charCount = 0
    for ch in plainText:
        if charCount % 2 == 0:
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch
        charCount = charCount + 1
    cipherText = oddChars + evenChars
    return cipherText

def scramble2Decrypt(cipherText):
    halfLength = len(cipherText) // 2
    evenChars = cipherText[halfLength:]  # halfLength to the end
    oddChars = cipherText[:halfLength]  # 0 to halfLength -1
    plainText = " "

    for i in range(halfLength):
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]

    if len(oddChars) < len(evenChars):
        plainText = plainText + evenChars[-1]

    return plainText


def encryptMessage():
    msg = input("Enter the message to encrypt:")
    cipherText = scramble2Encrypt(msg)
    print("The encrypted message is:", cipherText)

print(encryptMessage())


def caesarEncrypt():
    input("message")
    if "a" :print("a")
    if "b" :print("f")
    if "c" :print("e")
    if "b" :print("f")
    if "c" :print("g")

print(caesarEncrypt())

def ceasarCipher(val):
    input("Message:")
    Encryption = ""
    for E in val:
        num = ord(E)

        if num == 122:
            newnum = 97
        elif num == 90:
            newnum = 65
        else:
            newnum = + 1
        Encryption = Encryption + chr(newnum)
    return Encryption

print(ceasarCipher('10'))


alphabet = "abcdefghijklmnopqrstuvwxyz"

def ceasar(word):
    encrypt = ""
    for ch in word:
        index = alphabet.find(ch)
        nextIndex = (index + 3) % 26
        encrypt += alphabet[nextIndex]
    return encryptMessage()

print(ceasar("how was your day?"))
print(ceasar("that is great!"))
