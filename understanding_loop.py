#Youmay want to run different loops seperately(as running this whole script will print everything in a order)



#As the name suggests loop is nothing but doing a certain task repeatedly, let's understand this through an example, if somone asks you to print 
#print your name 5 times then the immediate idea that comes to your mind is to use print statement 5 times. But think what will happen if number is 1000,
#then using print statement isn't feasible, atleast doing that is too repetitive and obviously boring, here comes loop to the rescue
#Enough theory, let us take a look at implementation


for i in range(0,5): #It means that start i from 0 and end the loop when i=4 so it will run 5 times(always remember range function excludes the last number in range
    print('Joe')     #And now if you have to print it 1000 times change 5 to 1000, easy isn't it?

#Some more examples
n=10
for i in range(0,n):   #print numbers 0,1.....n-1
    print(i)
for i in range(1,10):   #prints the table of n(change n to get the tables of different number)
    print(i*n)



#Now, Let's take a look on some cool things which we can do using loops
for i in range(0,5):   #prints a pattern
    print('*'*i)       #notice that string multiplication(with integers ofcourse) is supported in python i.e '*'*2= **
                       #don't get confused,'*' represent a character whereas * represent multiplication
    
