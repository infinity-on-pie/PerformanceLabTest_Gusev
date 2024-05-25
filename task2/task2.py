circle_f = input('Введите путь к первому файлу: ')
with open(circle_f, 'r') as cf:
    # считываем данные для круга
    center_x, center_y = map(float, cf.readline().split())
    radius = float(cf.readline())

dots_f = input('Введите путь к второму файлу: ')
with open(dots_f, 'r') as df:
    # читаем строчки файла с точками пока строчки не будут пустыми
    while True: # бесконечный цикл
        line = df.readline()
        if not line: # когда строка будет будет пустой цикл прервется
            break
        dot_x, dot_y = map(float, line.split())
        distance = ((dot_x - center_x)**2 + (dot_y - center_y)**2)**0.5 # вычисляем расстояние между центром и точкой
        if distance == radius:
            print(0)
        elif distance < radius:
            print(1)
        else:
            print(2)