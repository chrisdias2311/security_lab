#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include<map>

using namespace std;

pair<int, int> getPosition(char letter, vector<vector<char>> baseVector) {
    pair<int, int> position;
    for (int i = 0; i < 5; i++) {
        auto it = find(baseVector[i].begin(), baseVector[i].end(), letter);
        if (it != baseVector[i].end()) {
            position.first = i;
            position.second = it - baseVector[i].begin();
            break;
        }
    }
    return position;
}

string playFair_Excrypt(vector<string> duets, vector<vector<char>> baseVector ){
    string excryptedText = "";

    for(auto i:duets){
        pair<int, int> position1 = getPosition(i[0], baseVector);
        pair<int, int> position2 = getPosition(i[1], baseVector);

        if(position1.first == position2.first){      //same row
            excryptedText += baseVector[position1.first][(position1.second+1)%5];
            excryptedText += baseVector[position2.first][(position2.second+1)%5];
        }else if(position1.second == position2.second){  //same column
            excryptedText += baseVector[(position1.first+1)%5][position1.second];
            excryptedText += baseVector[(position2.first+1)%5][position2.second];
        }else{      //different row and column
            excryptedText += baseVector[position1.first][position2.second];
            excryptedText += baseVector[position2.first][position1.second];
        }
    }
    return excryptedText;
}

int main() {
    string base = "monarchy";
    string plainText = "instruments";

    vector<vector<char>> baseVector(5, vector<char>(5));
    vector<char> letters;

    // Push the letters of Monarchy in the vector
    for (auto i : base) {
        letters.push_back(i);
    }

    // Push the further letters in the vector
    for (int i = 0; i < 26; i++) {
        char letter = char(i + 97);\
        auto it  = find(letters.begin(), letters.end(), letter);
        if (letter != 'j' && it==letters.end()) { // Skip 'j'
            letters.push_back(letter);
        }
    }

    //Build the matrix
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            baseVector[i][j] = letters[i * 5 + j];
        }
    }

    map<string, string> cipher;
    vector<string> duets;

    for(int i=0; i<plainText.size(); i++){
        string temp_duet = "";

        if(plainText[i]=='j'){
            plainText[i] = 'i';
        }

        if(i==plainText.size()-1){
            temp_duet += plainText[i];
            temp_duet += 'z';
        }else if(plainText[i]==plainText[i+1]){
            temp_duet += plainText[i];
            temp_duet += 'z';
            i++;
        }else{
            temp_duet += plainText[i];
            temp_duet += plainText[i+1];
            i++;
        }
        duets.push_back(temp_duet);

    }

    string encryptedText = playFair_Excrypt(duets, baseVector);
    cout<<"Encrypted Text: "<<encryptedText<<endl;


    //Display the duets
    // cout<<"display The duets:"<<endl;
    // for(auto i: duets){
    //     cout<<i<<" ";
    // }

    //Display the matrix
    // for (int i = 0; i < 5; i++) {
    //     for (int j = 0; j < 5; j++) {
    //         cout << baseVector[i][j] << " ";
    //     }
    //     cout << endl;
    // }

    return 0;
}
