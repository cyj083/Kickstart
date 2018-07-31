# -*- coding: UTF-8 -*-
# https://code.google.com/codejam/contest/6364486/dashboard#s=p0
import sys

# select a continous subarray whose sum no exceeding k
# can only work when arr no less than zero
# n is the size of array
def MostK(arr, n, k):
    start, end,  cur_sum, max_sum = 0, 0, 0, 0
    while end < n:
        cur_sum += arr[end]
        end += 1
        while cur_sum > k:
            cur_sum -= arr[start]
            start += 1
        max_sum = max(max_sum, cur_sum)

    return max_sum

# select a continous subarray whose sum not exceeding k and the number of odd not exceeding o
# can only work when arr no less than zero
def candies_positive(arr, n, k, o):
    start, end,  cur_sum, max_sum, odd_num, count = 0, 0, 0, None, 0, 0
    while end < n:
        cur_sum += arr[end]
        if arr[end] % 2 == 1:
            odd_num += 1
        end += 1
        count += 1
        while odd_num > o:
            cur_sum -= arr[start]
            count -= 1
            if arr[start] % 2 == 1:
                odd_num -= 1
            start += 1
        while cur_sum > k and start < end:
            cur_sum -= arr[start]
            if arr[start] % 2 == 1:
                odd_num -= 1
            start += 1
            count -= 1
        if max_sum == None and count > 0:
            max_sum = cur_sum
        elif max_sum != None and count > 0:
            max_sum = max(max_sum, cur_sum)
    if max_sum == None:
        return "IMPOSSIBLE"
    return max_sum


def main():
    t = int(raw_input())
    for j in xrange(1, t + 1):
        N, O, D = [int(x) for x in raw_input().split()]
        X = [0 for i in range(N)]
        S = [0 for i in range(N)]
        X[0], X[1], A, B, C, M, L = [int(x) for x in raw_input().split()]
        for i in range(N):
            if i >= 2:
                X[i] = (A * X[i - 1] + B * X[i - 2] + C) % M
            S[i] = X[i] + L
        print S
        res = candies_positive(S, N, D, O)
        print "Case #{}: {}".format(j, res)



main()

# this program can't process negtive inputs, like the following case.
#a = [-2, -2, 3]
#print candies_positive(a, len(a), 3, 1)

