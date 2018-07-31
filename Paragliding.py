#!/usr/bin/python
# -*- coding: UTF-8 -*-
from copy import deepcopy
def main():
    T = int(raw_input())
    for i in xrange(1, T + 1):
        N, K = [int(x) for x in raw_input().split()]

        (P, H, X, Y) = get_input_1(N, K)

        balloons = zip(X, Y)
        towers = zip(P, H)
        res = get_res1(N, towers, balloons, K)
        print "Case #{}: {}".format(i, res)

def get_input(N, K):
    A = [0 for i in range(4)]
    B = [0 for i in range(4)]
    C = [0 for i in range(4)]
    M = [0 for i in range(4)]
    P = [0 for i in range(N)]
    H = [0 for i in range(N)]
    X = [0 for i in range(K)]
    Y = [0 for i in range(K)]
    P[0], P[1], A[0], B[0], C[0], M[0] = [int(x) for x in raw_input().split()]
    H[0], H[1], A[1], B[1], C[1], M[1] = [int(x) for x in raw_input().split()]
    X[0], X[1], A[2], B[2], C[2], M[2] = [int(x) for x in raw_input().split()]
    Y[0], Y[1], A[3], B[3], C[3], M[3] = [int(x) for x in raw_input().split()]
    for i in range(2, N):
        P[i] = (A[0] * P[i - 1] + B[0] * P[i - 2] + C[0]) % (M[0] + 1)
        H[i] = (A[1] * H[i - 1] + B[1] * H[i - 2] + C[1]) % (M[1] + 1)
    for i in range(2, K):
        X[i] = (A[2] * X[i - 1] + B[2] * X[i - 2] + C[2]) % (M[2] + 1)
        Y[i] = (A[3] * Y[i - 1] + B[3] * Y[i - 2] + C[3]) % (M[3] + 1)
    return (P, H, X, Y)

def get_input_1(N, K):
    A = [0 for i in range(4)]
    B = [0 for i in range(4)]
    C = [0 for i in range(4)]
    M = [0 for i in range(4)]
    P = [0 for i in range(N)]
    H = [0 for i in range(N)]
    X = [0 for i in range(K)]
    Y = [0 for i in range(K)]
    P[0], P[1], A[0], B[0], C[0], M[0] = [int(x) for x in raw_input().split()]
    H[0], H[1], A[1], B[1], C[1], M[1] = [int(x) for x in raw_input().split()]
    X[0], X[1], A[2], B[2], C[2], M[2] = [int(x) for x in raw_input().split()]
    Y[0], Y[1], A[3], B[3], C[3], M[3] = [int(x) for x in raw_input().split()]
    for i in range(2, N):
        P[i] = (A[0] * P[i - 1] + B[0] * P[i - 2] + C[0]) % M[0] + 1
        H[i] = (A[1] * H[i - 1] + B[1] * H[i - 2] + C[1]) % M[1] + 1
    for i in range(2, K):
        X[i] = (A[2] * X[i - 1] + B[2] * X[i - 2] + C[2]) % M[2] + 1
        Y[i] = (A[3] * Y[i - 1] + B[3] * Y[i - 2] + C[3]) % M[3] + 1
    return (P, H, X, Y)

def get_res(N, K, P, H, X, Y):
    balloons = zip(X, Y)
    towers = zip(P, H)
    hit = 0
    for (i,j) in balloons:
        for (x,y) in towers:
            if j < y and y - j >= abs(x - i):
                hit += 1
                break
    return hit

towers = [(1,1), (2,2), (4,3), (8,7)]
get_res1(4, towers)
print towers[0][0]