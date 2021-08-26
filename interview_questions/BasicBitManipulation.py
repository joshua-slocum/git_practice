# Function sets a bit at index denoted by position regardless of prior bit value
def set_bit_one(position, binary_string=0):

    # create a bit mask based on the
    # position passed in
    # produces '10000' if passed in position = 4
    # our bit in index 4 is set to 1
    bit_mask = 1 << position


    # return our binary string or-ed with our mask

    return bit_mask | binary_string

# as a reminder, this function counts from zero!
def set_bit(int_type,offset=0):
    mask = 1 << offset
    return int_type | mask

def clear_bit(int_type, offset=0):
    mask = ~ (1 << offset)
    return int_type & mask

def toggle_bit(int_type, offset=0):
    mask = 1 << offset
    return int_type ^ mask



val = 0b111
val = toggle_bit(val, 1)
print(val)
print(bin(val))