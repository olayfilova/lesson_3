# None, type
# val_int = 123
# print(val_int, id(val_int))

# bool
# var_1 = True
# var_2 = False
# result = 1 > 2 #  >, <, ==, !=, >=, <=
# print(result)
#
# res_1  = "hello" == "hello!" # !=
# print(res_1)

# res_1  = "hello" > "hello!" # !=
#
# print(res_1)

# res_1  = "llo" in "hello!"
# print(res_1)
# res_1  = "ol" in "hello!"
# print(res_1)

# val_int = 11
# val_str = "12"
# result = str(val_int) + val_str
# print(result)
#
# var_1 = 11
# var_2 = "12"
# print(var_1 + int(var_2))

###### if

# weather = "cold"
# if weather == "cold":
#     print("it's cold")

# weather = "not too cold"
# if weather == "cold":
#     print("it's cold")
# else:
#     print("it's not cold")

#
# val_int = 2

# if val_int > 0 and val_int < 10:
#     print(f"{val_int} is bigger that 0")
# elif val_int > 0:
#     print(f"{val_int} is bigger that 0")
#
# else:
#     print(f"{val_int} is less than 0")
#
# val_int = -2
# if 0 < val_int < 10:
#     print(f"{val_int} is less that 10")
# elif val_int > 10 and val_int < 20:
#     print(f"{val_int} is bigger that 10")
# else:
#     print(f"{val_int} is less that 100")


    ### input()

# val_1 = input("please type a number: ")
# print(val_1)

# val_1 = input("please type a number: ")
# val_2 = input("please type another number: ")
# result = val_1 + val_2
# print(result)

# val_1 = input("please type a number: ")
# val_2 = input("please type another number: ")
# result = int(val_1) + int(val_2)
# print(result)

# try:
# val_1 = int(input("please type a number: "))
# except ValueError: #### ERROR TYPE!!!!
#  print("only digits: 1,2,3...")
# val_2 = int(input("please type another number: "))
# result = val_1 + val_2
# print(result)

# result = 0
# try:
#       val_1 = int(input("please type a number: "))
#       result = 1 / val_1 ### currency reverse!!
# except ValueError: #### ERROR TYPE!!!!
#  print("only digits: 1,2,3...")
# except ZeroDivisionError:
#  print(" can't divide on 0")
# except (EnvironmentError, ConnectionError):
#     print("system is busy now")
# print(result)
value_int = 123
print(value_int, id(value_int))
val_id = id(value_int)
print(val_id)