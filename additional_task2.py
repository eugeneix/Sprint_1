def digit_root(num):
    num = str(num)
    count = 0
    length_num = len(num)

    while length_num > 1:
        for i in num:
            count += int(i)
        num = str(count)
        count = 0
        length_num = len(num)
    return int(num)


print(digit_root(889987))