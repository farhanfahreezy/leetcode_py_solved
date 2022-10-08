class Solution:
    def numSplits(self, s: str) -> int:
        def distinct(s1: str) -> int:
            arr = []
            for i in range(len(s1)):
                if s1[i] not in arr:
                    arr.append(s1[i])
            return len(arr)
        
        numSplit = 0
        for i in range(len(s)-1):
            arr1 = s[0:i+1]
            if (distinct(arr1)>(len(s)-i-1)):
                break
            else:
                arr2 = s[i+1:len(s)]
                if (distinct(arr1)==distinct(arr2)):
                    numSplit+=1
        return numSplit
        