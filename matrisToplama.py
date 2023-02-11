'''
Matris örneği:
1 3 5
2 4 6
3 5 7

1 3 5
2 4 6
3 5 7

2 6 10
4 8 12
6 10 14
'''
#%%
matris1 = [[1, 3, 5], [2, 4, 6], [3, 5, 7]]
matris2 = [[1, 3, 5], [2, 4, 6], [3, 5, 7]]
sonuc = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for satir in range(len(matris1)):
    for sutun in range(len(matris2)):
        sonuc[satir][sutun] = matris1[satir][sutun] + matris2[satir][sutun]
print(sonuc)
#%%
print("Matrislerin satir sayisini giriniz (m)=")
m = int(input())
print("Matrislerin sutun sayisini giriniz (n)=")
n = int(input())

A = [[0 for i in range(n)] for i in range(m)]
print("A matrisini giriniz:")
for i in range(m):
    for j in range(n):
        print('A[{}][{}]'.format(i+1, j+1))
        A[i][j] = int(input())

B = [[0 for i in range(n)] for i in range(m)]
print("B matrisini giriniz:")
for i in range(m):
    for j in range(n):
        print('B[{}][{}]'.format(i+1, j+1))
        B[i][j] = int(input())

C = [[0 for i in range(n)] for i in range(m)]
for i in range(m):
    for j in range(n):
        C[i][j] = A[i][j] + B[i][j]
print(C)
# %%
