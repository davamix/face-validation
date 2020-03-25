import os

from services.user import UserService
from models.user import User

if __name__ == "__main__":
    user = User("yo", 0.123456789)

    s = UserService()
    # s.save_user(user)
    s.get_user("yo")
    