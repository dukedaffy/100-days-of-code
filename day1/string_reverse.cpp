#include <iostream>
#include <algorithm>  
using namespace std;

class Solution {
public:
    void reverseString(string s) {
        reverse(s.begin(), s.end());
        cout<<s;
   
        
    }
};
 
int main() {
	string str = "And still, I rise.";
	cout<<str;
	Solution obj;
	obj.reverseString(str);
   
}
