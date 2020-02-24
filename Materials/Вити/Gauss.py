def Gauss(a, n):
    x = [0 for z in range(n)]
    for k in range(1, n):
        for j in range(k, n):
            m = a[j][k - 1] / a[k - 1][k - 1]
            for i in range(0, n + 1):
                a[j][i] = a[j][i] - m * a[k - 1][i]
    for i in range(n-1,-1,-1):
        x[i] = (a[i][n]/a[i][i])
        for c in range(n-1,i,-1):
            x[i] = x[i] - a[i][c]*x[c]/a[i][i]
    return x

mas = [[3,4,-9,5,-14],[-15,-12,50,-16,44],[-27,-36,73,8,142],[9,12,-10,-16,-76]]

