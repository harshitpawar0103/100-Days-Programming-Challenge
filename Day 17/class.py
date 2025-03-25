class User : 
    #constructor
    def __init__(self,user_id,username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    # methods
    def follow(self,user):
        user.followers +=1
        self.following += 1



u1 = User(21,"Krishna")
u2 = User(23,"Kanha")

print(u1.id,u1.username,u1.followers)
u1.follow(u2)
print(u1.followers)
print(u1.following)
print(u2.followers)
print(u2.following)