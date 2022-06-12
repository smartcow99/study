
// C++ Stack 라이브러리 사용

#include <iostream>
#include <stack>
// stack 라이브러리 선언

using namespace std;

int main(void) {
  stack<int> s;
  // int형 element를 가지는 stack s를 선언
  s.push(1);
  // s에 1을 push
  s.push(2);
  // s에 1을 push
  s.push(3);
  // s에 1을 push
  cout << s.top() << endl;
  // s의 가장 마지막으로 저장된 데이터인 3이 출력
  s.pop();
  // s의 가장 마지막 데이터인 3을 삭제, 현재 top은 2
  cout << s.top() << endl;
  // 2가 출력
  s.pop();
  // top 데이터인 2를 삭제
  cout << s.top() << endl;
  // 1이 출력
  cout << "s is empty? : " << (s.empty() ? "yes!" : "no!") << endl;
  // s에 1이 남아있기에 s is empty? : no!
  s.pop();
  // top 데이터인 1을 삭제
  cout << "s is empty? : " << (s.empty() ? "yes!" : "no!") << endl;
  // s에 아무것도 없기에 s is empty? : yes
  return 0;
}
