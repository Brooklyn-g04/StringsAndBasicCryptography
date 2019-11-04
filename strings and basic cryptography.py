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


# String Methods to investigate:
    # Method        Use Example         Explanation
    # center        aStr.center(w)      Find the center of whatever you put into the parenthesis with the (w) being a word or phrase
    # ljust         aStr.ljust(w)       returns the string left justified in a string of length width and if the string is less than lens the original string will return
    # rjust         aStr.rjust(w)       returns the right string justified of length width and if width is less than lens than the original string will return
    # upper         aStr.upper()        it returns the upper cased string from the given string, it turns all of the lower case characters to uppercase
    # lower         aStr.lower()        it changes all of the uppercase characters to lowercase
    # index         aStr.index(item)    it searches for the given element from the beginning of the list to the return where the element appears in the lowest index
    # rindex        aStr.rindex(item)   it returns the last index where the substring is found or puts in an exception is no index exists.
    # find          aStr.find(item)     it returns the lowest index of the substring an dif substring is not given it returns -1
    # rfind         aStr.rfind(item)    it returns the highest index of the substring and if not given it returns -1
    # replace       aStr.replace(old, new)  it returns the copy of the string where all of the substring is replaced with another substring

    # Be sure to include multiple examples of all of them in use

# Character functions

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
