import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

N = int(input()) # the number of temperatures to analyse
TEMPS = [0]
POSITIVES = []
NEGATIVES = []
if (N>0):
    TEMPS = input() # the N temperatures expressed as integers ranging from -273 to 5526
    TEMPS = [int(x) for x in TEMPS.split(' ')]
    
POSITIVES = [x for x in TEMPS if (x >= 0)]
NEGATIVES = [x*-1 for x in TEMPS if (x < 0)]
POSITIVES = sorted(POSITIVES)
NEGATIVES = sorted(NEGATIVES)
print("TEMPS: "+str(TEMPS), file=sys.stderr)
print("NEGATIVES: "+str(NEGATIVES), file=sys.stderr)
print("POSITIVES: "+str(POSITIVES), file=sys.stderr)
    
RESULT=0

if ((len(NEGATIVES)>0) and (len(POSITIVES)==0)):
    RESULT=NEGATIVES[0]*-1
elif (((len(POSITIVES)>0) and (len(NEGATIVES)>0)) and (NEGATIVES[0] < POSITIVES[0])):
    RESULT=NEGATIVES[0]*-1
else:
    RESULT=POSITIVES[0]
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
print("TEMPS: "+str(TEMPS), file=sys.stderr)
print(RESULT)
