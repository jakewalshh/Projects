
my_str = input("Input a string: ")
index_int = 0
result_str = ''  # empty string
while index_int < (len(my_str) - 1):  # Line 1
    if my_str[index_int] > my_str[index_int + 1]:
        result_str = result_str + my_str[index_int]
    else:
        result_str = result_str * 2
        # Line 2
    index_int += 1 
print(result_str)  # Line 3





"""
my_list = [4, 7, 1, 2]
my_other_list = my_list
my_copy_list = my_other_list[:]
my_list[0] = 99

print(my_list)


print(my_other_list)
print(my_copy_list)













my_str = input("Input a string: ")
index_int = 0
result_str = ''  # empty string
while index_int < (len(my_str) - 1):  # Line 1
    if my_str[index_int] > my_str[index_int + 1]:
        result_str = result_str + my_str[index_int]
    else:
        result_str = result_str * 2
         # Line 2
    index_int += 1 
print("RESULT",result_str)  # Line 3





print("hello")
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = list1 + list2
result2 = list1 * 3

print(result)
print(result2)

"""