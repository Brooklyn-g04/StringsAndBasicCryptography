# Strings

# Concatenation
#   2 or more strings and put them together
firstName = "Wilma"
lastName = "Flintstone"


print(firstName + " " + lastName)

name = firstName + " " + lastName
lastFirst = lastName + ", " + firstName

print(name)
print(lastFirst)

# Repetition
#  repetition operator: *
print("Hip "*2 + "Hooray!")

def rowYourBoat():
    print("Row,"*3 + "your boat")
    print("Gently down the stream")
    print("Merrily,"*4)
    print("Life is but a dream")

rowYourBoat()

# Indexing
name = "Roy G Biv"
firstChar = name[0]

print(firstChar)

middleCharIndex = len(name) // 2

print(middleCharIndex)
print(name[middleCharIndex])
print(name[-2])


for i in range(0, len(name)+1):
    print(name[0:i])

# slicing and dicing

print(name[0:6])

# Searching

print("Biv" in name)
print("y" not in name)

# Character functions
# All characters have a value, a numeric value

print(ord('a'))
print(chr(104))
print(chr(75))
print(ord('&.'))
