import numpy as np

a = np.array(list(range(16)), dtype='uint8')
print(a)

for _ in range(16):
    a += 16
    print(a)

# uint8 means unsigned integer of 8 bits, this means only the number 0 through 255 can be represented,
# after that it loops back around

# try removing the u, this means the first bit signifies if the number is positive or negative,
# leaving only 7 bits for the actual number, so the range is from -128 to 127
