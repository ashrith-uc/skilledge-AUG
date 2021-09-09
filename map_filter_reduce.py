#range, map, filter, reduce, zip  are generator function
#lambda function
#if any function uses yield instead of return if becomes generator function

#if we need to get next value from a generator we have to use next function for example next(gen)
import sys
l = [1,2,3,4,5]

def map1(fn, m_l):
    new_l = []
    for n in m_l:
       new_l.append(fn(n))
    return new_l

#this is a actual implementation of python map generator
def generator(fn, m_l):
    for n in m_l:
        yield fn(n)



m2 = map1(lambda x:x*x, l)
print(m2)

gen = generator(lambda x:x*x, l)
print(next(gen))
print(next(gen))
#map is used to map each element of a given list to the given function
print(sys.getsizeof([n*n for n in l]))
print(sys.getsizeof(map(lambda num:num*num, l)))

#filter is used to filter values from the list based on the function provided to filter if it returns True element will be included or vice versa
print([n for n in l if n%2==0]) #less memory
print(list(filter(lambda num: num%2==0, l)))

#zip is used to combile multiple list into one where each element will be tuple of zipped item
name_list = ["pranav", "ankush", "rahul"]

marks_list = [50, 60, 70]

roll_number_list = [1,2,3]

print(list(zip(name_list, roll_number_list, marks_list)))

#reduce

l = [1,2,3,4]

sum = 0
for n in l:
    sum = sum+n
print("sum withpout reduce", sum)

import  functools
#reduce is used to reduce a list  based on the operation
print("Sum with reduce", functools.reduce(lambda x,y: x+y, l))



#range is used to get lust from number

print(range(5)) # this will create a list [0,1,2,3,4]
print(range(1,5)) # This will create a list [1,2,3,4]
print(range(1,5,2)) # This will create a list [1,3] since we have given a interval/step of 2 so this will skip one in between

#assignment : Write your own implementation of default filter and zip functions