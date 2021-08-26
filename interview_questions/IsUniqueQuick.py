def IsUnique(string):

    checker = 0
    for char in string:
        val = ord(char) - ord('a')
        if (1 << val) & checker > 0:
            return False
        checker |= (1 << val)

    return True

def clear_bit(int_type,offset):
    mask = ~ (1 << offset)
    return int_type & mask

def test_clear_bit(int_type,offset):
    mask = 1 << offset
    return int_type ^ mask

def set_bit(int_type,offset):
    mask = 1 << offset
    return int_type | mask