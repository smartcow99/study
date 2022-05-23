#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  int first, second;
  bool check = true;

  while(check) {
    cin >> first >> second;
    if(first == second) {
      check = false;
    }
    else if(first < second) {
      if(second % first == 0) {
        cout << "factor" << endl;
      }
      else {
        cout << "neither" << endl;
      }
    }
    else if(first > second) {
      if(first % second == 0) {
        cout << "multiple" << endl;
      }
      else {
        cout << "neither" << endl;
      }
    }


  }
}
