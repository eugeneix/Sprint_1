timeline = '1h 45m,360s,25m,30m 120s,2h 60s'
splitted_timeline = timeline.split(',')
total_minutes = 0

for time in splitted_timeline:
    division_time = time.split(' ')
    for i in division_time:
        if "h" in i:
            i = i.replace('h', '')
            total_minutes += int(i) * 60
        if "m" in i:
            i = i.replace('m', '')
            total_minutes += int(i)
        if "s" in i:
            i = i.replace('s', '')
            total_minutes += int(i) // 60
print(total_minutes)
            


