import random

def GenString(string_len = 100):
    string = ''
    for i in range(0, string_len):
        string = string + chr(random.randint(32, 126))

    return string

def GenPerms(string,trials = 1000):
    string_len = len(string)
    value_perms = []
    for i in range(0,trials+1):
        temp = sorted(string)
        random.shuffle(temp)
        temp_string = ''.join(temp)
        value_perms.append(temp_string)

    value_non_perms = []
    for i in range(0,trials):
        index = random.randint(0,string_len-1)
        sliced_string = string[0:index] + string[index+1:] + chr(random.randint(32,126))
        temp = sorted(sliced_string)
        random.shuffle(temp)
        sliced_string = ''.join(temp)
        value_non_perms.append(sliced_string)

    return value_perms,value_non_perms

def WritePerms(perms,fakes,num=1):
    with open('test_perms_'+str(num)+'.txt','w') as f:
        for string in perms:
            f.write(string+'\n')
        for string in fakes:
            f.write(string+'\n')
    print("Finished writing permutations and fake permutations to file!")
if __name__ == "__main__":
    string = GenString(string_len=100)
    perms, fakes = GenPerms(string,trials=10)
    WritePerms(perms,fakes)




