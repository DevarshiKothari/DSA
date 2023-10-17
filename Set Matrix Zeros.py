def bfa():
    rows = int(input())
    cols = int(input())
    ar=[]
    for i in range(rows):
        br=[]
        for j in range(cols):
            br.append(int(input()))
        ar.append(br)
    print(ar)
    for i in range(rows):
        for j in range(cols):
            if ar[i][j] == 0:
                for c in range(cols):
                    ar[i][c]=-1
                for c in range(rows):
                    ar[c][j]=-1
    for i in range(rows):
        for j in range(cols):
            if ar[i][j] == -1:
                ar[i][j] = 0
    print(ar)

def ba():
    rows = int(input())
    cols = int(input())
    r=[]
    c=[]
    ar=[]
    for i in range(rows):
        br=[]
        for j in range(cols):
            br.append(int(input()))
        ar.append(br)
    print(ar)
    for i in range(rows):
        for j in range(cols):
            if ar[i][j] == 0:
                r.append(i)
                c.append(j)
    r=set(r)
    c=set(c)
    for i in r:
        for j in range(len(c)):
            ar[i][j]=0
    for i in c:
        for j in range(len(r)):       
            ar[j][i]=0
    print(ar)
ba()