# input
n = int(input())
popular = {}

# minute in format xx:xx to seconds
def minToSec(time):
    minute,sec = time.split(":")
    
    if len(sec) > 1 and sec[0] == 0:
        sec = sec[1:]
    
    return int(minute) * 60 + int(sec)

# seconds in integer to xx:xx
def secToMin(time):
    time = int(time)
    minute = int(time / 60)
    remain = time % 60
    #print(time,minute,remain)
    
    if remain >= 10:
        return str(minute) + ":" + str(remain)
    
    else:
        return str(minute) + ":0" + str(remain)

# find genre of songs
for i in range(n):
    song = [str(text).strip() for text in input().split(",")]
    genre,time = song[-2:]
    
    popular[genre] = popular.get(genre,0) + minToSec(time)
    
# sort the song by play time
sortedPopular = sorted(popular.items(), key = lambda x: (-x[1],x[0]))
#print(sortedPopular)

# output
for element in sortedPopular[:3]:
    print(element[0], "-->", secToMin(element[1]))
