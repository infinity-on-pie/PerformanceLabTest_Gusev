n = int(input())
m = int(input())
"""Суть решения заключается в том, что каждый раз к предыдущему элементу мы будем прибавлять
значение диапазона - 1 (минус один, чтобы посчитать первый элемент списка) 
и отбрасывать целую часть , как бы убирая количество кругов, пройденных круговым массивом. Не забываем, что
остаток 0 на самом деле означает n"""
tmp = m % n
if tmp == 0:
    tmp = n
path = ['1', str(tmp)]
while (tmp - 1 + m) % n != 1:
    tmp = (tmp - 1 + m) % n
    if tmp == 0:
        tmp = n
    path.append(str(tmp))
print(''.join(path)) # в питоне join() списка быстрее, чем прямая конкатенация, что важно при большом объеме данных
