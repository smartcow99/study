#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int N;
    cin >> N;
    int score[N];
    int profile[N][2];
    for(int i=0; i<N; i++) {
      score[i] = 1;
      cin >> profile[i][0] >> profile[i][1];
    }
    for(int i=0; i<N; i++) {
      for(int j=i+1; j<N; j++) {
        if(profile[i][0] < profile[j][0] && profile[i][1] < profile[j][1]){
          score[i]++;
        }
      }
    }
    for(int i=0; i<N; i++) {
      cout << score[i] << ' ';
    }
    return 0;
}
