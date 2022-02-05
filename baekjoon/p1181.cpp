#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compareResult(string a, string b) {
  if(a.length() == b.length())
    return a<b;
  return a.length() < b.length();
}

int main() {

  int n;
  cin >> n;
  vector<string> vec;
  for(int i=0; i<n; i++) {
    string tmp;
    cin >> tmp;
    if(find(vec.begin(), vec.end(), tmp) == vec.end())
      vec.push_back(tmp);
  }
  sort(vec.begin(), vec.end(), compareResult);

  for(int i=0; i<vec.size(); i++) {
    cout << vec[i] << '\n';
  }

  return 0;
}
