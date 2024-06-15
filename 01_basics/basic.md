# installation
- install python
- online python compliers: google colab, jupiter, 
- softwares : anaconda,vscode, many more


# PYTHON INNER WORKING

CODE  ==> BYTE CODE ==> PYTHON V.M(Virtual machine)

## Compile to byte code(low level & platform independent)

- byte code runs faster
 .py -> compiled python(frozen binaries)

- __pycache__  (system folder-> internal useful)

##### src change & python version
 hello_chai.cpython-312(version).pyc
 - works only for imported files
 - not for top level files


## python virtual machine(PVM)

- code loop to iterate byte code
- run time engine
- also known as python interpreter

## byte code is not machine code
- python specific interpretation
- cpython(standard implementation), jython, iron python, stackless, PyPy 


# Article about inner working
### link ::: [https://why-dsa.hashnode.dev/python-internal-working-how-it-works-under-the-hood]

# Mutable and Immutable

```
>>> username = "hitesh"
>>> username
'hitesh'
>>> username = "chaiaurcode"
>>> username
'chaiaurcode'
>>> x = 10
>>> y = x
>>> x
10
>>> y
10
>>> x= 15
>>> y
10
```

# internal working continue

always datatype assign to memory but not to variables