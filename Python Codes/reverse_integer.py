def reverse_int(x):
        #If given argument is non-integer, we return 0
        if(x.isnumeric()==0):
            return 0
        #Taking Absolute of given integer in n
        n = abs(x)
        #Initializing reverse with 0
        reverse = 0
        while(n>0):
            #Getting the last digit of n
            r = n%10
            #Adding last digit in reverse
            reverse = (reverse*10) + r
            #Removing last digit of n
            n = n//10
        #If given integer is negative
        if(x<0):
            reverse = -reverse
            return reverse
        #If given integer is non-negative
        return reverse