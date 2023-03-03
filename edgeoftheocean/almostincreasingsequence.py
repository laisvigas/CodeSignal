"""
Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.

Example

For sequence = [1, 3, 2, 1], the output should be
solution(sequence) = false.
"""

def solution(sequence):
    a = 0
    b = 0
    for c in range(1, len(sequence)-1):
        if sequence[c] <= sequence[c - 1]:
            a += 1
        if sequence[c + 1] <= sequence[c - 1]:
            b += 1
    if sequence[len(sequence) - 1] <= sequence[len(sequence) - 2]:
        a += 1
    if a <= 1 and b <= 1:
        return True
    else:
        return False