#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int N, M, sum = 0, result = 0;

    cin >> N >> M;

    int card_list[N];

    for(int i=0; i<N; i++)
        cin >> card_list[i];

    sort(card_list, card_list + N);

    for(int i=0; i<N; i++) {
        for(int j=i+1; j<N; j++) {
            for(int k=j+1; k<N; k++) {
                sum = card_list[i] + card_list[j] + card_list[k];
                if(sum <= M && sum >= result)
                    result = sum;
            }
        }
    }
    cout << result;
    return 0;
}
