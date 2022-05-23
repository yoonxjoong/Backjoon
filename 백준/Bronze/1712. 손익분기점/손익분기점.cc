#include <iostream>

using namespace std;
int A, B, C;
int main(){
    cin >> A >> B >> C;
    
    if(C-B < 1){
        cout << -1;
        return 0;
    }
    
    cout << A / (C-B) + 1;
}