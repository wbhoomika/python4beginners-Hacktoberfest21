#We are given two numbers and we have to find all the self dividing numbers in this range
def selfDividingNumbers(left, right):
        #lst stores all the self dividing numbers
        lst = []
        for i in range(left,right+1):
            val = i
            while val>0:
                #Taking the last digit of the number
                r = val%10
                #If number contains 0 or a it's digit doesn't divide it, we break
                if r==0 or i%r!=0:
                    break
                #Removing last digit of the number
                val = val//10
            #val=0 means we have checked all digits of the number and they all divide it completely
            if val==0:
                #We add the self dividing number to lst
                lst.append(i)
        #We return the list of self dividng numbers
        return lst