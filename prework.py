def hello_name(user_name):
    # Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below. def hello_name(user_name):
    print("hello_"+user_name+"!")

def first_odds():
    # Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
    for x in range(101):
        if x % 2 == 1 :
            print(x, end=" ")
    print()

    
def max_num_in_list(a_list):
    # Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below. def max_num_in_list(a_list):
    max = 0
    for x in a_list:
        if x > max:
            max = x
    return max


 
def is_leap_year(a_year):
    # Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400. The return should 
    # be boolean Type (true/false). def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0 or a_year % 400 == 0:
        return True
    else:
        return False

 
def is_consecutive(a_list):
    # Write a function to check to see if all numbers in the list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, 
    # but [1,2,4,5] are not consecutive numbers. The return should be boolean Type. def is_consecutive(a_list):
    for x in range(len(a_list)):
        if x != 0:
            previous = a_list[x-1]
            current = a_list[x]
            if previous + 1 == current:
                continue
            else: return False
    return True


hello_name("Noah")

first_odds()

my_list = [1,2,3,4,5,100]
print(max_num_in_list(my_list))

print(is_leap_year(2000))

my_list2 = [5,6,7,8,9,10]
print(is_consecutive(my_list2))