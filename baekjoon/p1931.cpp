#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, result = 0;
int tmp1, tmp2, endtime = 0;
vector<pair<int, int>> v;

void meeting_time() {
  for(int i=0; i<N; i++) {
    cin >> tmp1 >> tmp2;
    v.push_back(make_pair(tmp2, tmp1));
  }
  sort(v.begin(), v.end());
  for(int i=0; i<v.size(); i++) {
    if(v[i].second >= endtime) {
      result++;
      endtime = v[i].first;
    }
  }
  cout << result;
}

int main() {
  cin >> N;
  meeting_time();
}
