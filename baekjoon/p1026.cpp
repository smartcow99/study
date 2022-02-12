#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, sum = 0, tmp;
vector<int> A, B;

void funS() {
  for(int i=0; i<N; i++) {
    cin >> tmp;
    A.push_back(tmp);
  }
  for(int i=0; i<N; i++) {
    cin >> tmp;
    B.push_back(tmp);
  }

  sort(A.begin(), A.end());
  sort(B.begin(), B.end());
  reverse(B.begin(), B.end());

  for(int i=0; i<N; i++)
    sum += A[i] * B[i];
  cout << sum;
}

int main() {
  cin >> N;
  funS();
}
