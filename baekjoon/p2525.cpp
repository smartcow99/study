#include <iostream>

using namespace std;

int A, B, C;


int main() {
  cin >> A >> B >> C;
  int hour, min;
  hour = C / 60;
  min = C % 60;
  A += hour;
  B += min;
  if(B > 59) {
    B -= 60;
    A++;
  }
  if(A > 23)
    A -= 24;
  cout << A << " " << B;
}
