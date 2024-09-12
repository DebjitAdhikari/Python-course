class User:
    def __init__(self,user_id,username): #constructor
        self.id=user_id
        self.name=username
        self.follower=0
        self.following=0
    def follow(self,user): #self refers to the object itself
        self.following+=1
        user.follower+=1

user1=User(101,"Debjit")
user2=User(102,"Srabani")
user1.follow(user2)
print(user1.following,user1.follower)
print(user2.following,user2.follower)
