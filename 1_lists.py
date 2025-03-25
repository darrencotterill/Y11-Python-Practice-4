from testhelper import test

# Write the function that squares all the numbers in the list
def square_numbers(numbers):
    pass # Replace this with your code


### TESTS - Run the code that calls the function to check it works.
test("Square numbers 1",[1,4,9,16,25], square_numbers([1,2,3,4,5]))
test("Square numbers 2",[1,4,9,16,25,36], square_numbers([1,2,3,4,5,6]))
test("Square numbers 3",[], square_numbers([]))


