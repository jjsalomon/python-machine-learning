# DPP Assessed exercises 9 - note: shorter than week 10

# Part 1: string manipulation, string literals, splitting and stripping, join
# in and index, find, count, replace, endswith, startswith, upper and lower

import re

# Q1 The below command will generate a random list of letters from abcdef of size 10
import numpy.random as npr
npr.choice(list('abcdef'),size=10)
# Suppose I want to generate a password of length 15 using all the letters a-z by joining this list together
# Type the command I should use (make sure the letters are in alphabetical order):
''.join(npr.choice(list('abcdefghijklmnopqrstuvwxyz'),size=15))

# Q2 I want to replace all the commas in the following string to new line characters
addr = ['Room 536, Library Building, University College Dublin, Dublin 4, Ireland', 'Room G03, Science Centre North University College Dublin, Belfield, Dublin 4, Ireland']
# Which of the following is the command to use?
[x.replace(',','\n') for x in addr]
# Others
addr.replace(',','\n')
addr.findall(',')
[z.strip(',') for z in addr]
[y.split(',') for y in addr]

################################################################################

# Part 2: regular expressions 1, split and findall, metacharacters, character classes, shortcuts

# Q1 I want to extract the area code from the following list of phone numbers
ph_num = '(01) 12 05 25, (04) 25 23 11, (08) 03 49 98'
# Which of the following regular expressions extracts the area codes (i.e. the numbers in the brackets)? (Make sure you understand what each line is doing)
re.findall('\(..\)',ph_num)
re.findall('\(\d{2}\)',ph_num)
re.findall('\([0-9]{2}\)',ph_num)
# Others
re.findall('\d',ph_num)

# Q2 I have a list of filenames and I want to extract all the file extensions (the values after the .)
files = ['lecture_9_code.py','graphs.jpeg','lecture_9.pdf','lecture9a.mp4']
# Which of the following will split the filenames everywhere there's a full stop
[re.split('[.]',x) for x in files]
[re.split('[\W]',x) for x in files]
# Others
[re.split('.',x) for x in files]
[re.findall('.',x) for x in files]

################################################################################

# Part 3: Repetitions with *, +, ? and {}, compiling regular expressions, flags
# Match and search

# Q1 I have a string consisting of email addresses and I want to find the domain (the part after the @)
em = ['andrew.parnell@ucd.ie','president@whitehouse.com','enda@gov.ie']
# Write a regular expression in a list comprehension that extracts the characters after the @ sign (your answer may include the @ sign
# (note: your answer might be different from mine so may be marked wrong by Blackboard but I will manually correct any that produce the right answer
# Possible things that work
[re.findall('@[a-z]+',x) for x in em]
[re.findall('@[a-z]*.[a-z]*',x) for x in em]
[re.findall('@\S+',x) for x in em]
[re.findall('@[a-z]*.[a-z]*',x) for x in em]
[re.compile('@[\w-]+(?:\.[a-zA-Z-]+)+').findall(x) for x in em]
[re.findall('@[a-z]+.[a-z]+',x) for x in em]
[re.findall('@[a-z]+\.[a-z]+',x) for x in em]
[re.findall("@[\w.]+",x) for x in em]
[re.split('.+@',x)[1] for x in em]
[re.compile('@[a-z.-]+\.[a-z]+').findall(x) for x in em ]
[re.findall('@+\w*.\w*',x) for x in em]
[re.findall("@[^@]{1,50}",x) for x in em]
[re.findall('@[\w,.]+',x) for x in em]
[re.compile('@[a-zA-Z0-9-]+\.[a-z]+').findall(x) for x in em ]
[[re.search('(?<=@)\D+',x) for x in em][a].group() for a in range(3)]
[re.findall('@+[a-z]*.[a-z]*',x) for x in em]
[re.findall("@[\w.]+", x) for x in em]
[re.compile('@[\w]+\.[\w]+').findall(x) for x in em]
[re.findall('@(.*)$',x) for x in em]
[re.search("@[\w.]+", x).group() for x in em]
[re.findall('@.*',x) for x in em]
[re.split('@',x)[1] for x in em]

# Q2 I have a list of strings created via:
continents = ['Australasia','America','Europe','asia','antartica','Africa']
# I want to extract all the continents that begin and end in the letter a (capitalised or not).
# What values should replace X and Y (write them out below separated by a space)?
#cont_re = re.compile('a[a-z]+a',flags=X)
#[cont_re.findall(x) for x in Y]
cont_re = re.compile('a[a-z]+a',flags=re.IGNORECASE)
[cont_re.findall(x) for x in continents]
# Other suitable answers
cont_re = re.compile('a[a-z]+a',flags=re.I)
[cont_re.findall(x) for x in continents]

################################################################################

# Part 4: | as or, ^ for matching at the beginning, $ to match at the end, () to group
# sub and subn, 

# Q1 I want to extract the email addresses in the following strings
junk_mails = ['John Koftaram <test@capahq.org> would like to connect on LinkedIn. How would you like to respond?',' Re: Your Abandoned Package For Delivery I have very vital information to give to you, but first I must have your trust before I review it to you because it may cause me my job, so I need somebody that I can trust for me to be able to review thesecret to you. Contact me at BENSON OMALU <admin@handwheel.com>','FROM DESKTOP OF MR.Manuel Medina-MoraCHIEF EXECUTIVE OFFICER E-MAIL: manuelmedina@aol.com ATTENTION BENEFICIARY']
# Write a regular expression which matches any characters (from a-z) at least once, 
# followed by an @ symbol, followed by any set of characters again, followed by a full stop, 
# followed by any set of characers again
# (don't forget the escape character) followed by any set of characters again.
# It should fit in the below code
# find_email = re.compile('HERE')
# and should be used with
# [find_email.findall(x) for x in junk_mails]
find_email = re.compile('[a-z]+@[a-z]+\.[a-z]+')
[find_email.findall(x) for x in junk_mails]
# Others
find_email = re.compile('[a-z]+@[a-z]+.[a-z]+')
[find_email.findall(x) for x in junk_mails]
find_email = re.compile('\w+@\w+.')
[find_email.findall(x) for x in junk_mails]
find_email = re.compile('[\w]+@[\w]+\.[\w]+')
[find_email.findall(x) for x in junk_mails]
find_email = re.compile('[a-z]+@[a-z]+.[a-z]+')
[find_email.findall(x) for x in junk_mails]
find_email = re.compile('\w+@[\w.]+')
[find_email.findall(x) for x in junk_mails]
find_email = re.compile('[a-z]+@[a-z]+[.][a-z]+')
[find_email.findall(x) for x in junk_mails]
find_email = re.compile('[a-z]+@[\w.]+')
[find_email.findall(x) for x in junk_mails]
find_email = re.compile('[\w]+@[\w.]+')
[find_email.findall(x) for x in junk_mails]
find_email = re.compile('[a-z]+@[a-z,.]+')
[find_email.findall(x) for x in junk_mails]
find_email = re.compile('[a-z]+@+[a-z]+\.+[a-z]+')
[find_email.findall(x) for x in junk_mails]
find_email = re.compile('\w+@\w+\.\w+')
[find_email.findall(x) for x in junk_mails]
find_email = re.compile('[\w]+@[\w]+[.][\w]+')
[find_email.findall(x) for x in junk_mails]
find_email = re.compile('[a-z]+@[a-z]+\.[a-z]+')
[find_email.findall(x) for x in junk_mails]
find_email = re.compile('[a-z]+@[a-z]+.[a-z]+')
[find_email.findall(x) for x in junk_mails]
find_email = re.compile('[a-z]+@[a-z,.]+')
[find_email.findall(x) for x in junk_mails]

# Q2 I have a list of file names which include dates in their titles:
files = ['code_230513.py','code_240613.py','code_040614.py','code_050814.py']
# I want to replace all the dates so that they are in the format yyyymmdd.
# I used the command:
[re.sub(r'(\d{2})(\d{2})(\d{2})', r'20\3\2\1',x) for x in files]
# Study the above command carefully and see if you can work out what it's doing
# I have some new files which look slightly different, they are in mmddyyyy format
# and I want them in yyyymmdd format as before. 
files2 = ['code_03052013.py','code_04062013.py','code_10312013.py','code_10082014.py']
# What new command should I use?
[re.sub(r'(\d{2})(\d{2})(\d{4})', r'\3\1\2',x) for x in files2]
# Others
[re.sub(r'(\d{2})(\d{2})(\d{4})', r'\3\2\1',x) for x in files2]
