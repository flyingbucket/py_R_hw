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
#     language: python
#     name: python3
# ---

# #hw3

# +
# 1. 汽车：编写一个函数，将一辆汽车的信息存储在一个字典中。这个函数总是接受制造商和型号，还接受任意数量的关键字实参。
# 这样调用这个函数：提供必不可少的信息，以及两个名称—值对，如颜色和选装配件。这个函数必须能够像下面这样进行调用：
# car = make_car('subaru', 'outback', color='blue', tow_package=True)

def make_car(brand,model,**car_info):
    car={}
    car['brand']=brand
    car['model']=model
    for key,val in car_info.items():
        car[key]=val
    return car
car = make_car('subaru', 'outback', color='blue', tow_package=True)
car # 交互式打印


# +
# 2. 餐馆：创建一个名为Restaurant 的类，其方法__init__()设置两个属性：restaurant_name 和cuisine_type。
# 创建一个名为describe_restaurant()的方法和一个名为open_restaurant()的方法，其中前者打印前述两项信息，
# 而后者打印一条消息，指出餐馆正在营业。
# 根据这个类创建一个名为restaurant 的实例，分别打印其两个属性，再调用前述两个方法。
class Restaurant():
    def __init__(self,name,type,number_served=0):
        self.restaurant_name=name
        self.cuisine_type=type
        self.number_served=number_served

    def describe_restaurant(self):
        print(f"restaurant name: {self.restaurant_name}, cuisine type: {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open now")
    
    def set_number_served(self,number):
        self.number_served=number
    
    def increment_number_served(self,number):
        self.number_served+=number

restaurant = Restaurant('KFC','fast food')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

# -

# 3. 三家餐馆：根据你为完成练习2而编写的类创建三个实例，并对每个实例调用方法describe_restaurant()。
restaurant1 = Restaurant('KFC','fast food')
restaurant2 = Restaurant('McDonald','fast food')
restaurant3 = Restaurant('Pizza Hut','Italian food')
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()


# +
# 4.用户：创建一个名为User 的类，其中包含属性first_name 和last_name，还有用户简介通常会存储的其他几个属性。
# 在类User 中定义一个名为describe_user()的方法，它打印用户信息摘要；
# 再定义一个名为greet_user()的方法，它向用户发出个性化的问候。
# 创建多个表示不同用户的实例，并对每个实例都调用上述两个方法。
class User():
    def __init__(self,first_name,last_name,login_attempts=0,**user_info):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempts=login_attempts
        self.__dict__.update(user_info)
        
    
    def describe_user(self):
        print(f"first name: {self.first_name}, last name: {self.last_name}")
        for key in self.__dict__.keys():
            if key not in ['first_name','last_name']:
                print(f"{key}: {getattr(self,key)}")
    
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}\n")

    def increment_login_attempts(self):
        self.login_attempts+=1
    
    def reset_login_attempts(self): 
        self.login_attempts=0
        
user1 = User('Tom','Lee',age=10,gender='F')
user2 = User('Jerry','Lee',hobby='running')
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()

# +
# 5. 就餐人数：在为完成练习2 而编写的程序中，添加一个名为number_served的属性，并将其默认值设置为0。
# 根据这个类创建一个名为restaurant 的实例；打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它。
# 添加一个名为set_number_served()的方法，它让你能够设置就餐人数。调用这个方法并向它传递一个值，
# 然后再次打印这个值。添加一个名为increment_number_served()的方法，它让你能够将就餐人数递增。
# 调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。


# 题目要求的属性和方法在第二题处添加了，没有在这个cell重新定义类，需要先运行第二题的cell

restaurant = Restaurant('KFC','fast food')
print(restaurant.number_served)
restaurant.set_number_served(10)
print(restaurant.number_served)
restaurant.increment_number_served(20)
print(restaurant.number_served)

# +
# 6. 尝试登录次数：在为完成练习4 而编写的User 类中，添加一个名为login_attempts 的属性。
# 编写一个名为increment_login_attempts()的方法，它将属性login_attempts 的值加1。
# 再编写一个名为reset_login_attempts()的方法，它将属性login_attempts 的值重置为0。
# 根据User 类创建一个实例，再调用方法increment_login_attempts()多次。
# 打印属性login_attempts 的值，确认它被正确地递增；然后，调用方法reset_login_attempts()，
# 并再次打印属性login_attempts 的值，确认它被重置为0。

# 题目要求的属性和方法在第四题处添加了，没有在这个cell重新定义类，需要先运行第四题的cell
user3=User('Tom','Smith')
print(user3.login_attempts)
for i in range(5):
    user3.increment_login_attempts()
print(user3.login_attempts)
user3.reset_login_attempts()
print(user3.login_attempts)
