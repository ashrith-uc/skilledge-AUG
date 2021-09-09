num_list = [1, 2, 3, 4, 5, 6, 7]
#
# even_list = []
#
# for num in num_list:
#     if num % 2==0:
#         even_list.append(num)
#
# print("Even List", even_list)
#
# sq_list = []
#
# for num in num_list:
#     sq_list.append(num * num)
#
# print("Square : ", sq_list)


sq_list = [num*num for num in num_list] #list comprehension

print("Square", sq_list)

sq_mapping = {num:num*num for num in num_list} #dict comprehension

print("Dict COmp", sq_mapping, type(sq_mapping))

even_list = [num for num in num_list if num%2==0]

even_odd = [num if num%2==0 else "odd" for num in num_list]

print("even list", even_list)
print("even odd list", even_odd)

#print("Positive") if a>0 else print("negative") if a<0 else print("zerro")

