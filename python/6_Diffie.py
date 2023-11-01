#Diffie-Hellman key exchange algorithm 
q = int(input("Enter the value of Q: "))
alpha = int(input("Enter the value of Alpha: "))
priv_A = int(input("Enter the private jey of A: "))
priv_B = int(input("Enter the private key of B: "))

#Calculation of public key of A & B
public_A = pow(alpha,priv_A,q)      #alpha^priv_A mod q
public_B = pow(alpha,priv_B,q)      #alpha^priv_B mod q

#Calculation of secret key of A & B
secret_A = pow(public_B,priv_A,q)    #public_B^priv_A mod q
secret_B = pow(public_A,priv_B,q)    #public_A^priv_B mod q

print("Secret key Of A: ",secret_A)
print("Secret key of B: ",secret_B)