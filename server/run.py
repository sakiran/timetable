import sys
import argparse
import json
from random import shuffle,randint
from copy import deepcopy
total_no_of_periods = 7
total_no_of_days = 6
period_tutorial = 2
period_labs = 3
# labs = ['L1', 'L2']
# tute = ['T1', 'T2', 'T3']
# subjects = ['S1', 'S2', 'S3']
'''print('Enter comma separated labs : \n')
labs = sys.stdin.readline().split(',')
print('Enter comma separated tutes : \n')
tute = sys.stdin.readline().split(',')
print('Enter comma separated subjects : \n')
subjects = sys.stdin.readline().split(',')

'''

parser = argparse.ArgumentParser(description='Process some strings')
parser.add_argument('-l', nargs="+", type=str )
parser.add_argument('-t', nargs="+", type=str )
parser.add_argument('-s', nargs="+", type=str )
args = parser.parse_args()
labs = args.l
tute = args.t
subjects = args.s

total_period_labs = len(labs) * period_labs
total_period_tutorial = len(tute) * period_tutorial
lab_sample = deepcopy(labs)
tute_sample = deepcopy(tute)
subjects_copy = deepcopy(subjects)
# Algorithm
'''
1). Allocate labs first to the first day from first period
2). Allocate tutes next to the second day from first period
3). Allocate subjects next

Assumptions -  Subjects are not greater than 5
               There is no constraint on no of periods for each subject
'''

timetable = [['','','','','','',''],
             ['','','','','','',''],
             ['','','','','','',''],
             ['','','','','','',''],
             ['','','','','','',''],
             ['','','','','','','']]
for day in range(0, total_no_of_days):
    periods = []
    if day % 2 == 0:
        if len(labs) > 0:
            p = randint(0, 4)

            timetable[day][p] = labs[0]
            timetable[day][p+1] = labs[0]
            timetable[day][p+2] = labs[0]
            del labs[0]
    else:
        if len(tute) > 0:
            p = randint(0, 5)
            timetable[day][p] = tute[0]
            timetable[day][p+1] = tute[0]
            del tute[0]


def fill_periods(elem):
    global subjects
    for i in range(0, len(elem)):
        if len(subjects) == 1:
            subjects = deepcopy(subjects_copy)
        if elem[i] == '':
            p = randint(0, len(subjects)-1)
            elem[i] = subjects[p]
            del subjects[p]
    return elem


while True:
    if len(set(lab_sample).intersection(set(timetable[5]))) != 0 or len(set(tute_sample).intersection(set(timetable[5]))) != 0:
        shuffle(timetable)
    else:
        break

timetable_ = map(fill_periods, timetable)

print timetable_ ;

#print("\n")
#for t in timetable_:
#    print(t)


'''

python run.py -l l1 l2 l3 -t t1 t2 -s s1 s2 s3 s4
'''







