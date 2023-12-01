with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()
    ans = 0
    digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for line in lines:
        first, last = "", ""
        for i, c in enumerate(line):
            if c.isdigit():
                if first == "":
                    first = c
                last = c
            else:
                for j, digit in enumerate(digits):
                    n = len(digit)
                    if line[i:i+n] == digit:
                        if first == "":
                            first = str(j)
                        last = str(j)
        num = int(first + last)
        ans += num
    print(ans)