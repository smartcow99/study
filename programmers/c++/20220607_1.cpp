#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

vector<string> split(string s) {
  vector<string> v;
  istringstream iss(s);
  string stringBuffer;

  v.clear();

  while(getline(iss, stringBuffer, ' ')) {
    v.push_back(stringBuffer);
  }
  return v;
}

vector<int> solution() {

    vector<int> answer;

    vector<string> id_list = {"muzi", "frodo", "apeach", "neo"};
    vector<string> report = {"muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"};
    int k = 2;


    vector<string> v = split(report, ' ');
    for(int i=0; i<v.size(); i++) {
      cout << v.at(i) << " ";
    }

    return answer;
}



int main() {
  solution();
  return 0;
}
