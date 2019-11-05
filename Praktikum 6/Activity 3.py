>>> nama="Dimas Riswanda Pradana Putra"
>>> nim="L200194011"
>>> x="1"+nim[7:]
>>> a=int(x)
>>> b=len(nama)
>>> type(a)
<class 'int'>
>>> #function "a" is a integer, bacause it was converted to integer
>>> type(b)
<class 'int'>
>>> #function "b" is a integer, because len function count the character and the output is integer numbers
>>> a/b
36.107142857142854
>>> #a function devided to b function
>>> a//b
36
>>> #a function devided to b function and then rounded off
>>> 10*(a-999)
120
>>> #a function minus 999 and times of 10
>>> b**2
784
>>> #b power 2
>>> a%b
3
>>> #a modulo b
>>> 
>>> c=12.5
>>> type(c)
<class 'float'>
>>> #c function is a float, because it is a decimal number
>>> a/c
80.88
>>> #a devided by c
>>> a//c
80.0
>>> #a devided by c then rounded off, but still in float type
>>> a%c
11.0
>>> #a modulo c in float type
>>> c>b
False
>>> #it false because b is bigger than c
>>> type(c>b)
<class 'bool'>
>>> #it is a boolean, because it only have 2 probability, true or false
>>> a>b and b>c
True
>>> #it is true because a is bigger than b and b is bigger than c
>>> a>1100 or b<10
False
>>> #it is false, because a is smaller than 1100 or b is bigger than 10