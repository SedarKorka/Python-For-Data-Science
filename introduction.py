#variable assign
x = 1
y = x + 2
print(y)

#This '=' is not equal
#1 = 
(t,h) = (5,15)
print((t,h))
print(t)

#Symbol table
#globals and locals()
globals
##Arithmetic operation
#floor division
fD = 7//3
print(fD)
#Simple division
sD = 5/3
print(sD)
#Module
mD = 7%3
print(mD)
#Eexponential 
print(2**3)
##String
#string concat
a = "Hello"
b = "World"
num = 5
print(a + ' ' +b)
#print(a + num) concat string and number this way, will give an error
#Strings can be concatenated without +
Great = "Monday" " " "Good" " " " " "Morning" 
print(Great)
#Comparaison and relatin operation
#equal == 
#less <
#great >
#less or equal <=
#grater or equal >=
#not equal !=
##Logical operation
#and , or and not()
if(not(5>7)):
    print("Good morning")
else:
    print("Hello")
##Identity of the object
var1 = 5
var2 = 15
if(var1 is var2):
    print(var1 is var2)
