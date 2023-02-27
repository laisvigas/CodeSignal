"""
Given the string, check if it is a palindrome.

Example

For inputString = "aabaa", the output should be
solution(inputString) = true;
For inputString = "abac", the output should be
solution(inputString) = false;
For inputString = "a", the output should be
solution(inputString) = true.
"""


def solution(inputString):
   return inputString == inputString[::-1]
    
def solutionRecursive(inputString):
    length = len(inputString)
    if length in [0, 1]:
        return True
        
    if inputString[0] != inputString[-1]:
        return False
    
    newString = inputString[1:-1]

    return solutionRecursive(newString)