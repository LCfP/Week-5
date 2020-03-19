with open("exercise_2.txt") as snakes:
    for line in snakes:
        if "snake" in line.lower():
            print(line)