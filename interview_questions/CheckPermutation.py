# Given two strings write a method to decide if one is a permutation of the other

def CheckPermutation(string_one, string_two):

    # first, can simply check if two strings have same length as sanity check
    if len(string_one) != len(string_two):
        return False

    # think about approaches where one string is put into a hash table
    # can also think about ordering the strings and then comparing string by string
    # in this case, implement a sorting algorithm (think runtime is nlog(n)) then compare n chars to get
    # n^2 log(n) run time

    # discovered sets in python which are unordered and mutable
    # can simply use set function
    return set(string_one) == set(string_two)

test = "q}7s+"

check = "+}q}7"
def DictCheckPermutation(string_one,string_two):
    if len(string_one) != len(string_two):
        return False
    char_counts = {}
    # consider fleshing out dictionary approach
    # not sure how the program will run in terms of efficiency
    for char in string_one:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    for char in string_two:
        if char in char_counts:
            char_counts[char] -= 1
        else:
            return False

    for key in char_counts:
        if char_counts[key] != 0:
            return False

    return True

# TODO: need to debug the dictionary approach still
# TODO: seems to struggle on longer strings still

if __name__ == "__main__":
    with open('test_perms_1.txt','r') as f:
        default = f.readline()
        lines = f.readlines()

    results = []
    results_dict = []

    for item in lines:
        results.append(CheckPermutation(default,item))
        results_dict.append(DictCheckPermutation(default,item))

    count = 0
    for item in results:
        if item != results_dict[count]:
            print(count)
        count += 1
