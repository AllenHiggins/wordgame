'''seven = open('seven.txt', 'w')
treeUpToLessSeven = open('treeUpToLessSeven.txt', 'w')

with open('words.txt') as file:
    for word in file:
        if len(word) > 7 and len(word) <= 17:
            seven.write(word.lower())
        if len(word) > 3 and len(word) <= 7:
            treeUpToLessSeven.write(word.lower())

seven.close()
treeUpToLessSeven.close()
'''
import datetime
import time

starttime = datetime.datetime.now()
time.sleep(5)
finishtime = datetime.datetime.now()

duration = finishtime.__sub__(starttime)


print()