class Solution(object):
    def reverseString(self, s):
        stack=[]
        res=[]
        i=0
        while i<len(s):
            stack.append(s[i])
            i+=1
            
        for i in range(len(s)):
        
                s[i]=stack.pop()
                
           
                

        
