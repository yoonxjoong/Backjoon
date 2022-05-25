#include <iostream>
#include <vector>

using namespace std;

int main(){
    vector<int> weight;
    vector<int> height;
    vector<int> result;
    int n = 0;
    int w = 0;
    int h = 0;
    cin >> n;
    for(int i=0; i < n; i++){
        cin >> w >> h;
        weight.push_back(w);
        height.push_back(h);
    }
      
    for(int i=0; i < n; i++){
        int rank = 1;
        for(int j=0; j< n; j++){
            if(weight[i] < weight[j] && height[i] < height[j]){
                rank++;
            }
        }
        cout << rank << " ";
    }
    cout << endl;
    return 0;
}