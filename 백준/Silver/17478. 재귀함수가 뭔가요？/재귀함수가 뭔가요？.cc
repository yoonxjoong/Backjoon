#include <iostream>

using namespace std;

string intro = "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.";
string question = "\"재귀함수가 뭔가요?\"";
string worng = "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.";
string worng_1 = "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.";
string worng_2 = "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"";
string correct = "\"재귀함수는 자기 자신을 호출하는 함수라네\"";
string finish = "라고 답변하였지.";
string tmp_bar = "";
int N;
void rec(int num, string bar){
    if(num == 0){
        cout << bar + question << endl;
        cout << bar + correct << endl;
        cout << bar + finish << endl;
        return;
    }
    tmp_bar += "____";
    cout << bar + question << endl;
    cout << bar + worng << endl;
    cout << bar + worng_1 << endl;
    cout << bar + worng_2 << endl;
    rec(num - 1, tmp_bar);
    cout << bar + finish << endl;
}

int main(){
    cin >> N;
    cout << intro << endl;
    rec(N, "");
    return 0;
}