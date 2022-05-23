#include <iostream>
#include <algorithm>
#include <stack>

using namespace std;

int main() {
  cin.tie(0);
  ios_base::sync_with_stdio(false);

  int N, height;
  cin >> N;

  stack<pair<int, int>> stk;

  for(int i=0; i<N; i++) {
    cin >> height;

    while(!stk.empty()) {
      if(height < stk.top().second) {
        cout << stk.top().first << " ";
        break;
      }
      stk.pop();
    }

    if(stk.empty())
      cout << 0 << " ";

    stk.push(make_pair(i+1, height));
  }

  return 0;
}
