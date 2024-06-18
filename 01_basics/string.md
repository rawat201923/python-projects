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