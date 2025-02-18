"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x<= 1:
        return x
    else:
        return foo(x-1) + foo(x-2)

def longest_run(mylist, key):
    max_run = 0
    current_run = 0

    for num in mylist:
        if num == key:
            current_run += 1
            max_run = max(max_run, current_run)
        else:
            current_run = 0

    return max_run


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):
    if not mylist:
        return Result(0, 0, 0, False)

   
    if len(mylist) == 1:
        is_match = mylist[0] == key
        return Result(1 if is_match else 0, 1 if is_match else 0, 1 if is_match else 0, is_match)

    
    mid = len(mylist) // 2
    left_result = longest_run_recursive(mylist[:mid], key)
    right_result = longest_run_recursive(mylist[mid:], key)

    
    combined_left_size = left_result.left_size if not left_result.is_entire_range else left_result.left_size + right_result.left_size
    combined_right_size = right_result.right_size if not right_result.is_entire_range else right_result.right_size + left_result.right_size

    
    middle_run = left_result.right_size + right_result.left_size if mylist[mid - 1] == key and mylist[mid] == key else 0

    
    longest_size = max(left_result.longest_size, right_result.longest_size, middle_run)

   
    is_entire_range = left_result.is_entire_range and right_result.is_entire_range

    return Result(combined_left_size, combined_right_size, longest_size, is_entire_range)




