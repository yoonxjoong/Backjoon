#include <iostream>

using namespace std;

int N;

int rec(int n){
    if(n == 0) return 0;
    if(n == 1) return 1;
    
    return rec(n-1) + rec(n-2);
}

int main(){
    cin >> N;
    
    cout << rec(N) << endl;
    
    return 0;
}