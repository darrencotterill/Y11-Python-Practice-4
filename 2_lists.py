from testhelper import test

# Write the function that combines 2 shopping lists or words, removing duplicates
# and returns the new list.
def combine_lists(list1, list2):
    return [] # Replace this line with your solution

### TESTS - Run the code that calls the function to check it works.
test("Combine lists 1",['melon', 'yoghurt', 'bread', 'apples', 'milk'], 
            combine_lists(['melon', 'bread', 'apples'], ['yoghurt', 'milk']))
test("Combine lists 2",['melon', 'yoghurt', 'bread', 'apples', 'milk'], 
            combine_lists(['melon', 'bread', 'apples'], ['yoghurt', 'milk', 'bread']))
test("Combine lists 2",['melon', 'yoghurt', 'bread', 'apples', 'milk'], 
            combine_lists(['melon', 'bread', 'bread'], ['yoghurt', 'milk', 'milk']))
