#include <iostream>
#include <algorithm>

using namespace std;

int n1, n2, n3;
int main() {
  cin >> n1 >> n2 >> n3;
  if(n1 == n2 && n2 == n3)
    cout << 10000 + n1*1000;
  else if(n1 == n2 && n2 != n3)
    cout << 1000 + n1*100;
  else if(n1 == n3 && n2 != n3)
    cout << 1000 + n1*100;
  else if(n1 != n2 && n2 == n3)
    cout << 1000 + n2*100;
  else
    cout << max({n1, n2, n3})*100;
}
