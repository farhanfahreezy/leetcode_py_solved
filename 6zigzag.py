class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows == 1 or len(s)==1):
            return s
        else:
            lenS = len(s)
            if (lenS<numRows):
                col = numRows
            else:
                col = (lenS//numRows)*(lenS-1)
            mathrick = [["" for i in range(col)] for j in range (numRows)]
            i = 0
            m = 0
            n = 0
            diagonal = False
            while (i != lenS):
                mathrick[n][m] = s[i]
                i+=1
                if (diagonal):
                    m+=1
                    n-=1
                    if (n==0):
                        diagonal = False
                elif (n==numRows-1):
                    m+=1
                    n-=1
                    diagonal = True
                    if (n==0):
                        diagonal = False
                else :
                    n+=1

            result = ""
            for i in range(numRows):
                for j in range(col):
                    if(mathrick[i][j]!=""):
                        result+=mathrick[i][j]
        return result
        