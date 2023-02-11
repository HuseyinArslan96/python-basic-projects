# Yöntem 1
def letterValue(name):
    name = name.lower()
    letterValues = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
                     'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
                     't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    values = []
    for char in name:
        values.append(letterValues[char])
    return values

name = input("İsim giriniz: ")
values = letterValue(name)
print("İsimdeki harflerin sayısal karşılığı" + " " + str(values))

# Yöntem 2
name = input("İsim giriniz: ")
numbers = []
for char in name.lower():
    numbers.append(
        ord(char) - 96
    )
print(numbers)

# Yöntem 3
import string
my_name = str(input("Enter a your name: "))
numbers      = []
characters   = []
output       = []
for x, y in zip(range(1, 27), string.ascii_lowercase):
    numbers.append(x)
    characters.append(y)
print(numbers)
print(characters)
print("----------------------------------------------------------------------")
input = my_name
input = input.lower()
for character in input:
    number = ord(character) - 96
    output.append(number)
print(output)
print("----------------------------------------------------------------------")
sum = 0
lent_out = len(output)
for i in range(0,lent_out):
    sum = sum + output[i]
print("result at sum is: ")
print("----------------- ")
print(sum)