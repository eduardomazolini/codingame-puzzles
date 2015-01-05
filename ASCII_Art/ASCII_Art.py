import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

L = int(input())
H = int(input())
T = input()
#print("T: "+str(T), file=sys.stderr)
ROW=[]
for i in range(H):
    value=input()
    ROW.append(list(value[i:i+L] for i in range(0, len(value), L)))
#    print("ROW["+str(i)+"]="+str(ROW[i]), file=sys.stderr)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
T = T.upper()
chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ?'
index = [chars.find(x) if chars.find(x) >= 0 else len(chars)-1 for x in T]
for i in range(H): print("".join([ROW[i][x] for x in index]))
