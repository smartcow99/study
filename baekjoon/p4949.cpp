#include <iostream>
#include <string>
#include <stack>

using namespace std;

int main() {
  string str;
  stack<char> stk;
  while(true) {
    str = "";
    getline(cin, str);
    if(str == ".")
      break;
    for(int i=0; i<str.size(); i++) {
      if(str[i] == '(' || str[i] == '[') {
        stk.push(str[i]);
      }
      else if(str[i] == ')') {
        if(!stk.empty() && stk.top() == '(') {
          stk.pop();
        }
        else {
          stk.push('O');
        }
      }
      else if(str[i] == ']') {
        if(!stk.empty() && stk.top() == '[') {
          stk.pop();
        }
        else {
          stk.push('O');
        }
      }
    }
    if(stk.empty())
      cout << "yes" << endl;
    else {
      cout << "no" << endl;
      while(!stk.empty()) stk.pop();
    }
  }
  return 0;
}
