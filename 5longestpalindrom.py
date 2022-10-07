class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(s) -> bool:
            length = len(s) 
            for i in range(length // 2):
                if s[i] != s[length - i - 1]:
                    return False
            return True
        lp = ""
        nlp = 0
        lenS = len(s)
        for i in range(lenS):
            check = ""
            if (len(s)-i <= nlp):
                break;
            for j in range(i,lenS):
                check+=s[j]
                if (len(check)>nlp):
                    if(isPalindrome(check) and len(check)>nlp):
                        lp = check
                        nlp = len(check)
        return lp
                    