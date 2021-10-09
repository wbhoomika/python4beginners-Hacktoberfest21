def romanToInt(s):
        dc = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans = 0
        for i in range(len(s)):
            if(i>0 and dc[s[i]]>dc[s[i-1]]):
                ans += dc[s[i]] - 2*dc[s[i-1]]
            else:
                ans += dc[s[i]]
        return ans