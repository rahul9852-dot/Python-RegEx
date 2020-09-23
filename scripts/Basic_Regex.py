
# Python regex
# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
#RegEx can be used to check if a string contains the specified search pattern.

import re

'''txt="The Train in Spain"
x=re.search("^The.*Spain$",txt)

if x:
    print("Yes! We have a match!")
else:
    print("No match")
'''

# Findall()-->the Findall function returns list Containing all matches.
'''
txt="The rain in Spain"
x=re.findall("ai",txt)
print(x)'''

# Return Empty if no match found
'''
txt="The rain in Spain"
x=re.findall("Poryugal",txt)
print(x)'''

# Search() Function--> searches the string for a match, and returns a Match object if there is a match.
#If there is more than one match, only the first occurrence of the match will be returned:

'''txt="The rain in spain"
x=re.search("\s",txt)
print("The first white-space character is located in position:", x.start())
'''

# split() Function-->returns a list where the string has been split at each match:
'''txt="The rain in Spain"
x=re.split("\s",txt)
print(x)
'''

#we can control the number of occurrences by specifying the maxsplit parameter:
'''
txt="The rain in Spain"
x=re.split("\s",txt,1)
print(x)'''

# sub() function--> function replaces the matches with the text of your choice:

'''txt="The rain in Spain"
x=re.sub("\s","9",txt)
print(x)'''

#we can control the number of replacements by specifying the count parameter:
'''
txt="The rain in spain"
x=re.sub("\s","9",txt,2)
print(x)'''
