#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, K, tmp, result = 0;
vector<int> v;

void findcoin() {
  for(int i=0; i<N; i++) {
    cin >> tmp;
    v.push_back(tmp);
  }
  reverse(v.begin(), v.end());
  for(int i=0; i<v.size(); i++) {
    result += K/v[i];
    K %= v[i];
    if(K == 0) break;
  }
  cout << result;
}

int main() {
  cin >> N >> K;
  findcoin();
}
