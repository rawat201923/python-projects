# iterations
- files and list
- inner working or iterations

```
>>> f = open('chai.py')
>>> f.__next__()
'import time\n'
>>> f.__next__()
'\n'
>>> f.__next__()
'print("chai is here")\n'
>>> f.__next__()
'username = "histesh"\n'
>>> f.__next__()
'print(username)'
>>> f.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> for line in open('chai.py'):
...     print(line)
... 
import time



print("chai is here")

username = "histesh"

print(username)
>>> for line in open('chai.py'):
...     print(line,end='')
... 
import time

print("chai is here")
username = "histesh"
print(username)>>> 
>>> f = open('chai.py')
>>> while True:
...     line = f,readline()
...     if not line: break
...     print(line, end='')
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: name 'readline' is not defined
>>> while True:
...     line = f.readline()
...     if not line: break
...     print(line, end='')
... 
import time

print("chai is here")
username = "histesh"
print(username)>>> 
>>> test = "hitesh"
>>> if not test:
...     print("chai")
... 
>>> test = ""
>>> if not test
  File "<stdin>", line 1
    if not test
               ^
SyntaxError: expected ':'
>>> test = ""
>>> if not test:
...     print("chai")
... 
chai
>>> myList = [1,2,3,4]
>>> I = iter(myList)
>>> I
<list_iterator object at 0x7c14f35e4ac0>
>>> I.__next__()
1
>>> I.__next__()
2
>>> I.__next__()
3
>>> I.__next__()
4
>>> I.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> f = open('chai.py')
>>> iter(f) is f
True
>>> iter(f) is f.__iter__()
True
>>> myNewList = [1,2,3]
>>> iter(myNewList) is myNewList
False
```