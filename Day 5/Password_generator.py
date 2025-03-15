import string
import random as r
print("Welcome to the pypassword genereator")
l = int(input("How many lowercase letters ? : "))
u = int(input("How many uppercase letters ? : "))
s = int(input("How manny symbols ? : "))
n = int(input("how many numbers ? : "))
t = l+u+s+n

# lowercase = list(string.ascii_lowercase)
# uppercase = list(string.ascii_uppercase)
# symbols = list(string.punctuation)
# numbers = list(map(lambda x : x,range(10)))

# final_list = list(map(lambda i : r.choice(lowercase),range(l))) + list(map(lambda i : r.choice(uppercase),range(u))) + list(map(lambda i : r.choice(symbols),range(s))) + list(map(lambda i : r.choice(numbers),range(n)))

# print("Your new password is : ",end = "")


# for i in r.sample(range(1,t+1),t):
#     print(final_list[i-1],end = "")
    
pass_char = (
              r.choices(string.ascii_lowercase, k=l) +
              r.choices(string.ascii_uppercase, k=u) +
              r.choices(string.punctuation, k=s) +
              r.choices(string.digits, k=n  )
)

r.shuffle(pass_char)

password = "".join(pass_char)

print("Your new passwrod is : ",password)

#mptaas id = PR1004284117