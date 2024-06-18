# Object Types / Data Types

- Number : 1234, 3.1415, 3+4j, 0b111, Decimal(), Fraction()
- String : 'spam', "Bob's", b'a\x01c', u'sp\xc4m'
- List : [1, [2, 'three'], 4.5], list(range(10))
- Tuple : (1, 'spam', 4, 'U'), tuple('spam'), namedtuple
- Dictionary : {'food': 'spam', 'taste': 'yum'}, dict(hours=10)

- Set : set('abc'), {'a', 'b', 'c'}

- File : open('eggs.txt'), open(r'C:\ham.bin', 'wb')

- Boolean : True, False
- None : None
- Funtions, modules, classes

- Advance: Decorators, Generators, Iterators, MetaProgramming

# examples

```

>>> mylist = [1,3,4,6,74,3,31,]
>>> mylist
[1, 3, 4, 6, 74, 3, 31]
>>> my= [1, [2, 'three'], 4.5]
>>> my
[1, [2, 'three'], 4.5]
>>> 12+12
24
>>> 2.5 *5
12.5
>>> 2**1000
10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
>>> 2**100
1267650600228229401496703205376
```
```
>>> import math
>>> math.pi
3.141592653589793
>>> import random
>>> random.choice([3,5,6,7,8,4])
4
>>> random.choice([3,5,6,7,8,4])
8
>>> random.choice([3,5,6,7,8,4])
5
>>> random.choice([3,5,6,7,8,4])
5
>>> random.choice([3,5,6,7,8,4])
6
>>> username="chaiaurcode"
>>> len(username)
11
>>> username[0]
'c'
>>> username[-1]
'e'
>>> username[-5]
'r'
>>> username[1:3]
'ha'
>>> dir(username)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
```

# sting operations

```
>>> chai = "Lemon Chai"
>>> chai
'Lemon Chai'
>>> print(chai)
Lemon Chai
>>> chai = "MASALA CHAI"
>>> first_char = chai[0]
>>> print(first_char)
M
>>> chai
'MASALA CHAI'
>>> print(chai)
MASALA CHAI
>>> chai[0:5]
'MASAL'
>>> slice_chai = chai[0:6]
>>> print(slice_chai)
MASALA
>>> chai[-1]
'I'
>>> num_list= "0123456789"
>>> num_list[:]
'0123456789'
>>> num_list[3:]
'3456789'
>>> num_list[:7]
'0123456'
>>> num_list[:7:2]
'0246'
>>> num_list[:7:3]
'036'
>>> num_list[:7:1]
'0123456'
```

## methods

```
>>> print(chai.lower())
masala chai
>>> print(chai.upper())
MASALA CHAI
>>> chai
'MASALA CHAI'
>>> chai = "  Masala Chai  "
>>> chai
'  Masala Chai  '
>>> print(chai.strip())
Masala Chai
>>> chai = "Lemon Chai"
>>> print(chai.replace("Lemon","Ginger")
... )
Ginger Chai
>>> print(chai.replace("Lemon","Ginger"))
Ginger Chai
>>> chai = "Lemon, Ginger, Masala, Mint"
>>> print(chai.split())  
['Lemon,', 'Ginger,', 'Masala,', 'Mint']
>>> print(chai.split(", "))  
['Lemon', 'Ginger', 'Masala', 'Mint']
>>> chai
'Lemon, Ginger, Masala, Mint'
>>> chai = "Masala Chai"
>>> print(chai.find("Chai"))
7
>>> print(chai.find("chai"))
-1
>>> chai = "Masala Chai Chai Chai"
>>> print(chai.count("chai"))
0
>>> print(chai.count("Chai"))
3
>>> chai_type = "Masala"
>>> quantity = 2
>>> order= "I ordered {} cups of {} chai"
>>> order
'I ordered {} cups of {} chai'
>>> print(order.format(quantity,chai_type))
I ordered 2 cups of Masala chai
>>> chai = "Lemon Chai"
>>> chai
'Lemon Chai'
>>> print(chai)
Lemon Chai
>>> chai = "MASALA CHAI"
>>> first_char = chai[0]
>>> print(first_char)
M
>>> chai
'MASALA CHAI'

>>> print(chai)
MASALA CHAI
>>> chai[0:5]
>>> chai
'MASALA CHAI'
>>> print(chai.lower())
masala chai
>>> print(chai.upper())
MASALA CHAI
>>> chai
'MASALA CHAI'
>>> chai = "  Masala Chai  "
>>> chai
'  Masala Chai  '
>>> print(chai.strip())
Masala Chai
>>> chai = "Lemon Chai"
>>> print(chai.replace("Lemon","Ginger")
... )
Ginger Chai
>>> chai_variety
['Lemon', 'Masala', 'Ginger']
>>> print("".join(chai_variety))
LemonMasalaGinger
>>> print(" ".join(chai_variety))
Lemon Masala Ginger
>>> print("-".join(chai_variety))
Lemon-Masala-Ginger
>>> print(", ".join(chai_variety))
Lemon, Masala, Ginger
>>> chai
'Masala Chai Chai Chai'
>>> print(len(chai))
21
>>> chai = "Masala Chai"
>>> chai
'Masala Chai'

```

```
>> chai
'Masala Chai'
>>> for letter in chai:
...     print(letter)
... 
M
a
s
a
l
a
 
C
h
a
i
>>> chai= "He said, \"Masala chai is awesome\" "
>>> chai
'He said, "Masala chai is awesome" '
>>> chai = "Masala\nChai"
>>> chai
'Masala\nChai'
>>> print(chai)
Masala
Chai
>>> chai = r"Masala\nchai"
>>> chai
'Masala\\nchai'
>>> print(chai)
Masala\nchai
```
# List manipulation

```
>>> tea_varities = ["Black", "Green", "Oolong", "White"]
>>> tea_varities
['Black', 'Green', 'Oolong', 'White']
>>> print(tea_varities)
['Black', 'Green', 'Oolong', 'White']
>>> print(tea_varities[0])
Black
>>> print(tea_varities[-1])
White
>>> print(tea_varities[1:3])
['Green', 'Oolong']
>>> print(tea_varities[:2])
['Black', 'Green']
>>> print(tea_varities[2:])
['Oolong', 'White']
>>> print(tea_varities[2:2])
[]
>>> print(tea_varities[:2:2])
['Black']
>>> tea_varities[3] = "Herbal"
>>> print(tea_varities)
['Black', 'Green', 'Oolong', 'Herbal']
```
```
>>> tea_varities= ["black","green","Oolong","Herbal"]
>>> print(tea_varities)
['black', 'green', 'Oolong', 'Herbal']
>>> tea_varities[1:2]
['green']
>>> tea_varities[1:2]="lemon"
>>> print(tea_varities)
['black', 'l', 'e', 'm', 'o', 'n', 'Oolong', 'Herbal']
>>> print(tea_varities)
['black', 'l', 'e', 'm', 'o', 'n', 'Oolong', 'Herbal']
>>> tea_varities= ["black","green","Oolong","white"]
>>> print(tea_varities)
['black', 'green', 'Oolong', 'white']
>>> tea_varities[1:2]
['green']
>>> tea_varities[1:2]=["lemon"]
>>> print(tea_varities)
['black', 'lemon', 'Oolong', 'white']
>>> tea_varities[1:3]
['lemon', 'Oolong']
>>> tea_varities[1:3]=["green","Masala"]
>>> print(tea_varities)
['black', 'green', 'Masala', 'white']
print(tea_varities)
['black', 'green', 'Masala', 'white']
>>> tea_varities[1:1]
[]
>>> tea_varities[1:1]=["test","test"]
>>> print(tea_varities)
['black', 'test', 'test', 'green', 'Masala', 'white']
>>> tea_varities[1:2]
['test']
>>> tea_varities[1:3]
['test', 'test']
>>> tea_varities[1:3]=[]
>>> print(tea_varities)
['black', 'green', 'Masala', 'white']
```

```
>>> print(tea_varities)
['black', 'green', 'Masala', 'white']
>>> for tea in tea_varities:
...     print(tea)
... 
black
green
Masala
white
>>> for tea in tea_varities:
...     print(tea,end=" ")
... 
black green Masala white >>> 
>>> for tea in tea_varities:
...     print(tea,end="-")
... 
black-green-Masala-white->>> 
>>> tea_varities
['black', 'green', 'Masala', 'white']
>>> if "Oolong" in tea_varities:
...     print("I have Oolong tea")
... 
>>> tea_varities.append("Oolong")
>>> tea_varities
['black', 'green', 'Masala', 'white', 'Oolong']
>>> if "Oolong" in tea_varities:
...     print("I have Oolong tea")
... 
I have Oolong tea
>>> tea_varities
['black', 'green', 'Masala', 'white', 'Oolong']
>>> tea_varities.pop()
'Oolong'
>>> tea_varities
['black', 'green', 'Masala', 'white']
>>> tea_varities.remove("green")
>>> tea_varities
['black', 'Masala', 'white']
>>> tea_varities
['black', 'Masala', 'white']
>>> tea_varities.insert(1,"green")
>>> tea_varities
['black', 'green', 'Masala', 'white']
```

```
>>> tea_varities_copy = tea_varities.copy()
>>> tea_varities_copy
['black', 'green', 'Masala', 'white']
>>> tea_varities_copy.append("Lemon")
>>> tea_varities
['black', 'green', 'Masala', 'white']
>>> tea_varities_copy
['black', 'green', 'Masala', 'white', 'Lemon']
```

## list comprihension
```
>>> squared_num = [x**2 for x in range(10)]
>>> squared_num
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> cube_num = [y**3 for y in range(5)]
>>> cube_num
[0, 1, 8, 27, 64]
```


# Dictionary

```
>>> chai_types = {"Masala":"spicy",}
>>> chai_types = {"Masala":"spicy","ginger":"zesty","green":"mild"}
>>> chai_types
{'Masala': 'spicy', 'ginger': 'zesty', 'green': 'mild'}
>>> chai_types["Masala"]
'spicy'
>>> chai_types.get("ginger")
'zesty'
>>> chai_types.get("gingery")
>>> chai_types.get("Masala")
'spicy'
>>> chai_types.get("Masalaa")
>>> chai_types
{'Masala': 'spicy', 'ginger': 'zesty', 'green': 'mild'}
>>> chai_types["green"]="fresh"
>>> chai_types
{'Masala': 'spicy', 'ginger': 'zesty', 'green': 'fresh'}
>>> for chai in chai_types:
...     print(chai)
... 
Masala
ginger
green
>>> for chai in chai_types:
...     print(chai,chai_types[chai])
... 
Masala spicy
ginger zesty
green fresh
>>> for key, values in chai_types.items():
...     print(key,values)
... 
Masala spicy
ginger zesty
green fresh
>>> for key, value in chai_types.items():
...     print(key,value)
... 
Masala spicy
ginger zesty
green fresh
>>> if "Masala" in chai_types:
...     print("I have masala chai")
... 
I have masala chai
>>> print(len(chai_types))
3
>>> chai_types
{'Masala': 'spicy', 'ginger': 'zesty', 'green': 'fresh'}
>>> chai_types["Earl grey"]="citrus"
>>> chai_types
{'Masala': 'spicy', 'ginger': 'zesty', 'green': 'fresh', 'Earl grey': 'citrus'}
>>> chai_types.pop("ginger")
'zesty'
>>> chai_types
{'Masala': 'spicy', 'green': 'fresh', 'Earl grey': 'citrus'}
>>> chai_types.popitem()
('Earl grey', 'citrus')
>>> chai_types
{'Masala': 'spicy', 'green': 'fresh'}
>>> del chai_types["green"]
>>> chai_types
{'Masala': 'spicy'}
>>> chai_types_copy= chai_types.copy()
>>> chai_types_copy
{'Masala': 'spicy'}
>>> chai_types
{'Masala': 'spicy'}
>>> tea_shop={
... "chai":{"Masala":"spicy","ginger":"zesty"},
... "tea":{"green":"fresh","black":"strong"}
... }
>>> tea_shop
{'chai': {'Masala': 'spicy', 'ginger': 'zesty'}, 'tea': {'green': 'fresh', 'black': 'strong'}}
>>> print(tea_shop)
{'chai': {'Masala': 'spicy', 'ginger': 'zesty'}, 'tea': {'green': 'fresh', 'black': 'strong'}}
>>> tea_shop["chai"]
{'Masala': 'spicy', 'ginger': 'zesty'}
>>> tea_shop["chai"]["ginger"]
'zesty'
>>> squared_num = {x:x**2 for x in range(6)}
>>> squared_num
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
>>> squared_num.clear()
>>> squared_num
{}

 keys=["masala","ginger","lemon"]
>>> keys
['masala', 'ginger', 'lemon']
>>> default_value = "Delicious"
>>> new_dict = dict.fromkeys(keys, default_value)
>>> new_dict
{'masala': 'Delicious', 'ginger': 'Delicious', 'lemon': 'Delicious'}
>>> new_dict = dict.fromkeys(keys, keys)
>>> new_dict
{'masala': ['masala', 'ginger', 'lemon'], 'ginger': ['masala', 'ginger', 'lemon'], 'lemon': ['masala', 'ginger', 'lemon']}
>>> new_dict = dict.
dict.clear(       dict.get(         dict.mro()        dict.setdefault(
dict.copy(        dict.items(       dict.pop(         dict.update(
dict.fromkeys(    dict.keys(        dict.popitem(     dict.values(
>>> new_dict = list.
list.append(   list.count(    list.insert(   list.remove(   
list.clear(    list.extend(   list.mro()     list.reverse(  
list.copy(     list.index(    list.pop(      list.sort(  


```