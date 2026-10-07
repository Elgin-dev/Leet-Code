class Solution:
    
    def removeInvalidParentheses(self, s: str) -> list[str]:
        self.valid =set()
        self.dfs(s,0,0,[])
        ans=[]
        if not self.valid:
            return [""]
        maxlen = max(map(len, self.valid))
        for i in self.valid:
            if len(i)==maxlen:
                ans.append(i)
        return ans


    def dfs(self,s,i,bal,curr):
        if bal<0:
            return
        if (i==len(s)):
            if (bal==0):
                self.valid.add("".join(curr))
            return 
        ch=s[i]
        if(ch!='(' and ch!=')' ):
            curr.append(ch)
            self.dfs(s,i+1,bal,curr)
            curr.pop()
        else:
            curr.append(ch)
            if(ch=='('):
                self.dfs(s,i+1,bal+1,curr)
            elif (ch==')'):
                self.dfs(s,i+1,bal-1,curr)
            curr.pop()
            self.dfs(s,i+1,bal,curr)