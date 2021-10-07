"""
Infix to Postfix method 2 !
Code contributed by: Hriday Agrawal
Github Name: HridayAg0102


#======SAMPLE INPUT:=========#

abc+-d(a^b*/c)

#======SAMPLE OUTPUT:=========#

Postfix for word abc+-d(a^b*/c) is: "abc+dab^*c/-"

"""



def infix_to_postfix(word):
    word = "(" + word + ")" 
    postfix = ""
    stack = []
    order= {"^":3,"/":2,"*":2,"+":1,"-":1} #preference order
    
    
    for i in range(len(word)):
        
        if word[i] == "(":
            stack.append("(")


    
        elif word[i] in order:

            if word[i-1] == "(" or word[i-1] not in order:
                if len(stack)>=1:
                    while stack[len(stack) - 1] in order and order[stack[len(stack) - 1]] >= order[word[i]]:
                        postfix += str(stack[len(stack)-1])  
                        stack.pop()
                stack.append(word[i])
                
    
            elif order[word[i-1]] < order[word[i]]:
                stack.append(word[i]) 

                #checks if the current char. has higher pref.
                #hence gets appended to the stack & not to word.


                
    
            elif order[stack[len(stack) - 1]] >= order[word[i]]:

                    #if current char has lower pref than previous
                    #add the last element of stack to the word, pop it, 
                    #append the current element to stack 

                postfix += stack[len(stack) - 1]
                stack.pop()
                stack.append(word[i])


                
    
        else:

            # Applying if condition to check ")" and then running a loop inside "()".

            if word[i] == ")":
                z = len(stack)-1
                while True:
                    if stack[z] == "(":
                        stack.pop(z)
                        
                        break
                    else:
                        postfix += stack[z]
                        stack.pop(z)
                    z-=1

                i = z-1 #reassigns value of i 


            else:        
                postfix += str(word[i])

    return postfix





if __name__ == "__main__":
    word = input()
    print(f"Postfix for word {word} is: \"{infix_to_postfix(word)}\"")


