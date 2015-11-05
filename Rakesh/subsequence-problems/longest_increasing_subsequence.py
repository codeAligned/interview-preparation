__author__ = 'rakesh'

#Longest increasing subsequence
#solution to this video https://www.youtube.com/watch?v=CE2b_-XfVDk
def solution(A):
    '''
    Find the longest increasng subsequence in A
    :param A: list[int]
    :return:
    '''
    if len(A) < 3: #you can modify it later on
        return None
    tempArray = [1] * len(A) #we want to have a temporary array of the same length and initally we assume that the length will be atleast 1
    j, i = 0, 1 #i starts with first position
    while i < len(A):

        if A[j] < A[i]:
            temp = tempArray[j] + 1
            if temp > tempArray[i]:
                tempArray[i] = temp
            j += 1
            if j == i:
                j = 0
                i += 1
        else:
            j += 1
            if i == j:
                j = 0
                i += 1

    return tempArray, max(tempArray)

print solution([-2, 4, -3, 0, 6, 2, 3])  #start counting backwarrd and capture all the values

#these questios can be solved using two pointers. Always remember to use two pointers for such question