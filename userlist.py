from user import User
class UserList:
    def __init__(self):
        self._users = []
    def add_user(self,user):
        if not isinstance(user,User):
            raise TypeError("Only User instances can be added")
        self._users.append(user)
    def __str__(self):
        return "\n".join(f"User ID: {user.id}, Name: {user.name}" for user in self._users)

# a=UserList()
# u1=User("Alice",1)
# u2=User("Bob",2)
# a.add_user(u1)
# a.add_user(u2)  
# print(a)

    