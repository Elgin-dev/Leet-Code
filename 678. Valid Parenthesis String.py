class Solution(object):
    def checkValidString(self, s):
       mini=0
       maxi=0
       for i in range(len(s)):
            if(s[i]=='('):
                mini+=1
                maxi+=1
            elif (s[i]==')'):
                mini-=1
                maxi-=1
            else:
                mini-=1
                maxi+=1
            if(maxi<0):
                return False
            mini=max(mini,0)
       return mini==0