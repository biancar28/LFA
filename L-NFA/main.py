f = open("input.txt")
N = int(f.readline())
Stari = [int(x) for x in f.readline().split()]
M = int(f.readline())
Tr = {}
for i in range(0, M):
    l = f.readline().split()
    t = (int(l[1]), l[2])
    if int(l[0]) not in Tr:
        Tr[int(l[0])] = [t]
    else:
        Tr[int(l[0])].append(t)
S = int(f.readline())
nrF = int(f.readline())
F = [int(x) for x in f.readline().split()]
nrCuv = int(f.readline())
Cuv = []
for i in range(0, nrCuv):
    s = f.readline()
    Cuv.append(s[:len(s)-1])

print(Tr)

f.close()
g = open("output.txt", "w")

def L_NFA(nod,Tr,cuv,F,viz,poz):
    global ok,Sol
    if poz == len(cuv):
        if nod in F:
            ok = 1
            if cuv not in Sol:
                Sol[cuv] = "Da"
        else:
            poz -= 1
            for tr in Tr[nod]:
                while tr[1] == '^' and tr[0] not in F:
                    tu = (nod, tr[0], tr[1], poz)
                    viz.append(tu)
                    nod = tr[0]

                if tr[1] == '^' and tr[0] in F:
                    tu = (nod, tr[0], tr[1], poz)
                    viz.append(tu)
                    ok = 1
                    if cuv not in Sol:
                        Sol[cuv] = "Da"
    else:
        for tr in Tr[nod]:
            if tr[1] == cuv[poz]:
                tu =(nod,tr[0],tr[1],poz)
                viz.append(tu)
                L_NFA(tr[0],Tr,cuv,F,viz,poz+1)
                viz = viz[:len(viz)-1]

            if tr[1] == '^':
                tu = (nod, tr[0], tr[1],poz)
                viz.append(tu)
                L_NFA(tr[0], Tr, cuv, F, viz, poz)
                viz = viz[:len(viz) - 1]

Sol = {}
for cuv in Cuv:
    poz = 0
    ok = 0
    viz = []
    L_NFA(S,Tr,cuv,F,viz,poz)
    if ok == 0:
        if cuv not in Sol:
            Sol[cuv] = "Nu"

for cuv in Cuv:
    g.write(Sol[cuv]+"\n")

g.close()
