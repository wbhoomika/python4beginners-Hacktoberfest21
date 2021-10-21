def longestCommonPrefix(strs):
        n = ""
        #Empty list
        if(len(strs)==0):
            return n
        minl = len(strs[0])
        
        for i in range(1,len(strs)):
            #length of smallest string
            minl = min(minl, len(strs[i]))
            
        for i in range(minl):
            curr = strs[0][i]
            
            for j in range(0, len(strs)):
                if(strs[j][i]!=curr):
                    return n
            n += curr
        return n
