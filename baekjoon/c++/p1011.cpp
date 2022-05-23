#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int main()
{
  int n;
  cin >> n;
  while(n != 0) {
    long long x, y, distance;
    cin >> x >> y;
    distance = y - x;
    if(distance == 1)
      cout << "1" << '\n';
    else if(distance == 2)
      cout << "2" << '\n';
    for(long long i = 2; i < distance; i++) {
      if(distance <= i*i) {
        cout << i*2-1 << '\n';
        i = distance;
      }
      else if(distance <= i*(i+1)) {
        cout << i*2 << '\n';
        i = distance;
      }
    }
    n--;
  }

  return 0;
}
