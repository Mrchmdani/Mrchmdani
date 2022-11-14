import abc
from ctypes import LibraryLoader
from curses.ascii import ETB
from msilib import sequence
from operator import length_hint
from select import select
from termios import N_TTY

from attr import Attribute


x = 1
print(x)
x = x + 1
print(x)

x = 2           #assignment statement
x = x + 1       #asignment with expression
print(x)        #print statement

# Interactive cs script
    # Interactive = type directly to python one line at a time and it responds
    # script = enter a sequence of statements (line) into a file using a text editor and tell Python to execute the statement in the file

#Conditional Steps
x = 5
if x < 10 :
    print('smaller')
if x > 20 :
    print('bigger')
print('Finish')

#Repeated Steps
n = 5
while n > 0 :
    print(n)
    n = n - 1
print('Blastoff')

#Sequential Code
name = input('Enter file:')
handle = open(name, 'r')

count = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)

#Variables
    #A variable is a named place in the memory where a programmer can store data and later retrieve it

x = 12.2
y = 14
x = 100     #rewrite the first 'x' variable

#python variable name rules
    #must start with a letter or underscore
    #must consist of letters, numbers, and underscore
    #case censitive

#Numeric Expression
    # + addition
    # - subtraction
    # * multiplication
    # / division
    # ** power
    # % remainder / modular operator -> bilangan yang tidak habis setelah dibagi misal: 23/5 -> 5*4 = 20 -> 23-20 = 3 -> 3 adalah sisanya/remainder/modular

#Operator Precedence Rules
    # Parenthese
    # Exponentiation (power)
    # Multiplication, division, and remainder
    #addition and subtraction
    # left to right

#User Input
name = input('Who are you? ')
print('Welcome', name)

#Comparison Operators
# < Less than
# <= Less than or Equal to
# == Equal to
# >= Greater than or Equal to
# > Greater than
# != Not equal

x = 5
if x == 5 :
    print('Equal 5')
if x > 4 :
    print('Greater than 4')
if x >= 5 :
    print('Greater than 5 or Equals 5')    
if x < 6 :
    print('Less than 4')
if x <= 5 :
    print('Less than or Equal 5')
if x != 6 :
    print('Not Equal 6')

#One-Way Decisions
x = 5
print('Before 5')
if x == 5 :
    print ('Is 5')
    print('Is Still 5')
    print('Third 5')
print('Afterwards 5')
print('Before 6')
if x -- 6 :
    print('Is 6')
    print('Is Still 6')
    print('Third 6')
print('Afterwards 6')

#Nested Decisions
x = 42
if x > 1 :
    print('More than one')
    if x < 100 :
        print('Less than 100')
print('All done')

#Two-way Decisions with Else
x = 4
if x > 2 :
    print('Bigger')
else :
    print('Smaller')
Print 'All done'

#Multi-way
if x < 2 :
    print('Small')
elif x < 10 :
    print*'Medium'
else :
    print('Large')
print('All done')

#Indent is matter, wrong index makes error

#IndetationError: unexpected indent
x = 5
    if x < 10 :         #there is spaces before "IF", that cause error
print('smaller')
print('Finish')

#IndetationError: unindent does not match any outer indentation level
x = 5
if x < 10 :
print('smaller')        #this code has the same number of spaces with before
print('Finish')

# Unindent does not match any outer indentation level. 
    # This line of code has fewer spaces at the start than the one before, but equally it does not match any other block it could be part of.
    # Python cannot decide where it goes.

#Try and except condition
astr = 'Bob'
try :
    print('Hallo')
    istr = int(astr)
    print('There')
except:
    istr = -1
print('Done', istr)

rawstr = input('Enter a number:')
try:
    ival = int(rawstr)
except:
    ival = -1
if ival > 0 :
    print('Nice work')
else:
    print('Not a number')

#Stored (and reused) Steps
def thing():
    print('Hello')
    print('Fun')
thing()         #Hello Fun
print('Zip')    #Zip
thing()         #Hello Fun

x = 5
print('Hello')
def print_lyric() :
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')
print('Yo')
print_lyric()
x = x + 2
print(x)

#Parameters
def greet(lang) :       # (lang), a parameter is a variable which we use in the function definition
    if lang == 'es' :
        print('Hola')
    elif lang == 'fr' :
        print('Bonjur')
    else :
        print('Halo')
greet('en')
greet('es')
greet('fr')

#Return Values
def greet():
    return "Hello"          #break the loop
print(greet(), "Glenn")
print(greet(), "Sally")

def greet(lang) :
    if lang == 'es' :
        print('Hola')
    elif lang == 'fr' :
        print('Bonjur')
    else :
        return('Halo')
print(greet('en'), 'Glenn')
print(greet('es'), 'Sally')
print(greet('fr'), 'Michael')

#Repeated Steps
n = 5
while n > 0 :
    print(n)
    n = n - 1           #iteration variable
print('Blastoff!')
print(n)

#Infinite Loop
n = 5
while n > 0 :
    print('Leater')     #No iteration variable that break the loops
    print('Rinse')
print('Dry off!')

#Another Loop
n = 0               #Loop that not run and skip to last line
while n > 0 :
    print('Leater')
    print('Rinse')
print('Dry off!')

#Breaking Out of a Loop
while True:
    line = input('> ')
    if line == 'done':
        break       #break
    print(line)
print('Done!')

#Finishing an Iteration with continue
while True:
    line = input('> ')
    if line[0] == '#' :
        continue
    if line == 'done' :
        break
    print(line)
print('Done!')

n = 0
while True:
    if n == 3:
        break       #break when loop reach 3
    print(n)
    n = n + 1

#A Simple Definite Loop
for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff!')

#Definite loop with strings
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')

#Looping through a Set
print('Before')
for thing in [9, 41, 12, 3, 74, 15] :
    print(thing)
print('After')

#Loop Idioms (Pattern)
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15] :
    if the_num > largest_so_far :
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('After', largest_so_far)

smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        break       #cause error / not running properly
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)

#Counting in a loop
zork = 0
print('Before', zork)
for thing in [3, 41, 12, 9, 74, 15]:
    zork = zork + 1
    print(zork, thing)
print('After', zork)

#Summing in a loop
zork = 0
print('Before', zork)
for thing in [3, 41, 12, 9, 74, 15]:
    zork = zork + thing
    print(zork, thing)
print('After', zork)

#Finding the Average in a loop
count = 0
sum = 0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum / count)

#Filtering in a Loop
print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20:
        print('Large number', value)
print('After')

#Search Using a Boolean Variable
found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
    print(found, value)
print('After', found)

#Finding the smallest value
smallest = None
print("Before")
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)
print("After", smallest)

#Finding the largest value
largest = None
print("Before")
for value in [9, 41, 12, 3, 74, 15]:
    if largest is None :
        largest = value
    elif value > largest :
        largest = value
    print(largest, value)
print("After", largest)

#Looking inside Strings
fruit = 'banana'
letter = fruit[1]       #Square brackets for index value
print(letter)

x = 3
w = fruit(x-1)          ##Square brackets for index value
print(w)

#Strings Have Length
fruit = 'banana'
print(len(fruit))       #len/length is number of word

#Looping Through Strings
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit(index)
    print(index, letter)
    index = index + 1

fruit = 'banana'
for letter in fruit:
    print(letter)

#Looping and Counting
word = 'banana'
count = 0
for letter in word :
    if letter == 'a' :
        count = count + 1
print(count)

#Slicing Strings
s = 'Monty Python'
print(s[0:4])
print(s[6:7])       #second number is stop value, it will take the letter before second number
print(s[6:20])      #if second number beyond the end of the string, it stop at the end

#String Concatenation
a = 'Hallo'
b = a + 'There'
print(b)
c = a + ' ' + 'There'
print(c)

#Using 'in' as a logical Operator
fruit = 'banana'
'n' in fruit

'm' in fruit

'nan' in fruit

if 'a' in fruit:
    print('Found it!')

#String Comparison
if word == 'banana':
    print('All right, bananas.')

if word < 'banana':
    print('Your word,' + word + 'comes before banana.')
elif word > 'banana' :
    print('Your word,' + word + 'comes after banana.')
else:
    print('All right, bananas.')

#String LibraryLoader
greet = 'Hallo Bob'
zap = greet.lower()     #lower() is lower case
print(zap)
print(greet)
print('Hi There'.lower())

stuff = 'Hello world'
type(stuff)     #checking type of string
dir(stuff)

#Searching a String
fruit = 'banana'
pos = fruit.find('na')
print(pos)

aa = fruit.find('z')
print(aa)

#Making UPPER LOWER CASE
greet = 'Hallo Bob'
nnn = greet.upper()     #Upper case
print(nnn)

nnn = greet.lower()     #Lower case
print(nnn)

#Search and Replace
greet = 'Hallo Bob'
nstr = greet.replace('Bob', 'Jane')
print(nstr)

#Stripping Whitespace
greet = '    Hallo Bob    '
greet.lstrip()      #remove whitespace at left
greet.rstrip()      #remove whitespace at right
greet.sstrip()      #remove whitespace at both (beginning and ending)

#Prefix
line = 'Please have a nice day'
line.startswith('Please')
line.startswith('p')

#Parsing and Extracting
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos +1 : sppos]
print(host)

#The newline Character
stuff = 'Hello\nWorld!'
stuff
print(stuff)

stuff = 'X\nY'
print (stuff)
len(stuff)

#Counting a File
fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count +1
print('Line Count:', count)

#Searching Through a File
fhand = open('mbox.txt')
for line in fhand:
    if line.startwith('From:') :
print(line)         #This will print newline (\n)

fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()    #fixed
    if line.startwith('From:') :
print(line)

fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()    
    if line.startwith('From:') :
        continue            #skipping with continue
print(line)

#Concatenating list
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

#building list from scratch
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)

#Is something in a list
some = [1, 9, 21, 10, 16]
9 in some
15 in some
20 not in some

#List are in Order
friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends)

#Built-in Function and Lists
nums = [9, 41, 12, 3, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

total = 0
count = 0
while True :
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    total = total + value
    count = count + 1
average = total / count
print('Average:', average)

numlist = list()
while True :
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print('Average:', average)

words = 'His e-mail is q-lar@freecodecamp.org'
pieces = words.split()      #split() break sentence into pieces
print(pieces)
parts = pieces[3].split('-') #split('-') break piece based on '-'
print(parts)
n = parts[1]
print(n)

line = 'A lot              of spaces'
etc = line.split()      #split() do not specify delimited and treated like one delimited
print(etc)
line = 'first;second;third'
thing = line.split()
print(thing)
print(len(thing))
line = 'first;second;third'
thing = line.split(';')
print(thing)
print(len(thing))

#list is linear of collection of values that stay in order
#dictionary is a 'bag' of values, each with it's own label

dict = {"Fri": 20, "Thu": 6, "Sat": 1}
print(dict)
dict["Thu"] = 13
dict["Sat"] = 2
dict["Sun"] = 9
print(dict)

#When we see a new name
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    if name not in counts :
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts)

#Counting pattern
counts = dict()
print('Enter a line of text:')
line = input('')
words = line.split()
print('Word', words)
print('Counting ...')
for word in words :
    counts[word] = counts.get(word,0) + 1
print('Count', counts)

counts = ('chuck' : 1, 'fred': 42, 'jan' : 100)
for key in counts :
    print(key, counts[key])

#Retrieving list of Keys and Values
jjj = {'chuck' : 1, 'fred': 42, 'jan' : 100}
print(list(jjj))
print(jjj.keys())
print(jjj.values())
print(jjj.items())

#two iteration variables
jjj = {'chuck' : 1, 'fred': 42, 'jan' : 100}
for aaa, bbb in jjj.items() :
    print(aaa, bbb)

name = input('Enter file:')
handle = open(name, 'r')

count = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    if counts[key] > 10:
        print(key, counts[key])

#Tuples are another kind of sequence that functions much like a list
    #They have element which are indexed starting at 0
x = ('Glenn', 'Sally', 'Joseph')
print(x[2])

y = (1, 9, 2)
print(y)
print(max(y))

for iter in y:
    print(iter)

#Tuples are "immutable"
    #can't alter it's content
x = [9, 8, 7]
x[2] = 6
print(x)

y = 'ABC'
y[2] = 'D'

z = (5, 4, 3)
z[2] = 0

x = (3, 2, 1)
x.sort()
x.append(5)
x.reverse()

#Different list and tuple
l = list()
dir(l)
t = tuple()
dir(t)

#Tuples and assignment
(x, y) = (4, 'fred')
print(y)
(a, b) = (99, 98)
print(a)

#tuples and dictionaries
d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k, v) in d.items():
    print(k,v)

tups = d.items()
print(tups)

d = dict()
d['quincy'] = 1
d['beau'] = 5
d['kris'] = 9
for (k,i) in d.items():
    print(k, i)

#tuples are comparable
(0, 1, 2) < (5, 1, 2)
(0, 1, 2000000) < (0, 3, 4)
('Jones', 'Sally') < ('Jones', 'Sam')
('Jones', 'Sally') > ('Adams', 'Sam')

#sorting list of tuples
d = {'a':10, 'b':1, 'c':22}
d.items()
sorted(d.items())

d = {'a':10, 'b':1, 'c':22}
t = sorted(d.items())
t
for k, v in sorted(d.items()):
    print(k, v)

#sort by values instead of key
c = {'a':10, 'b':1, 'c':22}
tmp = list()
for k, v in c.items():
    tmp.append((v,k))       #flipped key and value
print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)

fhand = open('romeo.txt')       #open files
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
for val, key in lst[:10]:
    print(key, val)

#sorter version
c = {'a':10, 'b':1, 'c':22}
print(sorted([(v,k) for k,v in c.items()]))

#using re.search() like find()

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From:') >= 0:
        print(line)

import re           #before use regular expresion must import library
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:') >= 0:
        print(line)

#using re.search() like find(), startwith()
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.startwith('From:') :
        print(line)

import re           #before use regular expresion must import library
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line) :
        print(line)

#wild-card character
^X.*:       # '^' start with X, '.' match any character, '*' many times
^X-\S+:     # '\S' match any non-whitespace character
            # '\s' match only a white space character

#matching and extracting data
import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9+', x)      #[0-9] find between this digit
print(y)                        #[0-9]+ find one or more digits
y = re.findall('AEIOU+', x)     #find uppercase AEIOU, none match because no uppercase
print(y)

#Greedy matching
import re
x = 'From: Using the' : character
y = re.findall('^F.+:', x)      #this code looking the longest string
print(y)                        #the repeat character (* and +) push outward in both directions(greedy) to match the largest posible sting

#Non-greedy matching
import re
x = 'From: Using the' : character
y = re.findall('^F.+?:', x)      # '.+?' one or more character but not greedy
print(y)  

#fine tuning string extraction
import re
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('\S+@\S+', x)    #at least one non-white space character
print(y)
y = re.findall('^From (\S+@\S+)', x)    #parenthese are not part of the match - but they tell where to start and stop what string to extact
print(y)

import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)

#double split pattern
line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])

#REGEX version
#Python Regular Expression Quick Guide

# ^        Matches the beginning of a line
# $        Matches the end of the line
# .        Matches any character
# \s       Matches whitespace
# \S       Matches any non-whitespace character
# *        Repeats a character zero or more times
# *?       Repeats a character zero or more times 
#          (non-greedy)
# +        Repeats a character one or more times
# +?       Repeats a character one or more times 
#          (non-greedy)
# [aeiou]  Matches a single character in the listed set
# [^XYZ]   Matches a single character not in the listed set
# [a-z0-9] The set of characters can include a range
# (        Indicates where string extraction is to start
# )        Indicates where string extraction is to end

import re
lin = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
y = re.findall('@([^ ]*)', lin)   #look through the string unting you find an '@' sign
print(y)
y = re.findall('^From .*@([^ ]*)', lin)

#escape character
#if you want a special regular expression character to just behave normally, you prefix it with '\'
import re
x = 'We just received $10.00' for cookies.
y = re.findall('\$[0-9.]+', x)
print(y)

#common tcp ports
Telnet(23) - Login
SSH(22) - Secure Login
HTTP(80)
HTTPS(443) - Secure
SMTP(25)(Mail)
IMAP(143/220/993) - Mail Retrieval
POP(109/110) - Mail Retrieval
DNS(53) - Domain Name
FTP(21) - File Transfer

#socket in python
import socket
mysock = socket.socket(socket.AFINET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

# An HTTP request in python
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1) :
        break
    print(data.decode())
mysock.close()

#simple web browser
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
mysock.close()

#using urlib in python
import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

#run only contents of "romeo.txt".
import urllib.request
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

#Web scraping
#When a program or script pretend to be a browser and retrieves web pages, looks at those web pages, extracts information, and then looks at more web oages
#search engine scrape wen pages - It's called "spidering the web" or "web crawling"

#the easy way install beautiful soup
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')     #input this : http://www.dr-chuck.com/page1.html -> http://www.dr-chuck.com/page2.html
html = urllib.request.urlopen(url).read()  
soup = BeautifulSoup(html, 'html.parser')

#retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

#XML basics
<person>
 <name>Chuck</name>
 <phone type="intl">
 +1 734 303 4456
 </phone>
 <email hide = "yes"/>
</person>

#xml schema - XSD structure
<person>
<lastname>Severance</lastname>
<age>17</age>
<dateborn>2001-04-17<dateborn>
</person>

#XSD schema
<xs:complexType name="person">
 <xs:sequence>
  <xs:element name="lastname" type="xs:string"/>
  <xs:element name="age" type="xs:integer"/>
  <xs:element name="dateborn" type="xs:date"/>
 </xs:sequence>
</xs:complexType>

#XSD constraints
<xs:element name="person">
 <xs:complexType>
  <xs:sequence>
   <xs:element name="full_name" type="xs:string"
    minOccurs="1" maxOccurs="1"/>
   <xs:element name="child_name" type="xs:integer"
    minOccurs="0" maxOccurs="10"/>
  </xs:sequence>
 </xs:complexType>
</xs:element>

<person>
 <full_name>Tove Refsnes</full_name>
 <child_name>Hege</child_name>
 <child_name>Stale</child_name>
 <child_name>Jim</child_name>
 <child_name>Borge</child_name>
</person>

#CSD data type
<xs:element name="full_name" type="xs:string"/>
<xs:element name="start" type="xs:string"/>
<xs:element name="startdate" type="xs:string"/>
<xs:element name="prize" type="xs:string"/>
<xs:element name="weeks" type="xs:string"/>

<customer>John Smith</customer>
<Start>2002-09-24</child_name>
<Startdate>2002-05-30T09:30:10</child_name>
<prize>999.50</child_name>
<weeks>30</child_name>

import xml.etree.Element Tree as ET
data = '''<person>
  <name>Chuck</name>
  <phone type="intl">
   +1 734 303 4456
  </phone>
  <email hide = "yes"/>
 </person>'''

tree = ET.fromstring(data)
print('Name', tree.find('name').text)
print('Attr', tree.find('email').get('hide'))       #STILL ERROR

#JSON language
#JSON represents data as nested "list" and "dictionaries"
import json
input = '''
  [
    { "id" : "001",
      "x" : "2",
     "name" : "Chuck"
    } ,
    { "id" : "009",
      "x" : "7",
      "name" : "Chuck"
    }
  ]'''

info = json.loads(input)
print('User count:', len(info))
for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])


import json
data = '''
  [
    { "id" : "001",
      "x" : "2",
     "name" : "Quincy"
    } ,
    { "id" : "009",
      "x" : "7",
      "name" : "Mrugesh"
    }
  ]
'''
info = json.loads(data)
print(info[1]['name'])

#Application Program Interface(API)
"status": "OK"
 "results": [
     {
         "geometry":{
             "location_type": "APPROXIMATE",
             "location": {
                 "lat": 42.2808256
                 "lng": -83.7430378
             }
         },
         "address_components": [
             {
                 'long_name': "Ann Arbor",
                 "types": [
                     "locality",
                     "political"
                 ],
                 "short_name": Ann Arbor
             }
         ],
         "formatted_address": "Ann Arbor, Mi, USA",
         "types": [
             "locality",
             "political"
         ]
     }
 ]


import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True :
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('=== Failure To Retrieve ===')
    print(data)
    continue

print(json.dumps(js, indent=4))

lat = js["results"][0]["geometry"]['location']["lat"]
lng = js["results"][0]["geometry"]['location']["lng"]
print('lat', lat, 'lng', lng)
location = js['results'][0]['formatted_address']
print(location)         #STILL ERROR

#EXERCISE: GeoJSON (https://www.youtube.com/watch?v=TJGJN0T8tak)
#EXERCISE: JSON (https://www.youtube.com/watch?v=vTmw5RtfGMY)
#EXERCISE: Twitter (https://www.youtube.com/watch?v=2c7YwhvpCro)
#EXERCISE: XML (https://www.youtube.com/watch?v=AopYOlDa-vY)

#python object
#input -> process -> output
inp = input('Europe floor?')
usf = int(int) + 1
print('US floor', usf)

class PartyAnimal:
    x = 0

    def party(self) :
        self.x = self.x +1
        print("So far", self.x)

an = PartyAnimal()
an.party()
an.party()
an.party()


class PartyAnimal:
    x = 0
    def party(self):
        self.x = self.x + 2
        print(self.x)

an = PartyAnimal()
an.party()
an.party()

#playing with dir() and type()
x = list()
type(x)
dir(x)      #to find "capabilities" of  newly created class

#constructor - to set up some instance variables to have the proper initial values when the object is created
#destructor - 
class PartyAnimal:
    x = 0

    def __init__(self) :            #constructors
        print('I am constructed')

    def party(self):
        self.x = self.x + 2
        print('So far', self.x)

    def __del__(self) :             #destructor
        print('I am destructed', self.x)

an = PartyAnimal()
an.party()
an.party()
an = 42
print('am contains', an)


class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, z):
        self.name = z
        print)self.name, "constructed"
    
    def party(self):
        self.x = self.x + 1
        print(self.name,"party count", self.x)
s = PartyAnimal("Sally")
s.party()

j = PartyAnimal("Jim")
j.party()
s.party()


class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name,'constructed')
    def party(self):
        self.x = self.x + 1
        print(self.name,'party count',self.x)

q = PartyAnimal('Quincy')
m = PartyAnimal('Miya')

q.party()
m.party()
q.party()

#inheritance
class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name,'constructed')
    def party(self):
        self.x = self.x + 1
        print(self.name,'party count',self.x)

class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)
s = PartyAnimal("Sally")
s.party()
j = FootballFan("Jim")
j.party()
j.touchdown()

#definitions
#Class - a template
#Attribute - a variable within a class
#Method - a function within a class
#Object - a particular instance of a class
#Constructor - code that runs when an object is created
#Inheritance - the ability to extend a class to make a new class

#make database (SQL)
  
#Single Table SQL
CREATE TABLE "Users" ("name" TEXT, "email" TEXT)

INSERT INTO Users (name, email) VALUES ('Chuck', 'csev@umich.edu')
INSERT INTO Users (name, email) VALUES ('Colleen', 'cvl@umich.edu')
INSERT INTO Users (name, email) VALUES ('Ted', 'ted@umich.edu')
INSERT INTO Users (name, email) VALUES ('Sally', 'a1@umich.edu')
INSERT INTO Users (name, email) VALUES ('Ted', 'ted@umich.edu')
INSERT INTO Users (name, email) VALUES ('Kristen', 'kf@umich.edu')

#SQL Delete
DELETE FROM Users WHERE email='ted@umich.edu'

#SQL update
UPDATE Users SET name="Charles" WHERE email='csev@umich.edu'

#Retrieving record: select
SELECT * FROM Users

SELECT * FROM Users WHERE email='csev@umich.edu'

#sorting with ORDER BY
SELECT * FROM Users ORDER BY email

SELECT * FROM Users ORDER BY name DESC

#Multi-Table SQL:
# primary key - generally an integer auto_increment field
# logical key - what the outside world uses for lookup
# foreign key - generally an integer key pointing to a row in another table

CREATE TABLE "Artist" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
    "name" TEXT)

CREATE TABLE "Album" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
    artist_id INTEGER,
    "title" TEXT)

CREATE TABLE "Genre" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
    "name" TEXT)

CREATE TABLE "Track" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
    album_id INTEGER, 
    genre_id INTEGER, 
    len INTEGER, rating INTEGER, 
    "title" TEXT, "count" INTEGER)

#insert table row
INSERT INTO Artist (name) VALUES ('Led Zepplin')
INSERT INTO Artist (name) VALUES ('AC/DC')

INSERT INTO Genre (name) VALUES ('Rock') ;
INSERT INTO Genre (name) VALUES ('Metal');

INSERT INTO Album (title, artist_id) VALUES ('Who Made Who', 2);
INSERT INTO Album (title, artist_id) VALUES ('IV', 1);

INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
    VALUES ('Black Dog', 5, 297, 0, 2, 1) ;
INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
    VALUES ('Stairway', 5, 482, 0, 2, 1) ;
INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
    VALUES ('About to Rock', 5, 313, 0, 1, 2) ;
INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
    VALUES ('Who Made Who', 5, 207, 0, 1, 2) ;

#join operation
SELECT Album.title, Artist.name FROM Album JOIN Artist 
    ON Album.artist_id = Artist.id

SELECT Album.title, Album.artist_id, Artist.id, Artist.name 
    FROM Album JOIN Artist ON Album.artist_id = Artist.id

SELECT Track.title, Track.genre_id, Genre.id, Genre.name 
    FROM Track JOIN Genre   

SELECT Track.title, Genre.name FROM Track JOIN Genre 
    ON Track.genre_id = Genre.id

SELECT Track.title, Artist.name, Album.title, Genre.name 
FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.id AND Track.album_id = Album.id 
    AND Album.artist_id = Artist.id
 

#Many-Many Relationship
CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE,
    email  TEXT
) ;

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
) ;

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
	role        INTEGER,
    PRIMARY KEY (user_id, course_id)
) ;

INSERT INTO User (name, email) VALUES ('Jane', 'jane@tsugi.org');
INSERT INTO User (name, email) VALUES ('Ed', 'ed@tsugi.org');
INSERT INTO User (name, email) VALUES ('Sue', 'sue@tsugi.org');

INSERT INTO Course (title) VALUES ('Python');
INSERT INTO Course (title) VALUES ('SQL');
INSERT INTO Course (title) VALUES ('PHP');

INSERT INTO Member (user_id, course_id, role) VALUES (1, 1, 1);
INSERT INTO Member (user_id, course_id, role) VALUES (2, 1, 0);
INSERT INTO Member (user_id, course_id, role) VALUES (3, 1, 0);

INSERT INTO Member (user_id, course_id, role) VALUES (1, 2, 0);
INSERT INTO Member (user_id, course_id, role) VALUES (2, 2, 1);

INSERT INTO Member (user_id, course_id, role) VALUES (2, 3, 1);
INSERT INTO Member (user_id, course_id, role) VALUES (3, 3, 0);

SELECT User.name, Member.role, Course.title
  FROM User JOIN Member JOIN Course
  ON Member.user_id = User.id AND Member.course_id = Course.id
  ORDER BY Course.title, Member.role DESC, User.name 

#Exercise: Email(https://www.youtube.com/watch?v=uQ3Qv1z_Vao)
#Exercise: Roster(https://www.youtube.com/watch?v=qEkUEAz8j3o)
#Exercise: Tracks(https://www.youtube.com/watch?v=I-E7avcPeSE)
#Exercise: Twfriends(https://www.youtube.com/watch?v=RZRAoBFIH6A)
#Exercise: Twspider(https://www.youtube.com/watch?v=xBaJddvJL4A)

##How does the PageRank algorithm work?
##It determines which pages are most highly connected.

#Exercise: Geodata(https://www.youtube.com/watch?v=KfhslNzopxo)
#Exercise: Gmane Model(https://www.youtube.com/watch?v=wSpl1-7afAk)
#Exercise: Gmane Spider(https://www.youtube.com/watch?v=H3w4lOFBUOI)
#Exercise: Gmane Viz(https://www.youtube.com/watch?v=LRqVPMEXByw)
#Exercise: Page Rank(https://www.youtube.com/watch?v=yFRAZBkBDBs)
#Exercise: Page Spider(https://www.youtube.com/watch?v=sXedPQ_AnWA)
#Exercise: Page Viz(https://www.youtube.com/watch?v=Fm0hpkxsZoo)
