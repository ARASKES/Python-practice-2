A = [
    " * ",
    "* *",
    "***",
    "* *",
    "* *"]
B = [
    "** ",
    "* *",
    "** ",
    "* *",
    "** "]
C = [
    " * ",
    "* *",
    "*  ",
    "* *",
    " * "]
D = [
    "** ",
    "* *",
    "* *",
    "* *",
    "** "]
E = [
    "***",
    "*  ",
    "** ",
    "*  ",
    "***"]
F = [
    "***",
    "*  ",
    "** ",
    "*  ",
    "*  "]
G = [
    " **",
    "*  ",
    "* *",
    "* *",
    " **"]
H = [
    "* *",
    "* *",
    "***",
    "* *",
    "* *"]
I = [
    "***",
    " * ",
    " * ",
    " * ",
    "***"]
J = [
    " **",
    "  *",
    "  *",
    "* *",
    " *"]
K = [
    "* *",
    "** ",
    "*  ",
    "** ",
    "* *"]
L = [
    "*  ",
    "*  ",
    "*  ",
    "*  ",
    "***"]
M = [
    "* *",
    "***",
    "***",
    "***",
    "* *"]
N = [
    "* *",
    "***",
    "***",
    "* *",
    "* *"]
O = [
    " * ",
    "* *",
    "* *",
    "* *",
    " * "]
P = [
    "** ",
    "* *",
    "** ",
    "*  ",
    "*  "]
Q = [
    " * ",
    "* *",
    "* *",
    "***",
    " **"]
R = [
    "** ",
    "* *",
    "** ",
    "** ",
    "* *"]
S = [
    " **",
    "*  ",
    " * ",
    "  *",
    "** "]
T = [
    "***",
    " * ",
    " * ",
    " * ",
    " * "]
U = [
    "* *",
    "* *",
    "* *",
    "* *",
    " * "]
V = [
    "* *",
    "* *",
    "* *",
    " * ",
    " * "]
W = [
    "***",
    "***",
    "***",
    "***",
    "* *"]
X = [
    "* *",
    "* *",
    " * ",
    "* *",
    "* *"]
Y = [
    "* *",
    "* *",
    " * ",
    " * ",
    " * "]
Z = [
    "***",
    "  *",
    " * ",
    "*  ",
    "***"]
SPACE = [
    "   ",
    "   ",
    "   ",
    "   ",
    "   "]

text = input()
output = []
for symbol in text:
    if symbol == "A":
        output.append(A)
    elif symbol == "B":
        output.append(B)
    elif symbol == "C":
        output.append(C)
    elif symbol == "D":
        output.append(D)
    elif symbol == "E":
        output.append(E)
    elif symbol == "F":
        output.append(F)
    elif symbol == "G":
        output.append(G)
    elif symbol == "H":
        output.append(H)
    elif symbol == "I":
        output.append(I)
    elif symbol == "J":
        output.append(J)
    elif symbol == "K":
        output.append(K)
    elif symbol == "L":
        output.append(L)
    elif symbol == "M":
        output.append(M)
    elif symbol == "N":
        output.append(N)
    elif symbol == "O":
        output.append(O)
    elif symbol == "P":
        output.append(P)
    elif symbol == "Q":
        output.append(Q)
    elif symbol == "R":
        output.append(R)
    elif symbol == "S":
        output.append(S)
    elif symbol == "T":
        output.append(T)
    elif symbol == "U":
        output.append(U)
    elif symbol == "V":
        output.append(V)
    elif symbol == "W":
        output.append(W)
    elif symbol == "X":
        output.append(X)
    elif symbol == "Y":
        output.append(Y)
    elif symbol == "Z":
        output.append(Z)
    elif symbol == " ":
        output.append(SPACE)
for j in range(5):
    for i in range(len(output)):
        print(output[i][j], end="  ")
    print()
