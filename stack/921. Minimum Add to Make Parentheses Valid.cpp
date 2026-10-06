class Solution {
public:
    int minAddToMakeValid(string s) {
        stack<char> sk;
        for(int i=0;i<=s.size();i++){
            char val=s[i];
            if (val =='('){
                sk.push(val);
                cout<<"pushed"<<endl;
            }else if(val==')' && sk.size()>=1 && sk.top()=='('){
                sk.pop();
                cout<<"poped"<<endl;
            }else if (val==')'&& sk.size()>=0) {
                sk.push(val);
            }
        }
        
        return sk.size();
    }
};