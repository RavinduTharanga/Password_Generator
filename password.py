import random

password_length=int(input("Enter the lenght of the password :"))

s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

password = "".join(random.sample(s,password_length))
print(password)
