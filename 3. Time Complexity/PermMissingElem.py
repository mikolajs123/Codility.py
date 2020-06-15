'''
  An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

  Your goal is to find that missing element.

  Write a function:

  def solution(A)

  that, given an array A, returns the value of the missing element.

  For example, given array A such that:

    A[0] = 2
    A[1] = 3
    A[2] = 1
    A[3] = 5
  the function should return 4, as it is the missing element.

  Write an efficient algorithm for the following assumptions:

  N is an integer within the range [0..100,000];
  the elements of A are all distinct;
  each element of array A is an integer within the range [1..(N + 1)].

'''

def solution1(A):
    n = len(A) 
    p = int((n + 1)*(n + 2) / 2) # because codility needs int type
    q = sum(A) 
    return p - q
    
def solution2(A):
    H = [0] * (len(A) + 1)
    for i in A:
        H[i - 1] = 1
    for index, value in enumerate(H):
        if value == 0:
            return index + 1

def solution3(A):
    A = sorted(A)
    j = 1
    for i in A:
        if i == j:
            j += 1
    return j
