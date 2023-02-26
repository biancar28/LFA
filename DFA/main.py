# f = open("input.txt")
# N = int(f.readline())
# Stari = [int(x) for x in f.readline().split()]
# M = int(f.readline())
# Tr = []
# for i in range(0,M):
#     l = f.readline().split()
#     L = [int(l[0]), int(l[1]), l[2]]
#     Tr.append(L)
# S = int(f.readline())
# nrF = int(f.readline())
# F = [int(x) for x in f.readline().split()]
# nrCuv = int(f.readline())
# Cuv = []
# for i in range(0,nrCuv-1):
#     s = f.readline()
#     Cuv.append(s[:-1])
# Cuv.append(f.readline())
# print(N,Stari,M,Tr,S,nrF,F,nrCuv,Cuv)
#
# f.close()
#
# def DFA(cuv,S,F,Tr):
#     st = []
#     st.append(S)
#     for litera in cuv:
#         for tr in Tr:
#             if tr[0] == st[len(st)-1] and tr[2] == litera:
#                 st.append(tr[1])
#                 break
#     if st[len(st)-1] in F:
#         return 1
#     else:
#         return 0
#
# g = open("output.txt", "w")
#
# for cuv in Cuv:
#     rez = DFA(cuv,S,F,Tr)
#     if rez == 1:
#         g.write("Da\n")
#     else:
#         g.write("Nu\n")
#
# g.close()

f = open("input.txt")
N = int(f.readline())
Stari = [int(x) for x in f.readline().split()]
M = int(f.readline())
Tr = []
for i in range(0,M):
    l = f.readline().split()
    L = [int(l[0]), int(l[1]), l[2]]
    Tr.append(L)
S = int(f.readline())
nrF = int(f.readline())
F = [int(x) for x in f.readline().split()]
nrCuv = int(f.readline())
Cuv = []
for i in range(0,nrCuv-1):
    s = f.readline()
    Cuv.append(s[:-1])
Cuv.append(f.readline())
print(N,Stari,M,Tr,S,nrF,F,nrCuv,Cuv)

f.close()

def NFA(nod,Tr,cuv,F,poz):
    global ok
    if poz == len(cuv):
        if nod in F:
            ok=1
            g.write("Da\n")
    else:
        for tr in Tr:
            if tr[0] == nod and tr[2] == cuv[poz]:
                NFA(tr[1],Tr,cuv,F,poz+1)

g = open("output.txt", "w")

for cuv in Cuv:
    poz = 0
    ok=0
    NFA(S,Tr,cuv,F,poz)
    if ok == 0:
        g.write("Nu\n")
g.close()
print("e")