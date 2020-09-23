# Metacharacters are characters with a special meaning.
'''
Character	Description	                                                               Example
[]	        A set of characters	                                                        "[a-m]"
\	        Signals a special sequence (can also be used to escape special characters)	"\d"
.	        Any character (except newline character)	                                "he..o"
^	        Starts with	                                                                "^hello"
$	        Ends with	                                                                "world$"
*	        Zero or more occurrences	                                                "aix*"
+	        One or more occurrences	                                                    "aix+"
{}	        Exactly the specified number of occurrences	                                "al{2}"
|	        Either or	                                                                "falls|stays"
()	        Capture and group'''

import re
# []
# find all charcter of lowercase between a-m.
'''txt="The rain in spain"
x=re.findall("[a-m]",txt)
print(x)'''

#[\]
# find all digit charcters
'''
txt="The will be 59 dollars"
x=re.findall("\d",txt)
print(x)'''

#.-->Search for a sequence that starts with "he", followed by two (any) characters, and an "o"
'''txt="Hello World"
x=re.findall("He..o",txt)
print(x)
x=re.findall("e..o",txt)
print(x)'''

#^-->Check if the string starts with 'hello'
'''
txt="Hello World"
x=re.findall("^Hello",txt)
if x:
    print("Yes, the string starts with hello")
else:
    print("No Match")'''

#$->Check if the string ends with 'world':
'''txt="Hello World"
x=re.findall("World$",txt)
if x:
    print("Yes, the string ends with world")
else:
    print("No Match")
'''
#ai*-->Check if the string contains "ai" followed by 0 or more "x" characters
'''txt="The rain in spain falls mainly in the plain"

x=re.findall("aix*",txt)

if x:
    print("Yes there is atleat one match!")
else:
    print("No match")'''

'''txt="Hey,how are you"
x=re.findall("aix*",txt)
print(x)
if x:
    print("Yes,there is at least one match!")
else:
    print("No Match")
'''
#'aix+'-->Check if the string contains "ai" followed by 1 or more "x" characters
'''
txt="The rain in spain falls mainly in the plain"

x=re.findall("aix+",txt)
print(x)

if x:
    print("Yes,there is at least one match!")
else:
    print("No match!")'''

#al{2}-->Check if the string contains "a" followed by exactly two "l" characters
'''txt="The rain in Spain falls Mainly in the plain"
x=re.findall("al{2}",txt)

print(x)

if x:
    print("yes,there is at least one match!")
else:
    print("No match")'''

# falls|stays-->Check if the string contains either "falls" or "stays"
txt="The rain in Spain falls mainly in the plain"
x=re.findall("falls|stays",txt)
print(x)

if x:
    print("Yes, there is atlest one match!")
else:
    print("No match")
