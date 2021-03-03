import sys
from util import create_users_hobby

users, hobby, result = sys.argv[1:]
create_users_hobby(users, hobby, result)
