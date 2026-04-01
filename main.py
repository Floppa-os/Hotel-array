import pickle
import os
import sys
from config import *
temp = 0
print(rooms_1_user)
print(rooms_2_user)
print(rooms_3_user)
while True:
    temp = 0
    cmd = input("main: ")
    if cmd == "save":
        print(rooms)
        with open('data.plk', 'wb') as file:
            pickle.dump(rooms, file)
            pickle.dump(rooms_1, file)
            pickle.dump(rooms_2, file)
            pickle.dump(rooms_3, file)
            pickle.dump(rooms_1_user, file)
            pickle.dump(rooms_2_user, file)
            pickle.dump(rooms_3_user, file)
            print(rooms)
    if cmd == "load":
        with open('data.plk', 'rb') as file:
            rooms = pickle.load(file)
            rooms_1 = pickle.load(file)
            rooms_2 = pickle.load(file)
            rooms_3 = pickle.load(file)
            rooms_1_user = pickle.load(file)
            rooms_2_user = pickle.load(file)
            rooms_3_user = pickle.load(file)
            print(rooms)
            print(rooms_1_user)
            print(rooms_2_user)
            print(rooms_3_user)
# rooms user add
    if cmd == "add rooms_1_user":
        temp = input("add rooms_1_user: ")
        rooms_1_user.append(temp)
        temp = 0
        print(rooms_1_user)
    if cmd == "add rooms_2_user":
        temp = input("add rooms_2_user: ")
        rooms_2_user.append(temp)
        temp = 0
        print(rooms_2_user)
    if cmd == "add rooms_3_user":
        temp = input("add rooms_3_user: ")
        rooms_3_user.append(temp)
        temp = 0
        print(rooms_3_user)
# rooms user del
    if cmd == "del rooms_1_user":
        with open("data/old_user.txt", "w") as file:
            temp = rooms_1_user.pop()
            file.write(str(temp))
        temp = rooms_1_user.pop()
        print(rooms_1_user)
    if cmd == "del rooms_2_user":
        with open("data/old_user.txt", "w") as file:
            temp = rooms_2_user.pop()
            file.write(str(temp))
        temp = rooms_2_user.pop()
        print(rooms_2_user)
    if cmd == "del rooms_3_user":
        with open("data/old_user.txt", "w") as file:
            temp = rooms_3_user.pop()
            file.write(str(temp))
        print(rooms_3_user)
# reset
    if cmd == "reset":
        os.remove("data.plk")