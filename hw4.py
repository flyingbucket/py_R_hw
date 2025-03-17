# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.7
#   kernelspec:
#     display_name: base
#     language: Python
#     name: python3
# ---

# %% [markdown]
# # hw4

# %% [markdown]

# 1.冰淇淋小店：冰淇淋小店是一种特殊的餐馆。编写一个名为IceCreamStand 的
# 类，让它继承你为完成第三次作业练习2 或练习5 而编写的Restaurant 类。这两个版本的
# Restaurant 类都可以，挑选你更喜欢的那个即可。添加一个名为flavors 的属性，用于
# 存储一个由各种口味的冰淇淋组成的列表。编写一个显示这些冰淇淋的方法。创建一个
# IceCreamStand 实例，并调用这个方法。

# %% cell 1
import json
import os


class Restaurant:
    def __init__(self, name, type, number_served=0):
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = number_served

    def describe_restaurant(self):
        print(
            f"restaurant name: {self.restaurant_name}, cuisine type: {self.cuisine_type}"
        )

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open now")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number


class IceCreamStand(Restaurant):
    def __init__(self, name, type, flavors, number_served=0):
        super().__init__(name, type, number_served)
        self.flavors = flavors

    def get_flavors(self):
        print(self.flavors)


ice_cream_stand = IceCreamStand("DQ", "ice_cream", ["coco", "strawberry"])
ice_cream_stand.get_flavors()

# %% [markdown]

# 2.管理员：管理员是一种特殊的用户。编写一个名为Admin 的类，让它继承你为
# 完成第三次作业中练习4 或练习6 而编写的User 类。添加一个名为privileges 的属性，用于存
# 储一个由字符串（如"can add post"、"can delete post"、"can ban user"等）组成的
# 列表。编写一个名为show_privileges()的方法，它显示管理员的权限。创建一个Admin
# 实例，并调用这个方法。


# %% cell 2
class User:
    def __init__(self, first_name, last_name, login_attempts=0, **user_info):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts
        self.__dict__.update(user_info)

    def describe_user(self):
        print(f"first name: {self.first_name}, last name: {self.last_name}")
        for key in self.__dict__.keys():
            if key not in ["first_name", "last_name"]:
                print(f"{key}: {getattr(self, key)}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}\n")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(
        self, first_name, last_name, privileges, login_attempts=0, **user_info
    ):
        super().__init__(first_name, last_name, login_attempts, **user_info)
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)


admin = Admin("John", "Marston", ["can add post", "can delete post", "can ban user"])
admin.show_privileges()

# %% [markdown]
# 3.权限：编写一个名为Privileges 的类，它只有一个属性——privileges，其中
# 存储了练习2所说的字符串列表。将方法show_privileges()移到这个类中。在Admin
# 类中，将一个Privileges 实例用作其属性。创建一个Admin 实例，并使用方法
# show_privileges()来显示其权限。


# %% cell 3
class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges


privileges = Privileges(
    ["can add post", "can delete post", "can ban user", "can delete user"]
)
admin = Admin("John", "Marston", privileges)
admin.show_privileges()

# 4.编写一个 while 循环，提示用户输入其名字。用户输入其名字后，
# 在屏幕上打印一句问候语，并将一条访问记录添加到文件 guest_book.txt 中。确保这个
# 文件中的每条记录都独占一行.

# %% cell 4
while True:
    name = input("please enter your name,enter 'q' to quit")
    with open("gues_book.txt", "a", encoding="utf-8") as file:
        if name.lower() != "q":
            file.write(f"{name} visited")
            print(f"welcome {name}\n")
        else:
            print("quiting ...")
            break

# %% [markdown]
# 5.编写一个程序，提示用户输入他喜欢的数字，并使用
# json.dump()将这个数字存储到文件中。再编写一个程序，从文件中读取这个值，并打
# 印消息“I know your favorite number! It’s _____.”。

# %% cell 5
f_num = input("entern your favourite number")
f_num = float(f_num)
with open("favourite_number.json", "a", encoding="utf-8") as f_obj:
    json.dump({"favourite_number": f_num}, f_obj)
    f_obj.write("\n")
with open("favourite_number.json", "r", encoding="utf-8") as f_obj:
    data = json.load(f_obj)
f_num = data["favourite_number"]
print(f"I know your favorite number! It’s {f_num}")

# %% [markdown]
# 6.将练习 5中的两个程序合而为一。如果存储了用户喜
# 欢的数字，就向用户显示它，否则提示用户输入他喜欢的数字并将其存储到文件中。运
# 行这个程序两次，看看它是否像预期的那样工作。

# %% cell 6
name = input("please enter your name")

if os.path.exists("favourite_number2.json"):
    with open("favourite_number2.json", "r", encoding="utf-8") as f_obj:
        data = json.load(f_obj)
        print(data)
    for info in data:
        if info["name"] == name:
            print(f"your favourite number is {info['f_num']}")
        break
    else:
        f_num = input(
            "there is no info of your favourite number. please enter your favourite number "
        )
        f_num = float(f_num)
        new_info = {"name": name, "f_num": f_num}
        with open("favourite_number2.json", "a", encoding="utf-8") as f_obj:
            json.dump([new_info], f_obj)
            f_obj.write("\n")
else:
    f_num = input(
        "there is no info of your favourite number. please enter your favourite number "
    )
    f_num = float(f_num)
    new_info = {"name": name, "f_num": f_num}
    with open("favourite_number2.json", "a", encoding="utf-8") as f_obj:
        json.dump([new_info], f_obj)
        f_obj.write("\n")

        
