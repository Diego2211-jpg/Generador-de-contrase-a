import random
caracteres = "+-/*!&$#?=@abcdefghijklmñnopqrstuvwxyzABCDEFGHIJKLMÑNOPQRSTUVWXYZ1234567890"

longitud = int(input("Digita la longitud de tu contraseña: "))
contraseña = ""

for i in range(longitud):
 
    contraseña = contraseña + random.choice(caracteres)
 

print("La contraseña segura es: ", contraseña)
