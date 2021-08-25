#start
#logic
#end condition
sample_list = [1,2,3,4,5,6,7]
str1 = "Pranav Kumar"

# i = 0
# for c in str1:
#     print(f"Iteration : {i}", c)
#     i+=1 # this is shorthand to i = i+1
#

#
# for i, ele in enumerate(str1):
#      print(f"Iteration : {i}", ele)

def str_reverse(original_str):
     reversed_str = ""
     for char in original_str:
          reversed_str = char + reversed_str
     return reversed_str

def str_reversev2(original_str):
     reversed_list = []
     str_len = len(original_str)
     for char in original_str:
          str_len = str_len - 1
          reversed_list.append(original_str[str_len])
     return "".join(reversed_list) # This is used to create a string by performing join on the given list


# reversed_str = str_reverse("pranav")
# print("Reversed string is", reversed_str)
#
# reversed_str = str_reversev2("pranav")
# print("Reversed string from V2 is", reversed_str)

#Home Work
def str_internal_rev(original_str):
     pass

#break, continue
#break statement is used to end the iteration based on some condition

#find index of element in list

def get_index(input_list, element):
     index = -1
     for pos, ele in enumerate(input_list):
          print("Iteration NO.", pos+1)
          if ele==element:
               index = pos
               break
     return index

# l = [4,6,7,2,8,9]
# ele = 6
# print(f"Position of {ele} is", get_index(l, ele))


#continue is used to skip the following statements in the loop
def get_sum_of_even_numbers(list_of_number):
     sum = 0
     for index, number in enumerate(list_of_number):
          print(f"Iteration {index+1} number=", number, not number%2==0)
          if not number%2==0:
               continue
          print("Adding ", number)
          sum += number # sum = sum+number
     return sum
#print(get_sum_of_even_numbers([1,2,3,5,6,7,8]))


# write a program to get numbers from user until it doesnot says exit

while(True):
     print("please enter a number")
     i = input()
     if i == "exit":
          break

