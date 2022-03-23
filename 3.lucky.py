# -*- coding: utf-8 -*-

series = '4556432455665334'

lucky = []
tmp = []
same = True
for i in series:
    if (i in ['5','6']):
        tmp.append(i)
        # check different numbers
        if (same == True) and (len(tmp)>1):
            same = tmp[-1] == tmp[-2]
    elif (len(tmp)>0):
        if (same == False) and (len(lucky)<len(tmp)):
            lucky = tmp
        tmp = []
        same = True

if (len(lucky)>0):
    print(''.join(lucky))
else:
    print ('zero')