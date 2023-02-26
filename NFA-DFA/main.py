f = open("input.txt")
N = int(f.readline())
Stari = [int(x) for x in f.readline().split()]
nrA = int(f.readline())
A = [x for x in f.readline().split()]
M = int(f.readline())
Tr={}
for i in Stari:
    Tr[i]={}
    for a in A:
        Tr[i][a]=[]

for i in range(0,M):
    l = f.readline().split()
    Tr[int(l[0])][l[2]].append(int(l[1]))

S = int(f.readline())
nrF = int(f.readline())
F = [int(x) for x in f.readline().split()]
print(Tr)

f.close()
g = open("output.txt", "w")


Tr2={}
Tr2[S]=Tr[S]
i = S
F2 =[]
Stari2=[]
Stari2.append(i)
ok=0
while ok!=1:
    aux = i
    for x in A:

        if len(Tr2[i][x])==1 and Tr2[i][x][0] not in Tr2:
            Tr2[Tr2[i][x][0]]=Tr[Tr2[i][x][0]]
            i = Tr2[i][x][0]
            Stari2.append(i)

        elif len(Tr2[i][x])==0:
            Stari.append(Stari[len(Stari)-1]+1)
            Tr2[Stari[len(Stari)-1]]={}
            for q in A:
                Tr2[Stari[len(Stari) - 1]][q]=[Stari[len(Stari) - 1]]
            i = Stari[len(Stari)-1]
            Stari2.append(i)

        elif len(Tr2[i][x])>1:
            s = str(Tr2[i][x][0])
            for j in range(1,len(Tr2[i][x])):
                s+="-"+str(Tr2[i][x][j])
            if s not in Tr2:
                Tr2[s]={}
                for y in A:
                    L = []
                    z=0
                    while z!=len(Tr2[i][x]):
                        L+=Tr[Tr2[i][x][z]][y]
                        z+=1
                    Tr2[s][y] = L
                i = s
                Stari2.append(i)

    if i == aux:
        ok=1
    else:
        if i in F:
            F2.append(i);
        elif i not in Stari:
            r=0
            for f in F:
                if str(f) in i:
                    r=1
            if r==1:
                F2.append(i)
print(Tr2)

g.write("Stari: ")
for stare in Stari2:
    g.write(str(stare)+" ")
g.write("\n")
g.write("Alfabet: ")
for x in A:
    g.write(x+" ")
g.write("\n")
g.write("Starea initiala: "+ str(S) + "\n")
g.write("Stari finale: ")
for f in F2:
    g.write(str(f)+" ")
g.write("\n")
g.write("Tranzitii: ")
for i in Stari2:
    for x in A:
        g.write(str(i))
        if len(Tr2[i][x])==1:
            g.write(" "+str(Tr2[i][x][0]))
        elif len(Tr2[i][x])>1:
            s = str(Tr2[i][x][0])
            for j in range(1,len(Tr2[i][x])):
                s+="-"+str(Tr2[i][x][j])
            g.write(" " + s)
        g.write(" " + x + "\n")