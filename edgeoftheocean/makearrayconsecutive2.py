"""
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.
"""

def solution(statues):
    statues.sort()
    l1 = []
    for c in range(statues[0], statues[-1]):
        l1.append(c)
    l2 = []
    for x in l1:
        if x not in statues:
            l2.append(x)
    return(len(l2))
