class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        shortest = 201
        for i in range(len(strs)):
            if (len(strs[i])<shortest):
                shortest = len(strs[i])
        i = 0
        search = True
        while(search and i<shortest):
            j = 0
            while (search and j<len(strs)-1):
                if(strs[j][i]!=strs[j+1][i]):
                    search = False
                j+=1
            if (search):
                prefix += strs[0][i]
            i+=1
        return prefix