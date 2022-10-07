class Solution:
    def myAtoi(self, s: str) -> int:
        lenS = len(s)
        strint = ""
        sign = ""
        i = 0
        searching = True
        isNum = False
        while (i<lenS and searching):
            if (ord(s[i])<=47 or ord(s[i])>=58):
                if (isNum):
                    searching = False
                else :
                    if(ord(s[i])==43 or ord(s[i])==45):
                        sign = s[i]
                        isNum= True
                        i+=1
                    elif(ord(s[i])==32):
                        i+=1
                    else:
                        searching = False
            else:
                strint +=s[i]
                isNum = True
                i+=1
        if strint == "":
            strint = 0
        if sign=='-':
            strint = (-1)*int(strint)
            if (strint<(-2147483648)):
                strint = -2147483648
        else :
            strint = int(strint)
            if (strint>2147483647):
                strint = 2147483647
        return strint