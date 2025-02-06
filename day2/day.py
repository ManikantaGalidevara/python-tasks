#Data types
#numeric:
#int, float, complex, bool
#list, tuple, string, range

#complex
a=4+2j
b=5+6j
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)

#boolean
a=(5>10)
b=(5>=10)
print(a)
print(b)
a=(5<=10)
print(a)

bool=True
bool1=False
print(type(bool))
print(type(bool1))
print(int(bool))
print(int(bool1))

#list is mutable
#its is enclosed with square brackets 
#list - collection of hetrogenous elements which are indexable and mutable
li=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, 'string', [1, 2, 3, 4, 5, 6]]
print(li[1])
print(li[4])
print(li[12][2])
#slicing
print(li[::])
print(li[1:6:2])
print(li[-1:-14:-1])
print(li[::3])
print(li[::-3])
print(li[-10:-1])

#tuple is faster than list
#tuple is immutable
#it is enclosed with parenthesis
tup=(1, 2, 2, 3, 4, 5, 6, 'string', 0.9)
print(tup)
print(tup[1])
print(tup[6])
#slicing
print(tup[::])
print(tup[::2])
print(tup[7:0:-1])
print(tup[-6:-1])
print(tup[-1:-7:-1])
print(tup[-1:-100:-2])
print(tup[7:0:-2])


#range
print(list(range(0, 100)))
print(list(range(100, 0, -1)))
print(list(range(0, 100, 3)))


##string
print("String")
#String is inmutable

s = "hello"
# s[0] = 'H'  This will raise an error because strings are immutable

