
'''
**************** Python Practice code ******************
These are multi line comments ----
Hello World & Print Function
'''




# variables is an indentifier / variable
# identifier can only be started with _ or a character/alphabet
# No special character other than 
# Number can appear in an identifier except at first position
#convention in Phython, use under score in between
#indentifier name cannot be a reserved name in phython
# in phython no need to declare variables




print ("HelloWorld !")
String = "HelloWorld!"
print (String)
# remembers only the last item that is assigned
string = "overwrite"
print(string)

print('''
Quaid-e-Azam's quote "we are a strong nation"
''')


'''
Variables & Numbers
'''

print (36)
age = 36 
print(age)
print (age+36)
added_number = age + 40
print (added_number)
float_variable = 50.0000
print (float_variable)
first_number = 100
Second_number = 20
print("add = " + str(first_number+Second_number))
print("subtract = " + str(first_number-Second_number))

print("divide = " + str(first_number/Second_number))
print("multiple = " + str(first_number*Second_number))

first_number = 100
first_number += 100
print(first_number)

first_number = 100
first_number -= 100
print(first_number)

first_number = 100
first_number *= 100
print(first_number)

first_number = 100
first_number /= 100
print(first_number)

float_variable = 50.00000
print(float_variable)
print( first_number  + float_variable)

#Answer is always in float
print (1.5+1.5)
print (1+1.5)

#modulas operator for reminder
print ( 16%3)

#convert to int if you want to get the quotient
print (int(16/3))

# elimination ambiguity
# operator precedence () , */ , +- ; if same precedence then left to right
z=1+2*3
print (z)

z=1+(2*3)
print (z)



# IF conditional expression
a = int(input ("Enter time to sleep"))
if a==10:
    print ("its sleep time") 
else:
    print("its still time to sleep")

day =input ("what is the day today")
if day== "Sun":
    print("Week end")
elif day==  "sat":
    print("Week end")
else: print("not Week end")
 
day = "sun"
temp =100

if day=="sun" and temp ==100:
    print("its a hot weekend")
if day!="sun" and temp ==100:
    print("its a hot weekend")

if (day=="sun" or day=="sat") and temp ==100:
    print("its a hot weekend")



