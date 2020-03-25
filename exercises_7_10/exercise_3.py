with open("exercise_3.py") as input_file:
    lines = input_file.readlines()

format = "{:04d} {}"

with open("exercise_3_output.txt", "w") as output_file:
    for line_number, line in enumerate(lines):
        output_file.write(format.format(line_number, line))
