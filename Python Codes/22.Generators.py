# Generators:- it is a memory effiecient and also time efficient
#    these are simple functions which returns in iterable set of item one at a time 
# Generator create refrence only 

# for example
# for i in range(10000000000):
#     # print(i)

# Range is a itself a generator and it is a memory efficient when we need to deal with a large dataset because it works on the fly
# And if all the memory has been kept in a system it makes the system slow thats why generator come into the existens



def generatt():
    yield 10
    yield 20
    yield 30

# g = generatt()

# p = next(g)
# print(p)

# p = next(g)
# print(p)

# p = next(g)
# print(p)



def generat2(num):
    print("Printing Generator value")
    while(num>0):
        yield num
        # return num
        num = num-2

# cd = generat2(20) 

# v = next(cd)
# print(v)   

# v = next(cd)
# print(v)   

# v = next(cd)
# print(v)   


# fibonacci number using generator (0,1,1,2,3,5,8)
def fibonacci(num):
    a,b = 0,1
    while(a<num):
        yield a
        a,b=b, a+b

for i in fibonacci(10):
    print(i)





# Generator vs List comparing as Time complexity and Space complexity
import sys

def func_list(size):
    lis = []
    num = 0 
    while(num<size):
        lis.append(num)
        num = num+1
    return lis


def func_generat(size):
    num=0
    while(num<size):
        yield num
        num=num+1


print(sum(func_list(10)))
print("size of list",sys.getsizeof(func_list(10)))

print(sum(func_generat(10)))
print("Size of generator",sys.getsizeof(func_generat(10)))



# another example
generat1 = (i for i in range(100) if i % 5 == 0)
print(sys.getsizeof(generat1))

list1 = [i for i in range(100) if i% 5 ==0]
print(sys.getsizeof(list1))


# To see time complexity
import timeit

print(timeit.timeit('''
input = range(100)
def div_by_5(num):
    if num%5 == 0:
        return True
    else:
        return False    

xyz = [i for i in input if div_by_5(i)]''', number=500))      #for list
# xyz = (i for i in input if div_by_5(i))''', number=500))    #for generator