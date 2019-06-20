def check_min(a,b):
    x = a.split(':')
    y = b.split(':')
    x = [int(x) for x in x]
    y = [int(x) for x in y]
    if x[0] < y[0]:
        x,y = y,x
    if (x[0] -y[0]) <= 12:
        return(abs((x[0]*60 + x[1]) - (y[0]*60 + y[1])))
    else:
        return(abs((x[0]*60 + x[1]) - ((y[0]+24)*60 + y[1])))
timePoints = ["05:31","22:08","00:35"]
check = []
min_global = float('inf')
for each in timePoints:
    t = each.split(':')
    t = int(t[0] + t[1])
    check.append(t)
timePoints_sorted = [x for _,x in sorted(zip(check, timePoints))]
timePoints_sorted = timePoints_sorted + [timePoints_sorted[0]]
print(timePoints_sorted)
for i in range(len(timePoints_sorted)-1):
    print(timePoints_sorted[i], timePoints_sorted[i+1])
    min_cur = check_min(timePoints_sorted[i], timePoints_sorted[i+1])
    if min_cur < min_global:
        min_global = min_cur
print(min_global)

