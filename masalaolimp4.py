from math import*
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
d=b*b-4*a*c
if d==0:
 print('x1=x2=',b/2*a)
if d>0:
 print('x1=',(-b-pow(d,2)/(2*a)))
 print('x2=',(-b+pow(d,2)/(2*a)))
if d<0:
 print('tenglama yechmga ega emas',end='.')