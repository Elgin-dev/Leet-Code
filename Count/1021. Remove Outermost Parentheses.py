class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans=""
        depth=0
        for i in range(len(s)):
            if s[i]=='(':

                if depth>0:
                    ans+='('
                depth+=1
                    
            else:
                depth-=1
                if depth>0:
                    ans+=')'
        return ans