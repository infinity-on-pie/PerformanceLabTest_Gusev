input_file = input('Введите путь к файлу с входными данными: ')

with open(input_file, 'r') as inp_f:
    sum_ = 0
    nums = []
    res = 0
    while True:
        line = inp_f.readline()
        if not line:
            break
        else:
            num = int(line)
            sum_ += num
            nums.append(num)
    aim = int(round(sum_/len(nums))) # минимальное количество шагов достигается при приведении всех значений к среднему
    for num_ in nums:
        res += abs(aim - num_)
    print(res)
