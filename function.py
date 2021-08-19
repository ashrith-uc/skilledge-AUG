def add_two_numbers():
    a = 10
    b = 20
    print(a+b)

#add_two_numbers()

def center1(str_to_center, n, fill_char="_"):
    print("inputs", fill_char)
    len_of_str = len(str_to_center)
    if n <= len_of_str:
        return str_to_center
    remaining_length_to_fill = n - len_of_str
    no_char_to_append = int(remaining_length_to_fill/2)
    left_fill = fill_char * no_char_to_append
    right_fill = fill_char * no_char_to_append
    str_to_center = left_fill + str_to_center + right_fill
    return str_to_center

string_to_fill = "pranav" #input()""
length_for_center = 10 #int(input())

print("Centered string is ", center1("pranav", 10, "*"))
print("Centered string is ", center1(string_to_fill, length_for_center))

