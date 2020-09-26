# A set is a set of charcters inside a pair of square [] with a special meaning:
#[arn]-->Returns where one of the specified charters (a,r,or n) are present.
import re
'''txt="The rain in Spain"
x=re.findall("[arn]",txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match!")'''

#[a-n]	Returns a match for any lower case character, alphabetically between a and n
'''txt="The rain in Spain"
x=re.findall("[a-n]",txt)
print(x)
if x:
    print("Yes there is at least one match!")
else:
    print("No match!")'''

'''txt="The rain in Spain"
x=re.findall("[A-N]",txt)
print(x)
if x:
    print("Yes there is at least one match!")
else:
    print("No match!")'''

#[^arn]-->Returns a match for any charcter Except a,r,and n

'''txt="The rain in Spain"
x=re.findall("[^arn]",txt)
print(x)
if x:
    print("Yes,there is at least one match!")
else:
    print("No match!")

txt="The rain in Spain"
x=re.findall("[^xyz]",txt)
print(x)
if x:
    print("Yes,there is at least one match!")
else:
    print("No match!")
'''

#[0123]-->Returns a match where any of the specified digits(0,1,2,0r,3) are present
'''
txt="The rain in Spain"

x=re.findall("[0123]",txt)
print(x)
if x:
    print("Yes there is at least one match!")
else:
    print("No match!")'''

# [0-9]-->check if the string has any digits:
'''txt="8 times before 11:45 AM"

x=re.findall("[0-9]",txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match!")
'''

#Returns a match for any charcter alphabetically between a and z, lower case OR upper case
'''txt="8 times before 11:45 AM"

x=re.findall("[a-zA-Z]",txt)
print(x)
if x:
    print("Yes,there is at least one match!")
else:
    print("No match!")
'''

#[0-5][0-9]-->Check if the string has any two-digit numbers, from 00 to 59
'''
txt="8 times before 11:45 AM"

x=re.findall("[0-5][0-9]",txt)

print(x)
if x:
    print("Yes,there is at least one match!")
else:
    print("No match")'''

#[+]-->Check if the string has any + characters

txt="The rain in Spain"

x=re.findall("[+]",txt)
print(x)
if x:
    print("Yes,there is at least one match!")
else:
    print("No match")
