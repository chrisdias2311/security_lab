#include<iostream>
#include<string> 
using namespace std;

string encryptesMessage(string message, int shift){
    string encryptedMessage = "";
    for(int i=0; i<message.length(); i++){
        if(message[i] >= 'a' && message[i] <= 'z'){
            encryptedMessage += char(int(message[i] + shift - 97) % 26 + 97);
        }
        else if(message[i] >= 'A' && message[i] <= 'Z'){
            encryptedMessage += char(int(message[i] + shift - 65) % 26 + 65);
        }
        else{
            encryptedMessage += message[i];
        }
    }
    return encryptedMessage;
}

int main(){

    string message, encryptedMessage, decryptedMessage;
    int shift;

    cout<<"Enter the message to be encrypted"<<endl;
    getline(cin, message);

    cout<<"Enter the shift value"<<endl;
    cin>>shift;

    encryptedMessage = encryptesMessage(message, shift);
    cout<<"Encrypted Message: "<<encryptedMessage<<endl;

    decryptedMessage = encryptesMessage(encryptedMessage, 26-shift);
    cout<<"Decrypted Message: "<<decryptedMessage<<endl;

    return 0;
}