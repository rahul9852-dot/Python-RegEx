# Special Sequences-->A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

#\A(char)--> Returns a match if the specified characters are at the beginning of the string.

import re

#\A(char)--> Returns a match if the specified characters are at the beginning of the string.

'''txt="Hii Anmol"
x=re.findall("\AThe",txt)
print(x)'''

#r"\b(ain)-->beginning",r"(ain)\b--->End"-->Returns a match where the specified characters are at the beginning or at the end of a word
#(the "r" in the beginning is making sure that the string is being treated as a "raw string")

'''txt="The rain in Spain"
x=re.findall(r"\bain",txt)
print(x)
if x:
    print("Yes,there is at least one match")
else:
    print("No Match")'''


'''r"(ain)\b--->End
txt="The rain in Spain"
x=re.findall(r"ain\b",txt)
print(x)
if x:
    print("yes,there is at lest one match!")
else:
    print("No Match")
# \B-->Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
'''
#"\d"-->Returns a match where the string contains digits (numbers from 0-9)

'''txt="The rain in Spain"
x=re.findall("\d",txt)
if x:
    print("Yes,there is at lest one match!")
else:
    print("No match")
'''
# "\D"-->Returns a match where the string DOES NOT contain digits

'''txt="The rain in Spain"
x=re.findall("\D",txt)
print(x)
if x:
    print("Yes, there is a match!")
else:
    print("No match!")'''

#"\s"-->Return a match at every white-space character

'''txt="The rain in Spain"
x=re.findall("\s",txt)
print(x)
if x:
    print("Yes,there is a match!")
else:
    print("No match!")
'''
# "\S"-->Returns a match where the string DOES NOT contain a white space character

'''txt="The rain in Spain"
x=re.findall("\S",txt)
print(x)
if x:
    print("Yes,there is a match!")
else:
    print("No match")
'''
# "\w"-->Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)

'''txt="Hii,How are you my phone number 989898737_"
x=re.findall("\w",txt)
print(x)
if x:
    print("Yes,there is a match!")
else:
    print("There is no match!")
'''

#"\W"-->Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.)
'''txt="The rain in Spain"
x=re.findall("\W",txt)
print(x)
if x:
    print("Yes there is a a match!")
else:
    print("No match")
'''
#"Spain\Z"-->Returns a match if the specified characters are at the end of the string.
'''txt="The rain in Spain"

x=re.findall("Spain\Z",txt)
print(x)
if x:
    print("Yes,there is a match")
else:
    print("No match")'''
