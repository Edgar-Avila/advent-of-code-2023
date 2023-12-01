with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()
    ans = 0
    for line in lines:
        first, last = "", ""
        for c in line:
            if c.isdigit():
                if first == "":
                    first = c
                last = c
        num = int(first + last)
        ans += num
    print(ans)