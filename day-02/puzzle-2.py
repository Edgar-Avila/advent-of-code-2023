with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()
    total_power = 0
    for i, line in enumerate(lines):
        cube_sets = line.split(':')[1].strip().split(';')
        fewest = {'red': 0, 'green': 0, 'blue': 0}
        for cube_set in cube_sets:
            cube_counts = [val.strip() for val in cube_set.split(',')]
            for cube_count in cube_counts:
                n, color = cube_count.split()
                n = int(n)
                fewest[color] = max(fewest[color], n)
        power = 1
        for val in fewest.values():
            power *= val
        total_power += power
    print(total_power)