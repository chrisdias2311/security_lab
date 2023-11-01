#include <bits/stdc++.h>
using namespace std;

int gcd(int a, int b) { 
    // Find Minimum of a and b 
    int result = min(a, b); 
    while (result > 0) { 
        if (a % result == 0 && b % result == 0) { 
            break; 
        } 
        result--; 
    } 
  
    return result; 
}

int main(){

    //P & Q should be prime numbers
    double p = 3;
    double q = 7;
    double n = p * q;
    double e = 2;

    double phi = (p-1)*(q-1);

    while(e<phi){
        if(gcd(e,phi)==1)
            break;
        else
            e++;
    }

    //Now our public key is ready  (e,n)    (Public key is e)

    //Now we need to calculate our private key (d,n)       (Private key is d)
    int k=2;
    double d = ((k*phi+1))/e;
    //Now our private key is ready (d,n)



    //Now we can finallY go to the step of encryption and decryption

    //Message to be encrypted 
    double msg = 12;
    cout<<"Message to be encrypted is: "<<msg<<endl;

    //Encryption
    // double c = pow(msg, e);
    // c = fmod(c,n)
    double c = fmod(pow(msg, e), n);
    cout<<"Encrypted message is: "<<c<<endl;


    //Decryption 
    double m = fmod(pow(c, d), n);
    cout<<"Decrypted message is: "<<m<<endl;

    return 0;
}