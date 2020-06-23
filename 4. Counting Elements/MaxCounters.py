'''
  You are given N counters, initially set to 0, and you have two possible operations on them:

  increase(X) − counter X is increased by 1,
  max counter − all counters are set to the maximum value of any counter.
  A non-empty array A of M integers is given. This array represents consecutive operations:

  if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
  if A[K] = N + 1 then operation K is max counter.
  For example, given integer N = 5 and array A such that:

      A[0] = 3
      A[1] = 4
      A[2] = 4
      A[3] = 6
      A[4] = 1
      A[5] = 4
      A[6] = 4
  the values of the counters after each consecutive operation will be:

      (0, 0, 1, 0, 0)
      (0, 0, 1, 1, 0)
      (0, 0, 1, 2, 0)
      (2, 2, 2, 2, 2)
      (3, 2, 2, 2, 2)
      (3, 2, 2, 3, 2)
      (3, 2, 2, 4, 2)
  The goal is to calculate the value of every counter after all operations.

  Write a function:

  def solution(N, A)

  that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.

  Result array should be returned as an array of integers.

  For example, given:

      A[0] = 3
      A[1] = 4
      A[2] = 4
      A[3] = 6
      A[4] = 1
      A[5] = 4
      A[6] = 4
  the function should return [3, 2, 2, 4, 2], as explained above.

  Write an efficient algorithm for the following assumptions:

  N and M are integers within the range [1..100,000];
  each element of array A is an integer within the range [1..N + 1].
'''

def solution1(N, A):
    counters = [0] * N
    max_1 = 0
    max_2 = 0
    for i in A:
        if 1 <= i <= N:
            if max_1 > counters[i - 1]:
                counters[i - 1] = max_1
            counters[i - 1] += 1
            if max_2 < counters[i - 1]:
                max_2 = counters[i - 1]
        else:
            max_1 = max_2
    counters = [max(max_1, i) for i in counters]    
    return counters

def solution2(N, A):
    counters = [0] * N
    
    start_line = 0
    current_max = 0
    
    for i in A:
        x = i - 1
        if i > N:
            start_line = current_max
        elif counters[x] < start_line:
            counters[x] = start_line + 1
        else:
            counters[x] += 1
        if i <= N and counters[x] > current_max:
            current_max = counters[x]
    
    for i in range(0, len(counters)):
        if counters[i] < start_line:
            counters[i] = start_line

    return counters
