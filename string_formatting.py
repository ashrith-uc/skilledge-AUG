print("Inside string formatting", __name__)
print("Enter The class name:")
class_name = input()
print("Enter number of Student:")
no_of_student = int(input())
#no_of_student = int(no_of_student)

print("Type of class_name", type(class_name))
print("Type of no_of_student", type(no_of_student))

print(f"There are {no_of_student} student in {class_name}")
