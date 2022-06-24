#include <iostream>
#include <map>

using namespace std;
int main() {
	int n = 0;
	map<int, int> m;
	cin >> n;
	
	for(int i=0; i < n; i++){
		int a = 0;
		cin >> a;
		m.insert(make_pair(a, 0));
	}

	for(auto iter = m.begin(); iter != m.end(); ++iter){
		cout << iter->first << endl;
	}
	
	return 0;
}