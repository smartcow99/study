#include <iostream>
#include <stack>

using namespace std;

int main() {
  int N, X;
  string str;
  stack<int> s;
  cin >> N;
  for(int i=0; i<N; i++) {
    cin >> str;
    if(str == "push") {
      cin >> X;
      s.push(X);
    }
    else if(str == "pop") {
      if(!s.empty()) {
        cout << s.top() << endl;
        s.pop();
      }
      else
        cout << -1 << endl;

    }
    else if(str == "size") {
      cout << s.size() << endl;
    }
    else if(str == "empty") {
      if(!s.empty())
        cout << 0 << endl;
      else
        cout << 1 << endl;
    }
    else if(str == "top") {
      if(!s.empty())
        cout << s.top() << endl;
      else
        cout << -1 << endl;
    }


  }
}
