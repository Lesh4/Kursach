import math
def Cholesky(A,n):
    L = [[0 for z in range(n)] for zz in range(n)]
    for i in range(0, n):
        for j in range(0, i):
            temp = 0
            for k in range(0, j):
                temp += L[i][k] * L[j][k]
            L[i][j] = (A[i][j] - temp) / L[j][j]
        temp = A[i][i]
        for k in range(0, i):
            temp -= L[i][k] * L[i][k]
        L[i][i] = math.sqrt(temp)
    return L

def SQRTMethod(a, answer, n):
    Lt = []
    L = Cholesky(a,n)
    y = [0 for z in range(n)]
    x = [0 for z in range(n)]
    for i in range(0,n):
        Lt.append([])
        for j in range (0,n):
            Lt[i].append(L[j][i])
    for i in range(0, n):
        for c in range(0, i):
            answer[i] = answer[i] - y[c]*L[i][c]
        y[i] = answer[i] / L[i][i]
    for i in range(n-1, -1,-1):
        for c in range(n-1, i,-1):
            y[i] = y[i] - x[c]*Lt[i][c]
        x[i] = y[i] / Lt[i][i]
    return(x)

mas = [[81,-45,45],[-45,50,-15],[45,-15,38]]
answer = [531,-460,193]
