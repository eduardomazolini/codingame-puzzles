import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

R = int(input()) # the length of the road before the gap.
G = int(input()) # the length of the gap.
L = int(input()) # the length of the landing platform.

print("length of the road before the gap. "+str(R), file=sys.stderr)
print("length of the gap. "+str(G), file=sys.stderr)
print("length of the landing platform. "+str(L), file=sys.stderr)
# game loop
while 1:
    S = int(input()) # the motorbike's speed.
    print("motorbike's speed. "+str(S), file=sys.stderr)
    X = int(input()) # the position on the road of the motorbike.
    print("position on the road of the motorbike. "+str(X), file=sys.stderr)
        
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    
    if (R+G<=X): # Freia depois do salto
        print("SLOW")
    elif (X+S+1>=R+G): # Pula quando da pra chegar do outro lado.
        print("JUMP")
    elif (S<G+1):
        print("SPEED") #Freia se tiver muito rapido
    elif (S>G+1):
        print("SLOW")

    else:
        print("WAIT") # A single line containing one of 4 keywords: SPEED, SLOW, JUMP, WAIT.
