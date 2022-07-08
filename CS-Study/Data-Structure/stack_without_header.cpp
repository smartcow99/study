// C++ stack 라이브러리 사용 X

#define Stack_Size 100
// Stack_Size를 100으로 선언
#include <iostream>

using namespace std;

struct stack {

  int array[Stack_Size];
  // stack을 구현할 리스트 선언
  int last = -1;
  // 스택의 데이터 위치

  bool empty() {
    if(last < 0) {
      // last < 0 이면 스택이 비어있음을 의미
      return true;
    }
    return false;
    // 아닌경우 false를 반환
  }

  void push(int element) {
    array[++last] = element;
    // 데이터의 위치를 옮기고 그 위치에 element를 저장
  }

  void pop() {
    if(empty()) {
      // 스택이 비어있는 경우
      return;
    }
    --last;
    // last의 위치를 하나 옮겨 데이터를 사용하지 못하게 함
  }

  int top() {
    if(empty()) {
      // 스택이 비어있는 경우 -1을 반환
      return -1;
    }
    return array[last];
    // last 위치의 데이터를 반환
  }
};

int main(void) {

  stack s;
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
