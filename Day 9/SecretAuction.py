
auction = {}
check = "yes"
while  check.lower() == "yes" or check.lower() == 'y':
    print("\033c", end="")
    name = input("What's your name ? : ")
    bid = int(input("What's your bid ? : $"))
    auction[name] = bid
    check = input("Are there any other bidders ? Type \'yes\' or \'no\' :")

print(auction)
max = 0
for key in auction:
    if max < auction[key]:
        max = auction[key]

print(f"Highest Bid : {max}")
print("Highest Bidder : ",end = "")
for key in auction:
    if auction[key]==max:
        print(key)
