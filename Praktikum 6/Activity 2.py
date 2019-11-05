## Account Program
## By Dimas R L200194011
import random
angka=random.randint(0,1000)

name="Dimas Riswanda Pradana Putra"
birth="27 October 2000"
nickname=((name[0])+". "+(name[6])+". "+(name[-5:]))
username=((name[0])+(birth[:2])+(birth[-4:]))
password=((name[:3])+str(angka))
print(name)
print(birth)
print(nickname)
print(username)
print(password)