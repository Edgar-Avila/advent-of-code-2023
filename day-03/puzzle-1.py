with open('input.txt', 'r') as input_file:
    grid = input_file.readlines()
    rows, cols = len(grid), len(grid[0]) - 1
    visited = set()
    total = 0
    directions = [ 
        (-1 ,-1), (-1 ,0), (-1 ,1),
        (0  ,-1), (0  ,0), (0  ,1),
        (1  ,-1), (1  ,0), (1  ,1),
    ]

    def get_num(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return 0
        if (r, c) in visited or not grid[r][c].isdigit():
            return 0
        start, end = c, c+1
        while start >= 1 and grid[r][start-1].isdigit():
            start -= 1
        while end < cols and grid[r][end].isdigit():
            end += 1
        val = grid[r][start:end]
        num = int(val)
        for i in range(start, end):
            visited.add((r, i))
        return num

    for r in range(rows):
        for c in range(cols):
            val = grid[r][c]
            if val != '.' and not val.isdigit():
                for nr, nc in [(r+d[0], c+d[1]) for d in directions]:
                    total += get_num(nr, nc)
    
    print(total)


