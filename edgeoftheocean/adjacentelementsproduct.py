"""
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.
"""

def solution(inputarray):
    maior = None
    for c in range(0, len(inputarray) - 1):
        mult = (inputarray[c] * inputarray[c + 1])
        if maior is None or mult > maior:
            maior = mult
    return maior