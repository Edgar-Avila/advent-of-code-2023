with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()
    id_sum = 0
    for i, line in enumerate(lines):
        game_id = i + 1
        cube_sets = line.split(':')[1].strip().split(';')
        possible = True
        for cube_set in cube_sets:
            cube_counts = [val.strip() for val in cube_set.split(',')]
            for cube_count in cube_counts:
                n, color = cube_count.split()
                n = int(n)
                if (color == 'red' and n > 12) or (color == 'green' and n > 13) or (color == 'blue' and n > 14):
                    possible = False
        if possible:
            id_sum += game_id
    print(id_sum)


            