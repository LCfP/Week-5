this = ["I", "am", "not", "a", "crook"]     # creates a list
that = ["I", "am", "not", "a", "crook"]     # creates a new list that happens to be the same

print("Test 1:", (this is that))            # this and that contain the same values but do not refer to the same memory location
that = this                                 # makes that refer to the same memory location as this
print("Test 2:", (this is that))            # now they clearly refer to the same memory location...
