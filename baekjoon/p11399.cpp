#include <iostream>
#include <numeric>
#include <vector>
#include <algorithm>
using namespace std;

int N, tmp, result = 0;;
vector<int> v;

int ATM_function(int n) {
  for(int i=0; i<N; i++) {
    cin >> tmp;
    v.push_back(tmp);
  }
  sort(v.begin(), v.end());
  tmp = 0;
  for(int i=0; i<N; i++) {
    result += v[i] + tmp;
    tmp += v[i];
  }
  return result;
}

int main() {

  cin >> N;
  cout << ATM_function(N);
}
