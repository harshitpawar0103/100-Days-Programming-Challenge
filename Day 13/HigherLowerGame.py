import random as r
from data import data

ndata = data
n=6
score = 0
while n>0:
    competitor1 = r.choice(ndata)
    competitor2 = r.choice(ndata)

    print(f"\nComapre A : {competitor1['name']}, has {competitor1['category']} as profession, from {competitor1['country']}")
    print("\nVS\n")
    print(f"Against B : {competitor2['name']}, has {competitor2['category']} as profession, from {competitor2['country']}")
    answer = input("\nWho has more followers ? Type 'A' or 'B' : ")
    if answer == 'A':
        if competitor1["followers"] > competitor2["followers"]:
            n=1
            score+=1
        else :
            print("You lose")
            n=0
    elif answer == 'B':
        if competitor1["followers"] < competitor2["followers"]:
            n=1
            score+=1
        else :
            n=0
            print("You lose")
    else :
        n=0
        print("You lose")

print(score)


