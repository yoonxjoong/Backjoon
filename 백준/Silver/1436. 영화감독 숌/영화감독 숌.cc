#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main()
{
    vector<int> v;
    int cnt = 0;
    int n = 0;
    cin >> n;
    int i = 0;
    while(true){
        string s = to_string(i);
        if (s.find("666") != string::npos) {
            cnt++;
            if (cnt == n) {
                cout << s << endl;
                break;
            }
        }
        i++;
    }
}
   