import sys
H, W, X, Y = map(int, sys.stdin.readline().split())
B = []
A = []

for i in range(H+X):
  B.append(list(map(int,sys.stdin.readline().split())))

for i in range(H):
    A.append(B[i][:W])

for i in range(X,H):
  for j in range(Y,W):
    A[i][j] = B[i][j] - A[i-X][j-Y]

for a in A:
    print(" ".join(map(str,a)))