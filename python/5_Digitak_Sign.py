#Digital Signature using RSA Encryption 
from itertools import count 

p = int(input("Enter the value of P: "))
q = int(input("Enter the value of Q: "))
n = p*q
phyn = (p-1)*(q-1)
e = int(input("Enter the value of E: "))
print('Public key: (',e,',',n,')')

for k in count(1,e):
    if(phyn*k+1)%e == 0:
        d = int((phyn*k+1)/e)
        print('Private Key: (',d,',',n,')')
        break

# Performing Encryption 
M = int(input("Enter the message: "))
Signature = (pow(M,d,n))     # Signature = (M^d) mod n
print('Digital Signature: ',Signature)

# Performing Decryption
DM = pow(Signature, e,n)    # DM = (Signature^e) mod n

if(DM==M):
    print('Digital Signature is valid')
else:
    print('Digital Signature is invalid')