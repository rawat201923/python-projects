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
```