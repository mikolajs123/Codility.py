'''
  This is a demo task.
  Write a function:
  def solution(A)
  that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
  For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
  Given A = [1, 2, 3], the function should return 4.
  Given A = [−1, −3], the function should return 1.
  Write an efficient algorithm for the following assumptions:
  N is an integer within the range [1..100,000];
  each element of array A is an integer within the range [−1,000,000..1,000,000].
'''

def solution1(A):
    occurrence = [False] * (len(A) + 1)
    for item in A:
        print('item: ', item)
        if 1 <= item <= len(A) + 1:
            occurrence[item - 1] = True
    for index in range(len(A) + 1):      
        if occurrence[index] == False:
            return index + 1

def solution2(A):
    A.sort()
    min = 1
    for elem in A:
        if elem == min:
            min += 1
    return min

def solution3(A):
    #set -> remove negatives values and duplicates
    #set(range(1, len(A) )) -> create dict from 1 to max + 1
    # dict.difference(dict) -> looking for difference in to dicts
    # min -> look for minimal value in dict
    return min(set(range(1, len(A) + 2 )).difference(set(A)))
