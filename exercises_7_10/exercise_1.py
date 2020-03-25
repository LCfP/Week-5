with open("exercise_1_input.txt") as input_file:
    lines = input_file.readlines()

with open("exercise_1_output.txt", "w") as output_file:
    for line in reversed(lines):
        output_file.write(line)
