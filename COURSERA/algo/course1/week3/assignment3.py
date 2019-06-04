#Uses Python3
final_stop = int(input())
capacity = int(input())
n = int(input())
stops_intput = input().split()
stops = [int(x) for x in stops_intput]
stops.append(final_stop)
max_cur = capacity
count = 0
for each in stops:
    if each > max_cur:
        max_cur = last_stop + capacity
        if max_cur < each:
            count = -1
            break
        if max_cur >= each:
            count += 1
    if each <= max_cur:
        last_stop = each
print(count)
        