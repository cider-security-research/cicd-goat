def hello(name):
    """
    This function greets to
    the person passed in as
    a parameter
    """
    return "Hello, " + name

def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""

    if num >= 0:
        return num
    else:
        return -num

def get_wings_length_of_griffin_based_on_age(age):
    if age >= 0 and age < 5:
        return 70
    elif age >= 5 and age < 10:
        return 130
    elif age >=10  and age < 25:
        return 170

def my_func():
	x = 10
	print("Value inside function:",x)

def get_head_weight_of_adult_griffin(age):
    return 70

def gryphon_legacy(n):
   
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")
 
    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0
 
    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
 
    else:
        return gryphon_legacy(n-1) + gryphon_legacy(n-2)
  