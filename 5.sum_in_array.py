# -*- coding: utf-8 -*-

sorted_array = [-3, 1, 4, 6]
S =7

def sum_in_array(sorted_array):
    revert_array = sorted_array[::-1]
    for key,i in enumerate(sorted_array):
        for r_key, j in enumerate(revert_array):
            if i+j == S:
                #stop when find first
                return [i,j]
            if i+j < S:
                #skip elements in start and end that we check
                revert_array = revert_array[r_key:-key-1]
                break
        #early exit for optimal steps
        if (len(revert_array)<=1):
            return [-1]    

print(sum_in_array(sorted_array))