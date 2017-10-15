
## String manipulation
SPLIT - STRIP - JOIN - INDEX- -COUNT - REPLACE - STARTSWITH and ENDSWITH - LOWER and UPPER

# Some revision - here's a simple string
my_string = 'Stately, plump Buck Mulligan came from the stairhead, bearing a bowl of lather on which a mirror and a razor lay crossed.'
# We can index and slice it just like a list
my_string[3:10]
my_string[-7:]

# We can add and multiply objects with strings:
my_string + ' - ' + 'J'*2 

# Can seperate out into a list by character
list(my_string)

# A quick note on string literals
# If I have something like this:
my_path = 'C:\documents\new'
print my_path
# Python will automatically interpret the \n as a new line
# One way of getting round this is to escape the backslashes with 
my_path_2 = 'C:\\documents\\new'
print my_path_2
# Another neat way we can get round this by using a string literals
# One example is a raw sting, pre-fixed by r
my_path_3 = r'C:\documents\new'
print my_path_3
# Another example is a unicode string (which allows many more characers), prefixed by u - commonly seen in Json objects

# Useful methods for strings:
# splitting
SPLIT
my_string.split(' ') 
my_string.split(',') 
my_string.split() # Removes any whitespace
# Can also specify the number of splits to remove
my_string.split(' ',5)  # splits into 5 by taking the first 4 spaces

# stripping - removes rather than separates but works on individual elements 
# Usually used via a comprehension
COMPREHENSION AND STRIP
my_string_2 = 'pineapple,  oranges, bananas,  apples'
my_string_3 = [x.strip(' ') for x in my_string_2.split(',')]
output ['pineapple', '  oranges', ' bananas', '  apples']
# The above separates out by , and then strips out the spaces

#JOIN
# If we have lots of strings to join together we can use join rather than +
', '.join(my_string_3)

# in gives a Boolean as to whether something occurs or not
'Buck' in my_string
'buck' in my_string # Note: case sensitive

INDEX : location
# index gives the first location of a ','
my_string.index(',')
my_string.index('Buck') # Note that this is the location of the 'B'
my_string.index('buck') # Gives an error when not found

FIND=INDEX
# an alternative is find which doesn't give an error
my_string.find(',') # Same as index
my_string.find('Buck') # Same as index
my_string.find('buck') # Returns -1

COUNT
# Count returns the number of times a character or string appears
my_string.count('t')
my_string.count('zzzz') # Gives zero for things not found

REPLACE
# Replace useful for turning one thing into another
my_string.replace('B','D')
my_string.replace('plump','slim')

STARTSWITH or ENDSWITH
# endswith and startswith give Boolean
my_string_4 = [x.strip(',. ') for x in my_string.split(' ')] # Get rid of full stops and commas
[x.startswith('a') for x in my_string_4]
[x.endswith('ing') for x in my_string_4]

LOWER and UPPER LETTER
# Lower and upper convert to upper case
[x.upper() for x in my_string_4]
my_string.lower()
