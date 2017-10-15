# Regular expressions 1
RE- RE.SPLIT - RE.FINDALL - METACHARTS - RE.SUB

import re

RE.SPLIT 
# Regular expressions have their own special language. For example \s means a single space and \s+ means at least one space
# This string has some places where there are double spaces, new lines and tab spaces:
hem_string = 'He was an old man who  fished alone in a\n skiff in the  Gulf Stream and he had  gone eighty-four days \tnow without taking a fish.'
print hem_string
# Use re.split
re.split('\s',hem_string)
# Compare wtih...
re.split('\s+',hem_string) # Much neater

RE.FINDALL
# We can use other methods too, e.g. findall finds all the specified characters:
re.findall('\s',hem_string)


METACHARACTERS : . ^ $ * + ? { } [ ] \ | ( )
# Regular expressions in more detail. A key part of regular expressions are 
# 'metacharacters' - here is a list of them:
# . ^ $ * + ? { } [ ] \ | ( )
# They each do special things, and we'll look at them in turn

[]
# First let's look at [ ]. These are used for character classes, for example:
re.findall('[xyz]',hem_string) # Find all the x y or z
re.split('[w-z]',hem_string) # split anywhere there's a w, x, y or z

# Note that sometimes if you include a metacharacter inside a character class it's no longer a metacharacter
re.split('[ab.]',hem_string)

^[] COMPLEMENT OF THE SET
# To find the complement of the set, i.e. the opposite, use ^
re.findall('[^(c-z)]',hem_string) # finds everything that's not between c and z

#SHORTCUTS
# To avoid having to write out lots of confusing classes, re has SHORTCUTS:
# \d: match any decimal digits
re.findall('\d',hem_string) # Empty
# \D: match non decimals
re.findall('\D',hem_string) # Everywhere
# \s: whitespace
# \S: Non-whitespace
re.findall('\S',hem_string)
# \w: alphanumeric
# \W: nonalphanumeric
re.findall('\W',hem_string)

# Cleverly you can combine these things, e.g.
# find every whitespace or .
re.findall('[\s,.]',hem_string)

################################################################################

## Regular expressions 2

## Looking for repititions

# A useful metacharacter here is * which means match zero or more of the previous character
# For example ca*t will match ct (i.e. zero a characters), cat (1 a character), caat (2 as), etc

CHART:*
cat_string = 'ct cat cot caat coat cake cate'
re.findall('ca*t',cat_string) # Note that cat is in cate
# A more complicated example is h[a-e]*d. This will match with h at the start, at least 0 of a to e, then ending in d
had_string = 'hd had hed head heed hade heady heaved'
re.findall('h[a-e]*d',had_string) 

# Instead of * (match zero or more times) you can use + which means match 1 or more times
# Notice the differences with the above

CHART:+
cat_string = 'ct cat cot caat coat cake cate'
re.findall('ca+t',cat_string) # Note that cat is in cate

CHART:?
# Or ? which means match exactly zero or once
had_string = 'hd had hed head heed hade heady heaved'
re.findall('h[a-e]?d',had_string) 

CHART: {x,y}
# If you want to generalise this you can use {x,y} where x is the min number of 
# repitions you want and y the max number
had_string_2 = 'hd had hed head heed heeed hbbeaccd'
re.findall('h[a-e]{1,2}d',had_string_2) # Match exactly once or twice
# Look at how complicated we've got already!

# More metacharacters

CHART : |
# The verical pipe | is the or operator so a|b matches a or b
# Be careful because bat|man matches bat or man, not baman or batan
bat_string = 'batman baman batan'
re.findall('bat|man',bat_string)

TO MATCH AT THE BEGINNING
chart: ^letter
# Use ^ to match at the beginning of lines
super_heroes = 'superman batman spiderman hulk ironman'
re.findall('^s',super_heroes) #start with s?
re.findall('^b',super_heroes) #start with b?
# This second one finds nothing because ^ only looks at the start of the string
MATCHING THE FIRST LETTER WITHIN STRING THROUGH COMPREHENSION
# Use with multiline or in a comprehension for looking within strings
[re.findall('^b',x) for x in super_heroes.split()]

CHART: $  TO MATCH AT THE END
# Use $ to match at the end of a string
re.findall('man$',super_heroes)
[re.findall('man$',x) for x in super_heroes.split()]

# Use \b TO MATCH  A WORD BOUNDARY
re.findall(r'\bStream\b',hem_string) # Stream is there
re.findall(r'\bream\b',hem_string) # ream is not
# Notice that i'm using raw string literals here, otherwise Python interprates 
# \b as the backspace character

# Grouping - use () in the same way you would in a mathematical expression
# e.g. (rm)+ means match at least one of pattern rm, different from r(m+)
re.findall('(rm)+',super_heroes)
re.findall('r(m+)',super_heroes) # Find a match of r followed by at least one of m
# You can do much more complicated things with () - see the tutorial

# SUB AND SUBN TO REPLACE
# sub changes a pattern into something else specified by replacement
re.sub('super|man','lex_luther',super_heroes)
# Replace super or man with lex_luther

# subn does the same thing but tells you how many replacements it made
re.subn('super|man','lex_luther',super_heroes) # 5 replacement
# Returns a 2-tuple

# If there's no match just returns the original string
re.sub('cat|woman','bruce_wayne',super_heroes)


