import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


# game loop
while 1:
    SX, SY = [int(i) for i in input().split()]
    MH = []
    for i in range(8):
        MH.append({'mountain':i, 'height':int(input())}) # represents the height of one mountain, from 9 to 0. Mountain heights are provided from left to right.
    
    MH = sorted(MH, key = lambda x: x['height'],reverse=True)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    if (MH[0]['mountain']==SX):
        print("FIRE")
    else:
        print("HOLD")# either:  FIRE (ship is firing its phase cannons) or HOLD (ship is not firing).
