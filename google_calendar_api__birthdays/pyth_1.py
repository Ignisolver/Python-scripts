Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from os import chdir
chdir(r'C:\Users\ignsz\OneDrive\Inne')
with open("ludzie.txt", 'r') as plik:
    lines = plik.readlines()

    
Traceback (most recent call last):
  File "<pyshell#4>", line 2, in <module>
    lines = plik.readlines()
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\encodings\cp1252.py", line 23, in decode
    return codecs.charmap_decode(input,self.errors,decoding_table)[0]
UnicodeDecodeError: 'charmap' codec can't decode byte 0x81 in position 453: character maps to <undefined>
with open("ludzie.txt", 'r') as plik:
    lines = plik.readlines(decode='utf-8')

    
Traceback (most recent call last):
  File "<pyshell#6>", line 2, in <module>
    lines = plik.readlines(decode='utf-8')
TypeError: TextIOWrapper.readlines() takes no keyword arguments
with open("ludzie.txt", 'r', decode='utf-8') as plik:
    lines = plik.readlines()

    
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    with open("ludzie.txt", 'r', decode='utf-8') as plik:
TypeError: 'decode' is an invalid keyword argument for open()
with open("ludzie.txt", 'r', encode='utf-8') as plik:
    lines = plik.readlines()

    
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    with open("ludzie.txt", 'r', encode='utf-8') as plik:
TypeError: 'encode' is an invalid keyword argument for open()
with open("ludzie.txt", 'r', encodeing='utf8') as plik:
    lines = plik.readlines()

    
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    with open("ludzie.txt", 'r', encodeing='utf8') as plik:
TypeError: 'encodeing' is an invalid keyword argument for open()
with open("ludzie.txt", 'r', encoding='utf8') as plik:
    lines = plik.readlines()

    
lines2 = []
for line in lines:
    if line[0] == "-"
    
SyntaxError: expected ':'

for line in lines:
    if line[0] == " - ":
        continue
    name_surneme, data  = line.split('-')
    data = data.strip()
    if data == "???":
        continue
    if data = "":
        
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
for line in lines:
    if line[0] == " - ":
        continue
    name_surneme, data  = line.split('-')
    data = data.strip()
    if data == "???":
        continue
    if data == "":
        continue
    if ',' in data:
        birthday, nameday = data.split(",")
    else
    
SyntaxError: expected ':'
for line in lines:
    if line[0] == " - ":
        continue
    name_surneme, data  = line.split('-')
    data = data.strip()
    if data == "???":
        continue
    if data == "":
        continue
    if ',' in data:
        birthsday, namesday = data.split(",")
    else:
        birthday, nameday = data, None
    print(name_sureme, "U:", birthstay, "I:", namesday)

    
Traceback (most recent call last):
  File "<pyshell#38>", line 14, in <module>
    print(name_sureme, "U:", birthstay, "I:", namesday)
NameError: name 'name_sureme' is not defined. Did you mean: 'name_surneme'?
for line in lines:
    if line[0] == " - ":
        continue
    name_surname, data  = line.split('-')
    data = data.strip()
    if data == "???":
        continue
    if data == "":
        continue
    if ',' in data:
        birthsday, namesday = data.split(",")
    else:
        birthday, nameday = data, None
    print(name_surame, "U:", birthstay, "I:", namesday)

    
Traceback (most recent call last):
  File "<pyshell#40>", line 14, in <module>
    print(name_surame, "U:", birthstay, "I:", namesday)
NameError: name 'name_surame' is not defined. Did you mean: 'name_surname'?
for line in lines:
    if line[0] == " - ":
        continue
    name_surname, data  = line.split('-')
    data = data.strip()
    if data == "???":
        continue
    if data == "":
        continue
    if ',' in data:
        birthsday, namesday = data.split(",")
    else:
        birthday, nameday = data, None
    print(name_surname, "U:", birthstay, "I:", namesday)

    
Traceback (most recent call last):
  File "<pyshell#42>", line 14, in <module>
    print(name_surname, "U:", birthstay, "I:", namesday)
NameError: name 'birthstay' is not defined. Did you mean: 'birthsday'?
for line in lines:
    if line[0] == " - ":
        continue
    name_surname, data  = line.split('-')
    data = data.strip()
    if data == "???":
        continue
    if data == "":
        continue
    if ',' in data:
        birthsday, namesday = data.split(",")
    else:
        birthsday, namesday = data, None
    print(name_surname, "U:", birthstay, "I:", namesday)

    
Traceback (most recent call last):
  File "<pyshell#44>", line 14, in <module>
    print(name_surname, "U:", birthstay, "I:", namesday)
NameError: name 'birthstay' is not defined. Did you mean: 'birthsday'?
for line in lines:
    if line[0] == " - ":
        continue
    name_surname, data  = line.split('-')
    data = data.strip()
    if data == "???":
        continue
    if data == "":
        continue
    if ',' in data:
        birthsday, namesday = data.split(",")
    else:
        birthsday, namesday = data, None
    print(name_surname, "U:", birthsday, "I:", namesday)

    
Dominika Kapanowska  U: 29 czerwca I:  8 sierpnia
Tomek Michalski  U: 18 sierpnia I: None
Maciej Pachucy  U: 30 lipca I: None
Traceback (most recent call last):
  File "<pyshell#46>", line 4, in <module>
    name_surname, data  = line.split('-')
ValueError: not enough values to unpack (expected 2, got 1)
with open("ludzie.txt", 'r', encoding='utf8') as plik:
    lines = plik.readlines()

    
for line in lines:
    if line[0] == " - ":
        continue
    name_surname, data  = line.split('-')
    data = data.strip()
    if data == "???":
        continue
    if data == "":
        continue
    if ',' in data:
        birthsday, namesday = data.split(",")
    else:
        birthsday, namesday = data, None
    print(name_surname, "U:", birthsday, "I:", namesday)

    
Dominika Kapanowska  U: 29 czerwca I:  8 sierpnia
Tomek Michalski  U: 18 sierpnia I: None
Maciej Pachucy  U: 30 lipca I: None
Traceback (most recent call last):
  File "<pyshell#50>", line 4, in <module>
    name_surname, data  = line.split('-')
ValueError: not enough values to unpack (expected 2, got 1)
with open("ludzie.txt", 'r', encoding='utf8') as plik:
    lines = plik.readlines()

    
for line in lines:
    if line[0] == " - ":
        continue
    name_surname, data  = line.split('-')
    data = data.strip()
    if data == "???":
        continue
    if data == "":
        continue
    if ',' in data:
        birthsday, namesday = data.split(",")
    else:
        birthsday, namesday = data, None
    print(name_surname, "U:", birthsday, "I:", namesday)

    

Traceback (most recent call last):
  File "<pyshell#54>", line 4, in <module>
    name_surname, data  = line.split('-')
ValueError: too many values to unpack (expected 2)
for line in lines:
    if line[0] == "-":
        continue
    name_surname, data  = line.split(' - ')
    data = data.strip()
    if data == "???":
        continue
    if data == "":
        continue
    if ',' in data:
        birthsday, namesday = data.split(",")
    else:
        birthsday, namesday = data, None
    print(name_surname, "U:", birthsday, "I:", namesday)

    


with open("ludzie.txt", 'r', encoding='utf8') as plik:
    lines = plik.readlines()

    
for line in lines:
    if line[0] == "-":
        continue
    name_surname, data  = line.split(' - ')
    data = data.strip()
    if data == "???":
        continue
    if data == "":
        continue
    if ',' in data:
        birthsday, namesday = data.split(",")
    else:
        birthsday, namesday = data, None
    print(name_surname, "U:", birthsday, "I:", namesday)

    

Traceback (most recent call last):
  File "<pyshell#60>", line 4, in <module>
    name_surname, data  = line.split(' - ')
ValueError: not enough values to unpack (expected 2, got 1)
for line in lines:
    if line[0] == "-" or line == '\n':
        continue
    name_surname, data  = line.split(' - ')
    data = data.strip()
    if data == "???":
        continue
    if data == "":
        continue
    if ',' in data:
        birthsday, namesday = data.split(",")
    else:
        birthsday, namesday = data, None
    print(name_surname, "U:", birthsday, "I:", namesday)

    

nametuple()
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    nametuple()
NameError: name 'nametuple' is not defined
from collections import namedtuple
Person = namedtuple("Person", "Name", "birtshday", "namesday")
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    Person = namedtuple("Person", "Name", "birtshday", "namesday")
TypeError: namedtuple() takes 2 positional arguments but 4 were given
Person = namedtuple("Person", ["Name", "birtshday", "namesday"])
persons = []
for line in lines:
    if line[0] == "-" or line == '\n':
        continue
    name_surname, data  = line.split(' - ')
    data = data.strip()
    if data == "???":
        continue
    if data == "":
        continue
    if ',' in data:
        birthsday, namesday = data.split(",")
    else:
        birthsday, namesday = data, None
    Person(name_surname, birthsday, namesday)

    

persons
[]
for line in lines:
    if line[0] == "-" or line == '\n':
        continue
    name_surname, data  = line.split(' - ')
    data = data.strip()
    if data == "???":
        continue
    if data == "":
        continue
    if ',' in data:
        birthsday, namesday = data.split(",")
    else:
        birthsday, namesday = data, None
    persons.append(Person(name_surname, birthsday, namesday))

    

persons

for person in persons:
    name, bd, nd = person

    
persons_processed = []
months = "sty, lut, maj, cze, lip, sie, wrz, paź, lis, gru"
months_nrs = range(1,13)
months_converter = dict(zip(months.split(', '), months_nrs))
_

months_converter['sty']
1
def convert_date(date):
    date = date.strip()
    day, month = date.split(" ")
    month = months_converter[month[0:3]]
    return int(day), month

for person in persons:
    name, bd, nd = person
    bd = convert_date(bd)
    nd = convert_date(nd)
    persons_processed.append(Person(name, bd, nd))

    
Traceback (most recent call last):
  File "<pyshell#97>", line 4, in <module>
    nd = convert_date(nd)
  File "<pyshell#92>", line 2, in convert_date
    date = date.strip()
AttributeError: 'NoneType' object has no attribute 'strip'


Date = namedtuple("Date", ["Day", "Month"])
def convert_date(date):
    if date is None:
        return None
    date = date.strip()
    day, month = date.split(" ")
    month = months_converter[month[0:3]]
    return Date(int(day), month)

for person in persons:
    name, bd, nd = person
    bd = convert_date(bd)
    nd = convert_date(nd)
    persons_processed.append(Person(name, bd, nd))

    
Traceback (most recent call last):
  File "<pyshell#104>", line 3, in <module>
    bd = convert_date(bd)
  File "<pyshell#102>", line 6, in convert_date
    month = months_converter[month[0:3]]
KeyError: 'kwi'
months = "sty, lut, mar, kwi, maj, cze, lip, sie, wrz, paź, lis, gru"

months_converter = dict(zip(months.split(', '), months_nrs))
def convert_date(date):
    if date is None:
        return None
    date = date.strip()
    day, month = date.split(" ")
    month = months_converter[month[0:3]]
    return Date(int(day), month)

for person in persons:
    name, bd, nd = person
    bd = convert_date(bd)
    nd = convert_date(nd)
    persons_processed.append(Person(name, bd, nd))

    
Traceback (most recent call last):
  File "<pyshell#111>", line 4, in <module>
    nd = convert_date(nd)
  File "<pyshell#109>", line 5, in convert_date
    day, month = date.split(" ")
ValueError: not enough values to unpack (expected 2, got 1)
def convert_date(date):
    if date is None:
        return None
    date = date.strip()
    try:
        day, month = date.split(" ")
    except:
        print(date)
    month = months_converter[month[0:3]]
    return Date(int(day), month)

for person in persons:
    name, bd, nd = person
    bd = convert_date(bd)
    nd = convert_date(nd)
    persons_processed.append(Person(name, bd, nd))

    
???
Traceback (most recent call last):
  File "<pyshell#115>", line 4, in <module>
    nd = convert_date(nd)
  File "<pyshell#113>", line 9, in convert_date
    month = months_converter[month[0:3]]
UnboundLocalError: local variable 'month' referenced before assignment
persons = []
for line in lines:
    if line[0] == "-" or line == '\n':
        continue
    name_surname, data  = line.split(' - ')
    data = data.strip()
    if data == "???":
        continue
    if data == "":
        continue
    if ',' in data:
        birthsday, namesday = data.split(",")
    else:
        birthsday, namesday = data if data.strip() is not "???" else None, None
    persons.append(Person(name_surname, birthsday, namesday))
    
SyntaxError: "is not" with a literal. Did you mean "!="?
for line in lines:
    if line[0] == "-" or line == '\n':
        continue
    name_surname, data  = line.split(' - ')
    data = data.strip()
    if data == "???":
        continue
    if data == "":
        continue
    if ',' in data:
        birthsday, namesday = data.split(",")
    else:
        birthsday, namesday = data if data.strip() != "???" else None, None
    persons.append(Person(name_surname, birthsday, namesday))

    
persons = []
for line in lines:
    if line[0] == "-" or line == '\n':
        continue
    name_surname, data  = line.split(' - ')
    data = data.strip()
    if data == "???":
        continue
    if data == "":
        continue
    if ',' in data:
        birthsday, namesday = data.split(",")
    else:
        birthsday, namesday = data if data.strip() != "???" else None, None
    persons.append(Person(name_surname, birthsday, namesday))

    
persons_processed = []
for person in persons:
    name, bd, nd = person
    bd = convert_date(bd)
    nd = convert_date(nd)
    persons_processed.append(Person(name, bd, nd))

    
???
Traceback (most recent call last):
  File "<pyshell#125>", line 4, in <module>
    nd = convert_date(nd)
  File "<pyshell#113>", line 9, in convert_date
    month = months_converter[month[0:3]]
UnboundLocalError: local variable 'month' referenced before assignment
persons

def convert_date(date):
    if date is None or date.strip() == "???":
        return None
    date = date.strip()
    try:
        day, month = date.split(" ")
    except:
        print(date)
    month = months_converter[month[0:3]]
    return Date(int(day), month)

for person in persons:
    name, bd, nd = person
    bd = convert_date(bd)
    nd = convert_date(nd)
    persons_processed.append(Person(name, bd, nd))

    

Traceback (most recent call last):
  File "<pyshell#130>", line 4, in <module>
    nd = convert_date(nd)
  File "<pyshell#128>", line 9, in convert_date
    month = months_converter[month[0:3]]
UnboundLocalError: local variable 'month' referenced before assignment
def convert_date(date):
    if date is None or date.strip() == "???" or date = "":
        return None
    date = date.strip()
    day, month = date.split(" ")
    month = months_converter[month[0:3]]
    return Date(int(day), month)
SyntaxError: invalid syntax
def convert_date(date):
    if date is None or date.strip() == "???" or date == "":
        return None
    date = date.strip()
    day, month = date.split(" ")
    month = months_converter[month[0:3]]
    return Date(int(day), month)

for person in persons:
    name, bd, nd = person
    bd = convert_date(bd)
    nd = convert_date(nd)
    persons_processed.append(Person(name, bd, nd))

    
persons_processed = []
for person in persons:
    name, bd, nd = person
    bd = convert_date(bd)
    nd = convert_date(nd)
    persons_processed.append(Person(name, bd, nd))

   
for i in persons_processed:
    print(i)

    

from os import chdir
chdir("C:\Users\ignsz\Desktop\calendar_API")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
chdir(r"C:\Users\ignsz\Desktop\calendar_API")
file = open("persons.bin",'wb')
from pickle import dump
dump(persons_processed, file)
file.close()
file = open("persons.bin",'wb')
dump(persons_processed, file)
file.close()
