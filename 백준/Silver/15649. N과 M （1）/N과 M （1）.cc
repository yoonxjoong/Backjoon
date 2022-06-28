#include <iostream>
#include <vector>
#include <algorithm>

// DFS를 활용한 백트래킹 문제 
// 백트래킹 : 해를 찾아가는 탐색을 하는 도중 지금 탐색 중인 경로가 해가 되지 않을 것 같으면 더 탐색하지 않고 되돌아 가는 기법
// 불필요한 탐색 연산 횟수를 줄임
// 완전 탐색 기법에 기반하며 완전 탐색 기법 중 하나로 DFS를 사용
// DFS는 모든 가능한 해(경로)를 탐색 하는 반면, 백트래킹은 불필요한 경로는 사전에 차단하여 탐색하지 않고 최대한 올바른 해를 탐색합니다. 

#include <iostream>
#include <vector>
#include <algorithm>

#define MAX 9
using namespace std;
int N, M;
vector<int> graph;

int main() {
	cin >> N >> M;

	for(int i=1; i<= N; i++){
		graph.push_back(i);
	}

	do{
		for(int i =0; i <M; i++){
			cout << graph[i] << " ";
		}
		cout << "\n";
		reverse(graph.begin() + M, graph.end());
	}while(next_permutation(graph.begin(), graph.end()));
	
	return 0;
}