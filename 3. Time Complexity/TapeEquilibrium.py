'''
  A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

  Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

  The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

  In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

  For example, consider array A such that:

    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 4
    A[4] = 3
  We can split this tape in four places:

  P = 1, difference = |3 − 10| = 7 
  P = 2, difference = |4 − 9| = 5 
  P = 3, difference = |6 − 7| = 1 
  P = 4, difference = |10 − 3| = 7 
  Write a function:

  def solution(A)

  that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

  For example, given:

    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 4
    A[4] = 3
  the function should return 1, as explained above.

  Write an efficient algorithm for the following assumptions:

  N is an integer within the range [2..100,000];
  each element of array A is an integer within the range [−1,000..1,000].
'''

def solution1(A):
    s = sum(A)
    c = 0
    sums = []
    for i in A[:-1]:
        c += i
        s -= i
        sums.append(abs(c - s))
    return min(sums)

def solution2(A):          
    s = sum(A)
    m = float('inf')
    left_sum = 0
    for i in A[:-1]:
        left_sum += i
        m = min(abs(s - 2 * left_sum), m)
    return m
  
from itertools import accumulate

def solution3(A):
    array_sum = sum(A)  # saving sum of all elements to have an O(n) complexity

    # accumulate returns accumulated sums
    # e.g. for input: [3, 1, 2, 4] it returns: [3, 4, 6, 10]
    # we are passing a copy of the array without the last element
    # including the last element doesn't make sense, becuase
    # accumulate[A][-1] == array_sum
    accumulated_list = accumulate(A[:-1])

    return min([abs(2 * x - array_sum) for x in accumulated_list])
