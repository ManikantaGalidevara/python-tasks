#printing single digit number
print(2)

#printing multiple digit number
print(66)
print(999)

#printing multiple  numbers
print(2,4,6,8,10)

#arthmatic operations without variables(+,-,*,/,**,%,//)
print(2+6)
print(2-6)
print(2*6)
print(2/6)
print(2**6)
print(2//6)
print(2%6)

#arthmatic operations with variables(+,-,*,/,**,%,//)
#addition(+)
a=66
b=40
print(a+b)
#subtraction(-)
a=66
b=40
print(a-b)
#multiplication(*)
a=66
b=40
print(a*b)
#division(/)
a=66
b=40
print(a/b)
#exponent(**)
a=66
b=40
print(a**b)
#print only integer value(//)
a=66
b=40
print(a//b)
#prints remainder(%)
a=66
b=40
print(a%b)

#print string('')
st='something special'
print(st)

#printing the length of the string(len())
ts="most welcome to institute"
print(len(ts))

#printing index of a string(:)
ts="most welcome to institute"
print(ts[1])
print(ts[:])#prints complete string
print(ts[:21])
print(ts[4:20])
#print index of string with negitive number(:)
print(ts[-1])
print(ts[-20:-4])
print(ts[-25:-1])
print(ts[-1:-26:-1])

#printing its type(type())
a="maxi"
print(type(a))
b=(22)
print(type(b))
a=2.6
print(type(a))
a=True
print(type(a))
b=False
print(type(b))

#slicing (start:end:step),(end-1)
sl='python high level programming language'
print(len(sl))
print(sl[0:35:2])
print(sl[::3])
print(sl[:37:1])#complete string printing
print(sl[:100:1])#its print up to (n-1)number
print(sl[-1:-37:-1])#it's printing reverse slicing
print(sl[-1:-37:-2])#it's printing reverse slicing by skipping 2 numbers
print(sl[-20:-6:2])
print(sl[-28::3])
