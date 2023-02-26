f = open("input.txt")
N = int(f.readline())
Stari = [int(x) for x in f.readline().split()]
nrA = int(f.readline())
A = [x for x in f.readline().split()]
M = int(f.readline())
Tr={}
for i in Stari:
    Tr[i]={}

for i in range(0,M):
    l = f.readline().split()
    Tr[int(l[0])][l[2]]=int(l[1])

S = int(f.readline())
nrF = int(f.readline())
F = [int(x) for x in f.readline().split()]

print(Tr)

f.close()
g = open("output.txt", "w")

E={}
S_F=[]
for s in Stari:
    if s not in F:
        S_F.append(s)
E[0]=[S_F,F]
i=1
ok=0
while ok!=1:
    E[i]=[]
    for j in range(0,len(E[i-1])):
        if len(E[i-1][j]) == 1:
            E[i].append(E[i-1][j])
        elif len(E[i-1][j])>1:
            for z in range(0,len(E[i-1][j])-1):
                for q in range(z+1,len(E[i-1][j])):
                    K=[0 for l in range(0,nrA)]
                    for x in range(0,nrA):
                        if Tr[E[i-1][j][z]][A[x]] == Tr[E[i-1][j][q]][A[x]]:
                            K[x]=1
                        else:
                            for list in E[i-1]:
                                if Tr[E[i-1][j][z]][A[x]] in list and Tr[E[i-1][j][q]][A[x]] in list:
                                    K[x]=1
                    if 0 not in K:
                        if len(E[i]) == 0:
                            E[i].append([E[i-1][j][z],E[i-1][j][q]])
                        p=0
                        for l in E[i]:
                            if E[i-1][j][z] in l and E[i-1][j][q] not in l:
                                l.append(E[i - 1][j][q])
                                p=1
                            if E[i-1][j][z] in l and E[i-1][j][q] in l:
                                p=1
                        if p==0:
                            E[i].append([E[i - 1][j][z], E[i - 1][j][q]])
                    else:
                        if len(E[i])==0:
                            E[i].append([E[i-1][j][z]])
                            E[i].append([E[i - 1][j][q]])
                        else:
                            k=0
                            for l in E[i]:
                                if E[i-1][j][q] in l:
                                    k=1
                            if k==0:
                                E[i].append([E[i-1][j][q]])

    Rep={}
    for s in Stari:
        Rep[s]=0
    for l in E[i]:
        for c in range(0,len(l)):
            Rep[l[c]]+=1
    for s in Stari:
        if Rep[s]>1:
            E[i].remove([s])

    if E[i-1]==E[i]:
        ok=1

    i += 1
print(E)
List=E[i-1]
Stari2=[]
F2=[]
for l in List:
    for f in F:
        if len(l)==1:
            Stari2.append(l[0])
            if l[0] == S:
                S2=l[0]
            if l[0] == f:
                F2.append(l[0])
        else:
            ok=0
            k=0
            s=str(l[0])
            if l[0] == S:
                ok=1
            if l[0] == f:
                k=1
            for j in range(1,len(l)):
                s+="-"+str(l[j])
                if l[j] == S:
                    ok=1
                if l[j] == f:
                    k=1
            if ok==1:
                S2=s
            Stari2.append(s)
            if k==1:
                F2.append(s)

g.write("Stari:")
for s in Stari2:
    g.write(" "+str(s))

g.write("\n")
g.write("Stare initiala: "+S2)
g.write("\n")
g.write("Stari finale:")
for f in F2:
    g.write(" "+str(f))
g.write("\n")
g.write("Tranzitii: ")
for j in range(0,len(List)):
    for x in A:
        for z in range(0,len(List)):
            if Tr[List[j][0]][x] in List[z]:
                g.write(str(Stari2[j])+" "+str(Stari2[z])+" "+x+"\n")