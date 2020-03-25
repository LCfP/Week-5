with open("exercise_3_output.txt") as input_file:
    lines = input_file.readlines()

with open("exercise_4_output_a.txt", "w") as output_file:
    for line in lines:
        output_file.write(line[5:])     # skip the first 5 characters, the four numbers and the space