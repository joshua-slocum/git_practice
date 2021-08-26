# implement an algorithm to determine if a string has all unique characters. What if you cannot use  additional data
# structures?

# first thought, if given a size of the alphabet s, then we can do a cursory check to see if s < length(string)
# in this case, we omit implementing the algorithm and return false

# preliminary results suggest correct behavior
# parameter s represents magnitude of character set
def IsUnique(string, s = 0):
    size = len(string)
    # brief sanity check
    if s > 0 and size > s:
        return False

    # will use a hash table
    table = {}

    for char in string:
        if char in table:
            return False
        table[char] = char

    return True

# think about using a bit vector
# find a way to map string characters to the set {0,1}
# if I map a value to an index in the bit vector that already has a value of 1, then I know it is a duplicate
# character
# below solution was implemented from the Cracking the Coding Interview book
# useful for thinking about bit manipulation!
# this function assumes only lowercase letters a through z!
# assuming that a string was encoded in ascii (which represents characters as byte strings)
# the below function would reduce space usage by a factor of 8
def IsUniqueBitVector(string):
    checker = 0
    offset_base = ord('a')
    for char in string:
        val = ord(char) - offset_base
        # the bitwise & operator will produce an int value at the end instead of a binary string!
        if (checker & (1 << val)) > 0:
            return False
        checker |= (1 << val)

    return True
