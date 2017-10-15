RE.COMPILE  RE.MATCH  RE.SEARCH


RE.COMPILE
# Perhaps the best way to use re (at least if you're doing this often) is to
#'compile' the command and re-use it
my_regex = re.compile('\s+')
my_regex.split(hem_string)
my_regex.split(my_string)
# This compiling makes code run much faster as otherwise each individual command
# needs to be compiled again within re

# Note that my_regex can be printed out to remind us what it is
my_regex
# Tell us what type of object it is
print my_regex

RE.COMPILE AND RE.IGNORECASE
# To make .compile a bit richer, you can add flags:
my_regex_2 = re.compile('\w',flags=re.IGNORECASE) # This will ignore the case in when searching for alphenumeric characters
#re.IGNORECASE
#Perform case-insensitive matching; expressions like [A-Z] will match lowercase letters, too. This is not affected by the current locale.

MULTILINE
# Another useful flag is MULTILINE, which matches things at the beginning 
# (and/or end) of each line within the string
# What else can you do with a regular expression?



MATCH AND SEARCH

# Match sees whether the re matches at the beginning of the string
# Search looks for all substrings whether the re matches

# Let's try a very simple expression
simple_re = re.compile('[a-z]+') # so does the string contain at least one of a to z
simple_re.search('54321 hello!') # Doesn't give me anything useful!
# It's actually better to store this in an object and then use methods on that object
h = simple_re.search('54321 hello!')
# Look at group: shows all the accepted bits
h.group() 

# Start shows where the search starts. indice inizio
h.start()

# end shows where the search ends. indice finisce
h.end()

# span shows both in a tuple
h.span()

# Notice the difference if I had called match instead
m = simple_re.match('54321 hello!')
# Should give errors now because it couldn't find it at the start; m is empty
m.group()
# This means you'd commonly check whether m was None or not before doing anything with it



