'''
  A small frog wants to get to the other side of the road. The frog is currently located at position X and wants to get to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.

  Count the minimal number of jumps that the small frog must perform to reach its target.

  Write a function:

  def solution(X, Y, D)

  that, given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or greater than Y.

  For example, given:

    X = 10
    Y = 85
    D = 30
  the function should return 3, because the frog will be positioned as follows:

  after the first jump, at position 10 + 30 = 40
  after the second jump, at position 10 + 30 + 30 = 70
  after the third jump, at position 10 + 30 + 30 + 30 = 100
  Write an efficient algorithm for the following assumptions:

  X, Y and D are integers within the range [1..1,000,000,000];
  X ≤ Y.
'''

def solution1(X, Y, D):
    p = Y - X
    if p % D == 0:
        return p // D
    else:
        return (p // D) + 1

import math

def solution2(X, Y, D):
    distance = (Y - X) / D
    return math.ceil(distance)

def solution3(X, Y, D):
    return (X - Y + (D - 1)) / D
