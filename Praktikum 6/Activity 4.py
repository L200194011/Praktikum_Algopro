>>> nama="Dimas Riswanda Pradana Putra"
>>> nim = 11
>>> tinggi=1.63
>>> berat=69
>>> tahunlahir=2000
>>> aku=(tahunlahir,berat,tinggi,nim,nama)
>>> data=[tahunlahir,berat,tinggi,nim,nama]
>>> 
>>> type(aku)
<class 'tuple'>
>>> #it is tuple because it use parenthese
>>> aku[0]
2000
>>> #it show tahunlahir because it summoning the character number 0 from the tuple
>>> a=nim%4;aku[a]
11
>>> #nim modulo by 4, then it summon the character by the result
>>> type(aku[a])
<class 'int'>
>>> #nim still in integer format
>>> aku[a:4]
(11,)
>>> #it call the character from a until 4 character to the right
>>> type(aku[4])
<class 'str'>
>>> #it is string because it include a character in string type
>>> aku[0]="ok"
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> #tuple cannot be manipulated
>>> type(data)
<class 'list'>
>>> #it is list because it use bracket
>>> type(data[4])
<class 'str'>
>>> #type data of list number 4 is a string
>>> data[4][5]
' '
>>> #character 4 in data is called, then calling the character 5
>>> data[4][a:6]
'as '
>>> #character 4 in data is called, then calling the character a until 6 to the right
>>> data[0]='ok';data
['ok', 69, 1.63, 11, 'Dimas Riswanda Pradana Putra']
>>> #it add 'ok' to the list, then calling the data
>>> data[-a]
1.63
>>> #it call the third list from the left
>>> range(a)
range(0, 3)
>>> #it call the range of a itself