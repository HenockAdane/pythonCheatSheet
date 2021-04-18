x = 2
x = x+1

if x > 20: print("x is less than 20")

elif x == 20: print("x is equal to 20")

else: print("x is less than 20")

#print(10 / x )
#while x < 21: 
 #   x= x+1
#print(type(x))
#print(x)

#inp = input("what is your name?")
#print(type(inp))
#print("user name is " + inp)

def functionExample(a):
    print("this is a function")
    print(a)
functionExample("this is a paramter")

a = [1,2,3,4,5,64,32,23]
z = None
for i in a:
     if z is None or z < i:
         z = i

string = "Naruto"
#prints the length of string
print(len(string))

#prints true or false if "uto" is in the string
print("uto" in string)

#gets the word within those positions of the string
print(string[2:4])

#gets the word from the first letter to the specified position
print(string[:5])

#gets the word from the specificed position to the end of the string
print(string[2:])

#Searches the string for a specified value and returns the position of where it was found
print(string.find("uto"))

#uppercases the string
print(string.upper())

#lowercases the string
print(string.lower())

#removes the whitespace at the beginning and end of the string
print(string.strip())

#replaces N with B
print(string.replace("N", "B"))

#splits the string into an array
print(string.split(""))

#some more string functions https://www.w3schools.com/python/python_strings_methods.asp

print(z)

# to change "123" into 123, you do int("123")
# to check the type of a constant, you do type(constant) e.g type("123")