import math
def calculate_private(e, phin):
    k=2
    
    d = (k*phin + 1)/2
    return int(d)

# p and Q should be prime numbers
p = 3
q = 7
n = p*q
e = 2
phin = (p-1)*(q-1)


while(e<phin):
    if(math.gcd(e, phin)==1):
        break
    else:
        e+=1



d = pow(e, -1, phin)         #Hence Private Key is (d,n)
message = 12
print("MEssage to be encrypted is: ", message)

#Encryption
encrypted_message = pow(message, e, n)
print("Encrypted Message is: ", encrypted_message)

#Decryption
decrypted_message = pow(encrypted_message, d, n)
print("Decrypted Message is: ", decrypted_message)


