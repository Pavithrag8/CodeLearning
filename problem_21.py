'''Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), 
find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.'''
#time_intervals = [(30, 75), (0, 50), (60, 150)]
time_intervals = [(0,10),(11,40),(35,49),(0,70),(50,59),(60,80),(71,80)]
sorted_time_intervals = sorted(time_intervals, key=lambda x: x[1])

if time_intervals:
    class_room = {1:0}
    class_room_count = 1

for time_interval in sorted_time_intervals:
    sorted_class_room = sorted(class_room.items(), key=lambda kv: kv[1])
    current_class_room = sorted_class_room[0]
    if time_interval[0] > current_class_room[1]:
        class_room[current_class_room[0]] = time_interval[1]
        continue
    else:
        class_room[current_class_room[0]+1] = time_interval[1]
        class_room_count += 1

print "class_room_count:",class_room_count

