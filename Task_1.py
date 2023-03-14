# Чуть переписал код, теперь нет суммирования списка, а сразу идет сложение элементов

times = '1h 45m,360s,25m,30m 120s,2h 60s'
a = times.split(',')
times = " ".join(a)


def summa(list_times: str) -> int:
    absolute_total = 0
    for i in list_times.split():
        if 'h' in i:
            absolute_total += int(i[:-1]) * 60
        elif 'm' in i:
            absolute_total += int(i[:-1])
        elif i[-1] == 's':
            absolute_total += int(i[:-1]) / 60
    return absolute_total


print(summa(times))
