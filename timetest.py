import datetime
import csv

# duration = float(finishtime) - float(starttime)
# duration = format(duration,'.6f')
starttime = datetime.datetime.now().strftime("%M.%S")

finishtime = datetime.datetime.now().strftime("%M.%S")

duration = float(finishtime) - float(starttime)
duration = format(duration,'.6f')

def finduserrank(filename,duration,usename):
    pos = 1
    data = [usename,duration]
    with open(filename, 'r', newline='') as file:
        w = csv.reader(file, delimiter=',')
        for row in w:
            #if usename == row[0] and duration == row[1]:
            if data == row:
                break
            pos += 1
    file.close()
    return pos
username = 'sammm'
duration = '0:00:41.639885'
pos = finduserrank('rank.txt',duration,username)
print(pos)
username = 'will'
duration = '0:00:50.344179'
pos = finduserrank('rank.txt',duration,username)
print(pos)



def readtoprank(filename):
    n = 1
    topten = []
    with open(filename, 'r', ) as file:
        w = file.read()
        for row in w:
            if n <= 10:
                topten.append(row)
                n += 1
            else:
                break
    file.close()
    return topten

rank = readtoprank('rank.txt')

#print(rank[0])
#print(rank[1])

